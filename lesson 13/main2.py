import pandas as pd


products = ["Apples", "Oranges", "Bananas", "Grape"]
sales = [150 ,235, 64, 82]

sale_series = pd.Series(sales , index=products)
print(sale_series)

print(sale_series["Grape"])

total_sales= sale_series.sum()
print(total_sales)

best_selling_products = sale_series.idxmax()
print(f"Best selling product is: {best_selling_products}")

data = { 'Name': ['Alice', 'Bob', 'Leon'],
        'Age' : [22, 30, 22],
        'City' : ['New York', 'San Francisco', 'Los Angeles']
}

df=pd.DataFrame(data)
print(df)

df2 = pd.read_csv('avgIQpercountry.csv')
print(df2.info())

print_rows = df2.head()

first_rows = df2.head()
print(first_rows)

subset = df2[['Country', 'Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ'] < 100]
print(filtered_df)


