from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Selenium.html")
content = driver.find_element_by_class_name("content")
print(content.text)
driver.quit()