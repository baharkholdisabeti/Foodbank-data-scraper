from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json
import re


url = 'https://www.foodbankscanada.ca/utility-pages/find-a-food-bank.aspx'
driver = webdriver.Chrome('chromedriver/chromedriver')
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
#try:


province_chooser = Select(driver.find_element_by_name('p$lt$zoneContent$pageplaceholder$p$lt$zoneColumnTwo$FindAFoodBank$drpSearchProvince'))
ontario = province_chooser.select_by_value('ON')
search_button = driver.find_element_by_xpath("//input[@id='p_lt_zoneContent_pageplaceholder_p_lt_zoneColumnTwo_FindAFoodBank_btnSearchLocation']")
search_button.click()

# wait for new page to load
time.sleep(10)

content = content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, "html.parser")
branch_arr = []

count = 1
for branch in soup.findAll('h2'):
    if branch.text == "Connect with Us":
        break
    details_list = branch.find_next_siblings(text=True)
    details = ""
    for detail in details_list:
        if detail.strip() != "":
            details += detail.strip() + "\n"

    branch_object = {
        "pk": count,
        "model": "foodbank.branch",
        "fields": {
            "branch_name": branch.text,
            "branch_info": details,
        },
    }
    print(branch_object)
    branch_arr.append(branch_object)
    count += 1

with open('branch_data.json', 'w') as outfile:
    json.dump(branch_arr, outfile)