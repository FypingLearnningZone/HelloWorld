# -*- coding: UTF-8 -*-
#猫眼电影爬虫，存储为csv格式

import requests
import re
from requests.exceptions import RequestException


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
with open('output.csv', 'a') as file:
    file.write('影片名,主演, , ,上映时间\n')

def html_get(c_url):
    try:
        r = requests.get(c_url,headers=headers)
        if r.status_code == 200:
            html_parser(r)
        else:
            return None
    except:
        RequestException

def html_parser(r):
    html = r.text
    nospace_html = re.sub(r'\s', '', html)
    res = re.findall(r'<dd>.*?title="(.*?)"class.*?<pclass="star">(.*?)</p>.*?<pclass="releasetime">(.*?)</p>.*?</dd>',nospace_html)
    for res_c in res:
        content = res_c[0]+','+res_c[1]+','+res_c[2]
        res_write(content)


def res_write(res):
    with open('output.csv', 'a') as file:
        file.write(res+'\n')

root_url = "http://maoyan.com/board/4?offset={num}"


if __name__ == '__main__':
    for count in range(10):
        c_url = root_url.format(num = count*10)
        print(c_url)
        html_get(c_url)
        print("num:"+str(count)+"....Done")