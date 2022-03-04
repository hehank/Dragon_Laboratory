from tkinter import *
from PIL import Image, ImageTk

fname = "koala_small.png"
win = Tk()
win.title(fname)
img = ImageTk.PhotoImage(Image.open(fname))
label = Label(win, image=img, bg='brown')
label.pack(padx=5, pady=5)
win.mainloop()