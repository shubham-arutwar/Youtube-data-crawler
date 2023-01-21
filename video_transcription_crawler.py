import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://youtu.be/hByfAzEoeKA"
tag = "ytd-transcript-segment-renderer"
id1 = "segments-container"
class1 = "style-scope ytd-transcript-segment-list-renderer"

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
    titles = soup.findAll("div",id="segments-container")
    time.sleep(1)
    for title in titles:
        print(title.text)
    
main()