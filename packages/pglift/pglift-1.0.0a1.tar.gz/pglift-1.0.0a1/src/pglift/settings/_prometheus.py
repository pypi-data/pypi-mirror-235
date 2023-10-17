import warnings
from typing import Any

from pydantic import Field, FilePath, validator

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

    queriespath: ConfigPath = Field(
        default=ConfigPath("prometheus/postgres_exporter_queries-{name}.yaml"),
        description="Path to the queries file.",
    )

    @validator("queriespath")
    def __queriespath_is_deprecated_(cls, value: Any) -> Any:
        warnings.warn(
            "'queriespath' setting is deprecated and will be removed in the next release",
            FutureWarning,
            stacklevel=2,
        )
        return value

    pid_file: RunPath = Field(
        default=RunPath("prometheus/{name}.pid"),
        description="Path to which postgres_exporter process PID will be written.",
    )
