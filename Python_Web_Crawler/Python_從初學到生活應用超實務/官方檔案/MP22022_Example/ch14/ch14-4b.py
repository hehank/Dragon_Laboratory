import os, hashlib

path = "./test/圖片3"
md5_dic = dict()
img_files = []
for img_name in os.listdir(path):
    fname  = os.path.splitext(img_name)
    if fname[1] == ".jpg":
        img_name = os.path.join(path, img_name)
        img_files.append(img_name)
        data = hashlib.md5(open(img_name, "rb").read()).digest()
        md5_dic[img_name] = data

for img_name in img_files:
    md5 = md5_dic[img_name]
    duplicate_images = []
    for key, value in md5_dic.items():
        if md5 == value:
            duplicate_images.append(key)
            img_files.remove(key)
    if (len(duplicate_images) >= 2):
        for img_name in duplicate_images:
            print(img_name)
    print() 
      
