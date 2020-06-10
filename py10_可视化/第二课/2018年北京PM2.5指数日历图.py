import datetime
import pandas as pd
from pyecharts import HeatMap

df = pd.read_csv('D:/data/beijing_AQI_2018.csv')

dom = df[['Date', 'PM']]
list1 = []
for i, j in zip(dom['Date'], dom['PM']):
    time_list = i.split('/')
    time = datetime.date(int(time_list[0]), int(time_list[1]), int(time_list[2]))
    PM = int(j)
    list1.append([str(time), str(PM)])
heatmap = HeatMap("2018年北京PM2.5指数日历图", title_pos='40%', title_top='10',
                  width=800, height=400)
heatmap.add(
    "", list1,
    is_calendar_heatmap=True,
    visual_text_color="#000",
    visual_range_text=["", ""],
    visual_range=[0, 300],
    calendar_cell_size=["auto", 30],
    is_visualmap=True,
    calendar_date_range="2018",
    visual_orient="horizontal",
    visual_pos="26%",
    visual_top="70%",
    is_piecewise=True,
    visual_split_number=5,

)
heatmap.render('2018年北京PM2.5指数日历图.html')