
def scrape():


    from splinter import Browser
    from bs4 import BeautifulSoup
    import pandas as pd


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA Mars News

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)



    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text

    news_p = soup.find('div', class_='article_teaser_body').text

    # JPL Mars Space Images - Featured Image

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    section = soup.find('section',class_='main_feature')
    section_foot = section.find('footer')
    img = section_foot.find('a')['data-fancybox-href']

    featured_image_url = f'https://www.jpl.nasa.gov{img}'

    # Mars Weather

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)



    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    section = soup.find('div', class_='js-tweet-text-container')
    text = [text for text in section.find('p')]
    text[0] = text[0].replace('\n', '')
    mars_weather = text[0]

    # Mars Facts

    url = 'https://space-facts.com/mars/'

    table = pd.read_html(url)




    df = table[0]
    df.columns = ['Description', 'Value']
    df.set_index('Description', inplace=True)




    mars_html_table = df.to_html()



    mars_html_table = mars_html_table.replace('\n', '')


    # # Mars Hemispheres


    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]

    # all info dictionary

    mars_info_dict = {'news_title': news_title,
                    'news_p': news_p,
                    'featured_image_url': featured_image_url,
                    'mars_weather': mars_weather,
                    'mars_facts': mars_html_table,
                    'hemisphere_image_urls': hemisphere_image_urls
                    }
    return mars_info_dict

