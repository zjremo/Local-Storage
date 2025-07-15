from pydantic import Field
from pydantic_settings import BaseSettings

class RemoteConfig(BaseSettings):
    REMOTE_CONFIG_URL: str = Field(default='', env='REMOTE_CONFIG_URL')
    REMOTE_CONFIG_TOKEN: str = Field(default='', env='REMOTE_CONFIG_TOKEN')