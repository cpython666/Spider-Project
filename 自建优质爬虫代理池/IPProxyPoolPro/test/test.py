import config
import requests
import chardet
from lxml import etree
def htmlDownLoad(url='http://www.66ip.cn/1.html'):
    try:
        r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT)
        r.encoding = chardet.detect(r.content)['encoding']
        print(r.encoding)
        if (not r.ok) or len(r.content) < 500:
            raise ConnectionError
        return r.text
    except:
        return False
def parseHtml(text):
    parser={
        'pattern': './/*[@id="main"]/div[1]/div[2]/div[1]/table/tr[position()>1]',
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[4]', 'protocol': ''}
    }
    root=etree.HTML(text)
    proxys=root.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tr[position()>1]')
    for proxy in proxys:
        ip = proxy.xpath(parser['position']['ip'])[0].text
        port = proxy.xpath(parser['position']['port'])[0].text
        # addr= proxy.xpath(parser['position']['port'])[0].text
        print(ip,port)

    return
# parseHtml(htmlDownLoad())
def checkIP():
    proxy='118.31.2.38:8999'
    proxies={
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    res=requests.get(url=config.TEST_IP,headers=config.get_header(),proxies=proxies).json()
    print(res)
    return
# checkIP()
def checkHTTP():
    proxy='118.31.2.38:8999'
    proxies={
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    res=requests.get(url=config.TEST_HTTP_HEADER,headers=config.get_header(),proxies=proxies).json()
    print(res)
    return
# checkHTTP()

def checkHTTPS():
    proxy='36.91.107.245:8080'
    proxies={
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    res=requests.get(url=config.TEST_HTTPS_HEADER,headers=config.get_header(),proxies=proxies).json()
    print(res)
    return
