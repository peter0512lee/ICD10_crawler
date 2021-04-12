import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd

driverPath = "./chromedriver.exe" #填入剛剛記下的路徑
driver = webdriver.Chrome(driverPath) # Chrome
driver.get("http://icdsearch.idv.tw/TRANS/trans.htm")
# print(driver.title)

driver.switch_to.frame(1)
driver.find_element(By.NAME, "Name").click()
driver.find_element(By.NAME, "Name").send_keys("733.1")
driver.find_element(By.NAME, "Name").send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# table = soup.find_all('table')
# print(table)

df_data = pd.DataFrame()

df = pd.read_html(driver.page_source, header=0)[0]
df_data = df
print(df_data)

driver.find_element(By.LINK_TEXT, "下一頁").click()
df = pd.read_html(driver.page_source, header=0)[0]
df_data.append(df)
print(df_data)

# df_data.to_csv(index = False)