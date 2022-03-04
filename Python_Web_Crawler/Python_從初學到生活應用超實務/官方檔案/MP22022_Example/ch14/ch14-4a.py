import os
from PIL import Image

path = "./test/圖片2"
for img_name in os.listdir(path):
    print(img_name)
    fname  = os.path.splitext(img_name)
    im = Image.open(os.path.join(path, img_name))
    im.save(os.path.join(path, fname[0] + ".png"))
    os.remove(os.path.join(path, img_name))
        

