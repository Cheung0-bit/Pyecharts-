# -*- coding:utf-8 -*-
from pyecharts.charts import Map,Timeline
from pyecharts import options as opts
import pandas as pd

def calculate(city_name,year):
    data = pd.read_csv('weather_'+city_name+'.csv',encoding='gb18030')
    data['日期'] = data['日期'].apply(lambda x: pd.to_datetime(x))
    data['year'] = data['日期'].dt.year
    temp = data[data['year'] == year]['最高气温'].tolist()
    max = -1
    for index, i in enumerate(temp):
        stri = str(i).strip()
        if stri == '-':
            stri = -1
        stri = int(stri)
        if stri > max:
            max = stri

    return max

if __name__ == "__main__":
    timeline = Timeline()
    for year in range(2011,2021):
        citynames = [
            '南京市',
            '徐州市',
            '宿迁市',
            '连云港市',
            '淮安市',
            '盐城市',
            '扬州市',
            '泰州市',
            '南通市',
            '镇江市',
            '常州市',
            '无锡市',
            '苏州市'
        ]
        city_distribution = {}
        for i in citynames:
            if i == '南京市':
                city_name = 'nanjing'
            elif i == '徐州市':
                city_name = 'xuzhou'
            elif i == '宿迁市':
                city_name = 'suqian'
            elif i == '连云港市':
                city_name = 'lianyungang'
            elif i == '淮安市':
                city_name = 'huaian'
            elif i == '盐城市':
                city_name = 'yancheng'
            elif i == '扬州市':
                city_name = 'yangzhou'
            elif i == '泰州市':
                city_name = 'taizhou2'
            elif i == '南通市':
                city_name = 'nantong'
            elif i == '镇江市':
                city_name = 'zhenjiang'
            elif i == '常州市':
                city_name = 'changzhou'
            elif i == '无锡市':
                city_name = 'wuxi'
            else:
                city_name = 'suzhou'
            city_distribution[i] = calculate(city_name,year)
        city = list(city_distribution.keys())
        values = list(city_distribution.values())
        map0 = (
            Map()
            .add('', [list(z) for z in zip(city, values)], '江苏')
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"江苏地区{year}年高温分布图"), visualmap_opts=opts.VisualMapOpts(min_=25,max_=43)
    ))
        timeline.add(map0,f"{year}年")
    timeline.render("江苏地区2011-2020年高温分布轮播图.html")