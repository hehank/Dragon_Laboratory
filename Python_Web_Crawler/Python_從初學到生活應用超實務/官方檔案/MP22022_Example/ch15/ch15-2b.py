from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "html.parser")
fp = open("Example.html", "w", encoding="utf8")
fp.write(soup.prettify())
print("寫入檔案Example.html...")
fp.close()
driver.quit()