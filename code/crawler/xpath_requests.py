#wiki百科爬取


import requests
import csv
from lxml import etree
from requests.exceptions import RequestException

ROOT_URL = 'http://www.mtime.com/top/tv/top100/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'http://127.0.0.1:1087'
}

def get_html(url):
    try:
        r = requests.get(url,headers=headers,proxies=proxies)
        if r.status_code == 200:
            res_text = parser(r)
            write(res_text)
        else:
            return None
    except:
        RequestException

def parser(response):
    html_text = response.text
    html = etree.HTML(html_text)
    result = etree.tostring(html)
    print(result.decode('utf-8'))

    return

def write(res):
    file = open('meng.txt', 'a', encoding='utf-8')
    file.write(res)
    file.close()

def main(num):
    get_html(ROOT_URL)
    print("Done..."+str(num))

if __name__ == '__main__':
    num = 0
    while num <100:
        main(num)
        num = num+1