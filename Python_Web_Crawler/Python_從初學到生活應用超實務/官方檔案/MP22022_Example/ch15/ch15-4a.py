from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://duckduckgo.com"
driver.get(url)

keyword = driver.find_element_by_css_selector("#search_form_input_homepage")
keyword.send_keys("XPath")
keyword.send_keys(Keys.ENTER)
items = driver.find_elements_by_class_name("result__a")
for item in items:
    print(item.text, end=" : ")
    print(item.get_attribute("href"))
driver.quit()