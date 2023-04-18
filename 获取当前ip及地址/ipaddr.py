import requests
def fun1():
    url='https://www.ip.cn/api/index?ip=154.16.180.182&type=1'
    res = requests.get(url=url).json()
    print(res)

def fun2():
    url='https://www.ip.cn/api/index?ip=&type=0'

    # proxy = '154.16.180.182:3128'
    # proxies = {
    #     'http': f'http://{proxy}',
    #     'https': f'https://{proxy}'
    # }
    # res = requests.get(url=url,proxies=proxies).json()
    res = requests.get(url=url).json()
    print(res)

try:
    fun1()
    fun2()
except:
    print('error')
    pass