import re
import time
import requests
from selenium.webdriver import Chrome
import os
flag=True
while flag:
    print('抖音视频无水印下载-------------------------------------------')
    print('使用说明:--------------------------------------------------')
    print('此程序需要同级目录下有chromwebdriver.exe文件-------------------')
    print('过程中弹出谷歌浏览器为正常现象,不要对浏览器进行关闭操作，它会自动关闭--')
    print('现有chromdriver.exe适用于谷歌浏览器99.0----------------------')
    print('如果闪退则说明浏览器版本与同级目录下的chromdriver.exe文件不兼容----')
    print('如果闪退则需要更换为与你电脑浏览器版本匹配的chromwebdriver.exe----')
    print('chromdriver.exe下载链接:http://chromedriver.storage.googleapis.com/index.html----------')
    print('chromdriver.exe下载链接:https://registry.npmmirror.com/binary.html?path=chromedriver/--')
    print('请输入抖音视频的链接:(格式如:https://www.douyin.com/video/7079562818550238477或https://v.douyin.com/NuTVdRL/)')
    url=input()
    web=Chrome()
    web.get(url)
    time.sleep(1)
    page_text=web.page_source
    web.quit()
    title=re.findall('<title>(.*?)</title>',page_text)[0]
    video_url=re.findall('src(.*?)vr%3D%2',page_text)[1]
    video_url=requests.utils.unquote(video_url).replace('":"','https:')
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    video=requests.get(url=video_url,headers=headers).content
    with open(title+'.mp4','wb') as f:
        f.write(video)
    size=os.path.getsize("./"+title+".mp4")
    size=size/1024/1024
    print(title,"   下载完毕~   ,文件大小为:{:.2f}Mb".format(size))
    print('是否继续下载？(y/n)')
    if input()==n:
        flag=False