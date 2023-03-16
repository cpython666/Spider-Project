import requests
import chardet
from IPProxyPoolPro import config
class Html_Downloader(object):
    @staticmethod
    def download(url):
        try:
            r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT)
            r.encoding = chardet.detect(r.content)['encoding']
            if (not r.ok) or len(r.content) < 500:
                raise ConnectionError
            else:
                return r.text
        except Exception:
            print(f'页面{url}下载error')
            # print(r.text)
            return False