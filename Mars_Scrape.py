import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

import pandas as pd


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)


def scrape():
    url = 'https://mars.nasa.gov/news'
    response = requests.get(url)

    soup = bs(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print(paragraph.text)

    results = soup.find_all('div', class_="content_title")

    browser.visit(url)
    browser.is_element_present_by_css("div.content_title a", wait_time=10)
    soup = browser.html

    title = browser.find_by_css("div.content_title a").first

    browser.visit(url)
    browser.is_element_present_by_css("div.article_teaser_body", wait_time=10)
    soup = browser.html

    article_teaser = browser.find_by_css("div.article_teaser_body").first

    browser.visit(url)
    browser.is_element_present_by_css("div.content_title", wait_time=10)
    soup = browser.html

    title = browser.find_by_css("div.content_title")

    from splinter import Browser
    from bs4 import BeautifulSoup
    import os
    import requests

    browser.visit(
        'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

    # Iterate through all pages#
    for x in range(50):
        # HTML object#
        html = browser.html
        # Parse HTML with Beautiful Soup#
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book# information
        articles = soup.find_all('article', class_='carousel_item')

        # Iterate through each book#
        for article in articles:
            # Use Beautiful Soup's find() method to navigate and retrieve attributes#

            print('-----------')
            print(article)
            print('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

        # Click the 'Next' button on each page#
        try:
            browser.click_link_by_partial_text('next')

        except:
            print("Scraping Complete")

        featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars.jpg'
        featured_image_url2 = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA00046_hires.jpg'

        twitter_url = 'https://twitter.com/marswxreport?lang=en'

        response = requests.get(twitter_url)

        soup = bs(response.text, 'html.parser')

        mars_weather = soup.find_all('p', class_="tweet-text")

        mars_weather[1].get_text("InSight sol")

        Cerberus_img_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
        Cerberus_title = "Cerberus Hemisphere"

        Cerberus_Dict = {
            "title":  "Cerberus Hemisphere", "img_url": 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
        }

        Schiaparelli_Dict = {"title": "Shiaparelli Hemisphere",
                             "img_url": 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'}
        Syrtis_Major_Dict = {"title": "Syrtis Major Hemisphere",
                             "img_url": 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'}
        Valles_Marineris_Dict = {"title": "Valles Marineris Hemisphere",
                                 "img_url": 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'}

        Hemisphere_List = []
        Hemisphere_List.append(Cerberus_Dict)
        Hemisphere_List.append(Schiaparelli_Dict)
        Hemisphere_List.append(Syrtis_Major_Dict)
        Hemisphere_List.append(Valles_Marineris_Dict)

        facts_url = 'http://space-facts.com/mars/'

        # Use Panda's `read_html` to parse the url
        mars_facts = pd.read_html(facts_url)

        mars_df = mars_facts[0]

        return mars_df
