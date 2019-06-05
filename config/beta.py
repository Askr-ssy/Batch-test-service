# -*- encoding: utf-8 -*-
from .base import BaseConfig

class BetaConfig(BaseConfig):
    MYSQL_HOST=''
    MYSQL_ACCOUNT=''
    MYSQL_PASSWORD=''
    MYSQL_DATABASE=''
    MYSQL_PORT=3306

    # redis链接
    REDIS_HOST='redis.service'
    REDIS_ACCOUNT=''
    REDIS_PASSWORD=None
    REDIS_PORT=6379
    REDIA_DB=0

    # log 
    LOG_LEVEL='INFO'
    LOG_FILE=None

    NLP_URL=""