from pydantic import Field
from pydantic_settings import BaseSettings


class RemoteConfig(BaseSettings):
    REMOTE_CONFIG_URL: str = Field(
        default="",
        validation_alias="REMOTE_CONFIG_URL",
        description="URL for fetching remote configuration settings",
    )
