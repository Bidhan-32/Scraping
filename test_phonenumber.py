from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Print the initial contents of the website
with open("phone.csv", "w") as file:
    for company_listing in company_listings:
        try:
            phone_element = company_listing.find_element(By.XPATH, './/span[@itemprop="telephone"]')
            phone_number = phone_element.text if phone_element.text else "123456789"
            print(phone_number)
            file.write(phone_number + "\n")
        except NoSuchElementException:
            print("NULL")
            file.write("0\n")

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
                phone_element = new_element.find_element(By.XPATH, './/span[@itemprop="telephone"]')
                phone_number = phone_element.text if phone_element.text else "123456789"
                print(phone_number)
                file.write(phone_number + "\n")
            except NoSuchElementException:
                print("NULL")
                file.write("0\n")

        company_listings = new_elements  # Update the company listings

        # Scroll down the page to load more elements
        scroll_element.send_keys(Keys.END)

# Close the web driver
driver.quit()
