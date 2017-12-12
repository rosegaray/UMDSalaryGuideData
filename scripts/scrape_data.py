from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import requests as rq
import re


# Using PhantomJS to render the webpage
driver = webdriver.PhantomJS(executable_path="/Users/rosegaray/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.set_window_size(1920,1080)

driver.get("http://salaryguide.diamondbacklab.com/#/salGuide")
# Wait for site to load
wait = WebDriverWait(driver, 20)

# Stores each page's data
data = {}

for page in range(2):
	# Grab "tbody" tag
	wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))

	# Store in data - page is a string containing all html
	data[page] = driver.page_source

	# Click on the next 
	driver.find_element_by_id("next").click()

driver.close()

for page in data.items():
	soup = bs(data[page], 'html.parser')
	soup.prettify()



# data = []
# table = soup.find('table', attrs={'class':'lineItemsTable'})
# table_body = table.find('tbody')

# rows = table_body.find_all('tr')
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     data.append([ele for ele in cols if ele]) # Get rid of empty values






