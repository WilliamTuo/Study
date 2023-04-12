import requests
from bs4 import BeautifulSoup
import json
import csv
base_URL_1_7day = 'http://www.weather.com.cn/weather/'
base_URL_15day = 'http://www.weather.com.cn/weather15d/'
url_end = '.shtml'#连接的结尾
city_ids = {'北京':'101010100'}
url_1day ={}
url_7day ={}
for city_name in city_ids.keys():
    url_7day[city_name] = base_URL_7day + city_ids[city_name] + url_end
    url_15day[city_name] = base_URL_15day + city_ids[city_name] + url_end
print(url_1day)
print(url_7day)
#获取网页的HTML
def getHTML(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('成功访问%s' % url)
        return r.text
    except:
        print('访问错误')
    return''
#从网页获取天气信息
def get_7day_weather_info(hrml):
    weather_1day = []
    bs = BeautifulSoup(html,'html.parser')
    html_body = bs.body
    div_class_leftdiv = html_body.find_all('div',{'class':'left-div'})
    text = div_class_leftdiv[2].find_all('scrip').string
    text = text[text.index('=') + 1:-2]
    print(text)
    jd = json.loads(text)
    day = jd['od']['od2']
    waather_day = []
    count = 0
    for d in day:
        temp = []
        if count <= 24:
            temp.append(d['od21'])
            temp.append(d['od22'])
            temp.append(d['od23'])
            temp.append(d['od24'])
            temp.append(d['od25'])
            temp.append(d['od26'])
            temp.append(d['od27'])
            temp.append(d['od28'])
            weather_day.append(temp)
        count = count+1
    div_id_7d = html_body.find('div', {'id':'7d'})
    ul = div_id_7d.find('ul')
    li = ul.find_all('li')
    i = 0
    for day in li:
        if 0 <= i < 7:
            temp = []
            date =day.find('h1').string
            date =date[0:date.index('日')]
            temp.append(tem_high)
        else:
            tem_high = inf[1].find('span').string
            if tem_high[-1] == '℃':
                temp.append(tem_high)
            else:
                temp.append(tem_high)
        wind = inf[2].find_all('apan')
        i = 0
        for j in wind:
            Temp = j['title']
            temp.append(Temp)
            i += 1
        if i == 1:
            temp.append(Temp)
            i = 0
        wind_scale = inf[2].find('i').string
        indexl = wind_scals.index('级')
        temp.append(int(wind_scale[indexl - 1:indexl]))
        get_7day.append(temp)
    i = i + 1
    return weather_day,weather_7day
# weather_day ,weather_7day = get_7day_weather_info(chongqing_7day_html)
# print(waather_day)
# print(weather_7day) 
def get_15day_weather_info(html):
    weather_info = []
    bs = BeautifulSoup(hrml,'html.parser')
    bady = bs.body
    data= body.find('div',{'id':'15d'})
    ul = data.find('ul')
    li = ul.find_all('li')
    i = 0
    for day in li:
        if i < 8:
            temp = []
            date = day.find('span',{'class':'time'}).string
            date = date[date.index('(') + 1:-2]
            temp.append(weather)
            tem = day.find('span',{'class':'tem'}).text
            temp.append(tem[tem.index('/') - 1])
            wind = day.find('span',{'class':'wind'}),string
            if '转'in wind:
                temp.append(wind[:wind.index('转')])
                temp.append(wind[wind.index('转') + 1:])
            else:
                temp.append(wind)
                temp.append(wind)
            wind_scale = day.find('span',{'class':'wind1'}).string
            index1 = wind_scale.index('级')
            temp.append(int(wind_scale[index1_1:index1]))
            weather_info.append(temp)
    return weather_info
# chongqing_15day_weather_info = get_15day_weather_info(chongqing_15day_hrml)
# peint(chongqing_15day_weather_info)
def wrire_weather_to_csv(file_name,data,day=14):
    with open(file_name,'w+',errors= 'ignore', newline='') as f:
        if day == 14:
            header = ['日期','天气','最低气温','风向1','风向2','风级']
        else:
            header = ['小时','温度','风力方向','风级','群水量','相对温度','空气质量']
    f_csv= csv.writer(f)
    f_csv.writerows(data)

def get_city_allweather_info(city):
    m1,m3 = get_7day_weather_info(getHTML(url_15day[city]))
    m3 = get_15day_weather_info(getHTML(url_15day[city]))
    print(len(m3))
    weather_1day =m1
    weather_15day =m2+m3
    return weather_day,weather_15day

# weather_1day,weather_15day = get_city_all_weather_info('北京')
# print(len(weather_1day))
# print(len(weather_15day))





















      
    













