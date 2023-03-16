from IPProxyPoolPro import config
from IPProxyPoolPro.spider.HtmlPraser import HtmlPraser
from IPProxyPoolPro.spider.HtmlDownLoader import Html_Downloader
# parser = {
#         'urls': ['http://www.kuaidaili.com/proxylist/%s/' % n for n in range(1, 11)],
#         'type': 'xpath',
#         'pattern': ".//*[@id='freelist']/table/tbody/tr[position()>0]",
#         'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[3]', 'protocol': './td[4]'}
#     }
parser={
    'urls': ['http://www.kuaidaili.com/free/%s/%s/' % (m, n) for m in ['inha', 'intr', 'outha', 'outtr'] for n in
             range(1, 11)],
    'type': 'xpath',
    'pattern': ".//*[@id='list']/table/tbody/tr[position()>0]",
    'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[3]', 'protocol': './td[4]'}
}

for url in parser['urls']:
    response = Html_Downloader.download(url)
    if response and parser['type'] == 'xpath':
        proxies = HtmlPraser.XpathPraser(response, parser)
        print(proxies)
        print(f'此{url}共有{len(proxies)}条代理存储完毕~,')
    else:
        print(f'此{url}页面爬取解析失败~')