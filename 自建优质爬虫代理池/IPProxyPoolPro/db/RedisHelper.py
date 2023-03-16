from IPProxyPoolPro import config
import redis
class RedisHelper(object):
    def __init__(self):
        self.host=config.DB_CONFIG['redis']['HOST']
        self.port=config.DB_CONFIG['redis']['PORT']
        self.db=config.DB_CONFIG['redis']['DB']
        self.password=config.DB_CONFIG['redis']['PASSWORD']
        self.pool=redis.ConnectionPool(host=self.host,port=self.port,db=self.db,password=self.password,decode_responses=True)

        self.redis_key=config.DB_CONFIG['redis']['REDIS_KEY']

        self.r=redis.StrictRedis(connection_pool=self.pool)

        self.default_sore=config.DEFAULT_SORE
        self.add_step=config.ADD_STEP
        self.decrease_step=config.DECREASE_STEP



    def clear(self):
        self.r.delete(self.redis_key)

    def count(self):
        return self.r.zcard(self.redis_key)

    def all(self):
        return self.r.zrevrange(self.redis_key,0,-1,withscores=True)

    def add(self, proxy):
        if self.r.zscore(self.redis_key,proxy):
            return self.r.zadd(self.redis_key,{proxy:100})
        else:
            return self.r.zadd(self.redis_key,{proxy:self.default_sore})

    def decrease(self,proxy):
        score= self.r.zincrby(self.redis_key,-1*self.decrease_step, proxy)
        if score<=0:
            self.r.zrem(self.redis_key,proxy)

    def getMax(self):
        ls=self.r.zrevrangebyscore(self.redis_key,100,100)
        return ls

if __name__ == "__main__":
    redisHelper=RedisHelper()
    for i in range(3):
        redisHelper.add(f'k{i}')

    redisHelper.count()


    redisHelper.all()
    redisHelper.decrease('k2')
    redisHelper.add('k1')
