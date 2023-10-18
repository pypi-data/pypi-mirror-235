from __future__ import annotations

import builtins
import importlib.resources
import sys
from typing import Any

if sys.version_info[:2] >= (3, 10):
    zip = builtins.zip
else:

    def zip(*iterables: Any, strict: bool = False) -> Any:
        return builtins.zip(*iterables)


if sys.version_info[:2] >= (3, 11):
    from typing import Self

    def read_resource(pkgname: str, name: str) -> str | None:
        resource = importlib.resources.files(pkgname).joinpath(name)
        if resource.is_file():
            return resource.read_text()
        return None

else:
    from typing_extensions import Self

    def read_resource(pkgname: str, name: str) -> str | None:
        if importlib.resources.is_resource(pkgname, name):
            return importlib.resources.read_text(pkgname, name)
        return None


__all__ = [
    "Self",
    "read_resource",
    "zip",
]
