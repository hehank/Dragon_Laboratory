from PIL import Image

im = Image.open("koala.png")
print(im.size)
new_width = 350
ratio = float(new_width)/im.width
new_height = int(im.height*ratio)
nim = im.resize((new_width, new_height))
print(nim.size)
nim.save("resized02.jpg")