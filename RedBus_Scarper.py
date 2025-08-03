from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from scraper.redbus_scraper import scrape_redbus
import pandas as pd
import time

def init_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_redbus(source, destination, travel_date):
    driver = init_driver()
    driver.get("https://www.redbus.in/")
    time.sleep(3)

    # Source
    src_input = driver.find_element(By.ID, "src")
    src_input.send_keys(source)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".autoFill li").click()

    # Destination
    dest_input = driver.find_element(By.ID, "dest")
    dest_input.send_keys(destination)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".autoFill li").click()

    # Date
    driver.find_element(By.ID, "onward_cal").click()
    time.sleep(1)
    # Date format: "03-Aug-2025"
    day, month, year = travel_date.split('-')
    driver.find_element(By.XPATH, f"//td[@class='wd day' or @class='we day' or @class='current day' or @class='day' or @class='past day'][text()='{int(day)}']").click()

    # Search
    driver.find_element(By.ID, "search_btn").click()
    time.sleep(7)

    buses = []
    elements = driver.find_elements(By.XPATH, "//div[@class='bus-item-details']")

    for elem in elements:
        try:
            name = elem.find_element(By.CLASS_NAME, "travels").text
            dep_time = elem.find_element(By.CLASS_NAME, "dp-time").text
            arr_time = elem.find_element(By.CLASS_NAME, "bp-time").text
            seats = elem.find_element(By.CLASS_NAME, "seat-left").text
            fare = elem.find_element(By.CLASS_NAME, "fare").text
            buses.append({
                "Bus Operator": name,
                "Departure": dep_time,
                "Arrival": arr_time,
                "Seat Availability": seats,
                "Fare": fare
            })
        except Exception:
            continue

    driver.quit()
    return pd.DataFrame(buses)
