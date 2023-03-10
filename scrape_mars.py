# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser()
     # Setting up windows browser with chromedriver 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


#NASA Mars News

def scrape_all():


 #URL to be scraped
    url= "https://redplanetscience.com/"
browser.visit(url)
html= browser.html
newssoup= soup(html,"html.parser")
newsobject= newssoup.select_one("div.list_text")
newsobject





scrape_data={
        "news_title": news_title,
        news_title= newsobject.find("div",class_="content_title").get_text()
        news_title
        "news_paragraph":news_p,
news_p= newsobject.find("div",class_="article_teaser_body").get_text()
news_p

    }


#Mars Space Image

url= "https://spaceimages-mars.com"
browser.visit(url)
images_button= browser.find_by_tag("button")[1]
images_button.click()
html= browser.html
soupimage= soup(html,"html.parser")
soupimage


shortimgurl= soupimage.find("img",class_="fancybox-image").get("src")
shortimgurl


featured_image_url= url+"/"+ shortimgurl
featured_image_url





#Mars Facts
df= pd.read_html("https://galaxyfacts-mars.com")[0]
df.head()

#Naming columns
#df.columns= ["Description","Mars","Earth"]
#df.set_index("Description",inplace=True)
df.head()

  #Use to_html method to generate HTML tables from df
df.to_html()





#Mars Hemispheres
url= "https://marshemispheres.com/"
browser.visit(url)

hemisphere_image_urls =[]
list= browser.find_by_css("a.product-item img")

for link in range(len(list)):
    hemidict={}
    browser.find_by_css("a.product-item img")[link].click()

    sampleobject= browser.find_by_text("Sample").first
    hemidict["img_url"]=sampleobject["href"]

    hemidict["title"]= browser.find_by_css("h2.title").text
    
# Creating final list of dictionaries
    hemisphere_image_urls.append(hemidict)
    browser.back()
hemisphere_image_urls



    return scrape_data
if __name__== "__main__":
    print(scrape_all())