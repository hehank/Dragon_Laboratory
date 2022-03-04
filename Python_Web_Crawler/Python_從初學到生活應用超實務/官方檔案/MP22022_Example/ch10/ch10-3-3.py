from tkinter import *

win = Tk()
win.title("溫度轉換程式")
lbl = Label(win, text="攝氏: ")
lbl.grid(row=0, column=0)
c_var = IntVar()
txt = Entry(win, textvariable=c_var)
txt.grid(row=0, column=1)
lbl1 = Label(win, text="華氏: ")
lbl1.grid(row=1, column=0)
r_var = DoubleVar()
lbl2 = Label(win, textvariable=r_var)
lbl2.grid(row=1, column=1)
def convert_f():
    c = c_var.get()
    r_var.set((9.0 * c) / 5.0 + 32.0)
btn = Button(win, text="轉換", command=convert_f)
btn.grid(row=2, columnspan=2)
win.geometry("250x100")
win.mainloop()


