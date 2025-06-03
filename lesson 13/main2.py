import pandas as pd


products = ["Apples", "Oranges", "Bananas", "Grape"]
sales = [150 ,235, 64, 82]

sale_series = pd.Series(sales , index=products)
print(sale_series)