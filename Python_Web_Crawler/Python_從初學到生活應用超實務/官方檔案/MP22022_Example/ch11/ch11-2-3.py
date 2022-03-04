from PIL import Image

im = Image.open("koala.png")
print(im.size)
nim = im.resize((400, 400))
print(nim.size)
nim.save("resized01.jpg")
