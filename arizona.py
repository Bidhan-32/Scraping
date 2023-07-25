import requests
from bs4 import BeautifulSoup
import re

def scrape_emails(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all email addresses using regular expressions
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, soup.get_text())

    # Remove duplicates from the list of emails
    unique_emails = list(set(emails))

    # Print the scraped email addresses
    for email in unique_emails:
        print(email)

# Example usage: Scrape emails from the faculty directory webpage
url = 'https://www.ecs.baylor.edu/faculty-directory'
scrape_emails(url)
