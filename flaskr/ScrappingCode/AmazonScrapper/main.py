import csv
from unittest import result
from bs4 import BeautifulSoup
from selenium import webdriver


#Getting the next page
def get_url(search_term):
    """Generate a url from search term"""
    template = "https://www.amazon.com/s?k={}&crid=17EQSZ8NCHJ78&sprefix=u%2Caps%2C108&ref=nb_sb_ss_pltr-ranker-20mins_1_1"
    search_term = search_term.replace(' ', '+')
    # add term query to url
    url = template.format(search_term)

    # add page query placeholder
    url += '&page()'
 
    return url

def extract_record(item):
    """Extract and return data from a single record"""
    # description and url
    atag = item.h2.a
    description = atag.text.strip() 
    url = 'https://www.amazon.com' + atag.get('href')
    try: 
        # price
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return
    try:
        # rank and rating
        rating = item.i.text
        review_count = item.find('span', {'class': 'a-size-base', 'dir' : 'auto' }).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (description, price, rating, review_count, url)

    return result

def main(search_term):
    """Run main program"""
    # startup the webdriver
    #using microsoft edge
    driver = webdriver.Edge(r'C:\Users\Guillermo\Documents\GitHub\test\NewRepo\flaskr\ScrappingCode\AmazonScrapper\msedgedriver.exe')

    record = []
    records = []
    url = get_url(search_term)

    for page in range (1, 21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)

    driver.close()

   


    # save data to csv file
    #with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    #    writer = csv.writer(f)
     #   writer.writerow(['Description', 'Price', 'Rating', 'ReviewCount', 'Url'])
    #    writer.writerows(records)


main('ultrawide monitor')