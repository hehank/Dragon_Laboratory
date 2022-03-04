import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Youbike.csv")
df_grouped = df.groupby("sarea")
tot = df_grouped["tot"].count()
tot.plot(kind="pie",
         figsize=(8, 8),
         title="各區Youbike站點數") 
plt.legend(tot.index, loc="best")




