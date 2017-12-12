from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import requests as rq
import re
import csv



# Using PhantomJS to render the webpage
driver = webdriver.PhantomJS(executable_path="/Users/rosegaray/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.set_window_size(1920,1080)

driver.get("http://salaryguide.diamondbacklab.com/#/salGuide?year=2017")
#2017 is 1029
#2016 is 1010
#2015 is 1022
#2014 is 1251
#2013 is 1210

# Wait for site to load
wait = WebDriverWait(driver, 20)

# Stores each page's data
data = {}
	
for page in range(1029):
	# Grab "tbody" tag
	wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))

	# Store in data - page is a string containing all html
	data[page] = driver.page_source

	# Click on the next 
	driver.find_element_by_id("next").click()

driver.close()

with open("2017_data.csv","w") as acct:
	writer = csv.writer(acct)
	for page, content in data.items():
		soup = bs(content, 'html.parser')
		soup.prettify()
		#print(soup)
		for tr in soup.find_all('tr'):
			stack = []
			for td in tr.findAll('td'):
				stack.append(td.text.replace('\n', '').replace('\t', '').strip())
			writer.writerow(stack)

