// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

use std::collections::HashMap;
use std::fmt::Debug;
use std::fmt::Formatter;
use std::fmt::Write;
use std::sync::Arc;

use async_trait::async_trait;
use base64::prelude::BASE64_STANDARD;
use base64::Engine;
use bytes::Buf;
use http::StatusCode;
use log::debug;
use log::warn;
use md5::Digest;
use md5::Md5;
use once_cell::sync::Lazy;
use reqsign::AwsAssumeRoleLoader;
use reqsign::AwsConfig;
use reqsign::AwsCredentialLoad;
use reqsign::AwsDefaultLoader;
use reqsign::AwsV4Signer;

use super::core::*;
use super::error::parse_error;
use super::error::parse_s3_error_code;
use super::pager::S3Pager;
use super::writer::S3Writer;
use crate::raw::*;
use crate::services::s3::writer::S3Writers;
use crate::*;

/// Allow constructing correct region endpoint if user gives a global endpoint.
static ENDPOINT_TEMPLATES: Lazy<HashMap<&'static str, &'static str>> = Lazy::new(|| {
    let mut m = HashMap::new();
    // AWS S3 Service.
    m.insert(
        "https://s3.amazonaws.com",
        "https://s3.{region}.amazonaws.com",
    );
    m
});

const DEFAULT_BATCH_MAX_OPERATIONS: usize = 1000;

/// Aws S3 and compatible services (including minio, digitalocean space, Tencent Cloud Object Storage(COS) and so on) support.
/// For more information about s3-compatible services, refer to [Compatible Services](#compatible-services).
#[doc = include_str!("docs.md")]
#[doc = include_str!("compatible_services.md")]
#[derive(Default)]
pub struct S3Builder {
    root: Option<String>,

    bucket: String,
    endpoint: Option<String>,
    region: Option<String>,

    // Credentials related values.
    access_key_id: Option<String>,
    secret_access_key: Option<String>,
    security_token: Option<String>,
    role_arn: Option<String>,
    external_id: Option<String>,
    disable_config_load: bool,
    disable_ec2_metadata: bool,
    allow_anonymous: bool,
    customed_credential_load: Option<Box<dyn AwsCredentialLoad>>,

    // S3 feature
    server_side_encryption: Option<String>,
    server_side_encryption_aws_kms_key_id: Option<String>,
    server_side_encryption_customer_algorithm: Option<String>,
    server_side_encryption_customer_key: Option<String>,
    server_side_encryption_customer_key_md5: Option<String>,
    default_storage_class: Option<String>,
    enable_virtual_host_style: bool,
    batch_max_operations: Option<usize>,
    enable_exact_buf_write: bool,

    http_client: Option<HttpClient>,
}

impl Debug for S3Builder {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        let mut d = f.debug_struct("Builder");

        d.field("root", &self.root)
            .field("bucket", &self.bucket)
            .field("endpoint", &self.endpoint)
            .field("region", &self.region);

        d.finish_non_exhaustive()
    }
}

impl S3Builder {
    /// Set root of this backend.
    ///
    /// All operations will happen under this root.
    pub fn root(&mut self, root: &str) -> &mut Self {
        self.root = if root.is_empty() {
            None
        } else {
            Some(root.to_string())
        };

        self
    }

    /// Set bucket name of this backend.
    pub fn bucket(&mut self, bucket: &str) -> &mut Self {
        self.bucket = bucket.to_string();

        self
    }

    /// Set endpoint of this backend.
    ///
    /// Endpoint must be full uri, e.g.
    ///
    /// - AWS S3: `https://s3.amazonaws.com` or `https://s3.{region}.amazonaws.com`
    /// - Aliyun OSS: `https://{region}.aliyuncs.com`
    /// - Tencent COS: `https://cos.{region}.myqcloud.com`
    /// - Minio: `http://127.0.0.1:9000`
    ///
    /// If user inputs endpoint without scheme like "s3.amazonaws.com", we
    /// will prepend "https://" before it.
    pub fn endpoint(&mut self, endpoint: &str) -> &mut Self {
        if !endpoint.is_empty() {
            // Trim trailing `/` so that we can accept `http://127.0.0.1:9000/`
            self.endpoint = Some(endpoint.trim_end_matches('/').to_string())
        }

        self
    }

    /// Region represent the signing region of this endpoint. This is required
    /// if you are using the default AWS S3 endpoint.
    ///
    /// If using a custom endpoint,
    /// - If region is set, we will take user's input first.
    /// - If not, we will try to load it from environment.
    pub fn region(&mut self, region: &str) -> &mut Self {
        if !region.is_empty() {
            self.region = Some(region.to_string())
        }

        self
    }

