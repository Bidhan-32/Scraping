import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set the URL
url = 'https://beachsearcher.com/en/search?object=region&object_id=82&pagesize=18&offset=0&smart=0'

# Launch the Firefox driver
driver = webdriver.Firefox()
driver.get(url)

# Wait for the content to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, './/span[@class="card__obj__desc__title-name"]/a[@class="card__obj__desc__title-link"]')))

# Initialize an empty list to store the beach names
beach_names = []

while True:
    # Find the beach names
    beaches = driver.find_elements(By.XPATH, './/span[@class="card__obj__desc__title-name"]/a[@class="card__obj__desc__title-link"]')

    # Extract the beach names for the current page
    beach_names.extend(beach.text for beach in beaches)

    # Save the beach names in a CSV file for each page
    data = {'Beach Name': beach_names}
    df = pd.DataFrame(data)
    df.to_csv('Aegean.csv', index=False, mode='a', header=False)

    # Check if "Next" button exists
    next_button = driver.find_element(By.XPATH, '//button[@class="section__pagination-btn pagination__next"]')
    if 'visibility: visible' not in next_button.get_attribute('style'):
        break  # Exit the loop if the "Next" button is not visible

    # Scroll the "Next" button into view
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    driver.execute_script("window.scrollBy(0, -100);")

    # Click the "Next" button
    driver.execute_script("arguments[0].click();", next_button)

    # Wait for 5 seconds
    time.sleep(1)

    # Clear the beach_names list to store the beach names for the next page
    beach_names.clear()

# Close the Firefox driver
driver.quit()
