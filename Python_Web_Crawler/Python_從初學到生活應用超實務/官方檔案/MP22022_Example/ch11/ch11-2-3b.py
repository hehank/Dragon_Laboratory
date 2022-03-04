from PIL import Image

im = Image.open("koala.png")
print(im.size)
im.thumbnail((300, 200))
print(im.size)
im.save("resized03.jpg")
