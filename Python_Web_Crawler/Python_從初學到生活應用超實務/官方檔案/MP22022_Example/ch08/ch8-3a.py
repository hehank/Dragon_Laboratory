import pandas as pd

df = pd.read_csv("Youbike.csv")
df.plot(kind="scatter", x="lat", y="lng", 
        title="Youbike各站點經緯度座標")


