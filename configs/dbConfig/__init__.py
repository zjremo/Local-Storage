from pydantic_settings import BaseSettings
from pydantic import Field

# mysql支持
import pymysql
pymysql.install_as_MySQLdb()

class DbConfig(BaseSettings):
    """
    数据库配置
    """
    MYSQL_HOST: str = Field(default='localhost', env='MYSQL_HOST')
    MYSQL_PORT: int = Field(default=3306, env='MYSQL_PORT')
    MYSQL_USER: str = Field(default='root', env='MYSQL_USER')
    MYSQL_PASSWORD: str = Field(default='123456', env='MYSQL_PASSWORD')
    MYSQL_DATABASE: str = Field(default='local', env='MYSQL_DATABASE')
    # 拼接database_url
    SQLALCHEMY_DATABASE_URI: str = Field(
        default=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}",
        env='SQLALCHEMY_DATABASE_URI'
    )
    # 对模型修改监控
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = Field(
        default=False,
        env='SQLALCHEMY_TRACK_MODIFICATIONS'
    )
    

    