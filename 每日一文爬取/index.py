import requests
from lxml import etree
url='https://meiriyiwen.com/random'
res=requests.get(url=url).text
root=etree.HTML(res)
article=root.xpath('//*[@id="article_show"]')[0]

title=article.xpath('./h1')[0].text
auther=article.xpath('./p/span')[0].text
text=article.xpath('./div')[0]
text = etree.tounicode(text)
print(title)
print(auther)
print(text)