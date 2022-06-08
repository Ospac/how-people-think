import psycopg2
from controller.DetectLanguage import DetectLanguage
from controller.KeyPhrases import KeyPhrases
from controller.SentimentReq import SentimentReq
from controller.TwitterCrawler import TwitterCrawler
from controller.MakeWordCloud import MakeWordCloud
from db import DB

def CrawledDataHandler(searchInput): 
    db = DB()
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
    imgPath, tags = MakeWordCloud(keywordList).values()

    sentimentDict = {
        'id'    : db.get_id('history'),
        'ts'    : db.get_timestamp(),
        'topic' : searchInput,
        'prob'  : sentiment[0]['confidenceScores']['positive']
    }

    db.insertDB(sentimentDict, list(tags.keys())[0:10])
    dbHistory = db.get_history(searchInput)
    keywordHistory = {}
    for idx in range(0,len(dbHistory['ts'])):
        keywordHistory[dbHistory['ts'][idx]] = {'keyword': {}, 'prob':{}}
        keywordHistory[dbHistory['ts'][idx]]['keyword'] = db.get_keywords(searchInput, dbHistory['ts'][idx])
        keywordHistory[dbHistory['ts'][idx]]['prob'] = dbHistory['prob'][idx]
    
    resultData = {
        "sentiment"         : sentiment,
        "searchInput"       : searchInput,
        "imgPath"           : imgPath,
        "keywordHistory"    : keywordHistory
    }
    return resultData
