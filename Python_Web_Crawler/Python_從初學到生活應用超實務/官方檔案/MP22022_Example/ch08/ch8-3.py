import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Youbike.csv")
df_grouped = df.groupby("sarea")
sites = df_grouped["tot"].count()
avg = df_grouped["tot"].mean()
data = pd.DataFrame()
data["站點數"] = sites
data["車位平均數"] = avg
data.plot(kind="bar")
plt.title("各行政區Youbike站點數和平均車位數")




