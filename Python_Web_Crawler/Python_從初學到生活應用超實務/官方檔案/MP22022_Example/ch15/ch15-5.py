from selenium import webdriver
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
driver.get(url)

keyword_css = "#main-form > div > div > form > input"
keyword = driver.find_element_by_css_selector(keyword_css)
keyword.send_keys("2330")
button_css = "#main-form > div > div > form > a.button.search"
button = driver.find_element_by_css_selector(button_css)
button.click()

table_tag = driver.find_element_by_id("report-table")
th_tags = table_tag.find_elements_by_tag_name("th")
row = []
for th_tag in th_tags:
    row.append(th_tag.text)
ws.append(row)
tr_tags = table_tag.find_elements_by_tag_name("tr")
for tr_tag in tr_tags:
    td_tags = tr_tag.find_elements_by_tag_name("td")
    row = []
    for td_tag in td_tags:
        row.append(td_tag.text)
    if row:
        ws.append(row)
driver.quit()
wb.save("2330.xlsx")