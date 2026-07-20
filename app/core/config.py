from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME : str
    APP_VERSION : str
    ENVIRONMENT :str

    LLM_PROVIDER : str
    LLM_MODEL : str
    LLM_API_KEY : str
    OPENAI_API_KEY: str
    LOG_LEVEL :str



    model_config = SettingsConfigDict(
    env_file = ".env",
    extra="ignore")

settings = Settings()
