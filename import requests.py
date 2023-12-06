import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = []

        for quote in soup.find_all('span', class_='text'):
            text = quote.get_text()
            author = quote.find_next('small', class_='author').get_text()
            quotes.append({'text': text, 'author': author})

        return quotes
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Example usage:
url = "http://quotes.toscrape.com"
quotes = scrape_quotes(url)

if quotes:
    for idx, quote in enumerate(quotes, start=1):
        print(f"{idx}. '{quote['text']}' - {quote['author']}")
