import time
import tkinter as tk
from tkinter import ttk, messagebox as msg
import pymouse, pykeyboard, pyperclip

# 创建用户窗口
mainForm = tk.Tk()
mainForm.title('自动群发')
mainForm.resizable(0, 0)

# 输入框，用于输入要群发的用户名
nameText = tk.Text(mainForm, height=40, width=40)
nameText.insert(0.0, "消息的名单")
nameText.grid(row=0, padx=5, pady=5)

msgText = tk.Text(mainForm, height=2, width=40)
msgText.insert(0.0, "内容")
msgText.grid(row=1, padx=5, pady=5)

mouseSearchXY = (-1, -1)
mouseInputXY = (-1, -1)


def onClickMouseButton():
    global mouseSearchXY, mouseInputXY
    m = pymouse.PyMouse()
    msg.showinfo('提示', '请在点击确认后2秒内将鼠标移动到QQ的搜索框，2秒后自动获取搜索框鼠标位置。')
    time.sleep(2)
    mouseSearchXY = m.position()
    msg.showinfo('成功', '成功，请在点击确认后2秒内将鼠标移动到QQ的输入框，2秒后自动获取输入框鼠标位置。')
    time.sleep(2)
    mouseInputXY = m.position()
    msg.showinfo('成功', '任务成功完成')


mouseButton = ttk.Button(mainForm, text='点击获取鼠标位置', width=40, command=onClickMouseButton)
mouseButton.grid(row=2, padx=5, pady=5)


def onClickStartButton():
    # 判断是否已经读取鼠标位置
    if mouseSearchXY == (-1, -1) or mouseInputXY == (-1, -1):
        msg.showerror('错误', '请先获取鼠标位置哦哦哦')
        return
    # 判断输入框有没有内容
    nameContent = nameText.get(0.0, tk.END).rstrip()
    if nameContent == '消息的名单' or nameContent == '':
        msg.showerror('错误', '请先输入名单')
        return
    msgContent = msgText.get(0.0, tk.END).rstrip()
    if msgContent == '内容' or msgContent == '':
        msg.showerror('错误', '请先输入内容')
        return
    # 开始群发
    if not msg.askokcancel('提示', '即将开始，在完成之前别动鼠标'):
        return
    m = pymouse.PyMouse()  # 获取鼠标对象
    k = pykeyboard.PyKeyboard()  # 获取键盘对象
    lst = nameContent.split()
    for i in lst:
        m.click(mouseSearchXY[0], mouseSearchXY[1])
        pyperclip.copy(i)
        k.press_key('Command')
        k.tap_key('v')
        k.release_key('Command')#Mac Os 的函数有点区别 k.press_keys(['Command','shift','3'])
        time.sleep(0.5)
        k.tap_key('Return')
        time.sleep(0.5)
        m.click(mouseInputXY[0], mouseInputXY[1])
        pyperclip.copy(msgContent)
        k.press_key('Command')
        k.tap_key('v')
        k.release_key('Command')
        time.sleep(0.5)
        k.tap_key('Return')
        time.sleep(0.5)
    msg.showinfo('提示', '完成！')


startButton = ttk.Button(mainForm, text='启动', width=40, command=onClickStartButton)
startButton.grid(row=3, padx=5, pady=5)

mainForm.mainloop()
