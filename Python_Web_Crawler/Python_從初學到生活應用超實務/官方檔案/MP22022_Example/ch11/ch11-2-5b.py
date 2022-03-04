from PIL import Image

im = Image.open("koala.png")
print(im.size)
nim = im.crop((50,100,300,400))
nim.save("croped01.jpg")