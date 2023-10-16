#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import messagebox

def welcome_screen():
    root = tk.Tk()
    root.title("欢迎界面")
    tk.Label(root, text="欢迎来到我的程序！", font=("Arial", 20)).pack()
    root.after(3000, lambda: root.destroy())  # 3000 毫秒后关闭欢迎界面

def main():
    root = tk.Tk()
    root.title("主界面")
    welcome_screen()
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="打开文件", command=open_file)
    file_menu.add_command(label="保存文件", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="退出程序", command=exit_program)

    menubar.add_cascade(label="文件", menu=file_menu)

    root.config(menu=menubar)
    root.mainloop()

def open_file():
    messagebox.showinfo("提示", "即将打开文件")

def save_file():
    messagebox.showinfo("提示", "即将保存文件")

def exit_program():
    if messagebox.askyesno("退出程序", "确定要退出程序吗？"):
        root.destroy()


if __name__ == '__main__':
    main()



