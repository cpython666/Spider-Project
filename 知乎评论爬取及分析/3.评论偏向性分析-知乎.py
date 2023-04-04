with open('comments_chatgpt.csv','r',encoding='utf-8') as f:
    comments=f.read()
comments=comments.split('\n\n')
comments=[comment.split('\t') for comment in comments if comment]

names=[c[0] for c in comments]
headlines=[c[1] for c in comments]
ips=[c[2] for c in comments]
contents=[c[3] for c in comments]
times=[c[4] for c in comments]
dislikes=[c[5] for c in comments]
likes=[c[6] for c in comments]

ip_set=set(ips)

print(f'ip总类别数为：{len(ip_set)}')
print(f'评论总数量：{len(comments)}')

comments.sort(key=lambda x:int(x[6]),reverse=True)
print(comments[:6])

# 时间折线图转化
import datetime

word_dict = {}
for word in times:
    word=datetime.datetime.fromtimestamp(int(word)).strftime("%Y-%m-%d")
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[0], reverse=False)

print(sorted_word_dict)

from snownlp import SnowNLP
res={
    '积极':0,
    '消极':0
}
for text in contents:
    s = SnowNLP(text)
    # 计算情感极性，范围为0到1，越接近1表示越积极
    sentiment_score = s.sentiments
    # 判断情感极性，返回'pos'或'neg'
    if sentiment_score >= 0.5:
        res['积极']+=1
    else:
        res['消极']+=1

print(res)

import pyecharts.options as opts
from pyecharts.charts import Pie

x_data = ["积极", "消极"]
y_data = [res['积极'],res['消极']]
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])

(
    Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
    .add(
        series_name="偏向性",
        data_pair=data_pair,
        rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="评论偏向性分析-知乎",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("评论偏向性分析-知乎.html")
)
