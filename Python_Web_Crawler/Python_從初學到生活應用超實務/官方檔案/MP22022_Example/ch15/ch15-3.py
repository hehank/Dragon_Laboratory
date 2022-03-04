from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Selenium.html")
form = driver.find_element_by_id("loginForm")
print(form.tag_name)
print(form.get_attribute("id"))
driver.quit()
