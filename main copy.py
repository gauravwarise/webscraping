import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.booking.com/searchresults.en-gb.html?ss=Goa%2C+India&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AqWFm7MGwAIB0gIkOTFhNDYwNWItOTFmZC00MjNlLTgwYWMtNTNiMWFhMmZjMDhh2AIF4AIB&sid=874c0b6171c3c3a376239bf3dc46e4c4&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=4127&dest_type=region&checkin=2024-06-10&checkout=2024-06-11&group_adults=2&no_rooms=1&group_children=0'

r = requests.get(url)
html_content = r.content

soup = BeautifulSoup(html_content, 'lxml')

soup.prettify()

# print(soup)


# Example: Extracting hotel names
hotel_names = []
for hotel in soup.find_all('div', class_='f6431b446c a15b38c233', attrs={"data-testid": "title"}):
    hotel_names.append(hotel.text.strip())

# # Example: Extracting prices
prices = []
# for price in soup.find_all('span', attrs={"id": "req_info"}):
for price in soup.find_all('div', attrs={"data-testid": "taxes-and-charges"}):
    print(price)
#     prices.append(price.text.strip())
# print(prices)

# # Example: Extracting ratings
# ratings = []
# for rating in soup.find_all('div', class_='bui-review-score__badge'):
#     ratings.append(rating.text.strip())

# Create pandas DataFrame
# data = {'Hotel Name': hotel_names, 'Price': prices, 'Rating': ratings} class="f6431b446c a15b38c233"

data = {'Hotel Name': hotel_names}
df = pd.DataFrame(data)

# print(df)