from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from time import sleep
import time
import os

twitterid = os.environ['TWITTERID']
twitterpw = os.environ['TWITTERPW']

def twitter_login(word):
    try:
        driver = webdriver.Chrome('./chromedriver')
        driver.wait = WebDriverWait(driver, 10)
        twitter_page = 'https://twitter.com/login'
        driver.get(twitter_page)
        driver.implicitly_wait(5)
        #driver.maximize_window()

        sign_in = driver.find_element(By.NAME, "text")
        sign_in.send_keys(twitterid)
        driver.implicitly_wait(1)

        next_btn = driver.find_element(By.XPATH,
                                       '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_btn.click()
        driver.implicitly_wait(5)
        password = driver.find_element(By.XPATH,
                                       '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
        password.send_keys(twitterpw)
        driver.implicitly_wait(1)
        login_btn = driver.find_element(By.XPATH,
                                        '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
        login_btn.click()
        return search_sentence(word, driver)
    except Exception as e:
        print(e)

def search_sentence(query, driver):
    finished = 0
    searched_word = {}
    sentence_history = set()
    box = driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')))    
    query='\"'+query+'\"'
    box.send_keys(query)
    box.submit()
    query = query[1:-1]
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.LINK_TEXT, '최신').click() # change to 'Latest' depending on your language
    sleep(2)

    for i in range(10):
        twitter_search(query, driver, searched_word, sentence_history, finished)
    driver.quit()
    return searched_word

def one_tweet(data):
    try:
        uploadtime = data.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:
        return
    sentence = data.find_element_by_xpath('.//div[2]/div[2]/div[2]/div[1]/div').text
    return sentence

def twitter_search(query, driver, searched_word, sentence_history, finished):
    if finished == 1:
        return
    tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
    for tweet in tweets[-15:]:
        text = one_tweet(tweet)
        if text:
            text = text.replace("\r", " ").replace("\n", " ") 
            history = ''.join(text)
            if text[0]=='@' or (text[0]=='h' and text[1]=='t' and text[2]=='t' and text[3]=='p'):
                continue
            if history not in sentence_history:
                sentence_history.add(history)
                query = query.replace('"',"")
                if query not in searched_word:
                    searched_word[query]=' '
                else:
                    if len(searched_word[query]) + len(text) >= 5120:
                        finished = 1
                        break
                    searched_word[query]+=text
            
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(1.5)

def TwitterCrawler(word):
    return twitter_login(word)
