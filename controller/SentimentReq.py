import requests, os, uuid, json
from dotenv import load_dotenv

load_dotenv()
key = os.environ['KEY']
endpoint = os.environ['ENDPOINT']
location = os.environ['LOCATION']

def SentimentReq(data):
    path = "text/analytics/v3.1"
    constructed_url = endpoint + path + "/sentiment"
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = {"documents": [{ "id": "1", "language": data["language"], "text" : data["text"] }]}

    try:
        req = requests.post(constructed_url, headers=headers, json=body)
    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)
    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)
    # Any Error except upper exception
    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)

    res = req.json()
    output = None
    if req.status_code == 200:
            output = res["documents"]
    else:
        output = res
        print(output)
    return output