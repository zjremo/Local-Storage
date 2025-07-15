from pydantic import Field
from pydantic_settings import BaseSettings

class FlaskConfig(BaseSettings):
    DEBUG: bool = Field(default=False, env='FLASK_DEBUG')
    APPName: str = Field(default='Local-Storage', env='FLASK_APP')
    # 调用flash需要设置密钥，用于session和flash消息
    SECRET_KEY: str = Field(default='123456', env='FLASK_SECRET_KEY')

    
