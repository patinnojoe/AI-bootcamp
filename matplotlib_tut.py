import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# name = ["Patrick", "Levi", "Gideon", "Victory"]
# age = [25, 27,23, 21]
# plt.plot(name, age)
# plt.show()

# year = [2022, 2023, 2024, 2025]
# sales = [10000, 20000, 25000, 42000]
# plt.bar(year,sales, color=['yellow', 'brown', 'blue', 'red'])
# plt.legend()
# plt.show()

# data = [3, 4, 1, 2,5, 6, 9, 5, 7, 3, 6, 7, 8]
# plt.hist(data, bins='auto', color="red", edgecolor="black")
# plt.title("First histogram")
# plt.show()

# x = [1, 2,4, 3, 5]
# y = [10,20,40,30, 50]
# plt.scatter(x,y, color="red")
# plt.show()

data = np.random.rand(5,5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title('heat map')
plt.show()