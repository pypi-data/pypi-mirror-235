import warnings
from typing import Any, Optional

from pydantic import Field, FilePath, validator
from pydantic.fields import ModelField

from .base import BaseModel, ConfigPath, RunPath


class Settings(BaseModel):
    """Settings for Prometheus postgres_exporter"""

    execpath: FilePath = Field(description="Path to the postgres_exporter executable.")

    role: str = Field(
        default="prometheus",
        description="Name of the PostgreSQL role for Prometheus postgres_exporter.",
    )

    configpath: ConfigPath = Field(
        default=ConfigPath("prometheus/postgres_exporter-{name}.conf"),
        description="Path to the config file.",
    )

    queriespath: Optional[ConfigPath] = Field(
        default=None,
        description="Path to the queries file (DEPRECATED).",
    )

    @validator("queriespath")
    def __queriespath_is_deprecated_(cls, value: Any, field: ModelField) -> Any:
        warnings.warn(
            f"{field.name!r} setting is deprecated; make sure the postgres_exporter in use supports this",
            FutureWarning,
            stacklevel=2,
        )
        return value

    pid_file: RunPath = Field(
        default=RunPath("prometheus/{name}.pid"),
        description="Path to which postgres_exporter process PID will be written.",
    )
