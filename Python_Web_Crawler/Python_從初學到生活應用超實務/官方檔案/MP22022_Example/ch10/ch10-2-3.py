from moviepy.editor import VideoFileClip

clip = VideoFileClip("使用fChart解統測與技競問題.mp4")
clip = clip.subclip(50,60)
clip.write_videofile("Output.webm")
