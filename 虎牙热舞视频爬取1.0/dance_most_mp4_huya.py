#导入相关包
import requests
from lxml import etree
import json
#主函数
def get_video():
    #U-A伪装及目标网址获取视频的id
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
            }
    url='https://v.huya.com/g/Dance'
    v_ids=[]
    for page in range(1,2):
        params={
            'set_id':'51',
            'order':'mostplay',
            'page':f'{page}'
        }
        response=requests.get(url=url,params=params,headers=headers).text
        tree=etree.HTML(response)
        ids=tree.xpath('//*[@id="root"]/div/article/section/ul[2]/li/@data-vid')
        v_ids.extend(ids)

    #通过视频id获取存储视频信息的json对象
    for v_id in v_ids:
        params={
                'videoId':f'{v_id}'
                }
        link='https://liveapi.huya.com/moment/getMomentContent'
        res=requests.get(link,params=params,headers=headers).text
        js=json.loads(res)

        #通过视频地址在json对象里的位置提取视频地址
        video_url=js["data"]["moment"]["videoInfo"]["definitions"][0]["url"]

        with open(f'./dance_most_mp4_huya_02.03.11/{v_id}.mp4','wb') as f:
            res=requests.get(video_url)
            video=res.content
            f.write(video)
            print(video_url,'下载完毕！')

get_video()