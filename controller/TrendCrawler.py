from flask import Flask
from flask_restful import Api
from routes.Index import Index
from routes.Result import Result

from controller.TrendCrawler import TrendCrawler

# importing the requests library

app = Flask(__name__)
api = Api(app)

#routes
api.add_resource(Index, '/')
api.add_resource(Result, '/result')

import requests
import time
import threading
global a
a = 0
trendinglist=[]


def sendrequest():
    URL = "http://localhost:8888/result"
    global a
    print(a)
    print(len(trendinglist))
    PARAMS = {'search_input': trendinglist[a]}
    a=a+1
    reqresult = requests.get(url=URL, params=PARAMS)

waitflag=0
import time
def printit():
    global waitflag
    time.sleep(5)
    if waitflag == 0:
        t = threading.Thread(target=sendrequest)
        t.start()
    global a
    if a == len(trendinglist)-1:
       a = 0
       return
    tt = threading.Thread(target=printit)
    tt.start()

def trendcrawl():
    global waitflag
    waitflag=1
    global trendinglist
    trendinglist = TrendCrawler()
    waitflag=0  
    t = threading.Thread(target=printit)
    t.start()
    time.sleep(200)
    tt = threading.Thread(target=trendcrawl)
    tt.start()

s = threading.Thread(target=trendcrawl)
s.start()
    # continue with the rest of your codes
#API Server
if __name__ == '__main__':
    app.run(debug=True)



