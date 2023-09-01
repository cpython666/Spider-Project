import json
import time

import scrapy

from HuxiuSpider.items import HuxiuspiderItem


class HuxiuArticleSpider(scrapy.Spider):
    def __init__(self):
        # 'https://www.huxiu.com/article/'
        self.url = 'https://api-article.huxiu.com/web/article/articleList'

    name = "huxiu_article"
    allowed_domains = ["api-article.huxiu.com"]

    def start_requests(self):
        timestamp = str(int(time.time()))
        form_data = {
            "platform": "www",
            "recommend_time": timestamp,
            "pagesize": "22"
        }
        yield scrapy.FormRequest(url=self.url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        item = HuxiuspiderItem()
        res = response.json()
        success = res['success']
        print(res)
        if success:
            data = res['data']
            is_have_next_page = data['is_have_next_page']
            last_dateline = data['last_dateline']
            total_page = data['total_page']
            dataList = data['dataList']

            for data_obj in dataList:
                item['url'] = 'https://www.huxiu.com/article/' + data_obj['aid'] + '.html'
                item['title'] = data_obj['title']
                item['author'] = data_obj['user_info']['username']
                item['allinfo'] = json.dumps(data_obj, ensure_ascii=False)

                item['visited'] = False
                yield item

            if is_have_next_page:
                form_data = {
                    "platform": "www",
                    "recommend_time": str(last_dateline),
                    "pagesize": "22"
                }
                yield scrapy.FormRequest(url=self.url, formdata=form_data, callback=self.parse)
        else:
            raise Exception('请求新闻列表的时候失败了~')
