# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from tkinter import *
import constants


class ImageDemo(object):
    def __init__(self):
        window = Tk()
        window.title("Image Demo")

        text1_Image = PhotoImage(file=constants.text1)
        # text2_Image = PhotoImage(file=constants.text1)

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image=text1_Image).pack(side=LEFT)
        # canvas = Canvas(frame1)
        # canvas.create_image(90, 50, image=text1_Image)
        # canvas["width"] = 200
        # canvas["height"] = 100
        # canvas.pack(side=LEFT)

        window.mainloop()


ImageDemo()
