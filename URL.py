from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the URL and XPATH
url = 'https://www.brewersassociation.org/directories/breweries/'

# Launch the web driver
driver = webdriver.Firefox()
driver.get(url)

# Wait for the page to load (optional)
# You can use WebDriverWait for more precise waiting
driver.implicitly_wait(5)  # Wait for 5 seconds

# Find the initial company listings
company_listings = driver.find_elements(By.CLASS_NAME, 'company-listing')

# Extract the phone numbers
phone_numbers = []

for company_listing in company_listings:
    phone_element = company_listing.find_element(By.XPATH, './/span[@itemprop="telephone"]')
    phone_number = phone_element.text
    phone_numbers.append(phone_number)

# Scroll down the page to load more elements
scroll_element = driver.find_element(By.TAG_NAME, 'body')
scroll_element.send_keys(Keys.END)

while True:
    # Wait for new elements to load
    wait = WebDriverWait(driver, 10)
    new_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'company-listing')))

    # Extract the phone numbers from the newly added elements
    for new_element in new_elements[len(company_listings):]:
        phone_element = new_element.find_element(By.XPATH, './/span[@itemprop="telephone"]')
        phone_number = phone_element.text
        phone_numbers.append(phone_number)

    company_listings = new_elements  # Update the company listings

    # Scroll down the page to load more elements
    scroll_element.send_keys(Keys.END)

    # Check if there are any new elements
    if len(new_elements) == len(company_listings):
        break  # No new elements, exit the loop

# Close the web driver
driver.quit()

# Print the extracted phone numbers
for phone_number in phone_numbers:
    print(phone_number)
