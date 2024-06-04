import locale

from pydantic_settings import BaseSettings, SettingsConfigDict

locale.setlocale(locale.LC_TIME, '')


class Settings(BaseSettings):
    youtube_api_key: str
    mode: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
