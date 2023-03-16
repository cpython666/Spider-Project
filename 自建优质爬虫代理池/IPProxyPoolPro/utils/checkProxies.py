from multiprocessing import Pool
from IPProxyPoolPro.db import RedisHelper
import requests

from IPProxyPoolPro import config
def checkproxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    try:
        res=requests.get(url=config.TEST_IP,headers=config.get_header(),proxies=proxies,timeout=config.TIMEOUT).json()
        # print(res)
        # 可能为高匿
        # {'code': '0x01900012', 'message': 'cannot find token param.'}
        print(res)
        if res['message']:
            print(f'此代理{proxy}可用，为高匿代理')
            return True
        elif res['origin']:
            print(f'此代理{proxy}可用')
            return True
        else:
            print(f'代理{proxy}不可用')
            return False
    except:
        print(f'代理{proxy}不可用------error')
        return False


def doProxy(redis,proxy):
    if checkproxy(proxy):
        redis.add(proxy)
    else:
        redis.decrease(proxy)

# if __name__=="__main__":
#     doProxy(proxy='61.242.134.130')