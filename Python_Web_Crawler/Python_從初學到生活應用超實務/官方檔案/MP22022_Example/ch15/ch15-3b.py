from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Selenium.html")
# 定位<form>標籤
form = driver.find_element_by_xpath('//*[@id="loginForm"]')
print(form.tag_name)
# 定位密碼欄位
pwd = driver.find_element_by_xpath('//*[@id="loginPwd"]')
print(pwd.get_attribute("type"))
# 定位清除按鈕
clear = driver.find_element_by_xpath('//*[@id="loginForm"]/input[4]')
print(clear.get_attribute("type"))
driver.quit()
