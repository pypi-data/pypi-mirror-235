from pydantic import Field

from .base import BaseModel, ConfigPath


class Settings(BaseModel):
    """Settings for logrotate."""

    configdir: ConfigPath = Field(
        default=ConfigPath("logrotate.d"), description="Logrotate config directory"
    )
