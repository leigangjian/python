# -*- encoding = utf-8 -*-
import qrcode
from tkinter import *
from tkinter import messagebox
import os

def made(string,filename):
    if not os.path.exists('images'):
        os.mkdir('images')
    os.chdir('images')
    img = qrcode.make(string)
    img.save(filename)
    messagebox.showinfo('提示','%s保存成功'%filename)
    os.chdir('..')

def inspection():
    string = entry.get()
    file = entry2.get()
    list = file.strip().split('.')
    try:
        if string.strip() != '' and (list[1]=='jpg' or list[1]=='png'):
            made(string,file)
        else:
            messagebox.showerror('错误','输入错误')
    except IndexError:
        messagebox.showerror('错误','请输入正确的文件名')

def attention():
    messagebox.showinfo('提示','输入二维码内容及\n保存的文件名(要加后缀,例如 test.jpg)后\n按下生成即可\n')

root = Tk()
root.title('二维码生成器')
root.geometry('340x200+610+240')
lable = Label(root,text='请输入生成二维码的内容',font=('微软雅黑',15))
lable.grid(sticky=W)
entry = Entry(root,font=('微软雅黑',20))
entry.grid()
lable2 = Label(root,text='请输入保存文件名,要加后缀(jpg/png)',font=('微软雅黑',15))
lable2.grid(sticky=W)
entry2 = Entry(root,font=('微软雅黑',20))
entry2.grid()
button = Button(root,text='生成',font=('微软雅黑',20),fg='red',command=inspection)
button.grid(sticky=W)
button2 = Button(root,text='注意',font=('微软雅黑',20),command=attention)
button2.grid(row=4,sticky=E)
root.mainloop()