from moviepy.editor import VideoFileClip

clip = VideoFileClip("使用fChart解統測與技競問題.mp4")
print("長度:", clip.duration)
print("每秒幀數:", clip.fps)

