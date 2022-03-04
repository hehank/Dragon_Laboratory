import matplotlib.pyplot as plt

labels = ["Python","C++","Java","JS","C","C#"]
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
plt.pie(ratings, labels=labels)
plt.title("Programming Language Usage")
plt.title("程式語言的使用率")  
plt.axis("equal")
plt.show()





