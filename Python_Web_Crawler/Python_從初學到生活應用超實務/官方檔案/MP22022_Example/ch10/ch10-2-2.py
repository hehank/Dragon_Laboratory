from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("Arduino01.mp4")
clip2 = VideoFileClip("Arduino02.mp4")

final_clip = concatenate_videoclips([clip1, clip2])
final_clip.write_videofile("final_clip.mp4")

