import pandas as pd


products = ["Apples", "Oranges", "Bananas", "Grape"]
sales = [150 ,235, 64, 82]

sale_series = pd.Series(sales , index=products)
print(sale_series)

print(sale_series("Grape"))

total_sales= sale_series.sum()
print(total_sales)

data = { 'Name': ['Alice', 'Bob', 'Leon'],
        'Age' : [22, 30, 22],
        'City' : ['New York', 'San Francisco', 'Los Angeles']
}

df=pd.DataFrame(data)
print(df)

df2 = pd.read_csv('cs.csv')
df2.to_csv('output_database.csv', index = False)