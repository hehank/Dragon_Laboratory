from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFilter

def getImgFile():
    global im, image
    fname = filedialog.askopenfilename()
    if fname:
        im = Image.open(fname)
        win.title(fname)
        im.thumbnail((450, 200))
        image = ImageTk.PhotoImage(im)
        lbl.configure(image=image)
        lbl.image = image
def blur():
    filter_name.set("BLUR")
    tmp = im.filter(ImageFilter.BLUR)
    tmp = ImageTk.PhotoImage(tmp)
    lbl.configure(image=tmp)
    lbl.image = tmp
def edge():
    filter_name.set("EDGE")
    tmp = im.filter(ImageFilter.EDGE_ENHANCE)
    tmp = ImageTk.PhotoImage(tmp)
    lbl.configure(image=tmp)
    lbl.image = tmp
def contour():
    filter_name.set("CONTOUR")
    tmp = im.filter(ImageFilter.CONTOUR)
    tmp = ImageTk.PhotoImage(tmp)
    lbl.configure(image=tmp)
    lbl.image = tmp
def emboss():
    filter_name.set("EMBOSS")
    tmp = im.filter(ImageFilter.EMBOSS)
    tmp = ImageTk.PhotoImage(tmp)
    lbl.configure(image=tmp)
    lbl.image = tmp
def smooth():
    filter_name.set("EMBOSS")
    tmp = im.filter(ImageFilter.SMOOTH)
    tmp = ImageTk.PhotoImage(tmp)
    lbl.configure(image=tmp)
    lbl.image = tmp
def normal():
    filter_name.set("NORMAL")
    lbl.configure(image=image)
    lbl.image = image
    
fname = "koala.png"
win = Tk() 
win.title(fname)
im = Image.open(fname)
im.thumbnail((450, 200))
image = ImageTk.PhotoImage(im)
filter_name = StringVar() 
filter_name.set("NORMAL")

lbl = Label(image=image)
lbl.grid(row=0 ,column=0, columnspan=5)
lbl1 = Label(textvariable=filter_name)
lbl1.grid(row=1 ,column=0, columnspan=4)
btn = Button(win , text="開啟圖檔",command=getImgFile) 
btn.grid(row=1,column=5)
btn1 = Button(win , text="BLUR",command=blur) 
btn1.grid(row=3,column=0)
btn2 = Button(win , text="EDGE ENHANCE",command=edge)
btn2.grid(row=3,column=1)
btn3 = Button(win , text="CONTOUR",command=contour)
btn3.grid(row=3,column=2)
btn4 = Button(win , text="EMBOSS",command=emboss)
btn4.grid(row=3,column=3)
btn5 = Button(win , text="SMOOTH",command=smooth)
btn5.grid(row=3,column=4)
btn6 = Button(win, text="NORMAL",command=normal) 
btn6.grid(row=3,column=5)
win.geometry("450x280")
win.mainloop()
