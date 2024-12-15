from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import csv
import os
import time

# URL of the page to scrape
URL = 'https://www.tesc.farm/produce.html'

# Setup Selenium WebDriver
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Run in headless mode (without GUI)
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# Load the webpage
driver.get(URL)

# Wait for the dynamic content to load
time.sleep(3)  # Adjust sleep time as necessary, or use WebDriverWait for better control

# Find the items and prices on the page
items = driver.find_elements(By.CSS_SELECTOR, 'main#main-content div.product-grid div.product-card div.product-details h3.product-name')
prices = driver.find_elements(By.CSS_SELECTOR, 'main#main-content div.product-grid div.product-card div.product-card-checkout p.price')

# Debugging: Print the number of items and prices found
print(f"Number of items found: {len(items)}")
print(f"Number of prices found: {len(prices)}")

# Prepare data for CSV
data = []
for item, price in zip(items, prices):
    item_name = item.text.strip()
    item_price = price.text.strip()
    print(f"Item: {item_name}, Price: {item_price}")  # Debugging: Print each item and price
    data.append([item_name, item_price])

# CSV file name
csv_file = 'veggie_scrape.csv'

# Check if the file already exists
file_exists = os.path.isfile(csv_file)

# Write data to CSV
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        # Write header if the file is newly created
        writer.writerow(['item name', 'price'])
    writer.writerows(data)

print(f"Data has been appended to {csv_file}")

# Quit the driver
driver.quit()
