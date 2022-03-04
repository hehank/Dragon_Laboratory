from PIL import Image

im = Image.open("koala_small.png")
print(im.size)
nim = im.rotate(45)
nim.save("rotated01.jpg")