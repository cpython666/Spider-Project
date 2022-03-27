import requests
from random import choice
from lxml import etree
ua=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0']
headers={
        'User-Agent':choice(ua)
            }
while True:
    url=input('请输入目标公众号文章的网址:')
    file_name=input('请输入文件保存的名字:')
    res=requests.get(url=url,headers=headers).text
    tree=etree.HTML(res)
    content_list=tree.xpath('//*[@id="page-content"]//text()')
    str1=' '.join(content_list)
    str1=str1.replace('\n','').replace(' ','')
    str1=str1.replace('。','。\n').replace('！','！\n').replace('？','？\n').replace('；','；\n').replace('：','：\n')
    with open(file_name+'.txt','w',encoding='utf-8') as f:
        f.write(str1)
    print('下载成功!文件位于同级目录下喔~')