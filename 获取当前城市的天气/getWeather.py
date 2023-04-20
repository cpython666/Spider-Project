import json
def getCitys():
    with open('ChinaCityMap.json','r',encoding='utf-8') as f:
        x=f.read()
    citys=json.loads(x)['RECORDS']
    return citys

import requests
def get_location():
    # 获取本机IP地址
    ip = requests.get('https://gwgp-cekvddtwkob.n.bdcloudapi.com/ip/local/geo/v1/district?').json()
    return ip['data']['prov']
pro=get_location().replace('省','')
print(f'检测到你现在所处省份为：{pro}')
for city in getCitys():
    if city['省份']==pro:
        pro_=city['省份_']
        break
print(f'检测到你现在所处省份为：{pro_}')
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
base_url='https://www.tianqi.com'
res=requests.get(url=base_url+'/province/'+pro_+'/',headers=headers).text

from lxml import etree
html=etree.HTML(res)

lis=html.xpath("//ul[@class='raweather760']/li")
for li in lis:
    print(''.join(li.xpath('.//text()')).replace('\n','').replace(' ',''),end='\t')
    print(f"详情见{base_url+li.xpath('.//a[1]/@href')[0]}",end='\t')
    print(f"15天天气预报见{base_url+li.xpath('.//a[2]/@href')[0]}")