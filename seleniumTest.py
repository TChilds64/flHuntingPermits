from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

#Define parameters
values =  ["Quota – Archery (2025)","Quota – General Gun (2025)", "Quota – Wild Hog (2025)"]
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                          options= options)

#Navigate to FWC Permit Availability Site
driver.get("https://license.gooutdoorsflorida.com/license/PublicQuotaInventory")

for value in values:
    #Choose hunt type
    dropdown = driver.find_element("id", "PhaseCategoryID")
    dropdown.click()
    dropdown.send_keys(value)
    dropdown.send_keys(Keys.ENTER)

    #Click Export Button
    time.sleep(4)
    exportButton = driver.find_element("class name", "buttons-excel")
    exportButton.click()
    #Clear search
    clearButton = driver.find_element("id", "btnClearSearch")
    clearButton.click()



