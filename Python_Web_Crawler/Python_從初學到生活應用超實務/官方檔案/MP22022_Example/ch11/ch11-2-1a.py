from PIL import Image

im = Image.open("koala.png")
print("圖檔名稱:", im.filename)
print("圖檔格式:", im.format)
print("圖檔尺寸:", im.size)
print("圖檔模式:", im.mode)
print("圖檔的寬:", im.width)
print("圖檔的高:", im.height)
# im.show()
import matplotlib.pyplot as plt

plt.imshow(im)
plt.axis("off")
plt.title("無尾熊")
plt.show()
