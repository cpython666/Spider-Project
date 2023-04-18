import requests
url='http://ipinfo.io'
res=requests.get(url=url).json()
print(res)