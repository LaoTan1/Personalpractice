import pandas as pd
from pyecharts import Pie, Grid
import numpy as np
citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
v = []
attrs = []
for i in range(4):
    filename = 'D:/data/' + citys[i] + '_AQI' + '_2018.csv'
    df = pd.read_csv(filename)

    Quality_grade_message = df.groupby(['Quality_grade'])
    Quality_grade_com = Quality_grade_message['Quality_grade'].agg(['count'])
    Quality_grade_com.reset_index(inplace=True)
    # print(Quality_grade_com)
    Quality_grade_com_last = Quality_grade_com.sort_values('count', ascending=False)

    Quality_grade_array = Quality_grade_com_last['Quality_grade']
    Quality_grade_array = np.array(Quality_grade_com_last['Quality_grade'])
    attrs.append(Quality_grade_array)
    Quality_grade_count = Quality_grade_com_last['count']
    Quality_grade_count = np.array(Quality_grade_com_last['count'])
    v.append(Quality_grade_count)

pie1 = Pie("北京", title_pos="28%", title_top="24%")
pie1.add("", attrs[0], v[0], radius=[20, 40], center=[30, 27], legend_pos="63%",
         legend_orient="vertical", is_label_show=True)

pie2 = Pie("上海", title_pos="52%", title_top="24%")
pie2.add("", attrs[1], v[1], radius=[20, 40], center=[54, 27], is_label_show=False, is_legend_show=False)

pie3 = Pie("广州", title_pos="28%", title_top="77%")
pie3.add("", attrs[2], v[2], radius=[20, 40], center=[30, 80], is_label_show=False, is_legend_show=False)

pie4 = Pie("深圳", title_pos="52%", title_top="77%")
pie4.add("", attrs[3], v[3], radius=[20, 40], center=[54, 80], is_label_show=False, is_legend_show=False)

grid = Grid("2018年北上广深全年空气质量情况", width=1200)
grid.add(pie1)
grid.add(pie2)
grid.add(pie3)
grid.add(pie4)
grid.render('2018年北上广深全年空气质量情况.html')