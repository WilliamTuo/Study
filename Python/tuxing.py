import requests
from bs4 import BeautifulSoup
def get_data(url):
    url = 'http://ww.tianqihoubao.com.lishi/guangzhou/month/201901.html'
    resp = requests.get(url)
    # print(resp.text)
    html = resp.content.decode('gbk')
    soup = BeautifulSoup(html,'html.parser')
    print(soup)
    tr_list = soup.find_all('tr')
    print(tr_list)
    for data in tr_list[1:]:#忽略第一个标签
        sub_data = data.text.split()
        print(sub_data)
