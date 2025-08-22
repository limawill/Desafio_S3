from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration settings.

    This class defines all configurable settings for the
    ChallengeAPI application.
    Settings can be loaded from environment variables or a .env file, with
    default values provided for all configuration options.

    Attributes:
        PORT (int): The port number on which the application will run.
            Default: 5879
        APP_NAME (str): The name of the application.
            Default: "ChallengeAPI"
        DEBUG (bool): Flag indicating whether debug mode is enabled.
            Default: False
        LOG_LEVEL (str): The logging level for the application.
            Default: "INFO"
    """

    PORT: int = 5879
    APP_NAME: str = "ChallengeAPI"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    class Config:
        """
        Pydantic configuration for settings class.
        Configures how settings are loaded and validated.
        """

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
