from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("book.csv")
print(df.head())

engine = create_engine("mysql+pymysql://root@localhost:3306/mybook")
df.to_sql("newbook", engine, index=False)
print("在 mybook 資料庫建立 newbook 資料表...")

