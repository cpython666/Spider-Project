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