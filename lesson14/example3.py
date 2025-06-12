import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Countries.csv")

df_melted = df.melt(id_vars="Country",
                    value_vars = ["Average_IQ", "GDP", "Education_Index", "Internet"],
                    var_name="Metric",
                    value_name="Value"
                    )

plt.figure(figsize=(10,8))
sns.boxplot(x="Metric", y="Value", data = df_melted)

plt.title("Distribution of intellegence and development metric")
plt.xlabel("Metric")
plt.ylabel("Value")
plt.tight_layout()

plt.show()