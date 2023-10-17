from pydantic import Field

from .base import BaseModel, ConfigPath


class Settings(BaseModel):
    """Settings for rsyslog."""

    configdir: ConfigPath = Field(
        default=ConfigPath("rsyslog"), description="rsyslog config directory"
    )
