import requests, uuid, json

subscription_Key = trans_key
endpoint = 'https://api.cognitive.microsofttranslator.com'
path = '/translate'
location = 'global'
url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['zh-Hant', 'ja', 'ko']
}
headers = {
    'Ocp-Apim-Subscription-Key': subscription_Key,
    'Ocp-Apim-Subscription-Region' : location,
    'Content-type': 'application/json',
    'charset':'UTF-8',
    'X-ClientTraceId': str(uuid.uuid4())
}

def trans_zhHant(text):
    body = [{'text': text}]
    response = requests.post(url, headers=headers, params=params, json=body).json()
    output = response[0]['translations'][0]['text']
    return output

def trans_jp(text):
    body = [{'text': text}]
    response = requests.post(url, headers=headers, params=params, json=body).json()
    output = response[0]['translations'][1]['text']
    return output

def trans_ko(text):
    body = [{'text': text}]
    response = requests.post(url, headers=headers, params=params, json=body).json()
    output = response[0]['translations'][2]['text']
    return output