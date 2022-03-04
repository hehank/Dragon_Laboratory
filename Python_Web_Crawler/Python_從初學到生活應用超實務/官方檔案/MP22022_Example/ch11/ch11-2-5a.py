from PIL import Image

im = Image.open("koala_small.png")
print(im.size)
nim = im.transpose(Image.ROTATE_90)
nim.save("rotated02.jpg")