from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

def trend_search():
    try:
        try:
            driver = webdriver.Chrome('./controller/chromedriver')
        except Exception as e:
            driver = webdriver.Chrome()
        driver.wait = WebDriverWait(driver, 10)
        trending_page = 'https://signal.bz/'
        driver.get(trending_page)
        driver.implicitly_wait(8)
        # driver.maximize_window()
        trendingword = []
        trendinglist1 = driver.find_elements(By.XPATH, '//*[@id="app"]/div/main/div/section/div/section/section[1]/div[2]/div/div[1]/div')
        for trendingtitle in trendinglist1:
            trendinglist = trendingtitle.find_element(By.XPATH, './/a/span[2]').text
            trendingword.append(trendinglist)
        trendinglist2 = driver.find_elements(By.XPATH, '//*[@id="app"]/div/main/div/section/div/section/section[1]/div[2]/div/div[2]/div')
        for trendingtitle in trendinglist2:
            print(trendingtitle)
            sentence = trendingtitle.find_element(By.XPATH, './/a/span[2]').text
            trendingword.append(sentence)
        print(trendingword)
        driver.quit()
        return trendingword
    except Exception as e:
        print(e)
    
def TrendCrawler():
    return trend_search()

