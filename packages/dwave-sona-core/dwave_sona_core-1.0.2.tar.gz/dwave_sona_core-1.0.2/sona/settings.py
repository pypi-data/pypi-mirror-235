import os
from typing import Dict, Optional

from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SONA_INFERENCER_CLASS: str | None = None

    # Storage settings
    SONA_STORAGE_LOCAL_PATH: str = os.getcwd()
    SONA_STORAGE_S3_SETTING: Dict = dict()
    SONA_STORAGE_S3_BUCKET: str = "sona"

    SONA_SOURCE_GOOGLE_SERVICE_ACCOUNT_INFO: Dict | None = None

    # Consumer settings
    SONA_WORKER_CONSUMER_SQS_SETTING: Optional[Dict] = None
    SONA_WORKER_CONSUMER_KAFKA_SETTING: Optional[Dict] = None
    SONA_WORKER_CONSUMER_REDIS_URL: Optional[RedisDsn] = None
    SONA_WORKER_CONSUMER_REDIS_GROUP: Optional[str] = "sona.anonymous"

    # Producer settings
    SONA_WORKER_PRODUCER_SQS_SETTING: Optional[Dict] = None
    SONA_WORKER_PRODUCER_KAFKA_SETTING: Optional[Dict] = None
    SONA_WORKER_PRODUCER_REDIS_URL: Optional[RedisDsn] = None

    # Worker settings
    SONA_WORKER_CLASS: str = "sona.worker.workers.InferencerWorker"
    SONA_WORKER_TOPIC_PREFIX: str = "sona.inferencer."

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
