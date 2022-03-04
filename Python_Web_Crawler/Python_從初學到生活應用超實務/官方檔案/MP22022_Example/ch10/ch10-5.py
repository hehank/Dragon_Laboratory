from tkinter import *
from pytube import YouTube

def download():    
    try: 
        status_lbl.configure(text="YouTube影片正在下載中...")
        win.update()
        yt = YouTube(link.get())
        res = "360p"
        if resType.get() == 1:
            res = "720p"
        videos = yt.streams.filter(subtype="mp4",res=res)
        videos.first().download(path.get())
        msg = "影片[" + yt.title + "]已經成功下載..."
        status_lbl.configure(text=msg)
    except: 
        status_lbl.configure(text="錯誤! YouTube影片下載錯誤...")

win = Tk()
win.title("YouTube影片下載器")
link = StringVar()
link.set("https://www.youtube.com/watch?v=igEakV59sFs")
path = StringVar()
path.set("download/")
resType = IntVar()
resType.set(1)

frame = Frame(win)
frame.grid(row=0,column=0,padx=70,pady=30)
get_info = Label(frame,text="輸入YouTube影片的URL網址: ")
get_info.grid(row=0,column=0,sticky=W)
yt_link = Entry(frame,width= 60,textvariable=link)
yt_link.grid(row=1,columnspan=3,padx=0,pady=3)
yt_link.focus()
get_info = Label(frame,text="請輸入下載路徑: ")
get_info.grid(row=2,column=0,sticky=W)
download_path = Entry(frame,width=60,textvariable=path)
download_path.grid(row=3,columnspan=3,padx=0,pady=3)
rad1 = Radiobutton(frame,text="MP4, 360p",value=0,var=resType)
rad1.grid(row=4, column=0)
rad2 = Radiobutton(frame,text="MP4, 720p",value=1,var=resType)
rad2.grid(row=4, column=1)
btn1 = Button(frame,text="下載影片",width=15,command=download)
btn1.grid(row=5,columnspan=3,padx=13,pady=7)
status_lbl = Label(frame,text="")
status_lbl.grid(row=6,column=0)
win.geometry("560x250")
win.mainloop()

