from playwright.sync_api import sync_playwright
import pandas as pd
import time

def main():

    with sync_playwright() as p:

        checkin_date = '2024-06-12'
        checkout_date = '2024-06-14'
        page_url = f'https://www.booking.com/searchresults.en-gb.html?ss=Goa%2C+India&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AqWFm7MGwAIB0gIkOTFhNDYwNWItOTFmZC00MjNlLTgwYWMtNTNiMWFhMmZjMDhh2AIF4AIB&sid=874c0b6171c3c3a376239bf3dc46e4c4&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=4127&dest_type=region&checkin={checkin_date}&checkout={checkout_date}&group_adults=2&no_rooms=1&group_children=0'

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(page_url, timeout=60000)

        # time.sleep(100)
        def scroll_page():
            # Scroll down to the bottom of the page
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)  # Wait for a while after scrolling

        # Scroll for a certain number of times or until the end of the page
        scroll_count = 3  # Change this value according to your requirement
        for _ in range(scroll_count):
            scroll_page()
            print('========= scrolled ==============')

            time.sleep(20)
        
        try:
            click_count = 10
            for _ in range(click_count):
                load_more_button = page.locator('//span[contains(text(), "Load more results")]')
                if load_more_button.is_visible():
                    load_more_button.click()
                    print('========= button clicked ==============')
                    time.sleep(10)
        except Exception as e:
            print(e)


        hotels = page.locator('//div[@data-testid="property-card"]').all()
        print(f'There are : {len(hotels)} hotels.')

        hotels_list = []

        for hotel in hotels:
            hotel_dict = {}
            hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            # hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
            hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text()

            hotels_list.append(hotel_dict)
        
        df = pd.DataFrame(hotels_list)
        print(df)
        print(df.to_csv('data.csv'))

        # browser.close()

if __name__ == '__main__':
    main()