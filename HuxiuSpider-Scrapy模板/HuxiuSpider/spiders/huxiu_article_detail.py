import scrapy


class HuxiuArticleDetailSpider(scrapy.Spider):
    name = "huxiu_article_detail"
    allowed_domains = ["api-article.huxiu.com"]
    start_urls = ["https://api-article.huxiu.com"]

    def parse(self, response):
        pass
