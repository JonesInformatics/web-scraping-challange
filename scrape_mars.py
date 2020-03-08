# <!-- * Start by converting your Jupyter notebook into a Python script called 
# `scrape_mars.py` with a function called `scrape` that will execute all of your 
# scraping code from above and return one Python dictionary containing all of the 
# scraped data. -->

# import nessacry packages

from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

import time
import pandas as pd
# create a function called scrape

def scrape(): 
    '''this is my function to access scrape data'''

    # scrape title of news
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # hemisphere 
    hemisphere_url = []
    url_image = "https://astrogeology.usgs.gov"

    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    cerberus_html = browser.html
    cerberusSoup = bs(cerberus_html, "html.parser")

    cerberus_pic = cerberusSoup.find('img', class_="wide-image")
    hemisphere_url.append({"title":"Cerberus Hemisphere", "URL": url_image + cerberus_pic['src']})

    schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelli)
    schiaparelli_html = browser.html
    schiaparelliSoup = bs(schiaparelli_html, 'html.parser')

    schiaparelli_pic = schiaparelliSoup.find('img', class_="wide-image")
    schiaparelli_pic['src']

    hemisphere_url.append({"title": "Schiaparelli Hemisphere", "URL": url_image + schiaparelli_pic['src']})
    
    syrtismajor = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtismajor)
    syrtismajor_html = browser.html
    syrtismajorSoup = bs(syrtismajor_html, 'html.parser')

    syrtismajor_pic = syrtismajorSoup.find('img', class_="wide-image")
    hemisphere_url.append({"title": "Syrtis Major Hemisphere", "URL": url_image + syrtismajor_pic['src']})
    
    vallesmarineris = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(vallesmarineris)
    vallesmarineris_html = browser.html
    vallesmarinerisSoup = bs(vallesmarineris_html, 'html.parser')

    vallesmarineris_pic = vallesmarinerisSoup.find('img', class_="wide-image")
    hemisphere_url.append({"title": "Valles Marineris Hemisphere", "URL": url_image +vallesmarineris_pic['src']})
    
    # scrape news data
    
    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+\
        desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    response = requests.get(news_url)
    soup= bs(response.text, 'html.parser')

    title=soup.find('div', class_="content_title").find('a').text.strip()

    #return title

    # scrape featurerd image

    # space_pic_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # browser.visit(space_pic_url)

    # browser.click_link_by_partial_text('FULL IMAGE')

    # image_html =browser.html

    # image_soup = bs(image_html, 'html.parser')

    # fetured_img_rel=image_soup.select_one(".carousel_item").get('style')
    # fetured_img_rel=fetured_img_rel.split("\'")[1]

    # fetured_img=f'https://www.jpl.nasa.gov{fetured_img_rel}'

    # scrape paragraph summary

    paragraph=soup.find('div', class_="rollover_description_inner").text.strip()

    #scrape twiiter feed

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    weather_stuff = requests.get(weather_url)
    twitter_soup = bs(weather_stuff.text, 'html.parser')
    mars_tweets = twitter_soup.find_all('div', class_='js-tweet-text-container')
    for tweet in mars_tweets:
        mars_weather = tweet.find('p').text
        if 'InSight' and 'sol' in mars_weather:
            mars_weather=mars_weather
        break
    else:
        pass


    # scrape mars facts
    facts_url = "https://space-facts.com/mars/"

    mars_facts = pd.DataFrame(pd.read_html(facts_url)[0])

    mars_facts.columns = ['Description','Value']

    mars_facts.set_index('Description', inplace=True)

    table_html =  mars_facts.to_html()

    #featurerd image
    space_pic_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(space_pic_url)

    browser.click_link_by_partial_text('FULL IMAGE')

    image_html =browser.html

    image_soup = bs(image_html, 'html.parser')
    # image_soup.select_one(".fancybox-image").get('src')
    fetured_img_rel=image_soup.select_one(".carousel_item").get('style')
    fetured_img_rel=fetured_img_rel.split("\'")[1]

    fetured_img=f'https://www.jpl.nasa.gov{fetured_img_rel}'


    mars_dict = {"hemisphere_url": hemisphere_url,"title": title, "paragraph":paragraph,"mars_weather":mars_weather,"table_html": table_html,"fetured_img":fetured_img}

    # Close the browser after scraping
    browser.quit()


   


    return mars_dict
    
    
    
    

# def scrape2(): 
#         '''this is my function to access scrape paragraph data'''
    
#     # scrape title of news
#         executable_path = {'executable_path': 'chromedriver.exe'}
#         browser = Browser('chrome', **executable_path, headless=False)
    
#         news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+\
#         desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

#         response = requests.get(news_url)
#         soup= bs(response.text, 'html.parser')

#     # scrape paragraph summary

#         paragraph=soup.find('div', class_="rollover_description_inner").text.strip()

    
    
#         return paragraph



    
