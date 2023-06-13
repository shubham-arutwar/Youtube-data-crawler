import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

# channel_url = input("enter channel URL : ")
# url = str(channel_url) + "/videos"
url = input("enter playlist URL : ")

def db_config(channel_name):
    client = MongoClient("mongodb+srv://cyanZEUS:cyanZEUS@cluster0.w4dydp9.mongodb.net/?retryWrites=true&w=majority")
    db = client[channel_name]
    collection = db["video_list"]
    return collection

def save_to_db(collection, title, link):
    collection.insert_one({"title": title, "link": link})
    
def replace_spaces(string):
    return string.replace(" ", "_")

def main():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(url)
    time.sleep(5)
    i = 1
    while i < 40:
        driver.execute_script("window.scrollBy(0,1000)","")
        print("scroll "+ str(i))
        time.sleep(3)
        i+=1

    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'html.parser')
    ch_name = soup.find("yt-formatted-string", id="text", class_="style-scope yt-dynamic-sizing-formatted-string yt-sans-28")
    titles = soup.findAll("a",id="video-title", class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")
    collection = db_config(replace_spaces(ch_name.text))
    print('\nChannel: {}\nURL: {}'.format(ch_name.text, url))
    i=1
    for title in titles:
        print('\n {} - {} : https://www.youtube.com{}'.format(i,title.text, title.get('href')))
        video_title = title.text
        video_link = "https://www.youtube.com"+str(title.get('href'))
        save_to_db(collection, video_title, video_link)
        i+=1

main()