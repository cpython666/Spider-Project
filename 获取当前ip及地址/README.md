# 来源：https://www.ip.cn/
## 接口1 返回某个ip的地址

`https://www.ip.cn/api/index?ip=154.16.180.182&type=1`
方法：

```python
import requests
url='https://www.ip.cn/api/index?ip=154.16.180.182&type=1'
res = requests.get(url=url).json()
print(res)
```
返回值：
`{'rs': 1, 
'code': 0, 
'address': '美国  伊利诺伊 芝加哥 ', 
'ip': '154.16.180.182', 
'isDomain': 0}`

## 返回请求的ip的地址：

https://www.ip.cn/api/index?ip=&type=0

方法：

```python
import requests
url='https://www.ip.cn/api/index?ip=&type=0'

proxy = '154.16.180.182:3128'
proxies = {
    'http': f'http://{proxy}',
    'https': f'https://{proxy}'
}
res = requests.get(url=url,proxies=proxies).json()
print(res)
```



返回值：
`{'rs': 1, `

`'code': 0, `

`'address': '美国  伊利诺伊 芝加哥 ', `

`'ip': '154.16.180.182', `

`'isDomain': 0}`

