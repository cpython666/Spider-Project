with open('comments_chatgpt.csv','r',encoding='utf-8') as f:
    comments=f.read()
comments=comments.split('\n\n')
comments=[comment.split('\t') for comment in comments if comment]

names=[c[0] for c in comments]
headlines=[c[1] for c in comments]

contents=[c[3] for c in comments]
dislikes=[c[5] for c in comments]
likes=[c[6] for c in comments]
import re
contents=[re.sub('<.*?>','',c) for c in contents]

text=' '.join(contents)+' '.join(headlines)+' '.join(names)

import jieba
from collections import Counter

words = jieba.cut(text) # 进行分词
stopwords=['一个','不是','这个','就是','什么','没有','为了','一下','一种','一股']
words=[i for i in words if i and len(i)>1 and i not in stopwords]
word_count = Counter(words) # 统计词频

print(word_count)
ls=word_count.most_common()
ls = filter(lambda x: '\u4e00' <= x[0] <= '\u9fa5', ls)
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType


words = ls
c = (
    WordCloud()
    .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="5.评论词云分析-知乎"))
    .render("5.评论词云分析-知乎.html")
)
