import os
from PIL import Image

path = "./test/圖片1"
for img_name in os.listdir(path):
    print(img_name)
    im = Image.open(os.path.join(path, img_name))
    im.thumbnail((20,20))
    im.save(os.path.join(path, img_name))
        

