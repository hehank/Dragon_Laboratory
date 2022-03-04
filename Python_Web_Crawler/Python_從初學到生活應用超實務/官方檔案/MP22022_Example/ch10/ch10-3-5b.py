from tkinter import *

win = Tk()
win.title("元件填充")
btn1 = Button(win, text="確定", padx=5, pady=5)
btn1.grid(row=0, column=0)
btn2 = Button(win, text="取消", padx=5, pady=5)
btn2.grid(row=0, column=1)
btn3 = Button(win, text="確定", padx=3, pady=3)
btn3.grid(row=1, column=0)
btn4 = Button(win, text="取消", padx=3, pady=3)
btn4.grid(row=1, column=1)
btn5 = Button(win, text="確定")
btn5.grid(row=2, column=0)
btn6 = Button(win, text="取消")
btn6.grid(row=2, column=1)
win.geometry("250x100")
win.mainloop()


