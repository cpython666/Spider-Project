import requests
import chardet
from lxml import etree
url='https://www.tianqi.com/chinacity.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}
r=requests.get(url=url,headers=headers)
print(chardet.detect(r.content)['encoding'])
r.encoding = chardet.detect(r.content)['encoding']
# r=str(r.content,'utf-8')
# print(r.text)
html=etree.HTML(r.text)
province_box=html.xpath('//div[@class="citybox"]//h2')
city_box=html.xpath('//div[@class="citybox"]//span')
print(len(province_box))
print(len(city_box))

city_list=[]

for i in range(len(province_box)):
    province_name=province_box[i].xpath('.//text()')[0]
    province_name2=province_box[i].xpath('.//a/@href')[0].replace('/','').replace('province','')

    city_name=city_box[i].xpath('.//a/text()')
    city_name2=city_box[i].xpath('.//a/@href')
    for j in range(len(city_name)):
        tmp_name=city_name[j]
        tmp_name2=city_name2[j].replace('/','')
        city={
            '省份':province_name,
            '省份_':province_name2,
            '城市':tmp_name,
            '城市_':tmp_name2
        }
        city_list.append(city)

import pymongo
# 连接 MongoDB
client = pymongo.MongoClient('39.1109', 27017, username='Bnt', password='69', authSource='Bent')
# 获取数据库
db = client['BigData-Mountent']
# 获取集合实例
collection = db["ChinaCityMap"]

l=[]

for i in city_list:
    l.append(i)

res = collection.insert_many(l)
print(res.inserted_ids)
