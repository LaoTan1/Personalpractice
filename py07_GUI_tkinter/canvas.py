# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from tkinter import *


class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvsa Demo")

        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btRectangle = Button(frame, text="Rectang", command=self.displayRect)
        btOval = Button(frame, text="Oval", command=self.displayOval)
        btClear = Button(frame, text="Clear", command=self.ClearCanvas)

        btRectangle.grid(row=1, column=1)
        btOval.grid(row=1, column=2)
        btClear.grid(row=1, column=3)

        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, fill="red", tags="rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    def ClearCanvas(self):
        self.canvas.delete("rect", "oval")


CanvasDemo()
