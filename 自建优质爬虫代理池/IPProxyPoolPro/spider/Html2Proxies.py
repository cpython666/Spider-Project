from IPProxyPoolPro.spider.HtmlDownLoader import Html_Downloader

from IPProxyPoolPro.spider.HtmlPraser import HtmlPraser
from IPProxyPoolPro import config
from IPProxyPoolPro.db.RedisHelper import RedisHelper
from time import sleep

class Html2Proxies(object):
    @staticmethod
    def getProxiesList():

        '''
        遍历解析器
        :param redis: 接受一个redishelper对象用来实时存储代理
        :return: 无返回值
        '''
        while True:

            redis=RedisHelper()
            # 每次运行项目先清理掉之前项目运行的代理
            redis.clear()
            for parser in config.parserList:
                for url in parser['urls']:
                    response=Html_Downloader.download(url)
                    if response and parser['type']=='xpath':
                        proxies=HtmlPraser.XpathPraser(response,parser)
                        for proxy in proxies:
                            redis.add(proxy)

                        print(f'此{url}共有{len(proxies)}条代理存储完毕~,目前共计{redis.count()}条代理')
                    else:
                        print(f'此{url}页面爬取解析失败~')

                    while True:
                        count=redis.count()
                        if count >=config.MAX_PROXY_NUMBER:
                            print(f'目前代理{count}已达到所设置存储上限，停止爬取。。。。。。')
                            sleep(30)
                        else:
                            break
            print('数据已爬取完毕')
            break

if __name__ =="__main__":
    print(Html2Proxies.getProxiesList())