import requests
def get_location():
    # 获取本机IP地址
    ip = requests.get('https://api.ipify.org').text
    print(ip)

    # 获取IP地址的城市
    url = 'https://ipapi.co/{}/json/'.format(ip)
    response = requests.get(url)
    data = response.json()
    city = data['city']
    region = data['region']
    country = data['country_name']

    return f'{country} {region} {city}'

print(get_location())