import tkinter
import time
import threading


class Choujiang:
    # 初始化魔术方法
    def __init__(self):
        # 准备好界面
        self.root = tkinter.Tk()
        self.root.title('今天午饭/晚饭吃什么？')
        self.root.minsize(600, 600)
        # 声明一个是否按下开始的变量
        self.isloop = False
        self.newloop = False
        # 调用设置界面的方法
        self.setwindow()
        self.root.mainloop()

    # 界面布局方法
    def setwindow(self):
        # 开始停止按钮
        self.btn_start = tkinter.Button(self.root, text='开始/停止', command=self.newtask, bg='gold')
        self.btn_start.place(x=200, y=250, width=170, height=100)
        self.btn1 = tkinter.Button(self.root, text='食堂', bg='red')
        self.btn1.place(x=40, y=40, width=100, height=100)
        self.btn2 = tkinter.Button(self.root, text='麻辣烫', bg='white')
        self.btn2.place(x=180, y=40, width=100, height=100)
        self.btn3 = tkinter.Button(self.root, text='千里香馄饨', bg='white')
        self.btn3.place(x=320, y=40, width=100, height=100)
        self.btn4 = tkinter.Button(self.root, text='沙县', bg='white')
        self.btn4.place(x=460, y=40, width=100, height=100)
        self.btn5 = tkinter.Button(self.root, text='炒米', bg='white')
        self.btn5.place(x=460, y=180, width=100, height=100)
        self.btn6 = tkinter.Button(self.root, text='汤粉', bg='white')
        self.btn6.place(x=460, y=320, width=100, height=100)
        self.btn7 = tkinter.Button(self.root, text='炸鸡', bg='white')
        self.btn7.place(x=460, y=460, width=100, height=100)
        self.btn8 = tkinter.Button(self.root, text='泡面', bg='white')
        self.btn8.place(x=320, y=460, width=100, height=100)
        self.btn9 = tkinter.Button(self.root, text='手抓饼', bg='white')
        self.btn9.place(x=180, y=460, width=100, height=100)
        self.btn10 = tkinter.Button(self.root, text='面包', bg='white')
        self.btn10.place(x=40, y=460, width=100, height=100)
        self.btn11 = tkinter.Button(self.root, text='河粉', bg='white')
        self.btn11.place(x=40, y=320, width=100, height=100)
        self.btn12 = tkinter.Button(self.root, text='吃粥', bg='white')
        self.btn12.place(x=40, y=180, width=100, height=100)
        # 将所有选项组成列表
        self.girlfrends = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8,
                           self.btn9, self.btn10, self.btn11, self.btn12]

    def rounds(self):
        # 判断是否开始循环
        if self.isloop == True:
            return
            # 初始化计数  变量
        i = 0
        # 死循环
        while True:
            if self.newloop == True:
                self.newloop = False
                return

            # 延时操作
            time.sleep(0.1)
            # 将所有的组件背景变为白色
            for x in self.girlfrends:
                x['bg'] = 'white'

            # 将当前数值对应的组件变色
            self.girlfrends[i]['bg'] = 'red'
            # 变量+1
            i += 1
            # 如果i大于最大索引直接归零
            if i >= len(self.girlfrends):
                i = 0

    # 建立一个新线程的函数
    def newtask(self):
        if self.isloop == False:
            # 建立线程
            t = threading.Thread(target=self.rounds)
            # 开启线程运行
            t.start()
            # 设置循环开始标志
            self.isloop = True
        elif self.isloop == True:
            self.isloop = False
            self.newloop = True


Choujiang()
