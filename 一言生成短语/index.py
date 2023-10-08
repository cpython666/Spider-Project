L1=['动画','漫画','游戏','文学','原创','来自网络','其他','影视','诗词','网易云','哲学','抖机灵']

L2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

import random
import requests
import json

url = 'https://v1.hitokoto.cn/?c='
data={
    'saying':[]
}
for i in range(20):
    a = requests.get(url=url+random.choice(L2)).json()
    saying_ = {
        "content": a['hitokoto'],
        'type': a["type"],
        'from': a['from'],
        'from_who': a['from_who'],
        'reviewer': a['reviewer'],
        'length': a['length'],
        '类别':L1[L2.index(a['type'])]
    }
    data['saying'].append(saying_)

with open('saying.json','a',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False)
