import scrapy

class HuxiuspiderItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    allinfo=scrapy.Field()

    visited=scrapy.Field()