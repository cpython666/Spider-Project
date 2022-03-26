import requests
import re
all_page=[]
#记录爬取到的弹幕数量
sum=0
#视频发布日期为2.02，截至今天2.26。
for data in range(2,26):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
    url=f'https://api.bilibili.com/x/v1/dm/list.so?oid=499893135&date=2022-02-{data}'
    response=requests.get(url=url,headers=headers)
    response.encoding=response.apparent_encoding
    page_text=response.text
    all_page.append(page_text)
for page in all_page:
    res=re.findall('<d p=".*?">(.*?)</d>',page)
    print('当日有'+str(len(res))+'条弹幕')
    sum += len(res)
    print((f"已装填{sum}条弹幕"))
    #持久化存储弹幕数据
    with open('./danmu.txt','a',encoding='utf-8') as f:
        f.write('\n'.join(res))
    print("ben页打印完毕！")


import imageio
import jieba
import wordcloud
img=imageio.imread('1.png')

f=open('danmu.txt', encoding='utf-8')
text=f.read()

text_list=jieba.lcut(text)
text_str=' '.join(text_list)

'''
font_path : string //字体路径，需要展现什么字体就把该字体路径+后缀名写上，如：font_path = '黑体.ttf'
width : int (default=400) //输出的画布宽度，默认为400像素
height : int (default=200) //输出的画布高度，默认为200像素
prefer_horizontal : float (default=0.90) //词语水平方向排版出现的频率，默认 0.9 （所以词语垂直方向排版出现频率为 0.1)
mask : nd-array or None (default=None) //如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮
罩形状被 mask 取代。除全白（#FFFFFF）的部分将不会绘制，其余部分会用于绘制词云。如：bg_pic = imread('读取一张图片.png')，背
景图片的画布一定要设置为白色（#FFFFFF），然后显示的形状为不是白色的其他颜色。可以用ps工具将自己要显示的形状复制到一个纯白色的画布
上再保存，就ok了。
scale : float (default=1) //按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍。
min_font_size : int (default=4) //显示的最小的字体大小
font_step : int (default=1) //字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差。
max_words : number (default=200) //要显示的词的最大个数
stopwords : set of strings or None //设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
background_color : color value (default=”black”) //背景颜色，如background_color='white',背景颜色为白色。
max_font_size : int or None (default=None) //显示的最大的字体大小
mode : string (default=”RGB”) //当参数为“RGBA”并且background_color不为空时，背景为透明。
relative_scaling : float (default=.5) //词频和字体大小的关联性
color_func : callable, default=None //生成新颜色的函数，如果为空，则使用 self.color_func
regexp : string or None (optional) //使用正则表达式分隔输入的文本
collocations : bool, default=True //是否包括两个词的搭配
colormap : string or matplotlib colormap, default=”viridis” //给每个单词随机分配颜色，若指定color_func
'''

wc=wordcloud.WordCloud(
    width=750,height=500,
    prefer_horizontal=1,
    mask=img,
    background_color='white',
    font_path='msyh.ttc'
)

wc.generate(text_str)

wc.to_file('base_1.png')