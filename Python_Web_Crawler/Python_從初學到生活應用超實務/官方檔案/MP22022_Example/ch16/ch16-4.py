import pymysql
import pandas as pd

conn = pymysql.connect("localhost","root","","mybook",charset="utf8")
sql = "SELECT * FROM book"
df = pd.read_sql(sql, con=conn)
print(df.head())
conn.close() 
