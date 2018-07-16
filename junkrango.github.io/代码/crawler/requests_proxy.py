import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
#http 代理
proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'http://127.0.0.1:1087'
}
#socks5代理 需要安装第三方库 pip install requests[socks]
# proxies = {
#     'http': 'socks5://user:pass@host:port',
#     'https': 'socks5://user:pass@host:port'
# }

r = requests.get("https://youtube.com",proxies=proxies,headers=headers)