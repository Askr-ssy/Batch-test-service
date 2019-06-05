# -*- encoding: utf-8 -*-

import redis
import os
import builtins
import config

class RedisHelper(object):
    def __init__(self):
        # self.pool=redis.ConnectionPool(host=u_config.REDIS_HOST,port=u_config.REDIS_PORT,password=u_config.REDIS_PASSWORD,db=u_config.REDIA_DB)
        # self.conn=redis.Redis(connection_pool=self.pool)
        self.conn=redis.Redis(host=u_config.REDIS_HOST,port=u_config.REDIS_PORT,password=u_config.REDIS_PASSWORD,db=u_config.REDIA_DB)
        self.sub_name=u_config.REDIS_SUB
    
        if not self.conn.ping():
            raise "redis conn error"


