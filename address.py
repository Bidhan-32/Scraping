from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from selenium.common.exceptions import NoSuchElementException


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

# Open the file in write mode
with open("addresses.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["street_address",  "postal_code"])  # Write header row

    # Print the initial contents of the website
    for company_listing in company_listings:
        try:
            # Find the address elements within the company listing
            address_element = company_listing.find_element(By.XPATH, './/div[@itemprop="address"]')
            street_address = address_element.find_element(By.XPATH, './/p[@itemprop="streetAddress"]').text
            locality = address_element.find_element(By.XPATH, './/span[@itemprop="addressLocality"]')
            region_element = address_element.find_element(By.XPATH, './/span[@itemprop="addressRegion"]')
            postal_code = address_element.text.split("\n")[-1]

            # Combine the address components
            address = f"{street_address}, {postal_code}"
            print(address)

            # Write address to CSV file
            writer.writerow([street_address, postal_code])

        except NoSuchElementException:
            print("Address not found")

    # Scroll down the page to load more elements
    scroll_element = driver.find_element(By.TAG_NAME, 'body')
    scroll_element.send_keys(Keys.END)

    while True:
        # Wait for new elements to load
        wait = WebDriverWait(driver, 10)
        new_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'company-listing')))

        # Print the newly added elements
        for new_element in new_elements[len(company_listings):]:
            try:
                # Find the address elements within the new element
                address_element = new_element.find_element(By.XPATH, './/div[@itemprop="address"]')
                street_address = address_element.find_element(By.XPATH, './/p[@itemprop="streetAddress"]').text
                locality = address_element.find_element(By.XPATH, './/span[@itemprop="addressLocality"]')
                region_element = address_element.find_element(By.XPATH, './/span[@itemprop="addressRegion"]')
                postal_code = address_element.text.split("\n")[-1]

                # Combine the address components
                address = f"{street_address}, {postal_code}"
                print(address)

                # Write address to CSV file
                writer.writerow([street_address, postal_code])

            except NoSuchElementException:
                print("Address not found")

        company_listings = new_elements  # Update the company listings

        # Scroll down the page to load more elements
        scroll_element.send_keys(Keys.END)

# Close the web driver
driver.quit()
