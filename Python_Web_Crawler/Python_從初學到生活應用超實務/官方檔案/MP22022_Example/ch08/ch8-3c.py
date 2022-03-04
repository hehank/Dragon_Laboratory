import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Youbike0001.csv")
data = pd.DataFrame()
def get_time(dt):
    return dt[8:10] + ":" + dt[10:12]
data["時間"] = df["mday"].astype(str)
data["時間"] = data["時間"].apply(get_time)
data["車輛數"] = df["sbi"]
data["空位數"] = df["bemp"]
data = data.set_index("時間")
data.plot(kind="line")
plt.title("捷運市政府站車輛數和空位數的趨勢圖")