from pydantic_settings import BaseSettings
from pydantic import Field


class DbConfig(BaseSettings):
    """
    数据库配置
    """

    MYSQL_HOST: str = Field(
        default="localhost",
        validation_alias="MYSQL_HOST",
        description="The hostname of the MySQL server.",
    )
    MYSQL_PORT: int = Field(
        default=3306,
        validation_alias="MYSQL_PORT",
        description="The port number of the MySQL server.",
    )
    MYSQL_USER: str = Field(
        default="root",
        validation_alias="MYSQL_USER",
        description="The username for MySQL authentication.",
    )
    MYSQL_PASSWORD: str = Field(
        default="123456",
        validation_alias="MYSQL_PASSWORD",
        description="The password for MySQL authentication.",
    )
    MYSQL_DATABASE: str = Field(
        default="local",
        validation_alias="MYSQL_DATABASE",
        description="The name of the MySQL database to connect to.",
    )

    # 动态生成SQLAlchemy URI
    @property
    def sqlalchemy_uri(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