    /// Set access_key_id of this backend.
    ///
    /// - If access_key_id is set, we will take user's input first.
    /// - If not, we will try to load it from environment.
    pub fn access_key_id(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.access_key_id = Some(v.to_string())
        }

        self
    }

    /// Set secret_access_key of this backend.
    ///
    /// - If secret_access_key is set, we will take user's input first.
    /// - If not, we will try to load it from environment.
    pub fn secret_access_key(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.secret_access_key = Some(v.to_string())
        }

        self
    }

    /// Set role_arn for this backend.
    ///
    /// If `role_arn` is set, we will use already known config as source
    /// credential to assume role with `role_arn`.
    pub fn role_arn(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.role_arn = Some(v.to_string())
        }

        self
    }

    /// Set external_id for this backend.
    pub fn external_id(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.external_id = Some(v.to_string())
        }

        self
    }

    /// Set default storage_class for this backend.
    ///
    /// Available values:
    /// - `DEEP_ARCHIVE`
    /// - `GLACIER`
    /// - `GLACIER_IR`
    /// - `INTELLIGENT_TIERING`
    /// - `ONEZONE_IA`
    /// - `OUTPOSTS`
    /// - `REDUCED_REDUNDANCY`
    /// - `STANDARD`
    /// - `STANDARD_IA`
    pub fn default_storage_class(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.default_storage_class = Some(v.to_string())
        }

        self
    }

    /// Set server_side_encryption for this backend.
    ///
    /// Available values: `AES256`, `aws:kms`.
    ///
    /// # Note
    ///
    /// This function is the low-level setting for SSE related features.
    ///
    /// SSE related options should be set carefully to make them works.
    /// Please use `server_side_encryption_with_*` helpers if even possible.
    pub fn server_side_encryption(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.server_side_encryption = Some(v.to_string())
        }

        self
    }

    /// Set server_side_encryption_aws_kms_key_id for this backend
    ///
    /// - If `server_side_encryption` set to `aws:kms`, and `server_side_encryption_aws_kms_key_id`
    /// is not set, S3 will use aws managed kms key to encrypt data.
    /// - If `server_side_encryption` set to `aws:kms`, and `server_side_encryption_aws_kms_key_id`
    /// is a valid kms key id, S3 will use the provided kms key to encrypt data.
    /// - If the `server_side_encryption_aws_kms_key_id` is invalid or not found, an error will be
    /// returned.
    /// - If `server_side_encryption` is not `aws:kms`, setting `server_side_encryption_aws_kms_key_id`
    /// is a noop.
    ///
    /// # Note
    ///
    /// This function is the low-level setting for SSE related features.
    ///
    /// SSE related options should be set carefully to make them works.
    /// Please use `server_side_encryption_with_*` helpers if even possible.
    pub fn server_side_encryption_aws_kms_key_id(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.server_side_encryption_aws_kms_key_id = Some(v.to_string())
        }

        self
    }

    /// Set server_side_encryption_customer_algorithm for this backend.
    ///
    /// Available values: `AES256`.
    ///
    /// # Note
    ///
    /// This function is the low-level setting for SSE related features.
    ///
    /// SSE related options should be set carefully to make them works.
    /// Please use `server_side_encryption_with_*` helpers if even possible.
    pub fn server_side_encryption_customer_algorithm(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.server_side_encryption_customer_algorithm = Some(v.to_string())
        }

        self
    }

    /// Set server_side_encryption_customer_key for this backend.
    ///
    /// # Args
    ///
    /// `v`: base64 encoded key that matches algorithm specified in
    /// `server_side_encryption_customer_algorithm`.
    ///
    /// # Note
    ///
    /// This function is the low-level setting for SSE related features.
    ///
    /// SSE related options should be set carefully to make them works.
    /// Please use `server_side_encryption_with_*` helpers if even possible.
    pub fn server_side_encryption_customer_key(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.server_side_encryption_customer_key = Some(v.to_string())
        }

        self
    }

    /// Set server_side_encryption_customer_key_md5 for this backend.
    ///
    /// # Args
    ///
    /// `v`: MD5 digest of key specified in `server_side_encryption_customer_key`.
    ///
    /// # Note
    ///
    /// This function is the low-level setting for SSE related features.
    ///
    /// SSE related options should be set carefully to make them works.
    /// Please use `server_side_encryption_with_*` helpers if even possible.
    pub fn server_side_encryption_customer_key_md5(&mut self, v: &str) -> &mut Self {
        if !v.is_empty() {
            self.server_side_encryption_customer_key_md5 = Some(v.to_string())
        }

        self
    }

    /// Enable server side encryption with aws managed kms key
    ///
    /// As known as: SSE-KMS
    ///
    /// NOTE: This function should not be used along with other `server_side_encryption_with_` functions.
    pub fn server_side_encryption_with_aws_managed_kms_key(&mut self) -> &mut Self {
        self.server_side_encryption = Some("aws:kms".to_string());
        self
    }

    /// Enable server side encryption with customer managed kms key
    ///
    /// As known as: SSE-KMS
    ///
    /// NOTE: This function should not be used along with other `server_side_encryption_with_` functions.
    pub fn server_side_encryption_with_customer_managed_kms_key(
        &mut self,
        aws_kms_key_id: &str,
    ) -> &mut Self {
        self.server_side_encryption = Some("aws:kms".to_string());
        self.server_side_encryption_aws_kms_key_id = Some(aws_kms_key_id.to_string());
        self
    }

    /// Enable server side encryption with s3 managed key
    ///
    /// As known as: SSE-S3
    ///
    /// NOTE: This function should not be used along with other `server_side_encryption_with_` functions.
    pub fn server_side_encryption_with_s3_key(&mut self) -> &mut Self {
        self.server_side_encryption = Some("AES256".to_string());
        self
    }

    /// Enable server side encryption with customer key.
    ///
    /// As known as: SSE-C
    ///
    /// NOTE: This function should not be used along with other `server_side_encryption_with_` functions.
    pub fn server_side_encryption_with_customer_key(
        &mut self,
        algorithm: &str,
        key: &[u8],
    ) -> &mut Self {
        self.server_side_encryption_customer_algorithm = Some(algorithm.to_string());
        self.server_side_encryption_customer_key = Some(BASE64_STANDARD.encode(key));
        self.server_side_encryption_customer_key_md5 =
            Some(BASE64_STANDARD.encode(Md5::digest(key).as_slice()));
        self
    }

    /// Set temporary credential used in AWS S3 connections
    ///
    /// # Warning
    ///
    /// security token's lifetime is short and requires users to refresh in time.
    pub fn security_token(&mut self, token: &str) -> &mut Self {
        if !token.is_empty() {
            self.security_token = Some(token.to_string());
        }
        self
    }

    /// Disable config load so that opendal will not load config from
    /// environment.
    ///
    /// For examples:
    ///
    /// - envs like `AWS_ACCESS_KEY_ID`
    /// - files like `~/.aws/config`
    pub fn disable_config_load(&mut self) -> &mut Self {
        self.disable_config_load = true;
        self
    }

    /// Disable load credential from ec2 metadata.
    ///
    /// This option is used to disable the default behavior of opendal
    /// to load credential from ec2 metadata, a.k.a, IMDSv2
    pub fn disable_ec2_metadata(&mut self) -> &mut Self {
        self.disable_ec2_metadata = true;
        self
    }

    /// Allow anonymous will allow opendal to send request without signing
    /// when credential is not loaded.
    pub fn allow_anonymous(&mut self) -> &mut Self {
        self.allow_anonymous = true;
        self
    }

    /// Enable virtual host style so that opendal will send API requests
    /// in virtual host style instead of path style.
    ///
    /// - By default, opendal will send API to `https://s3.us-east-1.amazonaws.com/bucket_name`
    /// - Enabled, opendal will send API to `https://bucket_name.s3.us-east-1.amazonaws.com`
    pub fn enable_virtual_host_style(&mut self) -> &mut Self {
        self.enable_virtual_host_style = true;
        self
    }

    /// Adding a customed credential load for service.
    ///
    /// If customed_credential_load has been set, we will ignore all other
    /// credential load methods.
    pub fn customed_credential_load(&mut self, cred: Box<dyn AwsCredentialLoad>) -> &mut Self {
        self.customed_credential_load = Some(cred);
        self
    }

    /// Specify the http client that used by this service.
    ///
    /// # Notes
    ///
    /// This API is part of OpenDAL's Raw API. `HttpClient` could be changed
    /// during minor updates.
    pub fn http_client(&mut self, client: HttpClient) -> &mut Self {
        self.http_client = Some(client);
        self
    }

    /// Check if `bucket` is valid
    /// `bucket` must be not empty and if `enable_virtual_host_style` is true
    /// it couldn't contain dot(.) character
    fn is_bucket_valid(&self) -> bool {
        if self.bucket.is_empty() {
            return false;
        }
        // If enable virtual host style, `bucket` will reside in domain part,
        // for example `https://bucket_name.s3.us-east-1.amazonaws.com`,
        // so `bucket` with dot can't be recognized correctly for this format.
        if self.enable_virtual_host_style && self.bucket.contains('.') {
            return false;
        }
        true
    }

    /// Build endpoint with given region.
    fn build_endpoint(&self, region: &str) -> String {
        let bucket = {
            debug_assert!(self.is_bucket_valid(), "bucket must be valid");

            self.bucket.as_str()
        };

        let mut endpoint = match &self.endpoint {
            Some(endpoint) => {
                if endpoint.starts_with("http") {
                    endpoint.to_string()
                } else {
                    // Prefix https if endpoint doesn't start with scheme.
                    format!("https://{endpoint}")
                }
            }
            None => "https://s3.amazonaws.com".to_string(),
        };

        // If endpoint contains bucket name, we should trim them.
        endpoint = endpoint.replace(&format!("//{bucket}."), "//");

        // Update with endpoint templates.
        endpoint = if let Some(template) = ENDPOINT_TEMPLATES.get(endpoint.as_str()) {
            template.replace("{region}", region)
        } else {
            // If we don't know where about this endpoint, just leave
            // them as it.
            endpoint.to_string()
        };

        // Apply virtual host style.
        if self.enable_virtual_host_style {
            endpoint = endpoint.replace("//", &format!("//{bucket}."))
        } else {
            write!(endpoint, "/{bucket}").expect("write into string must succeed");
        };

        endpoint
    }

    /// Set maximum batch operations of this backend.
    pub fn batch_max_operations(&mut self, batch_max_operations: usize) -> &mut Self {
        self.batch_max_operations = Some(batch_max_operations);

        self
    }

    /// Enable exact buf write so that opendal will write data with exact size.
    ///
    /// This option is used for services like R2 which requires all parts must be the same size
    /// except the last part.
    pub fn enable_exact_buf_write(&mut self) -> &mut Self {
        self.enable_exact_buf_write = true;

        self
    }

    /// Detect region of S3 bucket.
    ///
    /// # Args
    ///
    /// - endpoint: the endpoint of S3 service
    /// - bucket: the bucket of S3 service
    ///
    /// # Return
    ///
    /// - `Some(region)` means we detect the region successfully
    /// - `None` means we can't detect the region or meeting errors.
    ///
    /// # Notes
    ///
    /// We will try to detect region by the following methods.
    ///
    /// - Match endpoint with given rules to get region
    ///   - Cloudflare R2
    ///   - AWS S3
    ///   - Aliyun OSS
    /// - Send a `HEAD` request to endpoint with bucket name to get `x-amz-bucket-region`.
    ///
    /// # Examples
    ///
    /// ```no_run
    /// use opendal::services::S3;
    ///
    /// # async fn example() {
    /// let region: Option<String> = S3::detect_region("https://s3.amazonaws.com", "example").await;
    /// # }
    /// ```
    ///
    /// # Reference
    ///
    /// - [Amazon S3 HeadBucket API](https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/API/API_HeadBucket.html)
    pub async fn detect_region(endpoint: &str, bucket: &str) -> Option<String> {
        // Remove the possible trailing `/` in endpoint.
        let endpoint = endpoint.trim_end_matches('/');

        // Make sure the endpoint contains the scheme.
        let mut endpoint = if endpoint.starts_with("http") {
            endpoint.to_string()
        } else {
            // Prefix https if endpoint doesn't start with scheme.
            format!("https://{}", endpoint)
        };

        // Remove bucket name from endpoint.
        endpoint = endpoint.replace(&format!("//{bucket}."), "//");
        let url = format!("{endpoint}/{bucket}");

        debug!("detect region with url: {url}");

        // Try to detect region by endpoint.

        // If this bucket is R2, we can return auto directly.
        //
        // Reference: <https://developers.cloudflare.com/r2/api/s3/api/>
        if endpoint.ends_with("r2.cloudflarestorage.com") {
            return Some("auto".to_string());
        }

        // If this bucket is AWS, we can try to match the endpoint.
        if let Some(v) = endpoint.strip_prefix("https://s3.") {
            if let Some(region) = v.strip_suffix(".amazonaws.com") {
                return Some(region.to_string());
            }
        }

        // If this bucket is OSS, we can try to match the endpoint.
        //
        // - `oss-ap-southeast-1.aliyuncs.com` => `oss-ap-southeast-1`
        // - `oss-cn-hangzhou-internal.aliyuncs.com` => `oss-cn-hangzhou`
        if let Some(v) = endpoint.strip_prefix("https://") {
            if let Some(region) = v.strip_suffix(".aliyuncs.com") {
                return Some(region.to_string());
            }

            if let Some(region) = v.strip_suffix("-internal.aliyuncs.com") {
                return Some(region.to_string());
            }
        }

        // Try to detect region by HeadBucket.
        let req = http::Request::head(&url).body(AsyncBody::Empty).ok()?;

        let client = HttpClient::new().ok()?;
        let res = client
            .send(req)
            .await
            .map_err(|err| warn!("detect region failed for: {err:?}"))
            .ok()?;

        debug!(
            "auto detect region got response: status {:?}, header: {:?}",
            res.status(),
            res.headers()
        );

        // Get region from response header no matter status code.
        if let Some(header) = res.headers().get("x-amz-bucket-region") {
            if let Ok(regin) = header.to_str() {
                return Some(regin.to_string());
            }
        }

        // Status code is 403 or 200 means we already visit the correct
        // region, we can use the default region directly.
        if res.status() == StatusCode::FORBIDDEN || res.status() == StatusCode::OK {
            return Some("us-east-1".to_string());
        }

        None
    }
}

