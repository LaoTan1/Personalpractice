from tkinter import *
import mysql.connector


class MyDBTest:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost", port="3306",
            user="root", password="1224",
            database="testdb"
        )

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
        lbname.grid(row=1, column=1)
        txname.grid(row=1, column=2)
        lbpwd.grid(row=2, column=1)
        txpwd.grid(row=2, column=2)
        add.grid(row=3, column=1)
        log.grid(row=3, column=2)
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
            self.lbr["text"] = "用户名或者密码错误"
        else:
            self.lbr["text"] = "登录成功"


MyDBTest()
