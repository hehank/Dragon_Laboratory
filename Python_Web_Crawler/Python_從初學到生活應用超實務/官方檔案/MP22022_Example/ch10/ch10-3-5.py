from tkinter import *

win = Tk()
win.title("元件尺寸")
btn1 = Button(win, text="確定", height=5, width=10)
btn1.grid(row=0, column=0)
btn2 = Button(win, text="取消")
btn2.grid(row=0, column=1)
win.geometry("250x100")
win.mainloop()


