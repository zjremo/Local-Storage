from pydantic import Field
from pydantic_settings import BaseSettings

class CryptoConfig(BaseSettings):
    """加密配置类，用于加载和管理加密相关配置"""
    CRYPTO_KEY: str = Field(
        default='',
        validation_alias='AES_KEY',
        description='AES加密密钥'
    )