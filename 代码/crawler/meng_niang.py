#萌娘百科爬取


import requests
import csv
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

ROOT_URL = 'https://zh.moegirl.org/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def get_html(url):
    try:
        r = requests.get(url,headers=headers)
        if r.status_code == 200:
            res_text = parser(r)
            write(res_text)
        else:
            return None
    except:
        RequestException

def parser(response):
    html_text = response.text
    try:
        soup = BeautifulSoup(html_text, 'html5lib')
        a = soup.select(".firstHeading")
        for i in a:
            name = i.string
        point = soup.find_all("h2")
        desc1 = point[1].find_next_sibling()
        desc2 = desc1.find_next_sibling()
        desc = str(desc1) + str(desc2)
        desc = desc1.get_text() + desc2.get_text()
        res_text ="*****************************\n"+name+"\n\n简介:\n\n"+desc+"\n"
    except:
        pass

    return res_text

# def write(res):
#     file = open('meng.csv', 'a', encoding='utf-8')
#     writer = csv.writer(file, delimiter='*')
#     writer.writerow(res)
#     file.close()
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