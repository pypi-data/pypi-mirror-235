# OpenDAL Python Binding

Documentation: [main](https://opendal.apache.org/docs/python/)

This crate intends to build a native python binding.

![](https://github.com/apache/incubator-opendal/assets/5351546/87bbf6e5-f19e-449a-b368-3e283016c887)

## Installation

```bash
pip install opendal
```

## Usage

```python
import opendal

op = opendal.Operator("fs", root="/tmp")
op.write("test.txt", b"Hello World")
print(op.read("test.txt"))
print(op.stat("test.txt").content_length)
```

Or using the async API:

```python
import asyncio

async def main():
    op = opendal.AsyncOperator("fs", root="/tmp")
    await op.write("test.txt", b"Hello World")
    print(await op.read("test.txt"))

asyncio.run(main())
```

## Development

Setup virtualenv:

```shell
python -m venv venv
```

Activate venv:

```shell
source venv/bin/activate
````

Install `maturin`:

```shell
pip install maturin[patchelf]
```

Build bindings:

```shell
maturin develop
```

Run some tests:

```shell
maturin develop -E test
behave tests
```

Build API docs:

```shell
maturin develop -E docs
pdoc opendal
```
