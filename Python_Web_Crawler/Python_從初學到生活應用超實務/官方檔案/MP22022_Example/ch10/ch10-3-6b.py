from tkinter import *

win = Tk()
win.title("place()方法")
frame = Frame(win)
frame.pack(fill=BOTH, expand=1)
lbl1 = Label(frame, text="Python視窗")
lbl1.place(x=0, y=0)
lbl2 = Label(frame, text="Python視窗")
lbl2.place(x=100, y=0)
lbl3 = Label(frame, text="Python視窗")
lbl3.place(x=0, y=20)
lbl4 = Label(frame, text="Python視窗")
lbl4.place(x=100, y=20)
lbl5 = Label(frame, text="Python視窗")
lbl5.place(x=80, y=50, height=100, width=100)
win.geometry("300x150")
win.mainloop()

