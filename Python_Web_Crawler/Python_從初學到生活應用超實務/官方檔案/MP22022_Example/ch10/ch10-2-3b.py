from moviepy.editor import ImageSequenceClip

images = []
for i in range(10):
    images.append("imgs/color" + str(i) +".jpg")

clip = ImageSequenceClip(images, fps=1)
clip.write_gif("demo.gif")

