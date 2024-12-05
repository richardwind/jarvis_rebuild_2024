import requests
from bs4 import BeautifulSoup
from modules.logs import logger
import csv

def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        logger.error(f"Failed to fetch the webpage content. Error: {e}")
        return None

def extract_links(soup):
    return [a['href'] for a in soup.find_all('a', href=True)]

def extract_images(soup):
    return [img['src'] for img in soup.find_all('img', src=True)]

def extract_text_content(soup, tag, class_name=None):
    elements = soup.find_all(tag, class_=class_name)
    return [element.text for element in elements]

def handle_pagination(soup, base_url):
    next_page = soup.find('a', text='Next')  # Adjust based on the website's structure
    if next_page and 'href' in next_page.attrs:
        return base_url + next_page['href']
    return None

def store_data_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow([row])

# Example usage:
if __name__ == "__main__":
    url = "https://example.com"
    soup = fetch_webpage_content(url)
    
    if soup:
        links = extract_links(soup)
        images = extract_images(soup)
        texts = extract_text_content(soup, "p")  # Extracting paragraph content
        
        store_data_to_csv(links, "links.csv")
        store_data_to_csv(images, "images.csv")
        store_data_to_csv(texts, "texts.csv")
        
        next_page_url = handle_pagination(soup, url)
        if next_page_url:
            print(f"Next page URL: {next_page_url}")
