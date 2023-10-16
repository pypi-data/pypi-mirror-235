# rasc

For trashing your home directory (or `.config` or `.local/share`, for that
matter).

## Usage

Rasc can be used to handle config or other key-value data that can be
serialized into JSON or Python `dict`.  For config storage, one can use
directly or write a subclass of `storage.Configuration`.  For more generic
data, one can use `storage.Storage` instead.

Besides `json`, one can use different key-value formats by passing `load_func`,
`dump_func` and `ext` into the storage class to replace `json.load` and
`json.dump`.  For example, one can use [`tomllib.load`][tomllib] and
[`tomli_w.dump`][tomli_w], or write custom load/dump functions for SQLite.

[tomllib]: https://docs.python.org/3/library/tomllib.html
[tomli_w]: https://pypi.org/project/tomli-w/

Additionally, a simple CLI command parser is also included in `cli` for
demonstration purpose (with commands `rasc-demo` and `rasc-strict`),
but can also be used directly for your project.  Its usage can be seen in
`rasc/__init__.py` in the source code.

## Copying

This project is licensed under GPL version 3 only.  The license can be found in
`LICENSES/GPL-3.0-only.txt`.
