import json
from controller.DetectLanguage import DetectLanguage
from controller.SentimentReq import SentimentReq
from controller.TwitterCrawler import TwitterCrawler

def CrawledDataHandler(searchInput): #searchInput을 crawling function으로 전달
    #Get CrawledData
	#with open("test.json", "r") as crawledJson:
	    #crawledData = json.load(crawledJson)
    crawledData = TwitterCrawler(searchInput)
    if len(crawledData[searchInput]) >= 5120:
        return "5120자를 초과하였습니다." , 400

    #DetectLanguage (검색어만 detect)
    detectedlanguage = DetectLanguage(crawledData[searchInput])
    data = {
        "language"  :   detectedlanguage,
        "text"      :   crawledData[searchInput]
    }
    #DetectSentiment
    sentimentData = SentimentReq(data)
    return sentimentData[0]


