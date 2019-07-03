import tkinter as tk
from tkinter import messagebox
import GarbageSorting as gs


def on_click():
    result = entrence(text.get())
    print(result)
    if not isEmpty(result):
        tk.messagebox.showinfo("结果", result)
        text.set("")


def on_click_bin():
    binList = newSort.showBin()
    tk.messagebox.showinfo("结果", binList)


def on_click_clear():
    newSort.__init__()


def entrence(inputStr):
    print("calling with %s" % inputStr)

    if isEmpty(inputStr):
        print()
    elif "clear" == inputStr:
        newSort.__init__()
    elif "showFile" == inputStr:
        newSort.showFile()
    else:
        return newSort.search(inputStr)


def isEmpty(str):
    if str is None:
        return True
    elif len(str) == 0 or str.isspace():
        return True
    return False


newSort = gs.GarbageSorting()

root = tk.Tk()
width = 300
height = 200
root.title('我丢我丢我丢丢丢')
screenwidth = root.winfo_screenwidth()
screenheigh = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (
    width, height, (screenwidth - width) / 2, (screenheigh - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
backGround = tk.PhotoImage(file='background.gif')
f1 = tk.Frame(root, bg='blue')
f1.pack()
f2 = tk.Frame(root, bg='gray')
f2.pack()
lable = tk.Label(f1,
                 text="你是什么垃圾？",
                 justify=tk.LEFT,
                 image=backGround,
                 compound=tk.CENTER,
                 font=('黑体', 20),
                 fg='yellow')
lable.pack(fill="x")
text = tk.StringVar()
entry = tk.Entry(f2, textvariable=text, bd=1)
entry.pack(fill='x')
button1 = tk.Button(f2, text="丢出去", fg="blue", relief='raised', command=on_click)
button1.pack(side='left')
button2 = tk.Button(f2, text="看看丢了啥", fg="blue", relief='raised', command=on_click_bin)
button2.pack(side='left')
button2 = tk.Button(f2, text="倒垃圾桶", fg="blue", relief='raised', command=on_click_clear)
button2.pack(side='left')
root.mainloop()