impl Builder for S3Builder {
    const SCHEME: Scheme = Scheme::S3;
    type Accessor = S3Backend;

    fn from_map(map: HashMap<String, String>) -> Self {
        let mut builder = S3Builder::default();

        map.get("root").map(|v| builder.root(v));
        map.get("bucket").map(|v| builder.bucket(v));
        map.get("endpoint").map(|v| builder.endpoint(v));
        map.get("region").map(|v| builder.region(v));
        map.get("access_key_id").map(|v| builder.access_key_id(v));
        map.get("secret_access_key")
            .map(|v| builder.secret_access_key(v));
        map.get("security_token").map(|v| builder.security_token(v));
        map.get("role_arn").map(|v| builder.role_arn(v));
        map.get("external_id").map(|v| builder.external_id(v));
        map.get("server_side_encryption")
            .map(|v| builder.server_side_encryption(v));
        map.get("server_side_encryption_aws_kms_key_id")
            .map(|v| builder.server_side_encryption_aws_kms_key_id(v));
        map.get("server_side_encryption_customer_algorithm")
            .map(|v| builder.server_side_encryption_customer_algorithm(v));
        map.get("server_side_encryption_customer_key")
            .map(|v| builder.server_side_encryption_customer_key(v));
        map.get("server_side_encryption_customer_key_md5")
            .map(|v| builder.server_side_encryption_customer_key_md5(v));
        map.get("disable_config_load")
            .filter(|v| *v == "on" || *v == "true")
            .map(|_| builder.disable_config_load());
        map.get("disable_ec2_metadata")
            .filter(|v| *v == "on" || *v == "true")
            .map(|_| builder.disable_ec2_metadata());
        map.get("enable_virtual_host_style")
            .filter(|v| *v == "on" || *v == "true")
            .map(|_| builder.enable_virtual_host_style());
        map.get("allow_anonymous")
            .filter(|v| *v == "on" || *v == "true")
            .map(|_| builder.allow_anonymous());
        map.get("default_storage_class")
            .map(|v: &String| builder.default_storage_class(v));
        map.get("batch_max_operations")
            .map(|v| builder.batch_max_operations(v.parse().expect("input must be a number")));
        map.get("enable_exact_buf_write")
            .filter(|v| *v == "on" || *v == "true")
            .map(|_| builder.enable_exact_buf_write());

        builder
    }

