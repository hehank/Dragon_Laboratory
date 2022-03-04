import requests

url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$filter=SiteName%20eq%20%27%E4%B8%AD%E5%B1%B1%27&$orderby=SiteName&$skip=0&$top=1000&format=json"

response = requests.get(url)
if response.status_code == requests.codes.ok:
    data = response.json() 
    airQuality = data[0]
    print("測站名稱：", airQuality["SiteName"])
    print("發布時間：", airQuality["PublishTime"])
    print("空污狀態：", airQuality["Status"])
    print("AQI指標：", airQuality["AQI"])
    print("PM2.5：", airQuality["PM2.5"])
else:
    print("HTTP請求錯誤...")




