# import requests
# url='http://httpbin.org/ip'
# # res=requests.get(url=url).json()
# # print(res['origin'])
# # '43.128.114.47:15218'
# proxy='61.160.223.141:7302'
# proxies = {
#     'http': f'http://{proxy}',
#     'https': f'https://{proxy}'
# }
# res=requests.get(url=url,proxies=proxies).json()
# print(res)
#
import requests

# 代理服务器的地址和端口
pro='43.128.114.47:15454'
proxy = {
    'http': f'http://{pro}',
    'https': f'http://{pro}'
}

# 目标URL
url = 'https://baike.baidu.com/item/马斯克'
# 发送带代理的GET请求
response = requests.get(url, proxies=proxy)
print(response.text)
# 检查响应状态码
if response.status_code == 200:
    # 打印响应内容
    print(response.text)
else:
    print('请求失败，状态码:', response.status_code)