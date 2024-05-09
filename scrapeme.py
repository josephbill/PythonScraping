import requests
from bs4 import BeautifulSoup

# URL setup for a search term
search_term = "soccer boots"
url = f'https://www.amazon.com/s?k={search_term}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

# fetching url content 
response = requests.get(url, headers=headers)

# Initialize BeautifulSoup 
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product cards. The class name might change, so verify it first
product_cards = soup.find_all('div', {'data-component-type': 's-search-result'})

products = []

for card in product_cards:
    # Extracting image source
    image = card.find('img', {'class': 's-image'})
    img_src = image['src'] if image else "No Image Found"

    # Extracting product name
    title = card.find('span')
    product_name = title.text if title else "No Title Found"

    # Extracting price
    price = card.find('span', {'class': 'a-price-whole'})
    product_price = price.text if price else "No Price Found"

    # Appending each product's details to the products list
    products.append({
        'image_src': img_src,
        'product_name': product_name,
        'product_price': product_price
    })

# Print all products details
for product in products:
    print(product)
