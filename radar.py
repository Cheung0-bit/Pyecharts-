# -*- coding: utf-8 -*- check
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Radar
from pyecharts.commons.utils import JsCode

v = []
for year in range(2011,2021):
    df = pd.read_csv('weather_nanjing.csv', encoding='gb18030')
    df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x))
    df['year'] = df['日期'].dt.year
    temp = df[df['year'] == year]['风向']
    direction = {
        '东': 0,
        '东北':0,
        '南': 0,
        '东南':0,
        '西': 0,
        '西南':0,
        '北': 0,
        '西北':0
    }

    def a(item):
        for i in direction.keys():
            if i in item:
                direction[i] = direction[i] + 1

    temp.apply(a)
    v.append([[direction['北'],direction['东北'],direction['东'],direction['东南'],direction['南'],direction['西南'],direction['西'],direction['西北']]])
v1 = v[0]
v2 = v[1]
v3 = v[2]
v4 = v[3]
v5 = v[4]
v6 = v[5]
v7 = v[6]
v8 = v[7]
v9 = v[8]
v10 = v[9]
c = (
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="北", max_=200),
            opts.RadarIndicatorItem(name="东北", max_=125),
            opts.RadarIndicatorItem(name="东", max_=350),
            opts.RadarIndicatorItem(name="东南", max_=140),
            opts.RadarIndicatorItem(name="南", max_=300),
            opts.RadarIndicatorItem(name="西南", max_=80),
            opts.RadarIndicatorItem(name="西", max_=115),
            opts.RadarIndicatorItem(name="西北", max_=70),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        # splitarea_opt=opts.SplitAreaOpts(
        #     is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        # ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    .add("2011年", v1)
    .add("2012年", v2)
    .add("2013年", v3)
    .add("2014年", v4)
    .add("2015年", v5)
    .add("2016年", v6)
    .add("2017年", v7)
    .add("2018年", v8)
    .add("2019年", v9)
    .add("2020年", v10)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        legend_opts=opts.LegendOpts(selected_mode="multiple"),
        title_opts=opts.TitleOpts(title="江苏2011-2020年风向雷达图"),
    )
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .render("风向雷达分布图.html")
)