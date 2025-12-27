import pandas as pd
import numpy as np
csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df_csv = pd.read_csv(csv_url)

# print(df_csv.head())
# print(df_csv.tail())
# print(df_csv.info())
# print(df_csv.describe())
# print(df_csv[[ 0]])
# filtered_rows = df_csv[(df_csv["sepal_length"] > 5.0) & (df_csv["species"]== 'versicolor')]
# print(filtered_rows)
data = {
    'name': ["Cathrina", "recheal", "Oreoluwa", "Amaka", "mina", np.nan],
    "age": [26, np.nan, 22, 24, 23, 25],
    "score": [95, 46, np.nan, np.nan, 71, 83]
}

df = pd.DataFrame(data)
print("original data: \n", df)
# fill missing values
df["age"] = df['age'].fillna(df['age'].mean())
df['score'] = df['score'].interpolate()
print("updated data: \n", df)