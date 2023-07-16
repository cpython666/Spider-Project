# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 16:56
# @QQ  : 2942581284
# @File    : 08.下载图片.py
import os
import requests
import time
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
if not os.path.exists('imgs'):
    os.mkdir('imgs')
for page in range(1,2):
    response = requests.get(f'https://wallhaven.cc/toplist?page={page}',headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_list=soup.select('section li a[class="preview"]')
    src_list=[i.get('href') for i in img_list]
    print(src_list)
    for url in src_list:
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_url=soup.select('section img[id="wallpaper"]')[0].get('src')
        print(img_url)
        print(f'{url}开始下载。。。')
        response = requests.get(url=img_url, headers=headers)
        with open('imgs/'+img_url.split('/')[-1],'wb') as f:
            f.write(response.content)
        print(f'{url}下载完毕。。。')
        time.sleep(0.8)