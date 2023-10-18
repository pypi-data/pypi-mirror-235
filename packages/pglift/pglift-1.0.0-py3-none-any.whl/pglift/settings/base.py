import string
from collections.abc import Callable, Iterator
from pathlib import Path, PosixPath
from typing import Any, Union

import pydantic
from pydantic.fields import ModelField

from .._compat import Self


def string_format_variables(fmt: str) -> set[str]:
    return {v for _, v, _, _ in string.Formatter().parse(fmt) if v is not None}


class BaseModel(pydantic.BaseModel):
    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
        smart_union = True


class PrefixedPath(PosixPath):
    basedir = Path("")
    key = "prefix"

    @classmethod
    def __get_validators__(cls) -> Iterator[Callable[..., "PrefixedPath"]]:
        yield cls.validate

    @classmethod
    def validate(cls, value: Path, field: ModelField) -> Self:
        if not isinstance(value, cls):
            value = cls(value)
        # Ensure all template variables used in default field value are also
        # used in user value and that no unhandled variables are used.
        expected = string_format_variables(str(field.default))
        if expected != string_format_variables(str(value)):
            raise ValueError(
                "value contains unknown or missing template variable(s); "
                f"expecting: {', '.join(sorted(expected)) or 'none'}"
            )
        return value

    def prefix(self, prefix: Union[str, Path]) -> Path:
        """Return the path prefixed if is not yet absolute.

        >>> PrefixedPath("documents").prefix("/home/alice")
        PosixPath('/home/alice/documents')
        >>> PrefixedPath("/root").prefix("/whatever")
        PosixPath('/root')
        """
        if self.is_absolute():
            return Path(self)
        assert Path(prefix).is_absolute(), (
            f"expecting an absolute prefix (got {prefix!r})",
        )
        return prefix / self.basedir / self


class ConfigPath(PrefixedPath):
    basedir = Path("etc")


class RunPath(PrefixedPath):
    basedir = Path("")
    key = "run_prefix"


class DataPath(PrefixedPath):
    basedir = Path("srv")


class LogPath(PrefixedPath):
    basedir = Path("log")


def prefix_values(values: dict[str, Any], prefixes: dict[str, Path]) -> dict[str, Any]:
    for key, child in values.items():
        if isinstance(child, PrefixedPath):
            values[key] = child.prefix(prefixes[child.key])
        elif isinstance(child, pydantic.BaseModel):
            child_values = {k: getattr(child, k) for k in child.__fields__}
            child_values = prefix_values(child_values, prefixes)
            # Use .construct() to avoid re-validating child.
            values[key] = child.construct(
                _fields_set=child.__fields_set__, **child_values
            )
    return values


class ServerCert(BaseModel):
    """TLS certificate files for a server."""

    ca_cert: pydantic.FilePath = pydantic.Field(
        description="Certificate Authority certificate to verify client requests."
    )
    cert: pydantic.FilePath = pydantic.Field(
        description="Certificate file for TLS encryption."
    )
    key: pydantic.FilePath = pydantic.Field(
        description="Private key for the certificate."
    )
