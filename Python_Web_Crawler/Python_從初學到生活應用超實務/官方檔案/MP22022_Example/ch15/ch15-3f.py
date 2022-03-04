from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Selenium.html")
content = driver.find_element_by_css_selector("h3.content")
print(content.text)
p = driver.find_element_by_css_selector("p")
print(p.text)
driver.quit()