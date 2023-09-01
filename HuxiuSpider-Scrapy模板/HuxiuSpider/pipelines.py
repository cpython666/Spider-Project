from itemadapter import ItemAdapter
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

class HuxiuspiderPipeline:
    def __init__(self):
        self.client=MongoClient('localhost',
                      username='spiderdb',
                      password='password',
                      authSource='spiderdb',
                      authMechanism='SCRAM-SHA-1')
        self.db = self.client['spiderdb']
        self.collection = self.db['huxiu_links']

        self.collection.create_index("url", unique=True)

    def process_item(self, item, spider):
        item = dict(item)

        try:
            self.collection.insert_one(item)
        except DuplicateKeyError as e:
            pass

        return item

    def close_spider(self, spider):
        self.client.close()
