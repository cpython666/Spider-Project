import requests
def get_location():
    # 获取本机IP地址
    ip = requests.get('https://gwgp-cekvddtwkob.n.bdcloudapi.com/ip/local/geo/v1/district?').json()
    print(ip)

get_location()