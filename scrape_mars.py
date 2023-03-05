# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_all():




    scrape_data={
        "news_title": news_title,
        "news_paragraph":news_p,
    }

    return scrape_data
if __name__== "__main__":
    print(scrape_all())