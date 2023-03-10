l1=['动画','漫画','游戏','文学','原创','来自网络','其他','影视','诗词','网易云','哲学','抖机灵']

l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

import requests
import json
data={
    'data':[]
}
url = 'https://v1.hitokoto.cn/?c=i'

for i in range(20):
    a = requests.get(url).json()
    a_ = {
        "content": a['hitokoto'],
        'type': a["type"],
        'from': a['from'],
        'from_who': a['from_who'],
        'reviewer': a['reviewer'],
        'length': a['length'],
        '类别': l1[l2.index(a['type'])]
    }
    data['data'].append(a_)


with open('saying_i.json','a') as f:
    json.dump(data,f)
