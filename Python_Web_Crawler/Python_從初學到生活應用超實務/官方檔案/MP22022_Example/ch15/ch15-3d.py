from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Selenium.html")
h3 = driver.find_element_by_tag_name("h3")
print(h3.text)
p = driver.find_element_by_tag_name("p")
print(p.text)
driver.quit()