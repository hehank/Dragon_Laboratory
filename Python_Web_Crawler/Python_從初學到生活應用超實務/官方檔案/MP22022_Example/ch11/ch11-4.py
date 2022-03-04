from tkinter import *
import urllib.request

def download():
    if url.get()=="":
        status_lbl.configure(text="沒有輸入URL網址...")
    else:
        try:
            response = urllib.request.urlopen(url.get())
            fp = open(fname.get(), "wb")
            size = 0
            while True:
               info = response.read(10000)
               if len(info) < 1:
                   break
               size = size + len(info)
               tmp = fname.get()+"已經下載: "+str(size)+"個字元"
               status_lbl.configure(text=tmp)   
               win.update()
               fp.write(info)              
            fp.close()
            response.close()            
        except:
            status_lbl.configure(text="下載錯誤...") 
            
win = Tk()
win.title("圖檔下載工具")
url = StringVar()
url.set("https://fchart.github.io/img/Butterfly.png")
fname = StringVar()
fname.set("download.png")

url_lbl = Label(win,text="URL網址:",compound=LEFT)
url_lbl.grid(row=1,column=0,padx=10,pady=10)
url_txt = Entry(win,width=40,textvariable=url)
url_txt.grid(row=1,column=1,padx=10,pady=10)       
dwn_btn = Button(win,text="開始下載檔案",command=download)
dwn_btn.grid(row=1,column=2,padx=10,pady=10)
fname_lbl = Label(win,text="下載檔名:")
fname_lbl.grid(row=2,column=0)
fname_txt = Entry(win,width=40,textvariable=fname)
fname_txt.grid(row=2,column=1,padx=10,pady=10)   
status_lbl = Label(win,text="")
status_lbl.grid(row=3,column=1)
win.geometry("500x150")
win.mainloop()