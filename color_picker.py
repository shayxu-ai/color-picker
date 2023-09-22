#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateDate: 2023/09/22 Fri 15:34
# @Author: ShayXU
# @Filename: color_picker.py


"""
   代码重构: 使用ttk 
"""


from tkinter import *
from tkinter import ttk


class ColorPicker:

    def __init__(self, root):
        style = ttk.Style()
        root.title("屏幕取色")


        # 获取屏幕宽度和高度
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # 计算窗口的中心点坐标
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)
        # 将窗口移动至中心点位置
        root.geometry("+{}+{}".format(center_x, center_y))
        root.geometry("300x200")

        mainframe = ttk.Frame(root, borderwidth=5, padding=(10,10,10,10), relief="ridge")
        mainframe.grid(column=0, row=0, sticky='nsew')

       
        # 色块，显示当前像素的颜色
        color_block = ttk.Label(mainframe, background='white', width=10)
        button1 = ttk.Button(mainframe, text="选取", command=None)
        button2 = ttk.Button(mainframe, text="退出", command=root.destroy)

        color_block.grid(column=4, row=2, sticky='nsew')
        button1.grid(column=2, row=3, sticky='nsew')
        button2.grid(column=6, row=3, sticky='nsew')

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)





if __name__ == '__main__':
    root = Tk()
    ColorPicker(root)
    root.mainloop()