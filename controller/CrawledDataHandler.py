import json
from controller.DetectLanguage import DetectLanguage
from controller.SentimentReq import SentimentReq

def CrawledDataHandler(searchInput): #searchInput을 crawling function으로 전달
    #Get CrawledData
    with open("test.json", "r") as crawledJson:
        crawledData = json.load(crawledJson)
    if len(crawledData["document"]) >= 5120:
        return "5120자를 초과하였습니다." , 400

    #DetectLanguage (검색어만 detect)
    detectedlanguage = DetectLanguage(crawledData["search_word"])
    data = {
        "language"  :   detectedlanguage,
        "text"      :   crawledData["document"]
    }
    #DetectSentiment
    sentimentData = SentimentReq(data)
    return sentimentData[0]


