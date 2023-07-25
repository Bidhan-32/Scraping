from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Set the URL
url = 'https://beachnearby.com/'

# Launch the web driver
driver = webdriver.Firefox()
driver.get(url)

# Wait for the page to load (optional)
driver.implicitly_wait(5)  # Wait for 5 seconds

try:
    # Find the beach name elements
    beach_name_elements = driver.find_elements(By.XPATH, './/div[@class="jsx-1784889251"]/a/p[@class="jsx-1784889251 beachName"]')

    # Extract and print beach names
    with open("beachnearby.csv", "w", encoding="utf-8") as file:
        for beach_name_element in beach_name_elements:
            beach_name = beach_name_element.text.strip()
            print(beach_name)
            file.write(beach_name + "\n")
except NoSuchElementException:
    print("Beach names not found")

# Close the web driver
driver.quit()
