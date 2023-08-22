# SPDX-License-Identifier: MIT
#
# Copyright (c) 2021 The Anvil Extras project team members listed at
# https://github.com/anvilistas/anvil-extras/graphs/contributors
#
# This software is published at https://github.com/anvilistas/anvil-extras

import anvil.js

__version__ = "1.8.1"

_js_uuid = anvil.js.import_from("https://jspm.dev/uuid@8.3.2")
_v4, _parse, _validate = _js_uuid.v4, _js_uuid.parse, _js_uuid.validate


class UUID(str):
    def __init__(self, val):
        if not _validate(val):
            raise ValueError("badly formed hexadecimal UUID string")

    def __repr__(self):
        return f"UUID('{self}')"

    @property
    def bytes(self):
        return _parse(self)


def uuid4():
    """returns a uuid"""
    return UUID(_v4())


if __name__ == "__main__":
    x = uuid4()
    print(repr(x))
    print(x)
    print(x.bytes)
    try:
        UUID("foo")
    except ValueError as e:
        print(f"Succesfully raised - {e!r}")
    else:
        print("Value Error Not Raised")
