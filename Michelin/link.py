import requests
from bs4 import BeautifulSoup

# Specify the number of pages to scrape
num_pages = 8

# Create an empty set to store unique links
unique_links = set()

# Scrape links from each page
for page in range(1, num_pages+1):
    # Send a GET request to the website
    url = f"https://guide.michelin.com/vn/en/restaurants/page/{page}?q=vietnam"
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <a> elements with href attribute
    link_elements = soup.find_all("a", href=True)

    # Extract the href attribute values from the <a> elements
    links = [link["href"] for link in link_elements if "/vn/en/ho-chi-minh/" in link["href"] or "/vn/en/hanoi/" in link["href"]]

    # Add the links to the set to remove duplicates
    unique_links.update(links)

# Save the links into a text file
with open(f"scraped_links.txt", "w") as file:
    for link in unique_links:
        file.write(link + "\n")

print("Scraping complete. Links saved to scraped_links.txt file.")
