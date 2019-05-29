# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from colorama import Fore, Style
import mysql.connector
import mysql.connector.pooling


# class Student(object):
#     def __init__(self, id, name, adt, ):
#         self.id = id
#         self.name = name
#         self.adt = adt
#
#     def __str__(self):
#         msg = "学生信息：id=" + self.id + ",name=" + self.name + ",adt=" + self.adt
#         return msg
#
#     def getid(self):
#         return self.id
#
#     def getname(self):
#         return self.name
#
#     def getadt(self):
#         return self.adt
#
#     def setName(self, name):
#         self.name = name
#
#     def setAdT(self, adt):
#         self.adt = adt


class Student(object):
    config = {
        'host': 'localhost',
        'port': '6666',
        'database': 'student',
        'password': '1224',
        'user': 'root'
    }
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )

    def addStu(self):
        id = eval(input("请输入要添加的学生学号："))
        con = self.pool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        params = [id]
        sql = "select * from stu where id=%s"
        cursor.execute(sql, params)
        stu = cursor.fetchone()
        print("sql返回值：", stu)
        if stu != None:
            if id == stu[0]:
                print("该学号已存在，不能重复添加")
            con.close()
            return
        name = input("请输入学生姓名：")
        i = None
        while i != 1:
            try:
                age = input("请输入学生入学时间：")
                params = [id, name, age]
                sql = "insert into stu(id,name,adt) value(%s,%s,%s)"
                cursor.execute(sql, params)  # 把单个学生添加到总列表中
                con.commit()
                con.close()
                print("添加成功！")
                i = 1
            except:
                print('学生入学时间输入格式有误')
                con.rollback()
                continue

    def delStu(self):
        id = input("请输入要删除的学生学号：")
        con = self.pool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        params = [id]
        sql = "select * from stu where id=%s"
        cursor.execute(sql, params)
        stu = cursor.fetchone()
        if stu == None:
            print("该学号不存在，删除失败")
            con.close()
            return
        sql = 'delete from stu where id=%s'
        try:
            cursor.execute(sql, params)
            con.commit()
            con.close()
            print('删除成功！')
        except:
            con.rollback()
            print('删除失败！')

    def updateStu(self):
        id = eval(input('请输入要修改的学生学号：'))
        con = self.pool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        params = [id]
        sql = 'select * from stu where id=%s'
        cursor.execute(sql, params)
        stu = cursor.fetchone()
        if stu != None:
            print(stu)
            if id == stu[0]:
                name = input('请输入要修改的学生的姓名：')
                adt = input('请输入要修改的学生的入学日期：')
                sql = 'update stu set name=%s,adt=%s where id=%s'
                params = [name, adt, id]
                try:
                    cursor.execute(sql, params)
                    con.commit()
                    con.close()
                    print('修改成功！')
                except Exception as e:
                    con.rollback()
                    con.close()
                    print('修改失败！')
                    print(e)
                return
        print('找不到该学号，无法修改！')
        con.close()

    def selectStu(self):
        id = input('请输入要查询的学生的学号')
        con = self.pool.get_connection()
        cursor = con.cursor()
        pramas = [id]
        sql = 'select * from stu where id =%s'
        cursor.execute(sql, pramas)
        if cursor != None:
            for one in cursor:
                print('查询到的学生信息：')
                print(one[0], one[1], one[2])
                con.close()
                return
        print("查询失败，查不到该学生信息")
        con.close()

    def printingStu(self):
        con = self.pool.get_connection()
        cursor = con.cursor()
        sql = 'select * from stu'
        cursor.execute(sql)
        if cursor != None:
            for one in cursor:
                print(one[0], one[1], one[2])
                con.close()
                return
        print('学生信息为空')
        con.close()


def main():
    print(Fore.LIGHTBLUE_EX, "\t====================")
    print(Fore.LIGHTBLUE_EX, "\t欢迎使用学生管理系统")
    print(Fore.LIGHTBLUE_EX, "\t====================")
    print(Fore.LIGHTGREEN_EX, "\n\t1.添加学生信息  2.删除学生信息")
    print(Fore.LIGHTGREEN_EX, "\n\t3.修改学生信息  4.查询学生信息")
    print(Fore.LIGHTGREEN_EX, "\n\t5.打印学生信息  6.退出学生系统")
    print(Style.RESET_ALL)

    a = Student()
    while True:
        try:
            temp = eval(input('请输入你的操作：'))
            if temp == 1:
                a.addStu()
            elif temp == 2:
                a.delStu()
            elif temp == 3:
                a.updateStu()
            elif temp == 4:
                a.selectStu()
            elif temp == 5:
                a.printingStu()
            elif temp == 6:
                print('成功退出系统！')
                break
            else:
                print('输入指令错误，请重新输入！！')
        except Exception as e:
            print(e)


main()
