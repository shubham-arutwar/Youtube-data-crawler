import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

url = "https://www.youtube.com/watch?v=hByfAzEoeKA"
class1 = "style-scope ytd-transcript-segment-list-renderer"

client = MongoClient("mongodb+srv://cyanZEUS:cyanZEUS@cluster0.w4dydp9.mongodb.net/?retryWrites=true&w=majority")

def main():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    more_options_btn = driver.find_element("xpath", '//ytd-menu-renderer[@class="style-scope ytd-watch-metadata"]//yt-button-shape[@id="button-shape"]//button[@aria-label="More actions"]')
    more_options_btn.click()
    show_transcript_btn = driver.find_element("xpath", '//yt-formatted-string[normalize-space()="Show transcript"]')
    show_transcript_btn.click()
    time.sleep(3)

    content = driver.page_source.encode('utf-8').strip()
    time.sleep(1)
    soup = BeautifulSoup(content, 'lxml')
    time.sleep(1)
    time_stamp = soup.findAll("div", class_="segment-timestamp style-scope ytd-transcript-segment-renderer")
    transcript = soup.findAll("yt-formatted-string", class_="segment-text style-scope ytd-transcript-segment-renderer")
    time.sleep(1)
    for x in time_stamp:
        print('\n {} - {}'.format(x.text, transcript.text))

main()