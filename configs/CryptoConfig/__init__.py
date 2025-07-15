from pydantic import Field
from pydantic_settings import BaseSettings

class CryptoConfig(BaseSettings):
    CRYPTO_KEY: str = Field(default='', env='AES_KEY')