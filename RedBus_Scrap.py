# RedBus Data Scraping Full Pipeline
# Author: Naveen
# Description: Scrapes RedBus route and bus data for multiple RTCs and saves to CSV

import os
import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === STEP 1: Create folder structure ===
base_path = "E:/RedBus_Scraper_App"
os.makedirs(base_path, exist_ok=True)

# === STEP 2: Define function to scrape routes ===
def scrape_rtc_routes(rtc_name, pages):
    driver = webdriver.Chrome()
    driver.get("https://www.redbus.in/")
    wait = WebDriverWait(driver, 10)
    time.sleep(3)

    try:
        rtc_button = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[contains(text(),'{rtc_name}')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", rtc_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", rtc_button)
        time.sleep(2)

        route_names, route_links = [], []

        for page_number in range(1, pages + 1):
            routes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='route']")))
            for route in routes:
                route_names.append(route.text)
                route_links.append(route.get_attribute('href'))

            if page_number < pages:
                try:
                    next_button = driver.find_element(By.XPATH, f"//div[contains(@class, 'DC_117_pageTabs') and text() ='{page_number + 1}']")
                    driver.execute_script("arguments[0].scrollIntoView();", next_button)
                    time.sleep(2)
                    next_button.click()
                    time.sleep(3)
                except:
                    print(f"No more pages for {rtc_name} at page {page_number}")
                    break

    except Exception as e:
        print(f"Error for {rtc_name}: {e}")
        route_names, route_links = [], []

    driver.quit()
    df = pd.DataFrame({"Route_Name": route_names, "Route_Link": route_links})
    df.to_csv(f"{base_path}/df_{rtc_name.lower().replace(' ', '')}.csv", index=False)
    return df

# === STEP 3: Define all RTCs ===
rtc_list = {
    "HRTC": 4,
    "RSRTC": 2,
    "PEPSU": 2,
    "CTU RTC": 5,
    "JKSRTC": 1,
    "SBSTC": 5,
    "KTCL": 4,
    "NBSTC": 5,
    "KERALA RTC": 2,
    "BSRTC": 4,
    "APSRTC": 5,
    "UPSRTC": 5
}

for rtc, pages in rtc_list.items():
    print(f"Scraping {rtc} routes...")
    scrape_rtc_routes(rtc, pages)

# === STEP 4: Scrape Bus Details for Each RTC ===
def scrape_bus_details(df_routes):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    all_data = {
        'Route_name': [], 'Route_link': [], 'Bus_Name': [], 'Bus_Type': [],
        'Departing_Time': [], 'Duration': [], 'Reaching_Time': [], 'Star_Rating': [],
        'Price': [], 'Seats_available': []
    }

    for _, row in df_routes.iterrows():
        try:
            driver.get(row['Route_Link'])
            time.sleep(5)

            # Scroll to load all buses
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            # Extract details
            bus_names = driver.find_elements(By.CLASS_NAME, 'travels')
            bus_types = driver.find_elements(By.CLASS_NAME, 'bus-type')
            prices = driver.find_elements(By.CLASS_NAME, 'fare')
            departing_times = driver.find_elements(By.CLASS_NAME, 'dp-time')
            reaching_times = driver.find_elements(By.CLASS_NAME, 'bp-time')
            durations = driver.find_elements(By.CLASS_NAME, 'dur')
            star_ratings = driver.find_elements(By.XPATH, "//div[contains(@class,'rating-sec')]//span")
            seats = driver.find_elements(By.XPATH, "//div[contains(@class,'seat-left')]")

            for i in range(len(bus_names)):
                all_data['Route_name'].append(row['Route_Name'])
                all_data['Route_link'].append(row['Route_Link'])
                all_data['Bus_Name'].append(bus_names[i].text if i < len(bus_names) else 'NA')
                all_data['Bus_Type'].append(bus_types[i].text if i < len(bus_types) else 'NA')
                all_data['Departing_Time'].append(departing_times[i].text if i < len(departing_times) else '00:00')
                all_data['Duration'].append(durations[i].text if i < len(durations) else '0')
                all_data['Reaching_Time'].append(reaching_times[i].text if i < len(reaching_times) else '00:00')
                all_data['Star_Rating'].append(star_ratings[i].text if i < len(star_ratings) else '0')
                all_data['Price'].append(prices[i].text.replace("INR", "").strip() if i < len(prices) else '0')
                all_data['Seats_available'].append(seats[i].text.replace("Seats available", "").strip() if i < len(seats) else '0')

        except Exception as e:
            print(f"Error scraping buses for route {row['Route_Name']}: {e}")
            continue

    driver.quit()
    return pd.DataFrame(all_data)

# === STEP 5: Run scraping for each RTC file ===
final_df = pd.DataFrame()

for rtc in rtc_list.keys():
    rtc_file = f"{base_path}/df_{rtc.lower().replace(' ', '')}.csv"
    if os.path.exists(rtc_file):
        print(f"Scraping bus details for {rtc}...")
        df_routes = pd.read_csv(rtc_file)
        df_buses = scrape_bus_details(df_routes)
        final_df = pd.concat([final_df, df_buses], ignore_index=True)

# === STEP 6: Data Cleaning ===
final_df['Bus_Name'] = final_df['Bus_Name'].fillna('Not Available')
final_df['Bus_Type'] = final_df['Bus_Type'].fillna('Not Available')
final_df['Departing_Time'] = pd.to_datetime(final_df['Departing_Time'], format='%H:%M', errors='coerce').dt.time.fillna(pd.to_datetime('00:00', format='%H:%M').time())
final_df['Reaching_Time'] = pd.to_datetime(final_df['Reaching_Time'], format='%H:%M', errors='coerce').dt.time.fillna(pd.to_datetime('00:00', format='%H:%M').time())
final_df['Star_Rating'] = final_df['Star_Rating'].astype(str).str.replace("New", "").str.extract(r'(\d+\.?\d*)')[0].astype(float).fillna(0)
final_df['Price'] = pd.to_numeric(final_df['Price'], errors='coerce').fillna(0)
final_df['Seats_available'] = pd.to_numeric(final_df['Seats_available'], errors='coerce').fillna(0).astype(int)

final_df = final_df.replace({np.nan: None})
final_df.to_csv(f"{base_path}/final_busdetails.csv", index=False)
print("✅ All RedBus data scraped and saved successfully.")
