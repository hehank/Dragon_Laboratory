import matplotlib.pyplot as plt

labels = ["Python","C++","Java","JS","C","C#"]
index = range(len(labels))
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
plt.barh(index, ratings)
plt.xticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()





