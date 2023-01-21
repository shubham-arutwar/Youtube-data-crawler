import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.youtube.com/@joerogan/videos"
tag = "ytd-transcript-segment-renderer"
id1 = "segments-container"
class1 = "style-scope ytd-transcript-segment-list-renderer"

def main():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    
#    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    i = 1
    while i < 100:
        driver.execute_script("window.scrollBy(0,1000)","")
        print("scroll "+ str(i))
        time.sleep(3)
        i+=1
        
        
    content = driver.page_source.encode('utf-8').strip()
    print("Source content coppied")
    soup = BeautifulSoup(content, 'lxml')
    print("Object created")
    ch_name = soup.find("yt-formatted-string", id="text", class_="style-scope ytd-channel-name")
    print("ch_name")
    titles = soup.findAll("a",id="video-title-link", class_="yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media")
    print("titles")
    print('\nChannel: {}\nURL: {}'.format(ch_name.text, url))
    i=0
    for title in titles:
        print('\n {} - {} : https://www.youtube.com{}'.format(i,title.text, title.get('href')))

main()

'''1    time.sleep(2)
    more_options_btn = driver.find_element("xpath", '//ytd-menu-renderer[@class="style-scope ytd-watch-metadata"]//yt-button-shape[@id="button-shape"]//button[@aria-label="More actions"]')
    more_options_btn.click()
    show_transcript_btn = driver.find_element("xpath", '//yt-formatted-string[normalize-space()="Show transcript"]')
    show_transcript_btn.click()
    time.sleep(3)'''