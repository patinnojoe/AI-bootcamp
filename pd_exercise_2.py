import pandas as pd

data =  {
        "Class": ["A", "B", "A", "C", "B", "C", "D", "A", "D"],
        "Score": [80, 60, 86, 50, 63, 55, 47, 92, 44],
        "Age": [15, 15, 20, 22, 14, 16, 18, 15, 19]
        
    }

# df = pd.DataFrame(data)
# print("original data:\n ", df)

# grouped = df.groupby("Class").min()

# print("grouped mean data: \n", grouped)

# grouping data and getting aggregate stats

# stats = df.groupby("Class").agg(
#     {
#         "Score":["mean", "size", "max", "min"],
#         "Age": ["mean", "max", "min"]
#     }
# )

# print("aggregate stats: \n", stats)

# ADDITIONAL PRACTICE
sales_data = [
    {"product_category": "Electronics", "region": "North", "price": 1200},
    {"product_category": "Electronics", "region": "South", "price": 950},
    {"product_category": "Electronics", "region": "East", "price": 1100},
    {"product_category": "Electronics", "region": "West", "price": 1050},

    {"product_category": "Furniture", "region": "North", "price": 700},
    {"product_category": "Furniture", "region": "South", "price": 650},
    {"product_category": "Furniture", "region": "East", "price": 720},
    {"product_category": "Furniture", "region": "West", "price": 680},

    {"product_category": "Clothing", "region": "North", "price": 150},
    {"product_category": "Clothing", "region": "South", "price": 120},
    {"product_category": "Clothing", "region": "East", "price": 180},
    {"product_category": "Clothing", "region": "West", "price": 160},

    {"product_category": "Groceries", "region": "North", "price": 80},
    {"product_category": "Groceries", "region": "South", "price": 70},
    {"product_category": "Groceries", "region": "East", "price": 90},
    {"product_category": "Groceries", "region": "West", "price": 85},
]
df= pd.DataFrame(sales_data)
print(df.groupby("product_category")["price"].sum())
print(df.groupby("product_category")['region'].size())
