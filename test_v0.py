import streamlit as st
import os, requests, json
import uuid
from pprint import pprint

st.title('Spell Check')

userinput = st.text_input('在這裡試著輸入一段英文句子吧:','write something here~')



subscriptionKey = ''
endpointUrl = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"
params = '&to=zh-Hant&to=ja&to=ko'
constructed_url = f"{endpointUrl}{params}"
headers1 = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Ocp-Apim-Subscription-Region' : 'global',
    'Content-type': 'application/json',
    'charset':'UTF-8',
    'X-ClientTraceId': str(uuid.uuid4())
}




api_key = ''
endpoint = "https://api.bing.microsoft.com/"
url = f'{endpoint}/v7.0/SpellCheck'
params = {
    'mkt':'en-us',
    'mode':'proof'
    }
headers = {
    'Ocp-Apim-Subscription-Key': api_key,
        'Content-Type': 'application/x-www-form-urlencoded',
    }


text = userinput
data = {'text': text}
response = requests.post(url, headers=headers, params=params, data=data).json()



shift = 0
print('userinput: {}'.format(text))
print('~'*(15+len(userinput)))
for i in range(len(response['flaggedTokens'])):
    offset=response["flaggedTokens"][i]["offset"]
    wrong=response["flaggedTokens"][i]["token"]
    correct=response["flaggedTokens"][i]["suggestions"][0]["suggestion"]
    st.write(f"第{i+1}個錯誤:'{wrong}'"', 'f"修改後:'{correct}'")
    
    x = text[:(offset+shift)]
    x1 = offset+shift
    # print('x:{}'.format(x))
    
    y = x+(correct)
    # print('y:{}'.format(y))
    
    shift += len(correct)-len(wrong)
    
    z = y+(text[x1+len(wrong):])
    # print('z:{}'.format(z))    
    
    text = z
    
print('~'*(15+len(userinput)))
st.write('修正後的句子: {}'.format(text))

body = [{
    'text' : text
}]
response1 = requests.post(constructed_url, headers=headers1, json=body).json()

st.write(f"中文翻譯：{response1[0]['translations'][0]['text']}")
st.write(f"日文翻譯：{response1[0]['translations'][1]['text']}")
