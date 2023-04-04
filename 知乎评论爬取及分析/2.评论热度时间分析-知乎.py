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
# print(ip_set)
print(f'ip总类别数为：{len(ip_set)}')
print(f'评论总数量：{len(comments)}')


comments.sort(key=lambda x:int(x[6]),reverse=True)
print(comments[:6])

# 时间折线图转化
import datetime

# 将时间戳转换为datetime格式
# dt_object = datetime.datetime.fromtimestamp(timestamp)

# print(len(times))
# print(len(set(times)))

# 格式化输出日期时间字符串
# print(dt_object.strftime("%Y-%m-%d"))

word_dict = {}
for word in times:
    word=datetime.datetime.fromtimestamp(int(word)).strftime("%Y-%m-%d")
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[0], reverse=False)

print(sorted_word_dict)

x_data=[i[0] for i in sorted_word_dict]
y_data=[i[1] for i in sorted_word_dict]
import pyecharts.options as opts
from pyecharts.charts import Line

(
    Line()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="chatgpt热度变化折线图-知乎"),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        is_smooth=False,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("chatgpt热度变化折线图-知乎.html")
)
