from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import mysql.connector
from db_config import get_connection

def insert_data_to_db(data):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO rd_bus_routes (
        route_name, route_link, busname, bustype, departing_time,
        duration, reaching_time, star_rating, price, seats_available
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(query, data)
    conn.commit()
    cursor.close()
    conn.close()

def scrape_redbus_data():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)

    driver.get("https://www.redbus.in/")    
    sleep(3)

    # Sample route
    from_city = "Chennai"
    to_city = "Bangalore"
    date = "08-Aug-2025"

    # Fill in FROM, TO and DATE fields
    driver.find_element(By.ID, "src").send_keys(from_city)
    sleep(1)
    driver.find_element(By.ID, "dest").send_keys(to_city)
    sleep(1)
    driver.find_element(By.CLASS_NAME, "dateText").click()
    sleep(1)
    driver.find_element(By.XPATH, f"//span[text()='8']").click()
    sleep(2)
    driver.find_element(By.ID, "search_button").click()
    sleep(5)

    buses = driver.find_elements(By.XPATH, '//div[@class="travels lh-24 f-bold d-color"]')

    data = []
    for i in range(len(buses)):
        try:
            busname = buses[i].text
            bustype = driver.find_elements(By.XPATH, '//div[@class="bus-type f-12 m-top-16 l-color"]')[i].text
            departing_time = driver.find_elements(By.XPATH, '//div[@class="dp-time f-19 d-color f-bold"]')[i].text
            duration = driver.find_elements(By.XPATH, '//div[@class="dur l-color f-12"]')[i].text
            reaching_time = driver.find_elements(By.XPATH, '//div[@class="bp-time f-19 d-color disp-Inline"]')[i].text
            star_rating = float(driver.find_elements(By.XPATH, '//div[@class="rating-sec lh-24"]//span')[i].text)
            price = float(driver.find_elements(By.XPATH, '//div[@class="seat-fare  "]//span')[i].text.replace("₹", "").strip())
            seats = int(driver.find_elements(By.XPATH, '//div[@class="seat-left m-top-16"]')[i].text.split(" ")[0])
            
            data.append((
                f"{from_city} → {to_city}",
                driver.current_url,
                busname,
                bustype,
                departing_time,
                duration,
                reaching_time,
                star_rating,
                price,
                seats
            ))
        except Exception as e:
            print(f"Error for bus {i}: {e}")
            continue

    driver.quit()
    insert_data_to_db(data)
    print("Data inserted into MySQL")

if __name__ == "__main__":
    scrape_redbus_data()