    fn build(&mut self) -> Result<Self::Accessor> {
        debug!("backend build started: {:?}", &self);

        let root = normalize_root(&self.root.take().unwrap_or_default());
        debug!("backend use root {}", &root);

        // Handle bucket name.
        let bucket = if self.is_bucket_valid() {
            Ok(&self.bucket)
        } else {
            Err(
                Error::new(ErrorKind::ConfigInvalid, "The bucket is misconfigured")
                    .with_context("service", Scheme::S3),
            )
        }?;
        debug!("backend use bucket {}", &bucket);

        let default_storage_class = match &self.default_storage_class {
            None => None,
            Some(v) => Some(
                build_header_value(v).map_err(|err| err.with_context("key", "storage_class"))?,
            ),
        };

        let server_side_encryption = match &self.server_side_encryption {
            None => None,
            Some(v) => Some(
                build_header_value(v)
                    .map_err(|err| err.with_context("key", "server_side_encryption"))?,
            ),
        };

        let server_side_encryption_aws_kms_key_id =
            match &self.server_side_encryption_aws_kms_key_id {
                None => None,
                Some(v) => Some(build_header_value(v).map_err(|err| {
                    err.with_context("key", "server_side_encryption_aws_kms_key_id")
                })?),
            };

        let server_side_encryption_customer_algorithm =
            match &self.server_side_encryption_customer_algorithm {
                None => None,
                Some(v) => Some(build_header_value(v).map_err(|err| {
                    err.with_context("key", "server_side_encryption_customer_algorithm")
                })?),
            };

        let server_side_encryption_customer_key =
            match &self.server_side_encryption_customer_key {
                None => None,
                Some(v) => Some(build_header_value(v).map_err(|err| {
                    err.with_context("key", "server_side_encryption_customer_key")
                })?),
            };

        let server_side_encryption_customer_key_md5 =
            match &self.server_side_encryption_customer_key_md5 {
                None => None,
                Some(v) => Some(build_header_value(v).map_err(|err| {
                    err.with_context("key", "server_side_encryption_customer_key_md5")
                })?),
            };

        let client = if let Some(client) = self.http_client.take() {
            client
        } else {
            HttpClient::new().map_err(|err| {
                err.with_operation("Builder::build")
                    .with_context("service", Scheme::S3)
            })?
        };

        // This is our current config.
        let mut cfg = AwsConfig::default();
        if !self.disable_config_load {
            cfg = cfg.from_profile();
            cfg = cfg.from_env();
        }

        if let Some(v) = self.region.take() {
            cfg.region = Some(v);
        }
        if cfg.region.is_none() {
            return Err(Error::new(
                ErrorKind::ConfigInvalid,
                "region is missing. Please find it by S3::detect_region() or set them in env.",
            )
            .with_operation("Builder::build")
            .with_context("service", Scheme::S3));
        }

        let region = cfg.region.to_owned().unwrap();
        debug!("backend use region: {region}");

        // Building endpoint.
        let endpoint = self.build_endpoint(&region);
        debug!("backend use endpoint: {endpoint}");

        // Setting all value from user input if available.
        if let Some(v) = self.access_key_id.take() {
            cfg.access_key_id = Some(v)
        }
        if let Some(v) = self.secret_access_key.take() {
            cfg.secret_access_key = Some(v)
        }
        if let Some(v) = self.security_token.take() {
            cfg.session_token = Some(v)
        }

        let mut loader: Option<Box<dyn AwsCredentialLoad>> = None;
        // If customed_credential_load is set, we will use it.
        if let Some(v) = self.customed_credential_load.take() {
            loader = Some(v);
        }

        // If role_arn is set, we must use AssumeRoleLoad.
        if let Some(role_arn) = self.role_arn.take() {
            // use current env as source credential loader.
            let default_loader = AwsDefaultLoader::new(client.client(), cfg.clone());

            // Build the config for assume role.
            let assume_role_cfg = AwsConfig {
                region: Some(region.clone()),
                role_arn: Some(role_arn),
                external_id: self.external_id.clone(),
                sts_regional_endpoints: "regional".to_string(),
                ..Default::default()
            };
            let assume_role_loader = AwsAssumeRoleLoader::new(
                client.client(),
                assume_role_cfg,
                Box::new(default_loader),
            )
            .map_err(|err| {
                Error::new(
                    ErrorKind::ConfigInvalid,
                    "The assume_role_loader is misconfigured",
                )
                .with_context("service", Scheme::S3)
                .set_source(err)
            })?;
            loader = Some(Box::new(assume_role_loader));
        }
        // If loader is not set, we will use default loader.
        let loader = match loader {
            Some(v) => v,
            None => {
                let mut default_loader = AwsDefaultLoader::new(client.client(), cfg);
                if self.disable_ec2_metadata {
                    default_loader = default_loader.with_disable_ec2_metadata();
                }

                Box::new(default_loader)
            }
        };

        let signer = AwsV4Signer::new("s3", &region);

        let batch_max_operations = self
            .batch_max_operations
            .unwrap_or(DEFAULT_BATCH_MAX_OPERATIONS);
        debug!("backend build finished");
        Ok(S3Backend {
            core: Arc::new(S3Core {
                bucket: bucket.to_string(),
                endpoint,
                root,
                server_side_encryption,
                server_side_encryption_aws_kms_key_id,
                server_side_encryption_customer_algorithm,
                server_side_encryption_customer_key,
                server_side_encryption_customer_key_md5,
                default_storage_class,
                allow_anonymous: self.allow_anonymous,
                enable_exact_buf_write: self.enable_exact_buf_write,
                signer,
                loader,
                client,
                batch_max_operations,
            }),
        })
    }
}

