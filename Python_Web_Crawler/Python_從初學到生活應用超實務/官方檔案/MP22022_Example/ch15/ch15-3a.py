from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Selenium.html")
user = driver.find_element_by_name("username")
print(user.tag_name)
print(user.get_attribute("type"))
eles = driver.find_elements_by_name("continue")
for ele in eles:
    print(ele.get_attribute("type"))
driver.quit()
