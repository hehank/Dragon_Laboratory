from pytube import YouTube
import os

def progress(stream, chunk, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining 
    print('\r'+'[下載進度]:[%s%s]%.2f%%'%(
          '█'*(int(size*20/contentSize)),
          ' '*(20-int(size*20/contentSize)),
          float(size/contentSize*100)), end='')
filename = "youtube_videos.txt"
path = "tmp/"
if not os.path.isdir(path):
    os.mkdir(path)
with open(filename) as fp:
    for f in fp:
        yt = YouTube(f.rstrip(), 
                     on_progress_callback=progress)
        print("正在下載影片: ", yt.title)
        video = yt.streams.first()
        video.download(path)
        print()