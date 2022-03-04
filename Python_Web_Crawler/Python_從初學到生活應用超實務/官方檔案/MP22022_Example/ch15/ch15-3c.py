from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Selenium.html")
link1 = driver.find_element_by_link_text('Continue')
print(link1.text)
link2 = driver.find_element_by_partial_link_text('Conti')
print(link2.text)
link3 = driver.find_element_by_link_text('取消')
print(link3.text)
link4 = driver.find_element_by_partial_link_text('取')
print(link4.text)
driver.quit()