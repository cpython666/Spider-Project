with open('comments_chatgpt.csv','r',encoding='utf-8') as f:
    comments=f.read()
comments=comments.split('\n\n')
comments=[comment.split('\t') for comment in comments if comment]

others=['新加坡','日本','澳大利亚','美国','印度','冰岛','新西兰','加拿大',
        '巴西','瑞典','英国','马来西亚','澳大利亚','德国','荷兰','瑞士','意大利',
        '法国','莫桑比克', '芬兰','尼日利亚', '韩国', '柬埔寨', '俄罗斯', '北美地区', '澳门', '越南', '西班牙','沙特阿拉伯', '未知']

names=[c[0] for c in comments]
headlines=[c[1] for c in comments]

ips=[c[2].replace('IP 属地','').replace('中国','') for c in comments]
ips=[ip for ip in ips if ip not in others and ip]

contents=[c[3] for c in comments]
times=[c[4] for c in comments]
dislikes=[c[5] for c in comments]
likes=[c[6] for c in comments]

ip_set=set(ips)
print(ip_set)
print(f'ip总类别数为：{len(ip_set)}')
print(f'ip总数量：{len(comments)}')

comments.sort(key=lambda x:int(x[6]),reverse=True)

ip_dict = {}
for ip in ips:
    if ip not in ip_dict:
        ip_dict[ip] = 1
    else:
        ip_dict[ip] += 1

print(ip_dict)
sorted_word_dict = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
# sorted_word_dict=
print(sorted_word_dict)

from pyecharts import options as opts
from pyecharts.charts import Geo

c = (
    Geo()
    .add_schema(maptype="china")
    .add("热度", [list(z) for z in sorted_word_dict],type_='heatmap')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="评论地域性分析-知乎"),
        visualmap_opts=opts.VisualMapOpts(
            min_=1,
            max_=300,
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )

    .render("3.评论地域性分析-知乎.html")
)

# from pyecharts import options as opts
from pyecharts.charts import Bar

d = (
    Bar()
    .add_xaxis([i[0] for i in sorted_word_dict])
    .add_yaxis("热点", [i[1] for i in sorted_word_dict])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="评论地域性分析折线图-知乎"),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("3.评论地域性分析折线图-知乎.html")
)

