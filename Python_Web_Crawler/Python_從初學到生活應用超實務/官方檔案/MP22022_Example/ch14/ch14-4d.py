import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

path = "./tmp"
videos = []
for fname in os.listdir(path):
    print(fname)
    videos.append(VideoFileClip(os.path.join(path,fname)))
final_clip = concatenate_videoclips(videos)
final_clip.write_videofile("final_clip.mp4")