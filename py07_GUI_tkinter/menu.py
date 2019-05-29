# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from tkinter import *


class MenuDemo:
    def __init__(self):
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

        self.canvas = Canvas(self.window, width=200, height=200, bg="white")
        self.canvas.pack()
        mainloop()

    def drawOval(self):
        self.canvas.create_oval(10, 10, 190, 190, tags="oval")
        self.canvas.delete("rect")

    def drawRectangle(self):
        self.canvas.create_rectangle(10, 10, 190, 190, tags="rect")
        self.canvas.delete("oval")

    def exit(self):
        self.window.destroy()

    def text(self):
        pass


MenuDemo()
