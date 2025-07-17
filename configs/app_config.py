import logging

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from .CryptoConfig import CryptoConfig
from .flaskConfig import FlaskConfig
from .remote_settings import RemoteConfig
from .dbConfig import DbConfig

logger = logging.Logger(__name__)
logger.info("Loading Config")


# 配置项一定要全部大写最后才可以被加载到app.config中使用from_mapping
class CydbConfig(FlaskConfig, RemoteConfig, CryptoConfig, DbConfig):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