/// Backend for s3 services.
#[derive(Debug, Clone)]
pub struct S3Backend {
    core: Arc<S3Core>,
}

#[async_trait]
impl Accessor for S3Backend {
    type Reader = IncomingAsyncBody;
    type BlockingReader = ();
    type Writer = S3Writers;
    type BlockingWriter = ();
    type Pager = S3Pager;
    type BlockingPager = ();

    fn info(&self) -> AccessorInfo {
        let mut am = AccessorInfo::default();
        am.set_scheme(Scheme::S3)
            .set_root(&self.core.root)
            .set_name(&self.core.bucket)
            .set_native_capability(Capability {
                stat: true,
                stat_with_if_match: true,
                stat_with_if_none_match: true,

                read: true,
                read_can_next: true,
                read_with_range: true,
                read_with_if_match: true,
                read_with_if_none_match: true,
                read_with_override_cache_control: true,
                read_with_override_content_disposition: true,
                read_with_override_content_type: true,

                write: true,
                write_can_empty: true,
                write_can_multi: true,
                write_with_cache_control: true,
                write_with_content_type: true,
                // The min multipart size of S3 is 5 MiB.
                //
                // ref: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html>
                write_multi_min_size: Some(5 * 1024 * 1024),
                // The max multipart size of S3 is 5 GiB.
                //
                // ref: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html>
                write_multi_max_size: if cfg!(target_pointer_width = "64") {
                    Some(5 * 1024 * 1024 * 1024)
                } else {
                    Some(usize::MAX)
                },

                create_dir: true,
                delete: true,
                copy: true,

                list: true,
                list_with_limit: true,
                list_with_start_after: true,
                list_without_delimiter: true,
                list_with_delimiter_slash: true,

                presign: true,
                presign_stat: true,
                presign_read: true,
                presign_write: true,

                batch: true,
                batch_max_operations: Some(self.core.batch_max_operations),

                ..Default::default()
            });

        am
    }

