from select import select
import mysql.connector
from mysql.connector import errors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
s = Service('C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("https://affidavit.eci.gov.in/")


s1 = driver.find_element(by = By.XPATH,value = ('//*[@id="election"]'))
drp = Select(s1)
drp.select_by_index(2)
driver.implicitly_wait(10)
s2 = driver.find_element(by = By.XPATH,value = ('//*[@id="electionType"]'))
drp2 = Select(s2)

for i in range(1,len(drp2.options)):
	drp2.select_by_index(i)
	s3 = driver.find_element(by = By.XPATH,value = ('//*[@id="states"]'))
	drp3 = Select(s3)
	for j in range(1,len(drp3.options)-1):
		drp3.select_by_index(j)

		driver.find_element(by = By.XPATH,value=('//*[@id="CandidateCustomFilter"]/button')).click()
		s4 = driver.find_elements(by = By.XPATH,value = ('/html/body/main/section/div/div/div/div/div/div[2]/div/ul/li'))
		print(len(s4))
		for index in range(1,len(s4)):
			try:
				driver.refresh()
				driver.find_element(by = By.XPATH,value=f'/html/body/main/section/div/div/div/div/div/div[2]/div/ul/li[{index}]').click()
				records = driver.find_elements(by = By.XPATH ,value = ('//*[@id="data-tab"]/tbody/tr/td[2]'))
				driver.set_page_load_timeout(10)
				for record in records:
					print(record.text)
			except  StaleElementReferenceException as e: raise e







