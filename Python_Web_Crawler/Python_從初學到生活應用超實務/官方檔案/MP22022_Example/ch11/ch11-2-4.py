from PIL import Image

b_im = Image.open("koala_small.png")
n_im = Image.open("name.jpg")
print(b_im.size)
print(n_im.size)
x = int(b_im.width / 2)
y = int(b_im.height / 2)
x = x - int(n_im.width / 2)
y = y - int(n_im.height / 2)
print(x, y)
b_im.paste(n_im,(x, y))
b_im.save("pasted01.jpg")
