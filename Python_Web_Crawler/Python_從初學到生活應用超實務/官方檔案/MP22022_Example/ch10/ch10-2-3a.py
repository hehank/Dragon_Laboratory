from moviepy.editor import VideoFileClip

clip = VideoFileClip("使用fChart解統測與技競問題.mp4")
clip.audio.write_audiofile("test.mp3")
