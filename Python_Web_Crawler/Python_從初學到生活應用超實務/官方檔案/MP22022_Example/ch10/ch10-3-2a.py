from tkinter import *

win = Tk()
win.title("主視窗")
lbl1 = Label(win, text="姓名: ")
lbl1.grid(row=0, column=0)
lbl2 = Label(win, text="")
lbl2.grid(row=0, column=1)
def showname():
    lbl2.configure(text="陳會安")
btn = Button(win, text="顯示",command=showname)
btn.grid(row=1, column=1)
win.geometry("250x100")
win.mainloop()


