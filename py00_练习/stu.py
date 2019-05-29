# -*- coding:utf-8 -*-
# 学生管理系统v4.0

import mysql.connector
from tkinter import *


# 定义学生类
class Student:
    # 类似java的构造器
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    # 相当于java的toString()方法
    def __str__(self):
        msg = "学生信息：id=" + self.id + ",name=" + self.name + ",age=" + self.age
        return msg

    # 获取id
    def getId(self):
        return self.id

    # 获取name
    def getName(self):
        return self.name

    # 获取age
    def getAge(self):
        return self.age

    # 设置name
    def setName(self, name):
        self.name = name

    # 设置age
    def setAge(self, age):
        self.age = age


# 添加学生信息
def addStu():
    "添加学生信息"
    id = input("请输入学生学号：")
    conn = mysql.connector.connect(
        host='localhost', port="6666",
        database="test", user='root',
        passwd='1224'
    )
    cursor = conn.cursor()
    params = [id]
    sql = "select * from stu where id=%s"
    cursor.execute(sql, params)
    stu = cursor.fetchone()
    print("sql返回值：", stu)
    if stu != None:
        if id == stu[0]:
            print("该学号已存在，不能重复添加")
        conn.close()
        return
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    params = [id, name, age]
    sql = "insert into stu(id,name,age) value(%s,%s,%s)"
    cursor.execute(sql, params)  # 把单个学生添加到总列表中
    # 向数据库提交
    conn.commit()
    # 关闭连接
    conn.close()
    print("添加成功:")


# 删除学生信息
def delStu():
    "删除学生信息"
    id = input("请输入要删除的学生学号：")
    conn = mysql.connector.connect(
        host='localhost', port=6666,
        database="test", user='root',
        passwd='1224'
    )
    cursor = conn.cursor()
    params = [id]
    sql = "delete from stu where id=%s;"
    try:
        cursor.execute(sql, params)
        # 向数据库提交
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        conn.rollback()
        conn.close()
        print(e)
        return 1


# 修改学生信息
def updateStu():
    "修改学生信息"
    id = input("请输入要修改的学生学号：")
    conn = mysql.connector.connect(
        host='localhost', port=6666,
        database="test", user='root',
        passwd='1224'
    )
    cursor = conn.cursor()
    params = [id]
    sql = "select * from stu where id=%s"
    cursor.execute(sql, params)
    stu = cursor.fetchone()
    if stu != None:
        if id == stu[0]:
            name = input("请输入要修改的学生姓名：")
            age = input("请输入要修改的学生年龄：")
            sql = "update stu set name=%s,age=%s where id=%s;"
            params = [name, age, id]
            try:
                cursor.execute(sql, params)
                conn.commit()
                conn.close()
                print("修改成功")
            except Exception as e1:
                # 发生错误时回滚
                conn.rollback()
                conn.close()
                print("修改失败")
                print(e1)
            return
    print("找不到该学号，没法修改")


# 查询学生信息
def selectStu():
    "查询学生信息"
    id = input("请输入要查询的学生学号：")
    conn = mysql.connector.connect(
        host='localhost', port=6666,
        database="test", user='root',
        passwd='1224'
    )
    cursor = conn.cursor()
    params = [id]
    sql = "select * from stu where id=%s;"
    cursor.execute(sql, params)
    stu = cursor.fetchone()
    if stu != None:
        student = Student(stu[0], stu[1], stu[2])
        print("查询到的学生信息：", student)
    else:
        print("查询失败，查不到该学生信息")


def main():
    print("==" * 30)
    print("欢迎使用学生管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.退出系统")
    print("==" * 30)
    flag = 0

    while flag != 1:
        step = input("请输入你的操作：")
        step = int(step)
        if step == 1:
            addStu()
        elif step == 2:
            num = delStu()
            if num == 0:
                print("删除成功")
            elif num == 1:
                print("删除失败")
        elif step == 3:
            updateStu()
        elif step == 4:
            selectStu()
        elif step == 5:
            flag = 1
        else:
            print("输入指令错误，请重新输入！！")
    print("退出系统成功")


