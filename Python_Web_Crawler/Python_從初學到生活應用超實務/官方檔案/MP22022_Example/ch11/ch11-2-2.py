from PIL import Image

im = Image.open("koala.png")
print(im.format, im.size, im.mode)
print("轉換輸出成JPG格式...")
im.save("koala.jpg")
print("轉換輸出成GIF格式...")
im.save("koala.bmp", "GIF")