#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateDate: 2023/09/21 Thu 16:14
# @Author: ShayXU
# @Filename: color_picker.py


"""
   代码重构: 使用ttk 
"""


from tkinter import *
from tkinter import ttk

class ColorPicker:

    def __init__(self, root):

        root.title("屏幕取色")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        # 色块，显示当前像素的颜色
        ttk.Label(mainframe, ).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="选取", command=None).grid(column=4, row=3, sticky=W)
        ttk.Button(mainframe, text="退出", command=None).grid(column=3, row=3, sticky=W)




if __name__ == '__main__':
    root = Tk()
    ColorPicker(root)
    root.mainloop()