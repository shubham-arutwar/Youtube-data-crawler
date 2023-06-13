import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

url = "https://www.youtube.com/watch?v=BgdxjmGN7B4"
client = MongoClient("mongodb+srv://cyanZEUS:cyanZEUS@cluster0.w4dydp9.mongodb.net/?retryWrites=true&w=majority")

def db_trs_config(channel_name):
    db = client[channel_name]
    collection = db[""]
    return collection

# def save_to_db(collection, time_stamp, transcript):
#     collection.insert_one({time_stamp : transcript})
def save_to_trs_coll(collection, time_stamp, transcript):
    existing_doc = collection.find_one()
    if existing_doc:
        collection.update_one({}, {"$set": {time_stamp: transcript.strip()}})
    else:
        collection.insert_one({time_stamp: transcript})

    
def replace_spaces(string):
    return string.replace(" ", "_")

def remove_spaces(string):
    return string.replace(" ", "")

def click_show_transcript():
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
    soup = BeautifulSoup(content, 'html.parser')
    time.sleep(1)
    return soup

def main():
    soup = click_show_transcript()
    ch_name = soup.find("yt-formatted-string", class_="style-scope ytd-channel-name complex-string")
    v_title = soup.find("yt-formatted-string", class_="style-scope ytd-watch-metadata")
    time_stamp = soup.findAll("div", class_="segment-timestamp style-scope ytd-transcript-segment-renderer")
    transcript = soup.findAll("yt-formatted-string", class_="segment-text style-scope ytd-transcript-segment-renderer")
    time.sleep(1)
    collection = db_config(replace_spaces(ch_name.text))
    x = len(time_stamp)
    i=0
    while i < x:
        print(remove_spaces(time_stamp[i].text.strip()))
        print(transcript[i].text)
        tm_s = remove_spaces(time_stamp[i].text.strip())
        trs_tmp = transcript[i].text
        trs = trs_tmp
        save_to_trs_coll(collection, tm_s, trs)
        i+=1

main()