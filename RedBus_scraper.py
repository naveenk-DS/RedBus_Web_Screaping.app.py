#Data scraping Redbus
#data scraping of Route name and link for HRTC 
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

hrtc_button = driver.find_element(By.XPATH,'//div[@class="rtcName"]')
hrtc_button.click()

hrtc_route_names = []
hrtc_route_links = []
#routes = driver.find_elements(By.CSS_SELECTOR,"a[class='route']")

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        hrtc_route_names.append(route_name)
        hrtc_route_links.append(route_link)

for page_number in range(1, 5):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 4:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break

driver.quit()


df_hrtc = pd.DataFrame({"Route_Name":hrtc_route_names,"Route_Link":hrtc_route_links})
df_hrtc

path = r"E:/RedBus_Scraper_App/df_hrtc.csv"
df_hrtc.to_csv(path,index=False)


#data scraping of Route name and link for RSRTC
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

rsrtc_button = driver.find_element(By.XPATH, "//div[contains(text(),'RSRTC')]")
rsrtc_button.click()

rsrtc_route_names = []
rsrtc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        rsrtc_route_names.append(route_name)
        rsrtc_route_links.append(route_link)

for page_number in range(1, 3):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 2:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break

driver.quit()

df_rsrtc = pd.DataFrame({"Route_Name":rsrtc_route_names,"Route_Link":rsrtc_route_links})
df_rsrtc


path = r"E:/RedBus_Scraper_App/df_rsrtc.csv"
df_rsrtc.to_csv(path,index=False)


#data scraping of Route name and link for PEPSU
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

