from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os

def scrape_redbus_data(from_city='Chennai', to_city='Bangalore', date='16-Jul-2025'):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    url = 'https://www.redbus.in/'
    driver.get(url)
    time.sleep(2)

    driver.find_element(By.ID, "src").send_keys(from_city)
    time.sleep(1)
    driver.find_element(By.XPATH, f"//li[text()='{from_city}']").click()

    driver.find_element(By.ID, "dest").send_keys(to_city)
    time.sleep(1)
    driver.find_element(By.XPATH, f"//li[text()='{to_city}']").click()

    driver.find_element(By.ID, "onward_cal").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"//td[text()='{int(date.split('-')[0])}']").click()

    driver.find_element(By.ID, "search_btn").click()
    time.sleep(5)

    buses = driver.find_elements(By.XPATH, '//div[@class="travels lh-24 f-bold d-color"]')
    prices = driver.find_elements(By.XPATH, '//div[@class="fare d-block"]')
    timings = driver.find_elements(By.XPATH, '//div[@class="dp-time f-19 d-color f-bold"]')

    bus_names, ticket_prices, departure_times = [], [], []

    for i in range(min(len(buses), len(prices), len(timings))):
        bus_names.append(buses[i].text.strip())
        ticket_prices.append(prices[i].text.strip().replace('₹', ''))
        departure_times.append(timings[i].text.strip())

    driver.quit()

    df = pd.DataFrame({
        'Bus Operator': bus_names,
        'Price': ticket_prices,
        'Departure Time': departure_times,
        'From': from_city,
        'To': to_city,
        'Date': date
    })

    output_dir = r'E:\Naveen\Scrap data'
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'redbus_data.csv'), index=False)
    return df
