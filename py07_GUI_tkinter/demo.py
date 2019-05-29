# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import pymysql
from tkinter import *


class MyDBTest:
    def __init__(self):
        self.con = pymysql.connect(host="localhost_6666", user="root", password="1224", database="TestDb")
        self.loginflag = ""
        w = Tk()
        f = Frame(w)
        f.pack()
        f2 = Frame(w)
        f2.pack()
        self.lbr = Label(f2, text="")
        self.lbr.pack()
        lbname = Label(f, text="用户名")
        self.name = StringVar()
        txname = Entry(f, textvariable=self.name)
        lbpwd = Label(f, text="密码")
        self.pwd = StringVar()
        txpwd = Entry(f, textvariable=self.pwd)
        add = Button(f, text="注册", command=self.adduser)
        log = Button(f, text="登录", command=self.login)

        updbtn = Button(f, text="更新", command=self.updateuser)
        delbtn = Button(f, text="删除", command=self.deleteuser)
        lbname.grid(row=1, column=1)
        txname.grid(row=1, column=2)
        lbpwd.grid(row=2, column=1)
        txpwd.grid(row=2, column=2)
        add.grid(row=3, column=1)
        log.grid(row=3, column=2)
        updbtn.grid(row=3, column=3)
        delbtn.grid(row=3, column=4)
        w.mainloop()

    def adduser(self):
        un = self.name.get()
        up = self.pwd.get()

        cur = self.con.cursor()
        cur.execute("insert into Utable(cname,cpwd) values('" + un + "','" + up + "')")
        self.con.commit()
        self.lbr["text"] = "添加用户成功"

    def login(self):
        un = self.name.get()
        up = self.pwd.get()

        cur = self.con.cursor()
        cur.execute("select count(cname) from Utable where cname='" + un + "' and cpwd='" + up + "'")
        data = cur.fetchall()
        if data[0][0] == 0:
            self.loginflag = ""
            self.lbr["text"] = "用户名或者密码错误"
        else:
            self.loginflag = un
            self.lbr["text"] = "登录成功"

    def updateuser(self):
        un = self.name.get()
        up = self.pwd.get()

        if un == self.loginflag:
            cur = self.con.cursor()
            cur.execute("update Utable set cpwd='" + up + "' where cname='" + un + "'")
            self.con.commit()
            self.lbr["text"] = "密码修改成功"
        else:
            if self.loginflag == "":
                self.lbr["text"] = "请您先登录系统"
            else:
                self.lbr["text"] = "密码修改失败，您只能修改自己的密码"

    def deleteuser(self):
        un = self.name.get()
        up = self.pwd.get()
        if un == self.loginflag:
            cur = self.con.cursor()
            cur.execute("delete from Utable where cname='" + un + "'")
            self.con.commit()
            self.lbr["text"] = "用户删除成功"
        else:
            if self.loginflag == "":
                self.lbr["text"] = "请您先登录系统"
            else:
                self.lbr["text"] = "删除用户失败，您只能修改自己的密码"
MyDBTest()