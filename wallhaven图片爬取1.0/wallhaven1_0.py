'''此项目是爬取walllhaven图片网hot板块的图片，由于网页是动态加载的，所以本项目采用把图片目录网页下载到本地开始的。'''
#导入相关的库
import requests
from lxml import etree
import os
#img_url_list用于存放所有图片的详情页
img_url_list=[]
#headers用于U-A伪装
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
            }
#将本地的wallhaven网站hot图片目录用etree实例化为一个对象
tree=etree.parse('./wall.html',etree.HTMLParser())
#page_list存放页面列表
page_list=tree.xpath('//*[@id="thumbs"]/section')
#记录已经下载图片数量
count=1
#遍历page_list，分别对其中的图片详情页发起请求
#本地文件wall.html共26页，本项目只爬取了1-19页
for page in range(1,20):
    li_list=page_list[page].xpath('./ul/li')
    for li in li_list:
        #分别对图片详情页请求之后实例化对象并且提取图片源地址
        tree=etree.HTML(requests.get(url=li.xpath('./figure/a/@href')[0],headers=headers).text)
        img_url=tree.xpath('//*[@id="wallpaper"]/@src')
        #如果爬取到图片源地址
        if img_url:
            img_url=img_url[0]
            img_url_list.append(tree.xpath('//*[@id="wallpaper"]/@src')[0])
            #对源地址请求获取图片二进制形式
            file=requests.get(img_url).content
            file_name=img_url.split('-')[-1]
            #文件夹不存在则新建
            if 'wallhaven_hot_20' not in os.listdir('./'):
                os.makedirs('wallhaven_hot_20')
            #持久化存储
            with open('./wallhaven_hot_20/'+file_name,'wb') as f:
                f.write(file)
            print(f'第{count}张图片下载完成'+img_url.split('-')[-1],'下载完成...')
            count+=1