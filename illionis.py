from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Set the URL and XPATH
url = 'https://scai.engineering.asu.edu/computer-science-and-engineering-faculty/'

# Launch the web driver
driver = webdriver.Firefox()
driver.get(url)

# Wait for the page to load (optional)
# You can use WebDriverWait for more precise waiting
driver.implicitly_wait(5)  # Wait for 5 seconds

# Find the initial faculty listings
faculty_listings = driver.find_elements(By.CLASS_NAME, 'directory table table-bordered table-striped table-condensed')

# Print the initial contents of the website
with open("purdue.csv", "w") as file:
    for faculty_listing in faculty_listings:
        try:
            email_element = faculty_listing.find_element(By.XPATH, './/div[@class="et_pb_text_inner"]/a[starts-with(@href, "mailto:")]')
            email_address = email_element.get_attribute("href").split(":")[1]
            print(email_address)
            file.write(email_address + "\n")
        except NoSuchElementException:
            print("NULL")
            file.write("0\n")

    # Scroll down the page to load more elements
    scroll_element = driver.find_element(By.TAG_NAME, 'body')
    scroll_element.send_keys(Keys.END)

    while True:
        # Wait for new elements to load
        wait = WebDriverWait(driver, 10)
        new_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'post-content')))

        # Print the newly added elements
        for new_element in new_elements[len(faculty_listings):]:
            try:
                email_element = new_element.find_element(By.XPATH, './/div[@class="et_pb_text_inner"]/a[starts-with(@href, "mailto:")]')
                email_address = email_element.get_attribute("href").split(":")[1]
                print(email_address)
                file.write(email_address + "\n")
            except NoSuchElementException:
                print("NULL")
                file.write("0\n")

        faculty_listings = new_elements  # Update the faculty listings

        # Scroll down the page to load more elements
        scroll_element.send_keys(Keys.END)

# Close the web driver
driver.quit()
