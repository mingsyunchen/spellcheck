# https://docs.microsoft.com/zh-tw/azure/cognitive-services/bing-spell-check/quickstarts/python

import streamlit as st
import requests, uuid, json

print('SPLCHK_key:')
api_key = input()
endpoint = "https://api.bing.microsoft.com"
url = f'{endpoint}/v7.0/SpellCheck'
params = {
    'mkt':'en-us',
    'mode':'proof' # proof(攔截大部分的拼字/文法錯誤)；spell(攔截大部分的拼字檢查錯誤，但沒有多少文法錯誤)
    }
headers = {
    'Ocp-Apim-Subscription-Key': api_key,
    'Content-Type': 'application/x-www-form-urlencoded',
    }

def spellcheck(text):
    data = {'text': text}
    response = requests.post(url, headers=headers, params=params, data=data).json()

    shift = 0
    for i in range(len(response['flaggedTokens'])):
        offset=response["flaggedTokens"][i]["offset"]
        wrong=response["flaggedTokens"][i]["token"]
        correct=response["flaggedTokens"][i]["suggestions"][0]["suggestion"]
        st.write(f"第{i+1}個錯誤:'{wrong}'"', 'f"修改後:'{correct}'")
        
        x = text[:(offset+shift)] # part before offset
        x1 = offset+shift
        # print('x:{}'.format(x))
        
        y = x+(correct)
        # print('y:{}'.format(y))
        
        shift += len(correct)-len(wrong)
        
        z = y+(text[x1+len(wrong):])
        # print('z:{}'.format(z))    
        
        text = z
    return text