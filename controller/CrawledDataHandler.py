from controller.DetectLanguage import DetectLanguage
from controller.KeyPhrases import KeyPhrases
from controller.SentimentReq import SentimentReq
from controller.TwitterCrawler import TwitterCrawler
from controller.MakeWordCloud import MakeWordCloud
from db import DB

def CrawledDataHandler(searchInput): 
    sentiment= []
    imgPath = 0
    keywordHistory = 0
    tags = 0
    db = DB()
    dbHistory = db.get_history(searchInput)
    hasRecentHistory = db.history_exist(searchInput)
    if hasRecentHistory:
        ts = dbHistory['ts'][0]
        keywords = db.get_keywords(searchInput, ts)
        editedKeywordList = []
        offset = len(keywords) * 10
        for item in keywords:
            for idx in range(0, offset):
                editedKeywordList.append(item)
            offset -= 10
        imgPath, tags = MakeWordCloud(editedKeywordList).values()
        prob = [
            dbHistory['pos_prob'][0],
            dbHistory['neg_prob'][0],
            dbHistory['neu_prob'][0]
        ]
        sentiment = [{
            "confidenceScores"  : {
                "positive"  :   prob[0],
                "negative"  :   prob[1],
				"neutral"   :   prob[2]
            },      
            "sentiment"     : "mixed"
            }]
    else:
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
        prob = [
            sentiment[0]['confidenceScores']['positive'], 
            sentiment[0]['confidenceScores']['negative'],
            sentiment[0]['confidenceScores']['neutral']
        ]
        sentimentDict = {
            'id'        : db.get_id('history'),
            'ts'        : db.get_timestamp(),
            'topic'     : searchInput,
            'pos_prob'  : prob[0],
            'neg_prob'  : prob[1],
            'neu_prob'  : prob[2]
        }

        db.insertDB(sentimentDict, list(tags.keys())[0:10])

    keywordHistory = {}
    for idx in range(0,len(dbHistory['ts'])):
        if(idx == 5): break
        keywordHistory[dbHistory['ts'][idx]] = {'keyword': {}, 'prob':{}}
        keywordHistory[dbHistory['ts'][idx]]['keyword'] = db.get_keywords(searchInput, dbHistory['ts'][idx])
        keywordHistory[dbHistory['ts'][idx]]['pos_prob'] = dbHistory['pos_prob'][idx]
        keywordHistory[dbHistory['ts'][idx]]['neg_prob'] = dbHistory['neg_prob'][idx]
        keywordHistory[dbHistory['ts'][idx]]['neu_prob'] = dbHistory['neu_prob'][idx]

    resultData = {
        "sentiment"         : sentiment,
        "searchInput"       : searchInput,
        "imgPath"           : imgPath,
        "keywordHistory"    : keywordHistory
    }
    return resultData
