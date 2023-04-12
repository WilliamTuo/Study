from bs4 import BeautifulSoup
import requests
import os

# 全国 Map 页面
# headersMap= {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
#     'Upgrade-Insecure-Requests':'1',
#     'Referer':'https://weather.cma.cn/web/weather/54511.html',
#     'Host': 'weather.cma.cn',
# }
# respMap = requests.get('https://weather.cma.cn/web/weather/map.html', headers=headersMap)
# htmlMap = respMap.content.decode('utf8')
#print(htmlMap)



def GetBeiJing():
    # 北京市页面
    headersCity={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Upgrade-Insecure-Requests':'1',
        'Referer':'https://weather.cma.cn/',
        'Host': 'weather.cma.cn'
    }

    BeiJingArea = {"北京":54511, 
                   "顺义":54398,
                   "大兴":54594,
                   "密云":54416,
                   "平谷":54424,
                   "延庆":54416,
                   "怀柔":54419,
                   "房山":54596,
                   "昌平":54499,
                   "通州":54431,
                   "门头沟":54505,
                   "丰台":54514,
                   "朝阳":54433,
                   "海淀":54399,
                   "石景山":54513}
    urlBase = "https://weather.cma.cn/web/weather/"
    resp = {}
    # 依次请求每个区的天气情况：
    # for value in BeiJingArea.values():
    #     url = urlBase + '%s.html'%(value)
    #     #print(url)
    #     resp = ReqCityAreaWeather(url, headersCity)
    
    url = urlBase + '%s.html'%(54511)
    resp = ReqCityAreaWeather(url, headersCity)
    htmlCity = resp.content.decode('utf8')
    # print(htmlCity)
    # data = resp.content.decode('utf8')
    # with open('./Weather/weatherCity.html', 'w', encoding='utf-8') as f:
    #     f.write(data)

    # 将 html 内容解析到soup
    soup = BeautifulSoup(htmlCity, 'html.parser')
    # print(soup)
    # with open('./Weather/weatherCitySoup.html', 'w', encoding='utf-8') as f:
    #     f.write(str(soup))

    # 找到今天的天气内容
    todayTemperature = soup.find_all('div', attrs={'class': 'pull-left day actived'})
    for tempratureData in todayTemperature:
        subTem = tempratureData.text.split()
        weekDay = subTem[0]
        date = subTem[1]
        weatherDay = subTem[2]
        weatherNight = subTem[7]
        temprature = ' ~ '.join(subTem[5:7])
        weather = weatherDay + '转' + weatherNight
        windDirDay = subTem[3]
        windDirNight = subTem[8]
        windPowerDay = subTem[4]
        windPowerNeght = subTem[9]
    # 找到今天详细的天气内容
    # 时间（每次增加3小时），天气，温度，降水，风速，风向，气压，湿度，云量
    timeHour, weatherHour, tempratureHour, precipitationHour, windPowerHour, windDirHour, pressureHour, humidity, cloudPercent = [],[],[],[],[],[],[],[],[]
    todayWeatherDetail = soup.find_all('table', attrs={'class': 'hour-table', 'id':'hourTable_0'})
    for weatherDetail in todayWeatherDetail:
        subWeather = weatherDetail.text.split()
        idx = 1
        for i in range(8):
            timeHour.append(subWeather[idx+i])
        # print(timeHour)
        # 每小时的天气情况需要换一种方式去获取
        subWeatherHour = weatherDetail.find_all('td', attrs={'class': 'wicon'})
        for tmpWeather in subWeatherHour:
            weatherImg = tmpWeather.find_all('img')
            srcImg = weatherImg[0].get('src')
            # print(srcImg)
            # /static/img/w/icon/w1.png
            src = os.path.split(srcImg)
            # src = srcImg.split('/')
            # print(src)
            weatherHour.append(src[1])
            # print(weatherImg)
        # print(subWeatherHour)
        print(weatherHour)
        idx = 11
        for i in range(8):
            tempratureHour.append(subWeather[idx+i])   
        # print(tempratureHour)
        idx = 20
        for i in range(8):
            precipitationHour.append(subWeather[idx+i])   
        # print(precipitationHour)
        idx = 29
        for i in range(8):
            windPowerHour.append(subWeather[idx+i])   
        # print(windPowerHour)
        idx = 38
        for i in range(8):
            windDirHour.append(subWeather[idx+i])   
        # print(windDirHour)
        idx = 47
        for i in range(8):
            pressureHour.append(subWeather[idx+i])   
        # print(pressureHour)
        idx = 56
        for i in range(8):
            humidity.append(subWeather[idx+i])
        # print(humidity)          
        idx = 65
        for i in range(8):
            cloudPercent.append(subWeather[idx+i])
        # print(cloudPercent)          
        
def ReqCityAreaWeather(url, header):
    return requests.get(url, headers=header)

def main():
    GetBeiJing()

if __name__ == '__main__':
    main()