main()


class MenuDemo:
    def __init__(self):
        self.s = Zsgz()
        self.window = Tk()
        self.window.title("Menu Demo")
        menubar = Menu(self.window)
        self.window.config(menu=menubar)  # Display the menu bar
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operation", menu=operationMenu)
        operationMenu.add_command(label="Draw an oval", command=self.drawOval)
        operationMenu.add_command(label="Draw an rectangle", command=self.drawRectangle)

        exitMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Exit", menu=exitMenu)
        exitMenu.add_command(label="exit", command=self.exit)

        testMenu = Menu(menubar, tearoff=0)
        exitMenu.add_cascade(label="test", menu=testMenu)
        testMenu.add_command(label="item1")
        testMenu.add_command(label="item2")

        textMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Text", menu=textMenu)
        textMenu.add_command(label="text1", command=self.text)
        textMenu.add_command(label="text2", command=self.text)

        mainloop()


class Zsgz(object):
    # 添加学生信息
    def addStu(self):
        "添加学生信息"
        id = input("请输入学生学号：")
        conn = mysql.connector.connect(
            host='localhost', port="6666",
            database="test", user='root',
            passwd='1224'
        )
        cursor = conn.cursor()
        params = [id]
        sql = "select * from stu where id=%s"
        cursor.execute(sql, params)
        stu = cursor.fetchone()
        print("sql返回值：", stu)
        if stu != None:
            if id == stu[0]:
                print("该学号已存在，不能重复添加")
            conn.close()
            return
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        params = [id, name, age]
        sql = "insert into stu(id,name,age) value(%s,%s,%s)"
        cursor.execute(sql, params)  # 把单个学生添加到总列表中
        # 向数据库提交
        conn.commit()
        # 关闭连接
        conn.close()
        print("添加成功:")

    # 删除学生信息
    def delStu(self):
        "删除学生信息"
        id = input("请输入要删除的学生学号：")
        conn = mysql.connector.connect(
            host='localhost', port=6666,
            database="test", user='root',
            passwd='1224'
        )
        cursor = conn.cursor()
        params = [id]
        sql = "delete from stu where id=%s;"
        try:
            cursor.execute(sql, params)
            # 向数据库提交
            conn.commit()
            conn.close()
            return 0
        except Exception as e:
            conn.rollback()
            conn.close()
            print(e)
            return 1

    # 修改学生信息
    def updateStu(self):
        "修改学生信息"
        id = input("请输入要修改的学生学号：")
        conn = mysql.connector.connect(
            host='localhost', port=6666,
            database="test", user='root',
            passwd='1224'
        )
        cursor = conn.cursor()
        params = [id]
        sql = "select * from stu where id=%s"
        cursor.execute(sql, params)
        stu = cursor.fetchone()
        if stu != None:
            if id == stu[0]:
                name = input("请输入要修改的学生姓名：")
                age = input("请输入要修改的学生年龄：")
                sql = "update stu set name=%s,age=%s where id=%s;"
                params = [name, age, id]
                try:
                    cursor.execute(sql, params)
                    conn.commit()
                    conn.close()
                    print("修改成功")
                except Exception as e1:
                    # 发生错误时回滚
                    conn.rollback()
                    conn.close()
                    print("修改失败")
                    print(e1)
                return
        print("找不到该学号，没法修改")

    # 查询学生信息
    def selectStu(self):
        "查询学生信息"
        id = input("请输入要查询的学生学号：")
        conn = mysql.connector.connect(
            host='localhost', port=6666,
            database="test", user='root',
            passwd='1224'
        )
        cursor = conn.cursor()
        params = [id]
        sql = "select * from stu where id=%s;"
        cursor.execute(sql, params)
        stu = cursor.fetchone()
        if stu != None:
            student = Student(stu[0], stu[1], stu[2])
            print("查询到的学生信息：", student)
        else:
            print("查询失败，查不到该学生信息")
