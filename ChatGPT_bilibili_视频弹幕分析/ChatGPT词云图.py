import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
# 爬取页面数为1
for page in range(1):
    url=f'https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page={page+1}&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=chatgpt&qv_id=OsLuGCd6UZ6rKzXmoGpSDCZXeSsrOq8F&ad_resource=5654&source_tag=3&category_id=&search_type=video&dynamic_offset=48&w_rid=44bba346f310defe866492c7b867e219&wts=1677047859'
    videos_list=requests.get(headers=headers,url=url).json()

    videos_list=videos_list['data']['result']
# 获取到视频bvid的list
print(videos_list)

print(len(videos_list))

bvid_list=[]
for video in videos_list:
    bvid_list.append(video['bvid'])

print(bvid_list)
# 获取到视频cid的list
cid_list=[]
for i in range(len(bvid_list)):
    cid_url=f'https://api.bilibili.com/x/player/pagelist?bvid={bvid_list[i]}'
    res=requests.get(headers=headers,url=cid_url).json()
    cid_list.append(str(res['data'][0]['cid']))

print(len(cid_list))

print(cid_list)
# 持久化视频的bvid和cid
with open('ChatGpt_bilibili_videos_bvid_cid.txt','w',encoding='utf-8') as f:
    for i in range(len(bvid_list)):
        f.write(f'{bvid_list[i]}\t{cid_list[i]}\n')

import re

result_info=[]
result_detail=[]
for i in range(len(cid_list)):
    danmu_url=f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid_list[i]}'
#     print(danmu_url)
    danmu_page=requests.get(headers=headers,url=danmu_url)
    danmu_page=str(danmu_page.content,'utf-8')
    danmu_tuple_list=re.findall('<d p="(.*?)">(.*?)</d>',danmu_page)
    danmu_info=[i[0] for i in danmu_tuple_list]
    danmu_detail=[i[1] for i in danmu_tuple_list]
    result_info.extend(danmu_info)
    result_detail.extend(danmu_detail)

print(len(result_info))
print(len(result_detail))
# 持久化弹幕的信息和弹幕内容
with open('danmu.txt','w',encoding='utf-8') as f:
    for i in range(len(result_info)):
        f.write(f'{result_info[i]}\t{result_detail[i]}\n')
# 对弹幕进行结巴分词并生成词云
import jieba

result_str=' '.join(result_detail)
res_list=jieba.lcut(result_str)
res_str=' '.join(res_list)

print(res_str)

import imageio
import wordcloud

img=imageio.imread('1.jpg')
wc=wordcloud.WordCloud(
    width=750,height=500,
    prefer_horizontal=1,
    mask=img,
    background_color='white',
    font_path='msyh.ttc',
    stopwords=set([line.strip() for line in open('cn_stopwords.txt', mode='r', encoding='utf-8').readlines()] )
)
wc.generate(res_str)
wc.to_file('base_1_.jpg')