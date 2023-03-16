from lxml import etree

class HtmlPraser(object):

    @staticmethod
    def XpathPraser(response,parser):
        '''
        此方法接受网页text源代码，
        xpath方法提取代理
        返回代理列表
        '''
        proxylist = []
        root = etree.HTML(response)
        proxys = root.xpath(parser['pattern'])
        for proxy in proxys:
            try:
                ip = proxy.xpath(parser['position']['ip'])[0].text
                port = proxy.xpath(parser['position']['port'])[0].text
            except Exception as e:
                continue
            proxy = ip+':'+port
            proxylist.append(proxy)
        return proxylist
