import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("average_iq_by_country.csv")

countries = df["Country"]
iq_score = df["Average_IQ"]

plt.figure(figsize=(8,8))
plt.pie(iq_score, labels=countries, autopct="%1.1f%%", startangle=140)
plt.title("Average IQ distribuation by country")
plt.axis("equal")
plt.tight_layout()

plt.show()