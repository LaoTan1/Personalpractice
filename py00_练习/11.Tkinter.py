# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = '谭华锦'

# import tkinter
# tkinter._test()
from tkinter import *


# class Sum:
#     def __init__(self):
#         window = Tk()
#         window.title('累加')
#         self.v1 = IntVar()
#         frame = Frame(window)
#         frame.pack()
#         lable = Lable(window, text='Enter a number:')
#         lable.pack()
#         self.name=StringVar()
#
#
#
#
#     def getsum(self):
#         pass


class CanvasDemo:
    def __init__(self):
        window = Tk()
        # 创建window
        window.title("Canvas Demo")
        # 设置主窗口对象的标题栏
        # 把窗口名称设为Canvas Demo

        # 创建一个画布。
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        # 创建一个框架frame,后面用来存放那些Button按钮

        '''
        text 用来设计按钮的显示名称
        command 用来链接按钮和引用的函数
        '''
        # 创建这是按钮，把它们放在框架 frame里
        btRectangle = Button(frame, text="Rectangle", command=self.displayRect)
        btOval = Button(frame, text="Oval", command=self.displayOval)
        btArc = Button(frame, text="Arc", command=self.displayArc)
        btPolygon = Button(frame, text="Polygon", command=self.displayPolygon)
        btLine = Button(frame, text="Line", command=self.displayLine)
        btString = Button(frame, text="String", command=self.displayString)
        btClear = Button(frame, text="Clear", command=self.clearCanvas)

        # 利用框架frame，在框架frame 里给按钮排位置，row 表示行，column 表示列2
        btRectangle.grid(row=1, column=1)
        btOval.grid(row=1, column=2)
        btArc.grid(row=1, column=3)
        btPolygon.grid(row=1, column=4)
        btLine.grid(row=1, column=5)
        btString.grid(row=1, column=6)
        btClear.grid(row=1, column=7)
        window.mainloop()

    # 这里作用是在里画图
    def displayRect(self):
        # 里面有四个数，前两个数代表一个坐标，后面两个数代表一个坐标，例如矩形，矩形的两个对角的顶点可以确定一个矩形
        self.canvas.create_rectangle(10, 10, 190, 190, tags="rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="green", tags="oval")

    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0, extent=90, width=8, fill="yellow", tags="arc")

    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags="polygon", fill="green", outline='#f11')

    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, dash=(4, 2), fill="red", arrow="both", activefill="blue", tags="line")
        self.canvas.create_line(60, 60, 190, 100, fill="red", arrow="both", activefill="blue", tags="line")

    def displayString(self):
        self.canvas.create_text(60, 40, text="Hello World", font="Time 10 bold underline", tags="string")

    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")


CanvasDemo()
