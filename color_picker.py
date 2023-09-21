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
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, borderwidth=5, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

       
        # 色块，显示当前像素的颜色
        ttk.Label(mainframe).grid(column=4, row=2)

        ttk.Button(mainframe, text="选取", command=None).grid(column=3, row=3, columnspan=3)
        ttk.Button(mainframe, text="退出", command=root.destroy).grid(column=5, row=3, columnspan=3)







if __name__ == '__main__':
    root = Tk()
    ColorPicker(root)
    root.mainloop()