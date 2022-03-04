from tkinter import *

win = Tk()
win.title("主視窗")
lbl1 = Label(win, text="姓名: ")
lbl1.grid(row=0, column=0)
name_var = StringVar()
lbl2 = Label(win, textvariable=name_var)
lbl2.grid(row=0, column=1)
def showname():
    name_var.set("陳會安")
btn = Button(win, text="顯示",command=showname)
btn.grid(row=1, column=1)
win.geometry("250x100")
win.mainloop()


