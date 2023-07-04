import requests
from bs4 import BeautifulSoup

with open("scraped_links.txt", "r") as file:
    links = file.readlines()

for link in links:
# Send a GET request to the website
    url = link.strip()
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the desired elements and extract their content
    restaurant_title = soup.find("h1", class_="restaurant-details__heading--title").text.strip()
    restaurant_address = soup.find("li", class_="restaurant-details__heading--address").text.strip()

    classfication_contents = soup.find_all(class_="classfication-content")
    content_list = [
        content.get_text(strip=True)
        for content in classfication_contents
        if content.find("span", class_="distinction-icon") is None
    ]

    restaurant_description = soup.find("div", class_="restaurant-details__description--text").text.strip()
    services_list = soup.find("ul", class_="row restaurant-details__services--list").text.strip()

    # Create a text file and write the scraped content
    with open("scraped_content.txt", "a", encoding="utf-8") as file:
        file.write(restaurant_title + "\n")
        file.write(restaurant_address + "\n")
        for content in content_list:
            file.write(content + "\n")
        file.write(restaurant_description + "\n")
        file.write(services_list + "\n\n")

print("Scraping complete. Content saved to 'scraped_content.txt' file.")
