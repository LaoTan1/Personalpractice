# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = '谭华锦'

from tkinter import *

root = Tk()


def A(i):
    sum = 0
    t = i
    for i in range(t, 101, 1):
        sum = sum + i
    return sum


i = Entry(root)
i.pack()
t = i.get()
int(t)
a = A(t)
print(a)
root.mainloop()
