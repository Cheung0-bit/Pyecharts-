#导入模块
import requests
from lxml import etree
import csv

def getWeather(url):
    weather_info = []
    headers = {
        'referer':'https://lishi.tianqi.com/nanjing/index.html',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp_html = etree.HTML(resp.text)
    resp_list = resp_html.xpath("//ul[@class='thrui']/li")

    for li in resp_list:
        day_weather_info = {}
        day_weather_info['data_time'] = li.xpath('./div[1]/text()')[0].split(' ')[0]
        high = li.xpath("./div[2]/text()")[0]
        day_weather_info['high'] = high[:high.find('℃')]
        low = li.xpath("./div[3]/text()")[0]
        day_weather_info['low'] = low[:low.find('℃')]
        if len(li.xpath("./div[4]/text()")) > 0:
            day_weather_info['weather'] = li.xpath("./div[4]/text()")[0]
        else:
            day_weather_info['weather'] = ''
        day_weather_info['wind'] = li.xpath("./div[5]/text()")[0]
        weather_info.append(day_weather_info)

    print(weather_info)
    return weather_info

if __name__ == "__main__":
    weathers = []
    citynames = [
        'nanjing',
        'xuzhou',
        'suqian',
        'lianyungang',
        'huaian',
        'yancheng',
        'yangzhou',
        'taizhou2',
        'nantong',
        'zhenjiang',
        'changzhou',
        'wuxi',
        'suzhou'
    ]
    for cityname in citynames:
        weathers = []
        for Year in range(2011,2021):
            for month in range(1,13):
                if month < 10:
                    weather_time = (str)(Year)+('0'+str(month))
                else :
                    weather_time = (str)(Year)+(str)(month)
                url = f'https://lishi.tianqi.com/{cityname}/{weather_time}.html'
                weather = getWeather(url)
                weathers.append(weather)
        #print(weathers)

            with open(f'weather_{cityname}.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow(['日期', '最高气温', '最低气温', '天气', '风向'])
                writer.writerows([list(day_weather_dict.values()) for month_weather in weathers for day_weather_dict in month_weather])

            # list_year = []
            # for month_weather in weathers:
            #     for day_weather_dict in month_weather:
            #         list_year.append(list(day_weather_dict.values()))
            # writer.writerows(list_year)