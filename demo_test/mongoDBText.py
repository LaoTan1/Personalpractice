from pymongo import *

# 获得客户端,建立链接
client = MongoClient("mongodb://localhost:27017/py3")  # 没有那个设置权限的可以 不用写 用户名 和密码 直接写ip 和 端口 就ok了

# 切换数据库
db = client.py3

# 获取集合
stu = db.stu

# 增加  直接insert 也可以
# s = stu.insert_one({"name":"清晨起来开开窗,老婆美美哒"})
# print(s)  这个对象的值是 mongod集合的 _id

# 修改  直接update 也可以
# stu.update_one({"name":"清晨起来开开窗,老婆美美哒"},{"$set":{"name":"老婆美美哒"}})

# 删除  直接delete_one 也可以
# stu.remove({"name":"老婆美美哒"})

# 查询 find_one 只查一条  find 是全部
# cursor = stu.find()  # cursor 是那块数据的地址 find里面可以写条件
# for s in cursor:
#    print(s) # s 是每一个数据的集合 在python3里也就是字典 s 也可以取这个集合的元素 列 s["name"]

# sort根据_id排序 -1逆序 1顺序 记住这里面不是josn 如果是多个属性
# 列[("_id",-1),("name",1)]
# skip(1) 跳过一条数据  limit(1) 显示一条数据
cursor = stu.find({"gender": "无价的老婆大人"}).sort("_id", -1).skip(1).limit(1)

for s in cursor:
    print(s["name"])