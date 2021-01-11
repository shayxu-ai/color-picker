#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/01/09 Sat
# @Author: ShayXU
# @Filename: 屏幕取色.py


"""
    tkinter教程 https://coderslegacy.com/python/python-gui/
    # pyqt5教程 https://coderslegacy.com/python/pyqt5-tutorial/
"""

from PIL import ImageGrab
import tkinter


def RGB_to_Hex(rgb, reverse=False):          # 将RGB格式划分开来
    color = r'#'
    for i in rgb:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        if not reverse:
            color += str(hex(num))[-2:].replace('x', '0').upper()
        else:
            color += str(hex((num+128)%255))[-2:].replace('x', '0').upper()
    return color


if __name__ == "__main__":
    
    def run(event):
        global color_hex
        image = ImageGrab.grab()
        color = image.getpixel((event.x_root, event.y_root))
        color_hex = RGB_to_Hex(color)

        l['bg'] = color_hex
        l['fg'] = RGB_to_Hex(color, reverse=True)
        l['text'] = color_hex
        l_pos['text'] = "按'ESC'取消选取，并将颜色复制至粘贴板\r\n" + "鼠标坐标: ({}, {})".format(event.x_root, event.y_root)
        return color_hex

    def run_button():
        # root.bind('<Motion>', run)
        root.attributes("-alpha", 0.002)
        top_color.attributes("-topmost", False,
                             "-alpha", 0.8)

    def run_button_unbind(event):
        global color_hex
        # 复制至粘贴板
        root.clipboard_clear()
        root.clipboard_append(color_hex)

        # root.unbind('<Motion>')
        root.attributes("-alpha", 0)
        top_color.attributes("-topmost", True,
                             "-alpha", 1)
    
    def auth_info():
        # 创建顶级窗口
        top_level = tkinter.Toplevel()
        top_level.attributes("-topmost", True)
        top_level.title("关于")
        top_level.resizable(0,0)
        

        tkinter.Label(top_level, width=30, height=5, text="作者：ShayXU\r\n版本: 1.0.0\r\n日期: 2021/01/09").pack()

    color_hex = ""
    
    # 创建Tk对象
    root = tkinter.Tk()
    root.attributes("-topmost", True,        # 界面置顶
                    "-alpha", 0.002,         # 最小值
                    '-fullscreen', True) 
    # root.wm_attributes("-alpha", 0)      
    root.option_add('*tearOff', False)      # 删除下拉栏虚线。
    # top = tkinter.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    

    # root.attributes('-alpha', 0.5)
    # 修改窗口标题
    # root.title("Pack - Example")
    root.wm_title("屏幕取色")
    
    # 色块
    top_color = tkinter.Toplevel(root)
    top_color.attributes("-alpha", 0.95,)
    # frame.attributes("-alpha", 1)     # Canvas, Frame无该函数
    l = tkinter.Label(top_color, bg='blue', width=50, height=10, border=1,  borderwidth=1)
    l.pack()
    
    # 创建导航栏
    menubar = tkinter.Menu(top_color, tearoff=False)
    menubar.add_cascade(label="关于",command=auth_info)
    top_color['menu'] = menubar

    # 按键
    # 使用Frame增加一层容器
    fm2 = tkinter.Frame(top_color)

    root.bind('<Motion>', run)    # 开启采集像素
    test = tkinter.Button(fm2, text="选取", command=run_button)
    test.pack(padx=10, side=tkinter.LEFT)
    root.test = test

    quit = tkinter.Button(fm2, text="退出", command=root.destroy)
    quit.pack(padx=10, side=tkinter.RIGHT)
    fm2.pack(pady=5)

    l_pos = tkinter.Label(top_color, text="按'ESC'取消选取，并将颜色复制至粘贴板\r\n", width=50)
    l_pos.pack(pady=5)

    # Esc 退出颜色采集
    root.bind('<Escape>', run_button_unbind)
    top_color.bind('<Escape>', run_button_unbind)
    

    # The following three commands are needed so the window pops
    # up on top on Windows...
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()
    

