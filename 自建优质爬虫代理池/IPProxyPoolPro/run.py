from multiprocessing import Process

from time import sleep
from IPProxyPoolPro.spider.Html2Proxies import Html2Proxies
from IPProxyPoolPro.db.RedisHelper import RedisHelper

from IPProxyPoolPro.flaskapp.GetProxy import app
from IPProxyPoolPro import config
from IPProxyPoolPro.TestIP.TestIP import TestIP

testIP=TestIP()
redis = RedisHelper()

def runTestIP():
    testIP.randomTest()

def runSpider():
    Html2Proxies.getProxiesList()
def runFlask():
    app.run(host='0.0.0.0', port=config.API_PORT, debug=False)
if __name__=="__main__":
    p1=Process(target=runSpider)
    p2=Process(target=runFlask)
    p1.start()
    p2.start()
    p_list=[]
    for i in range(config.TEST_NUMBER):
        p=Process(target=runTestIP)
        p.start()
        p_list.append(p)

    p1.join()
    p2.join()
    for i in p_list:
        i.join()


    # process3=Process(runSpider,args=(redis,))

    # print('Process Ended')