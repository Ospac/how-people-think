import requests
import time
import threading
import time
from controller.TrendCrawler import TrendCrawler

index = 0
trendinglist = []

def InitThreading():
    s = threading.Thread(target=ThreadingStart)
    s.start()
   
def ThreadingStart():
    global trendinglist
    trendinglist = TrendCrawler() # Scrape Trending Search Words
    t = threading.Thread(target=AutoCrawler) # Start Auto Crawling
    t.start()
    time.sleep(600)
    tt = threading.Thread(target=ThreadingStart) # Repeat with Interval
    tt.start()
    
def AutoCrawler():
    time.sleep(5)
    t = threading.Thread(target=SendRequest) # Sending Request
    t.start()
    global index
    if index == len(trendinglist)-1:
       index = 0
       return
    tt = threading.Thread(target=AutoCrawler) # Repeat until the end of index
    tt.start()
    
def SendRequest():
    URL = "http://localhost:8888/result"
    global index
    PARAMS = {'search_input': trendinglist[index]}
    index=index+1
    reqresult = requests.get(url=URL, params=PARAMS)

