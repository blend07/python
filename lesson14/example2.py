import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Countries.csv")

plt.figure(figsize=(8,8))
sns.heatmap(df.drop(columns="Countries").corr(), annot=True, cmap="coolwarm")
plt.title("Average IQ distribuation by country")


plt.tight_layout()

plt.show()