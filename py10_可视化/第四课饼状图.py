from pyecharts import Pie
import pandas as pd

vote_result = pd.read_csv('vote_result.csv')
data_x = vote_result['Area_of_interest']
data_y = vote_result['Votes']

pie = Pie(title="饼图示例-用户感兴趣领域", title_pos='left',
          subtitle="以下是读者的投票结果。\n读者对金融、医疗保健、市场业3个领域最感兴趣。")
pie.add("系列1", data_x, data_y, center=[60, 60], legend_orient="vertical", legend_pos="right",
        is_label_show=True, is_toolbox_show=False)

pie.render('饼图示例.html')