    async fn create_dir(&self, path: &str, _: OpCreateDir) -> Result<RpCreateDir> {
        let mut req = self.core.s3_put_object_request(
            path,
            Some(0),
            &OpWrite::default(),
            AsyncBody::Empty,
        )?;

        self.core.sign(&mut req).await?;

        let resp = self.core.send(req).await?;

        let status = resp.status();

        match status {
            StatusCode::CREATED | StatusCode::OK => {
                resp.into_body().consume().await?;
                Ok(RpCreateDir::default())
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn read(&self, path: &str, args: OpRead) -> Result<(RpRead, Self::Reader)> {
        let resp = self.core.s3_get_object(path, args).await?;

        let status = resp.status();

        match status {
            StatusCode::OK | StatusCode::PARTIAL_CONTENT => {
                let meta = parse_into_metadata(path, resp.headers())?;
                Ok((RpRead::with_metadata(meta), resp.into_body()))
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn write(&self, path: &str, args: OpWrite) -> Result<(RpWrite, Self::Writer)> {
        let writer = S3Writer::new(self.core.clone(), path, args);

        let w = oio::MultipartUploadWriter::new(writer);

        Ok((RpWrite::default(), w))
    }

    async fn copy(&self, from: &str, to: &str, _args: OpCopy) -> Result<RpCopy> {
        let resp = self.core.s3_copy_object(from, to).await?;

        let status = resp.status();

        match status {
            StatusCode::OK => {
                // According to the documentation, when using copy_object, a 200 error may occur and we need to detect it.
                // https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html#API_CopyObject_RequestSyntax
                resp.into_body().consume().await?;

                Ok(RpCopy::default())
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn stat(&self, path: &str, args: OpStat) -> Result<RpStat> {
        // Stat root always returns a DIR.
        if path == "/" {
            return Ok(RpStat::new(Metadata::new(EntryMode::DIR)));
        }

        let resp = self
            .core
            .s3_head_object(path, args.if_none_match(), args.if_match())
            .await?;

        let status = resp.status();

        match status {
            StatusCode::OK => parse_into_metadata(path, resp.headers()).map(RpStat::new),
            StatusCode::NOT_FOUND if path.ends_with('/') => {
                Ok(RpStat::new(Metadata::new(EntryMode::DIR)))
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn delete(&self, path: &str, _: OpDelete) -> Result<RpDelete> {
        let resp = self.core.s3_delete_object(path).await?;

        let status = resp.status();

        match status {
            StatusCode::NO_CONTENT => Ok(RpDelete::default()),
            // Allow 404 when deleting a non-existing object
            // This is not a standard behavior, only some s3 alike service like GCS XML API do this.
            // ref: <https://cloud.google.com/storage/docs/xml-api/delete-object>
            StatusCode::NOT_FOUND => Ok(RpDelete::default()),
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn list(&self, path: &str, args: OpList) -> Result<(RpList, Self::Pager)> {
        Ok((
            RpList::default(),
            S3Pager::new(
                self.core.clone(),
                path,
                args.delimiter(),
                args.limit(),
                args.start_after(),
            ),
        ))
    }

    async fn presign(&self, path: &str, args: OpPresign) -> Result<RpPresign> {
        // We will not send this request out, just for signing.
        let mut req = match args.operation() {
            PresignOperation::Stat(v) => {
                self.core
                    .s3_head_object_request(path, v.if_none_match(), v.if_match())?
            }
            PresignOperation::Read(v) => self.core.s3_get_object_request(path, v.clone())?,
            PresignOperation::Write(_) => self.core.s3_put_object_request(
                path,
                None,
                &OpWrite::default(),
                AsyncBody::Empty,
            )?,
        };

        self.core.sign_query(&mut req, args.expire()).await?;

        // We don't need this request anymore, consume it directly.
        let (parts, _) = req.into_parts();

        Ok(RpPresign::new(PresignedRequest::new(
            parts.method,
            parts.uri,
            parts.headers,
        )))
    }

    async fn batch(&self, args: OpBatch) -> Result<RpBatch> {
        let ops = args.into_operation();
        if ops.len() > 1000 {
            return Err(Error::new(
                ErrorKind::Unsupported,
                "s3 services only allow delete up to 1000 keys at once",
            )
            .with_context("length", ops.len().to_string()));
        }

        let paths = ops.into_iter().map(|(p, _)| p).collect();

        let resp = self.core.s3_delete_objects(paths).await?;

        let status = resp.status();

        if let StatusCode::OK = status {
            let bs = resp.into_body().bytes().await?;

            let result: DeleteObjectsResult =
                quick_xml::de::from_reader(bs.reader()).map_err(new_xml_deserialize_error)?;

            let mut batched_result = Vec::with_capacity(result.deleted.len() + result.error.len());
            for i in result.deleted {
                let path = build_rel_path(&self.core.root, &i.key);
                batched_result.push((path, Ok(RpDelete::default().into())));
            }
            for i in result.error {
                let path = build_rel_path(&self.core.root, &i.key);

                // set the error kind and mark temporary if retryable
                let (kind, retryable) =
                    parse_s3_error_code(i.code.as_str()).unwrap_or((ErrorKind::Unexpected, false));
                let mut err: Error = Error::new(kind, &format!("{i:?}"));
                if retryable {
                    err = err.set_temporary();
                }

                batched_result.push((path, Err(err)));
            }

            Ok(RpBatch::new(batched_result))
        } else {
            Err(parse_error(resp).await?)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_valid_bucket() {
        let bucket_cases = vec![
            ("", false, false),
            ("test", false, true),
            ("test.xyz", false, true),
            ("", true, false),
            ("test", true, true),
            ("test.xyz", true, false),
        ];

        for (bucket, enable_virtual_host_style, expected) in bucket_cases {
            let mut b = S3Builder::default();
            b.bucket(bucket);
            if enable_virtual_host_style {
                b.enable_virtual_host_style();
            }
            assert_eq!(b.is_bucket_valid(), expected)
        }
    }

    #[test]
    fn test_build_endpoint() {
        let _ = tracing_subscriber::fmt().with_test_writer().try_init();

        let endpoint_cases = vec![
            Some("s3.amazonaws.com"),
            Some("https://s3.amazonaws.com"),
            Some("https://s3.us-east-2.amazonaws.com"),
            None,
        ];

        for endpoint in &endpoint_cases {
            let mut b = S3Builder::default();
            b.bucket("test");
            if let Some(endpoint) = endpoint {
                b.endpoint(endpoint);
            }

            let endpoint = b.build_endpoint("us-east-2");
            assert_eq!(endpoint, "https://s3.us-east-2.amazonaws.com/test");
        }

        for endpoint in &endpoint_cases {
            let mut b = S3Builder::default();
            b.bucket("test");
            b.enable_virtual_host_style();
            if let Some(endpoint) = endpoint {
                b.endpoint(endpoint);
            }

            let endpoint = b.build_endpoint("us-east-2");
            assert_eq!(endpoint, "https://test.s3.us-east-2.amazonaws.com");
        }
    }

    #[tokio::test]
    async fn test_detect_region() {
        let cases = vec![
            (
                "aws s3 without region in endpoint",
                "https://s3.amazonaws.com",
                "example",
                Some("us-east-1"),
            ),
            (
                "aws s3 with region in endpoint",
                "https://s3.us-east-1.amazonaws.com",
                "example",
                Some("us-east-1"),
            ),
            (
                "oss with public endpoint",
                "https://oss-ap-southeast-1.aliyuncs.com",
                "example",
                Some("oss-ap-southeast-1"),
            ),
            (
                "oss with internal endpoint",
                "https://oss-cn-hangzhou-internal.aliyuncs.com",
                "example",
                Some("oss-cn-hangzhou-internal"),
            ),
            (
                "r2",
                "https://abc.xxxxx.r2.cloudflarestorage.com",
                "example",
                Some("auto"),
            ),
            (
                "invalid service",
                "https://opendal.apache.org",
                "example",
                None,
            ),
        ];

        for (name, endpoint, bucket, expected) in cases {
            let region = S3Builder::detect_region(endpoint, bucket).await;
            assert_eq!(region.as_deref(), expected, "{}", name);
        }
    }
}
