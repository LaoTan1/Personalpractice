from pymongo import MongoClient
import matplotlib.pyplot as plt
import matplotlib
import re

# 连接MongoDB数据库
client = MongoClient('localhost', 27017)
db = client.get_database("lianjia")
col = db.get_collection("loupan")

# 对地区分组计算平均房价和最高房价
groupPipeline = [
    {"$group":
        {
            "_id": "$area",
            "avgPrice": {"$avg": "$price"},
            "MaxPrice": {"$max": "$price"}
        }
    },
]

# 设置match和group分组聚合管道得到城市每个区住房的房价信息
pipeline = [
    {"$match":
        {
            "type": "住宅",
            "price": {"$ne": 0}
        }
    },
    {"$group":
        {
            "_id": "$area",
            "avgPrice": {"$avg": "$price"},
            "MaxPrice": {"$max": "$price"}
        }
    },
]
# 设置match和group分组聚合管道得到城市某区各街道住房的房价信息
areaPipeline = [
    {"$match":
        {
            "type": "住宅",
            "area": "武昌",
            "price": {"$ne": 0}
        }
    },
    {"$group":
        {
            "_id": "$detail_area",
            "avgPrice": {"$avg": "$price"},
            "MaxPrice": {"$max": "$price"}
        }
    },
]
# 进行聚合计算操作
lists = col.aggregate(pipeline)
label_list = []
num_list1 = []
num_list2 = []
# 获取聚合后的数据并插入label_list ，num_list1，num_list2，用于纵横坐标显示。
for list in lists:
    label_list.append(list['_id'])
    num_list1.append(round(list['avgPrice'], 1))
    num_list2.append(list['MaxPrice'])

# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
x = range(len(num_list1))

# 绘制条形图 :条形中点横坐标；height:长条形高度；width:长条形宽度，默认值0.8；label:为后面设置legend准备
rects1 = plt.bar(x, height=num_list1, width=0.4, alpha=0.8, color='red', label="平均房价")
rects2 = plt.bar([i + 0.4 for i in x], height=num_list2, width=0.4, color='green', label="最高房价")
plt.ylim(0, max(num_list2) + 1000)  # y轴取值范围
plt.ylabel("价格")

# 设置x轴刻度显示值；参数一：中点坐标；参数二：显示值
plt.xticks([index + 0.2 for index in x], label_list)
plt.xlabel("区域")
plt.title("武汉地区房价")
plt.legend()  # 设置题注

for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
# 显示条形图
plt.show()
# 关闭数据库连接
client.close()
