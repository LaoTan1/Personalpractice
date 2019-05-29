# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = '谭华锦'

from tkinter import *


class GetSum:
    def __init__(self):
        window = Tk()
        window.title('累加')
        frame1 = Frame(window)
        frame1.pack()
        label = Label(frame1, text='Enter first number：')
        labe2 = Label(frame1, text='Enter second number：')
        self.var1 = IntVar()
        self.var2 = IntVar()
        entry1 = Entry(frame1, textvariable=self.var1)
        entry2 = Entry(frame1, textvariable=self.var2)
        button1 = Button(frame1, text='Get number', command=self.getsum)
        label.grid(row=1, column=1,sticky = E)
        labe2.grid(row=2, column=1,sticky = E)
        entry1.grid(row=1, column=2)
        entry2.grid(row=2, column=2)
        button1.grid(row=3,column = 2,sticky = E)
        window.mainloop()

    def getsum(self):
        n1 = self.var1.get()
        n2 = self.var2.get()
        if n1 > n2:
            t = n1
            n1 = n2
            n2 = t
        sum = n1
        for n1 in range(n1, n2 + 1, 1):
            sum += n1
        print(sum)


GetSum()
