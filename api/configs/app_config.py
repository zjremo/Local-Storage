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
        env_file=".flaskenv",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,  # 初始化参数
        env_settings,  # 环境变量中的配置
        dotenv_settings,  # .env文件加载的配置
        file_secret_settings,  # 从文件加载的敏感配置
    ):
        # 定义优先级： .env > init > os.environ > file
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )
