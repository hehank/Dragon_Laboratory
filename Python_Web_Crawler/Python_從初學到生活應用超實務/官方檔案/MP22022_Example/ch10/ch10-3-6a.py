from tkinter import *

win = Tk()
win.title("grid()方法")
frame = Frame(win)
frame.pack(fill=BOTH, expand=1)
lbl1 = Label(frame, text="Python視窗")
lbl1.grid(row=0, column=0)
lbl2 = Label(frame, text="Python視窗")
lbl2.grid(row=0, column=1)
lbl3 = Label(frame, text="Python視窗")
lbl3.grid(row=1, column=0)          
lbl4 = Label(frame, text="Python視窗")
lbl4.grid(row=1, column=1)
lbl5 = Label(frame, text="Python視窗")
lbl5.grid(row=2, columnspan=2)
lbl6 = Label(frame, text="Python視窗")
lbl6.grid(row=3, column=2, sticky="E")
win.geometry("250x100")
win.mainloop()

