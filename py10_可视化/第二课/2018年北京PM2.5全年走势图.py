import pandas as pd
from pyecharts import Line
df = pd.read_csv('D:/data/beijing_AQI_2018.csv')
attr = df['Date']
v1 = df['PM']
line = Line("2018年北京PM2.5全年走势图", title_pos='center',title_top='18',
            width=800, height=400)
line.add("PM2.5值:", attr, v1, mark_line=['average'], is_fill=True,
         area_color="#000", area_opacity=0.3, mark_point=["max", "min"],
         mark_point_symbol="circle", mark_point_symbolsize=25)
line.render("2018年北京PM2.5全年走势图.html")