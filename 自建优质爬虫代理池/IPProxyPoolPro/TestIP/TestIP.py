from IPProxyPoolPro.db.RedisHelper import RedisHelper
import random
from IPProxyPoolPro.utils.checkProxies import doProxy
from time import sleep
class TestIP(object):
    def __init__(self):
        self.redisHelper=RedisHelper()

        print('测试类已开启')

    def randomTest(self):
        while True:
            if self.redisHelper.count()>0:
                proxy_list=self.redisHelper.all()
                for i in range(10):
                    proxy=random.choice(proxy_list)[0]
                    doProxy(self.redisHelper,proxy)
            else:
                sleep(2)


