# 前言
😎🥳😎🤠😮🤖🙈💭🍳🍱

知乎评论爬虫

本贴仅作学习交流笔记使用，请勿用于非法途径

---
# 主要内容
🦞🦐🦀🦑🦪
如何爬到关于某个话题的文章的评论

分析逻辑：
某乎登陆后搜索某个关键字，到文章搜索结果页面，

文章只显示十几条，下滑触底加载更多文章，可一直下滑，直到没有更多相关话题文章，此时复制整个页面，到时候正则提取出文章评论的接口id

点击显示评论，观看网络发现请求评论的接口主要只需要一个文章评论的id，

接口返回数据paging里有一个isend标识是否是此文章评论的最后一页评论，有一个next记录此文章评论的下一页评论，所以只要isend不为true，就一直请求next里的接口


详细代码如下：

```python
import requests
import re
import time
times=[i/5+0.5 for i in range(6)]

def addComment(comment):
    # 用户个人介绍，昵称，ip
    ip_text = '未知ip'
    if comment['comment_tag']:
        for i in comment['comment_tag']:
            if i['type'] == 'ip_info':
                ip_text = i['text']
    c = {
        'author_headline': comment['author'].get('headline', '') or '无',
        'author_name': comment['author']['name'],
        'author_ip': ip_text,
        'content': comment['content'],
        'created_time': comment['created_time'],
        'dislike_count': comment['dislike_count'],
        'like_count': comment['like_count']
    }
    comments_list.append(c)

    comment_count=comment.get('child_comments',[])
    for j in range(len(comment_count)):
        addComment(comment['child_comments'][j])


def getComments(url):
    time.sleep(0.2)
    res = requests.get(url).json()

    totals = res['paging']['totals']

    isend = res['paging']['is_end']
    next = res['paging']['next']
    data = res['data']
    print(f'本文章共有{totals}条评论')
    print(f'本接口{url}有{len(data)}条评论')
    print(f'共爬取{len(comments_list)}条评论')
    for comment in data:
        # 用户个人介绍，昵称，ip
        addComment(comment)
    if not isend:
        getComments(next)


with open('知乎_文章_chatgpt.html','r',encoding='utf-8') as f:
    page=f.read()

ids=re.findall('class="ContentItem AnswerItem" name="(.*?)"',page)
ids=list(set(ids))
comments_list=[]
for id in ids:
    print(f'正在爬取第{ids.index(id)+1}个文章的评论')
    url=f'https://www.zhihu.com/api/v4/comment_v5/answers/{id}/root_comment?order_by=score&limit=20'
    getComments(url)
    time.sleep(2)

print(comments_list)

f=open('comments_chatgpt.csv','a',encoding='utf-8')

for c in comments_list:
    # 用户昵称，用户个人介绍，用户ip，评论内容，评论时间，评论点赞数量，评论点踩数量
    f.write(f'{c["author_name"]}\t{c["author_headline"]}\t{c["author_ip"]}\t{c["content"]}\t{c["created_time"]}\t{c["dislike_count"]}\t{c["like_count"]}\n\n')
```





---
# 总结
🐋 🐬 🐶 🐳 🐰 🦀☝️ ⭐ 👉 👀

如果你对这篇文章感兴趣，欢迎在评论区留言，分享你的想法和建议。如果你喜欢我的博客，请记得点赞、收藏和关注我，我会持续更新更多有用的网页技巧和教程。谢谢大家！

---
# 更多宝藏
🍇🍉🍊🍏🍋🍅🥝🥥🫒🫕🥗
项目仓库看这里🤗：
[https://github.com/w-x-x-w](https://github.com/w-x-x-w)
[https://gitee.com/w-_-x](https://gitee.com/w-_-x)
博客文章看这里🤭：
[https://blog.csdn.net/weixin_62650212](https://blog.csdn.net/weixin_62650212)
视频推送看这里🤤：
[https://space.bilibili.com/1909782963](https://space.bilibili.com/1909782963)