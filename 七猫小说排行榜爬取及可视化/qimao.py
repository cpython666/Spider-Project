import warnings

warnings.filterwarnings("ignore", message="Support for.*")

import requests
url='https://www.qimao.com/paihang/boy/hot/date/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
   'cookie':'Hm_lvt_1b6d0fc94c391c78c2fbeda715896432=1684668637; acw_tc=76b20fef16846705288226879e58706706e3cf522e4d2a4fa0945ceff7d33d; acw_sc__v2=646a08400f2b2c54483885c817de8c5c6d519dd4; Hm_lpvt_1b6d0fc94c391c78c2fbeda715896432=1684670530'
}
res=requests.get(url=url,headers=headers).text
# print(res)

from lxml import etree
html=etree.HTML(res)
book_list=html.xpath('//*[@class="rank-list"]/li')
# print('--------------',book_list)
print(len(book_list))
if len(book_list) == 0:
    assert Exception('Cookie已过期，请添加新的Cookie~，获取链接：https://www.qimao.com/paihang/boy/hot/date/')
cnt=5 if len(book_list)>=5 else len(book_list)
cur,name_list,length_list=0,[],[]
for song_div in book_list:
    title=song_div.xpath('./div/div[2]/div/a/text()')
    length=song_div.xpath('./div/div[2]/span[1]/em[6]/text()')
    name_list.append(title[0])
    length_list.append(float(length[0].replace('万字','')))
    print(title,length)
    cur+=1
    if cur>=cnt:
        break
print(name_list)
print(length_list)

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(name_list,length_list)
plt.title("七猫小说大热榜")
plt.xlabel("小说名称")
plt.ylabel("小说字数")
plt.savefig('./qimao_bar.png')
plt.show()
