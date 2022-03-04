import os
from PIL import Image

path = "./test/圖片4"
n_im = Image.open("./test/arrow.png")
for img_name in os.listdir(path):
    print(img_name)
    im = Image.open(os.path.join(path, img_name))
    x = int(im.width - n_im.width)
    y = int(im.height - n_im.height)
    im.paste(n_im,(x, y),n_im)
    im.save(os.path.join(path, img_name))