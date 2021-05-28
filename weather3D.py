# -*- coding:utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map3D, Timeline
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode
import pandas as pd

for year in range(2011,2021):
    data_list_rain  = []
    data_list_sunny = []
    data_list_cloudy = []
    data_list_snow = []
    data_list_others = []
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
    for city in citynames:
        if city == '南京市':
            city_name = 'nanjing'
            latitude = 32.071209
            longitude = 118.806388
        elif city == '徐州市':
            city_name = 'xuzhou'
            latitude = 34.203994
            longitude = 117.283988
        elif city == '宿迁市':
            city_name = 'suqian'
            latitude = 33.963008
            longitude = 118.275162
        elif city == '连云港市':
            city_name = 'lianyungang'
            latitude = 34.59637
            longitude = 119.221573
        elif city == '淮安市':
            city_name = 'huaian'
            latitude = 33.550945
            longitude = 119.112997
        elif city == '盐城市':
            city_name = 'yancheng'
            latitude = 33.34832
            longitude = 120.162417
        elif city == '扬州市':
            city_name = 'yangzhou'
            latitude = 32.394285
            longitude = 119.412868
        elif city == '泰州市':
            city_name = 'taizhou2'
            latitude = 32.528857
            longitude = 119.980546
        elif city == '南通市':
            city_name = 'nantong'
            latitude = 31.981434
            longitude = 120.894671
        elif city == '镇江市':
            city_name = 'zhenjiang'
            latitude = 32.188089
            longitude = 119.424756
        elif city == '常州市':
            city_name = 'changzhou'
            latitude = 31.810916
            longitude = 119.974029
        elif city == '无锡市':
            city_name = 'wuxi'
            latitude = 31.491064
            longitude = 120.311889
        else:
            city_name = 'suzhou'
            latitude = 31.299473
            longitude = 120.585197
        rain = 0
        snow = 0
        cloudy = 0
        sunny = 0
        others = 0
        data = pd.read_csv('weather_' + city_name + '.csv', encoding='gb18030')
        data['日期'] = data['日期'].apply(lambda x: pd.to_datetime(x))
        data['year'] = data['日期'].dt.year
        temp = data[data['year'] == year]['天气'].tolist()
        for i in temp:
            try:
                if '雨' in i:
                    rain = rain + 1
                elif '雪' in i:
                    snow = snow + 1
                elif '晴' in i:
                    sunny = sunny + 1
                elif '云' in i:
                    cloudy = cloudy + 1
                else:
                    others = others + 1
            except:
                pass
        data_list_rain.append((city, [longitude,latitude,rain]))
        data_list_sunny.append((city, [longitude,latitude,sunny]))
        data_list_cloudy.append((city, [longitude,latitude,cloudy]))
        data_list_snow.append((city, [longitude,latitude,snow]))
        data_list_others.append((city, [longitude,latitude,others]))


    m0 = (
        Map3D()
        .add_schema(
            maptype = '江苏',
            itemstyle_opts=opts.ItemStyleOpts(
                color="rgb(5,101,123)",
                opacity=1,
                border_width=0.8,
                border_color="rgb(62,215,213)",
            ),
            map3d_label=opts.Map3DLabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
            ),
            emphasis_label_opts=opts.LabelOpts(
                is_show=False,
                color="#fff",
                font_size=10,
                background_color="rgba(0,255,127,0)",
            ),
            light_opts=opts.Map3DLightOpts(
                main_color="#F5DEB3",
                main_intensity=1.2,
                main_shadow_quality="high",
                is_main_shadow=False,
                main_beta=10,
                ambient_intensity=0.3,
            ),
        )
        .add(
            # maptype = '江苏省',
            series_name="雨天",
            stack='datas',
            data_pair=data_list_rain,
            type_=ChartType.BAR3D,
            bar_size=1,
            shading="lambert",
            label_opts=opts.LabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
            ),
        )
        .add(
            series_name="晴天",
            stack='datas',
            data_pair=data_list_sunny,
            type_=ChartType.BAR3D,
            bar_size=1,
            shading="lambert",
            label_opts=opts.LabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
            ),
        )
        .add(
            series_name="多云",
            stack='datas',
            data_pair=data_list_cloudy,
            type_=ChartType.BAR3D,
            bar_size=1.5,
            shading="lambert",
            label_opts=opts.LabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
            ),
        )
        .add(
            series_name="雪天",
            stack='datas',
            data_pair=data_list_snow,
            type_=ChartType.BAR3D,
            bar_size=2.6,
            shading="lambert",
            label_opts=opts.LabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
            ),
        )
        .add(
            series_name="其它",
            stack='datas',
            data_pair=data_list_others,
            type_=ChartType.BAR3D,
            bar_size=2,
            shading="lambert",
            label_opts=opts.LabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=f'{year}年天气情况分布图'))
    )
    m0.render(f'{year}年天气情况分布图.html')
