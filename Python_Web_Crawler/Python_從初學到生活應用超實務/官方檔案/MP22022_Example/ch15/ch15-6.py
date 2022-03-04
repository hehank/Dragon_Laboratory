from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("http://stats.nba.com/players/traditional/?sort=PTS&dir=-1")

button = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
button.click()
time.sleep(1)

pages_remaining = True
page_num = 1
while pages_remaining:
    df = pd.read_html(driver.page_source)
    df[0].to_csv("ALL_players_stats" + str(page_num) + ".csv")
    print("儲存頁面:", page_num)
    try:   
        next_link = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]')
        next_link.click()
        time.sleep(5)
        if page_num < 11:
            page_num = page_num + 1
        else:
            pages_remaining = False
    except Exception:
        pages_remaining = False        
driver.close()