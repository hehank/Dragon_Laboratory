from tkinter import *

win = Tk()
win.title("pack()方法")
frame = Frame(win)
frame.pack(fill=BOTH, expand=1)
lbl1 = Label(frame, text="Python視窗")
lbl1.pack(side=TOP)
lbl2 = Label(frame, text="Python視窗")
lbl2.pack(side=BOTTOM)
lbl3 = Label(frame, text="Python視窗")
lbl3.pack(side=LEFT)
lbl4 = Label(frame, text="Python視窗")
lbl4.pack(side=RIGHT)
win.geometry("250x100")
win.mainloop()

