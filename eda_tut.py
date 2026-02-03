import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# inspect data
# print(df.describe())
# print(df.info())
# print(df.head())

# fixing missing data

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# remove duplicates
df = df.drop_duplicates()
first_class = df[df['Pclass']==1]
# print(first_class.head())

# create a bar chart of survival rate by class
survival_by_class = df.groupby("Pclass")['Survived'].mean()
# survival_by_class.bar(survival_by_class, title="Survival by Class", color="green" )
survival_by_class.plot(kind="bar", color="green")
plt.title("Titanic Survival rate by class")
plt.legend()
plt.show()
