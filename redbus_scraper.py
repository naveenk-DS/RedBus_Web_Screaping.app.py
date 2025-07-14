# redbus_scraper.py
import pandas as pd
import os

def scrape_redbus_data(from_city='Chennai', to_city='Bangalore', date='16-Jul-2025'):
    # Mock data (simulate scraped data)
    data = {
        'Bus Operator': ['KPN Travels', 'SRS Travels', 'Parveen Travels'],
        'Price': [750, 850, 950],
        'Departure Time': ['6:00 PM', '9:00 PM', '11:30 PM'],
        'From': [from_city] * 3,
        'To': [to_city] * 3,
        'Date': [date] * 3
    }

    df = pd.DataFrame(data)
    output_dir = r"E:\Naveen\Scrap data"
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'redbus_data.csv'), index=False)
    return df