pepsu_button = driver.find_element(By.XPATH, "//div[contains(text(),'PEPSU')]")
driver.execute_script("arguments[0].scrollIntoView(true);", pepsu_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", pepsu_button)

pepsu_route_names = []
pepsu_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        pepsu_route_names.append(route_name)
        pepsu_route_links.append(route_link)

for page_number in range(1, 3):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 2:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break

driver.quit()

df_pepsu = pd.DataFrame({"Route_Name":pepsu_route_names,"Route_Link":pepsu_route_links})
df_pepsu

path = r"E:/RedBus_Scraper_App/df_pepsu.csv"
df_pepsu.to_csv(path,index=False)


#data scraping of Route name and link for CTURTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

cturtc_button = driver.find_element(By.XPATH, "//div[contains(text(),'CTU RTC')]")
driver.execute_script("arguments[0].scrollIntoView(true);", cturtc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", cturtc_button)

cturtc_route_names = []
cturtc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        cturtc_route_names.append(route_name)
        cturtc_route_links.append(route_link)

for page_number in range(1, 6):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 5:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break

driver.quit()

df_cturtc = pd.DataFrame({"Route_Name":cturtc_route_names,"Route_Link":cturtc_route_links})
df_cturtc

path = r"E:/RedBus_Scraper_App/df_cturtc.csv"
df_cturtc.to_csv(path,index=False)


#data scraping of Route name and link for JKSRTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

jksrtc_button = driver.find_element(By.XPATH, "//div[contains(text(),'JKSRTC')]")
driver.execute_script("arguments[0].scrollIntoView(true);", jksrtc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", jksrtc_button)

jksrtc_route_names = []
jksrtc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        jksrtc_route_names.append(route_name)
        jksrtc_route_links.append(route_link)

scrape_routes()
driver.quit()

df_jksrtc = pd.DataFrame({"Route_Name":jksrtc_route_names,"Route_Link":jksrtc_route_links})
df_jksrtc

path = r"E:/RedBus_Scraper_App/df_jksrtc.csv"
df_jksrtc.to_csv(path,index=False)


#data scraping of Route name and link for SBSTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

sbstc_button = driver.find_element(By.XPATH, '//div[@class="rtcBack"]//div[contains(text(),"SBSTC")]')
driver.execute_script("arguments[0].scrollIntoView(true);", sbstc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", sbstc_button)

sbstc_route_names = []
sbstc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        sbstc_route_names.append(route_name)
        sbstc_route_links.append(route_link)

for page_number in range(1, 6):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 5:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break

driver.quit()

df_sbstc = pd.DataFrame({"Route_Name":sbstc_route_names,"Route_Link":sbstc_route_links})
df_sbstc

path = r"E:/RedBus_Scraper_App/df_sbstc.csv"
df_sbstc.to_csv(path,index=False)


#data scraping of Route name and link for KTCL
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

ktcl_button = driver.find_element(By.XPATH, '//div[@class="rtcBack"]//div[contains(text(),"KTCL")]')
driver.execute_script("arguments[0].scrollIntoView(true);", ktcl_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", ktcl_button)

ktcl_route_names = []
ktcl_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        ktcl_route_names.append(route_name)
        ktcl_route_links.append(route_link)

for page_number in range(1, 5):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 4:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break


driver.quit()

df_ktcl = pd.DataFrame({"Route_Name":ktcl_route_names,"Route_Link":ktcl_route_links})
df_ktcl

path = r"E:/RedBus_Scraper_App/df_ktcl.csv"
df_ktcl.to_csv(path,index=False)


#data scraping of Route name and link for NBSTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

nbstc_button = driver.find_element(By.XPATH, '//div[@class="rtcBack"]//div[contains(text(),"NBSTC")]')
driver.execute_script("arguments[0].scrollIntoView(true);", nbstc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", nbstc_button)

nbstc_route_names = []
nbstc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        nbstc_route_names.append(route_name)
        nbstc_route_links.append(route_link)

for page_number in range(1, 6):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 5:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break


driver.quit()

df_nbstc = pd.DataFrame({"Route_Name":nbstc_route_names,"Route_Link":nbstc_route_links})
df_nbstc

path = r"E:/RedBus_Scraper_App/df_nbstc.csv"
df_nbstc.to_csv(path,index=False)


#data scraping of Route name and link for KSRTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

klrtc_button = driver.find_element(By.XPATH, '//div[@class="rtcBack"]//div[contains(text(),"KERALA RTC")]')
driver.execute_script("arguments[0].scrollIntoView(true);", klrtc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", klrtc_button)

klrtc_route_names = []
klrtc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        klrtc_route_names.append(route_name)
        klrtc_route_links.append(route_link)

for page_number in range(1, 3):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 2:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break


driver.quit()

df_klrtc = pd.DataFrame({"Route_Name":klrtc_route_names,"Route_Link":klrtc_route_links})
df_klrtc

path = r"E:/RedBus_Scraper_App/df_klrtc.csv"
df_klrtc.to_csv(path,index=False)


#data scraping of Route name and link for BSRTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

bsrtc_button = driver.find_element(By.XPATH, '//div[@class="rtcBack"]//div[contains(text(),"BSRTC")]')
driver.execute_script("arguments[0].scrollIntoView(true);", bsrtc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", bsrtc_button)

bsrtc_route_names = []
bsrtc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        bsrtc_route_names.append(route_name)
        bsrtc_route_links.append(route_link)

for page_number in range(1, 5):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 4:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break


driver.quit()

df_bsrtc = pd.DataFrame({"Route_Name":bsrtc_route_names,"Route_Link":bsrtc_route_links})
df_bsrtc

path = r"E:/RedBus_Scraper_App/df_bsrtc.csv"
df_bsrtc.to_csv(path,index=False)


#data scraping of Route name and link for APSRTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

apsrtc_button = driver.find_element(By.XPATH, '//div[@class="rtcBack"]//div[contains(text(),"APSRTC")]')
driver.execute_script("arguments[0].scrollIntoView(true);", apsrtc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", apsrtc_button)

apsrtc_route_names = []
apsrtc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        apsrtc_route_names.append(route_name)
        apsrtc_route_links.append(route_link)

for page_number in range(1, 6):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 5:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break


driver.quit()

df_apsrtc = pd.DataFrame({"Route_Name":apsrtc_route_names,"Route_Link":apsrtc_route_links})
df_apsrtc

path = r"E:/RedBus_Scraper_App/df_apsrtc.csv"
df_apsrtc.to_csv(path,index=False)


#data scraping of Route name and link for UPSRTC
driver = webdriver.Chrome()
driver.get('https://www.redbus.in/');
time.sleep(3)
wait = WebDriverWait(driver, 10)

upsrtc_button = driver.find_element(By.XPATH, '//div[@class="rtcBack"]//div[contains(text(),"UPSRTC")]')
driver.execute_script("arguments[0].scrollIntoView(true);", upsrtc_button)
time.sleep(2)
driver.execute_script("arguments[0].click();", upsrtc_button)

upsrtc_route_names = []
upsrtc_route_links = []

def scrape_routes():
    routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
    for route in routes:
        route_name = route.text  # Get the route name
        route_link = route.get_attribute('href')  # Get the route link
        #print(f"Route Name: {route_name}, Route Link: {route_link}")
        upsrtc_route_names.append(route_name)
        upsrtc_route_links.append(route_link)

for page_number in range(1, 6):
    #print(f"Scraping page {page_number}...")
    # Scrape the current page
    scrape_routes()
    if page_number < 5:
    # Navigate to the next page
        try:
            # Locate the pagination element
            next_page_button = driver.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text() ="{page_number + 1}"]')
            
            # Scroll to the pagination button and click it
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
            time.sleep(2)
            next_page_button.click()
            
            # Wait for the page to load
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break


driver.quit()

df_upsrtc = pd.DataFrame({"Route_Name":upsrtc_route_names,"Route_Link":upsrtc_route_links})
df_upsrtc

path = r"E:/RedBus_Scraper_App/df_upsrtc.csv"
df_upsrtc.to_csv(path,index=False)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Function for scraping data of bus details 
def scrap_details():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    bus_name_1 = []
    bus_type_1 = []
    departing_time_1 = []
    duration_1 = []
    reaching_time_1 = []
    star_rating_1 = []
    price_1 = []
    seats_available_1 = []
    Route_Names = []
    Route_links = []
    
    for i, k in df_1.iterrows():
        link = k['Route_Link']
        routes = k['Route_Name']
    
        driver.get(link)
        time.sleep(4)
    
        elements = driver.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
        for element in elements:
            element.click()
            time.sleep(4)
    
        try:
            view_bus = driver.find_element(By.XPATH, "//div[@class='button']")
            view_bus.click()
        except Exception as e:
            print(f"Error clicking view bus: {e}")
            pass #Continue scraping without clicking the button
        
        time.sleep(3)
        
        scrolling = True
        last_height = driver.execute_script("return document.body.scrollHeight")
        while scrolling:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                scrolling = False
            last_height = new_height
        
        try:
            # Collecting bus details
            bus_name_elements = driver.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
            bus_type_elements = driver.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
            price_elements = driver.find_elements(By.XPATH, "//*[@class='fare d-block']")
            departing_time_elements = driver.find_elements(By.XPATH, "//div[@class='dp-time f-19 d-color f-bold']")
            reaching_time_elements = driver.find_elements(By.XPATH, "//div[@class='bp-time f-19 d-color disp-Inline']")
            duration_elements = driver.find_elements(By.XPATH, "//div[@class='dur l-color lh-24']")
            star_rating_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'rating-sec lh-24')]//span")
            seats_available_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'seat-left')]")
            
            num_buses = len(bus_name_elements)
    
            # Ensure each list has the same length, adding placeholders when needed
            for idx in range(num_buses):
                bus_name_1.append(bus_name_elements[idx].text if idx < len(bus_name_elements) else None)
                bus_type_1.append(bus_type_elements[idx].text if idx < len(bus_type_elements) else None)
                price_1.append(price_elements[idx].text if idx < len(price_elements) else None)
                departing_time_1.append(departing_time_elements[idx].text if idx < len(departing_time_elements) else None)
                reaching_time_1.append(reaching_time_elements[idx].text if idx < len(reaching_time_elements) else None)
                duration_1.append(duration_elements[idx].text if idx < len(duration_elements) else None)
                star_rating_1.append(star_rating_elements[idx].text if idx < len(star_rating_elements) else None)
                seats_available_1.append(seats_available_elements[idx].text if idx < len(seats_available_elements) else None)
                Route_Names.append(routes)
                Route_links.append(link)
    
        except Exception as e:
            print(f"Error retrieving bus details: {e}")
            continue
    
    # Creating DataFrame and saving to CSV
    data = {
        'Route_name': Route_Names,
        'Route_link': Route_links,
        'Bus_Name': bus_name_1,
        'Bus_Type': bus_type_1,
        'Departing_Time': departing_time_1,
        'Duration': duration_1,
        'Reaching_Time': reaching_time_1,
        'Star_Rating': star_rating_1,
        'Price': price_1,
        'Seats_available': seats_available_1
    }
    
    driver.quit()  # Close the browser when done
    
    return data


#Scraping data of ksrtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_klrtc.csv")
df_klrtc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_klrtc_buses.csv"
df_klrtc_buses.to_csv(path, index=False)

#Scraping data of jksrtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_jksrtc.csv")
df_jksrtc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_jksrtc_buses.csv"
df_jksrtc_buses.to_csv(path, index=False)


#Scraping data of cturtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_cturtc.csv")
df_cturtc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_cturtc_buses.csv"
df_cturtc_buses.to_csv(path, index=False)


#Scraping data of ktcl bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_ktcl.csv")
df_ktcl_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_ktcl_buses.csv"
df_ktcl_buses.to_csv(path, index=False)


#Scraping data of nbstc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_nbstc.csv")
df_nbstc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_nbstc_buses.csv"
df_nbstc_buses.to_csv(path, index=False)


#Scraping data of pepsu bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_pepsu.csv")
df_pepsu_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_pepsu_buses.csv"
df_pepsu_buses.to_csv(path, index=False)


#Scraping data of rsrtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_rsrtc.csv")
df_rsrtc_buses = pd.DataFrame(scrap_details())
path = r"E:/URedBus_Scraper_App/df_rsrtc_buses.csv"
df_rsrtc_buses.to_csv(path, index=False)


#Scraping data of sbstc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_sbstc.csv")
df_sbstc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_sbstc_buses.csv"
df_sbstc_buses.to_csv(path, index=False)


#Scraping data of bsrtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_bsrtc.csv")
df_bsrtc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_bsrtc_buses.csv"
df_bsrtc_buses.to_csv(path, index=False)


#Scraping data of hrtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_hrtc.csv")
df_hrtc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_hrtc_buses.csv"
df_hrtc_buses.to_csv(path, index=False)


#Scraping data of apsrtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_apsrtc.csv")
df_apsrtc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_apsrtc_buses.csv"
df_apsrtc_buses.to_csv(path, index=False)


#Scraping data of upsrtc bus
df_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_upsrtc.csv")
df_upsrtc_buses = pd.DataFrame(scrap_details())
path = r"E:/RedBus_Scraper_App/df_upsrtc_buses.csv"
df_upsrtc_buses.to_csv(path, index=False)


import pandas as pd
import mysql.connector
import numpy as np


#Concatinating all Bus data csv file into single Data frame
df_bus_1 = pd.read_csv(r"E:/RedBus_Scraper_App/df_hrtc_buses.csv")
df_bus_2 = pd.read_csv(r"E:/RedBus_Scraper_App/df_bsrtc_buses.csv")
df_bus_3 = pd.read_csv(r"E:RedBus_Scraper_App/df_sbstc_buses.csv")
df_bus_4 = pd.read_csv(r"E:RedBus_Scraper_App/df_rsrtc_buses.csv")
df_bus_5 = pd.read_csv(r"E:RedBus_Scraper_App/df_pepsu_buses.csv")
df_bus_6 = pd.read_csv(r"E:RedBus_Scraper_App/df_nbstc_buses.csv")
df_bus_7 = pd.read_csv(r"E:RedBus_Scraper_App/df_ktcl_buses.csv")
df_bus_8 = pd.read_csv(r"E:RedBus_Scraper_App/df_cturtc_buses.csv")
df_bus_9 = pd.read_csv(r"E:RedBus_Scraper_App/df_klrtc_buses.csv")
df_bus_10 = pd.read_csv(r"E:RedBus_Scraper_App/df_jksrtc_buses.csv")
df_bus_11 = pd.read_csv(r"E:RedBus_Scraper_App/df_apsrtc_buses.csv")
df_bus_12 = pd.read_csv(r"E:RedBus_Scraper_App/df_upsrtc_buses.csv")

final_df = pd.concat([df_bus_1,df_bus_2,df_bus_3,df_bus_4,df_bus_5,df_bus_6,
                      df_bus_7,df_bus_8,df_bus_9,df_bus_10,df_bus_11,df_bus_12],ignore_index = True)



final_df.info()


#DATA CLEANING
final_df['Bus_Name'] = final_df['Bus_Name'].fillna('Not Available')
final_df['Bus_Type'] = final_df['Bus_Type'].fillna('Not Available')
final_df['Departing_Time'] = pd.to_datetime(final_df['Departing_Time'], format = '%H:%M',errors='coerce').dt.time
final_df['Departing_Time'] = final_df['Departing_Time'].fillna(pd.to_datetime('00:00', format='%H:%M').time())
final_df['Duration'] = final_df['Duration'].fillna('0')
final_df['Reaching_Time'] = pd.to_datetime(final_df['Reaching_Time'], format = '%H:%M',errors='coerce').dt.time
final_df['Reaching_Time'] = final_df['Reaching_Time'].fillna(pd.to_datetime('00:00', format='%H:%M').time())
final_df['Star_Rating'] = final_df['Star_Rating'].astype(str)
final_df['Star_Rating'] = final_df['Star_Rating'].str.replace("New","").str.strip()
final_df['Star_Rating'] = final_df['Star_Rating'].str.split().str[0]
final_df['Star_Rating'] = pd.to_numeric(final_df['Star_Rating'], errors = 'coerce')
final_df['Price'] = final_df['Price'].astype(str)
final_df['Price'] = final_df['Price'].str.replace('INR', '').str.strip()
final_df['Price'] = pd.to_numeric(final_df['Price'], errors='coerce')
final_df['Price'] = final_df['Price'].fillna(0)
final_df['Seats_available'] = final_df['Seats_available'].str.replace("Seats available","").str.strip()
final_df['Seats_available'] = pd.to_numeric(final_df['Seats_available'], errors='coerce').fillna(0).astype(int)


final_df = final_df.replace({np.nan: None})
path = r"E:/RedBus_Scraper_App/final_busdetails_df.csv"
final_df.to_csv(path,index = False)
