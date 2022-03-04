from tkinter import *

win = Tk()
win.title("選擇付款方式")
selected = IntVar()
selected.set(1)
def clicked():
    rad_value = selected.get()
    chk_value = state.get()
    msg = str(rad_value) + "/" + str(chk_value)
    lbl1.configure(text=msg)
rad1 = Radiobutton(win, text="信用卡", value=0, 
                   var=selected, command=clicked)
rad1.grid(row=0, column=0)
rad2 = Radiobutton(win, text="轉帳", value=1,
                   var=selected, command=clicked)
rad2.grid(row=0, column=1)
state = BooleanVar()
state.set(True)
chk = Checkbutton(win, text="含稅", var=state,
                  command=clicked)
chk.grid(row=1, columnspan=2)
lbl1 = Label(win, text="")
lbl1.grid(row=2, column=1)
win.geometry("250x100")
win.mainloop()


