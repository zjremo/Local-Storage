from pydantic import Field
from pydantic_settings import BaseSettings


from pydantic import Field
from pydantic_settings import BaseSettings


class FlaskConfig(BaseSettings):
    DEBUG: bool = Field(
        default=False,
        validation_alias="DEBUG",
        description="Enable or disable debug mode for the Flask application. Debug mode provides detailed error pages and auto-reloads the server on code changes.",
    )
    APPNAME: str = Field(
        default="Local-Storage",
        validation_alias="APPNAME",
        description="The name of the Flask application. This is used for logging and identifying the application in various contexts.",
    )
    SECRET_KEY: str = Field(
        default="dev",
        validation_alias="FLASK_SECRET_KEY",
        description="A secret key used for securely signing session cookies and other security-related needs. In production, this should be a strong, randomly generated string.",
    )
