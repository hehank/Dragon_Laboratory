from PIL import Image

b_im = Image.open("koala_small.png")
n_im = Image.open("myname.png")
n_im = n_im.resize((100,40))
print(b_im.size)
print(n_im.size)
x = int(b_im.width - n_im.width)
y = int(b_im.height - n_im.height)
print(x, y)
b_im.paste(n_im,(x, y),n_im)
b_im.save("pasted02.jpg")
