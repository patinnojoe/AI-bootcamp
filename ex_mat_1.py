import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# years = [2020,2021,2022,2023,2024,2025,2026]
# sales = [100, 300, 600, 1000, 1500, 2000, 3500]

# plt.plot(years, sales, label="Sales trend", marker="o", color="blue")
# plt.xlabel("years")
# plt.ylabel("Sales")
# plt.title("Patrick Sales")
# plt.legend()
# plt.show()

# categories= ["clothing", "electronics", "grociries"]
# revenue = [100, 150, 300]
# plt.bar(categories, revenue, color="green")
# plt.title("Revenue")
# plt.show()

# hours_study = [1,2,3,4,5]
# exam_scores = [50, 55, 60, 70, 85]

# plt.scatter(hours_study, exam_scores, color="red")
# plt.title("Hours Studied vs Exam Scores")
# plt.xlabel("Hours Studied")
# plt.ylabel("Exam Scores")
# plt.show()
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df = pd.DataFrame(data)
del df['species']
correlation_metrics = df.corr()
sns.heatmap(correlation_metrics, annot=True, cmap="coolwarm")
plt.title("Heat map")
plt.show()

