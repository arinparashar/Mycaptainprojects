import argparse
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
   
    response = requests.get(url)
    
      soup = BeautifulSoup(response.text, 'html.parser')
    
       links = soup.find_all('a')
    for link in links:
        print(link.get_text())

if __name__ == '__main__':
   
    parser = argparse.ArgumentParser(description='Web Scraping Script')
    parser.add_argument('url', help='URL of the website to scrape')
    
      args = parser.parse_args()
      scrape_website(args.url)
