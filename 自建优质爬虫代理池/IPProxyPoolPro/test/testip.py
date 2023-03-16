import requests
url='http://httpbin.org/ip'
# res=requests.get(url=url).json()
# print(res['origin'])

proxy='61.160.223.141:7302'
proxies = {
    'http': f'http://{proxy}',
    'https': f'https://{proxy}'
}
res=requests.get(url=url,proxies=proxies).json()
print(res)
