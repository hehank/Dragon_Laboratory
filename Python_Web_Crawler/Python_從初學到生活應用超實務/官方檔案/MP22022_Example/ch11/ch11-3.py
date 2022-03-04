import pytesseract
from PIL import Image

im = Image.open("number.jpg")
str = pytesseract.image_to_string(im, lang="eng")
print(str)
im = Image.open("traditional.jpg")
str = pytesseract.image_to_string(im, lang="chi_tra")
print(str)
im = Image.open("simple.jpg")
str = pytesseract.image_to_string(im, lang="chi_sim")
print(str)
