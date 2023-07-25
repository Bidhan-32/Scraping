import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the Firefox driver
driver = webdriver.Firefox()

# Set the URL
url = 'https://beachsearcher.com/en/search?object=region&object_id=82&pagesize=18&offset=0&smart=0'

# Navigate to the initial URL
driver.get(url)

# Initialize an empty list to store the beach names
beach_names = []

while True:
    # Find the beach names on the current page
    beaches = driver.find_elements(
        By.XPATH,
        './/span[@class="card__obj__desc__title-name"]/a[@class="card__obj__desc__title-link"]'
    )
    beach_names.extend(beach.get_attribute('textContent') for beach in beaches)

    # Check if "Next" button exists
    next_button = driver.find_element(
        By.XPATH,
        '//button[@class="section__pagination-btn pagination__next"]'
    )
    if 'visibility: visible' not in next_button.get_attribute('style'):
        break  # Exit the loop if the "Next" button is not visible

    # Scroll the "Next" button into view
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    driver.execute_script("window.scrollBy(0, -100);")

    # Click the "Next" button
    driver.execute_script("arguments[0].click();", next_button)

    # Wait for 5 seconds
    time.sleep(5)

# Close the Firefox driver
driver.quit()

# Print the beach names
for beach_name in beach_names:
    print(beach_name)
