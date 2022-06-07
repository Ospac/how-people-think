from controller.DetectLanguage import DetectLanguage
from controller.KeyPhrases import KeyPhrases
from controller.SentimentReq import SentimentReq
from controller.TwitterCrawler import TwitterCrawler
from controller.MakeWordCloud import MakeWordCloud
# from db import DB
def CrawledDataHandler(searchInput): 
    crawledData = TwitterCrawler(searchInput)
    if len(crawledData[searchInput]) >= 5120:
        return '5120자를 초과하였습니다.' , 400

    detectedlanguage = DetectLanguage(crawledData[searchInput])
    data = {
        'language'  :   detectedlanguage,
        'text'      :   crawledData[searchInput]
    }
    sentiment = SentimentReq(data)
    totalLength = len(data["text"])
    splitedLength = int(totalLength / 10) + 1
    splitedData = [ data["text"][i : i + splitedLength] for i in range(0, totalLength, splitedLength)]
    keyPhrase = KeyPhrases({'language' : data['language'], 'text' : splitedData})
    keywordList = []
    for data in keyPhrase:
        for key in data['keyPhrases']:
           keywordList.append(key)
    imgPath = MakeWordCloud(keywordList)
    # sentimentDict = {
    #     'ts' : DB.get_timestamp(),
    #     'topic' : searchInput,
    #     'prob'  : sentiment['sentimentData'][0]['confidenceScores']['positive']
    # }
    # keywordDict = {
    #     'keyword' : keyPhrase,
    # }
    resultData = {
        "sentiment" : sentiment,
        "searchInput" : searchInput,
        "imgPath" : imgPath
    }
    return resultData
