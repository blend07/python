import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("average_iq_by_country.csv")

plt.figure(figsize=(8,8))
sns.histplot(data=df, x="Average_IQ", bins= 5, kde=True)
plt.title("Average IQ distribuation by country")
plt.xlabel("Average IQ")
plt.ylabel("Frequency")

plt.tight_layout()

plt.show()