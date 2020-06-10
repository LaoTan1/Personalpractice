import pandas as pd
from pyecharts import Pie

df = pd.read_csv('D:/data/beijing_AQI_2018.csv')

rank_message = df.groupby(['Quality_grade'])
rank_com = rank_message['Quality_grade'].agg(['count'])
rank_com.reset_index(inplace=True)
rank_com_last = rank_com.sort_values('count', ascending=False)
attr = rank_com_last['Quality_grade']
v1 = rank_com_last['count']
pie=Pie('2018年北京全年空气质量情况', title_pos='center', title_top=0)
pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient="vertical", legend_pos="left", legend_top="%10")
pie.render('2018年北京全年空气质量情况.html')