import streamlit as st
from spellcheck import spellcheck as sc
from translate import trans_zhHant, trans_jp, trans_ko

st.title('Spell Check')

st.write('splchk_key:')
splchk_key = input()
st.write('trans_key:')
trans_key = input()
text = st.text_input('在這裡試著輸入一段英文句子吧:','write something here~')
text1 = sc(text)
st.write('修正後的句子: {}'.format(text1))
st.write(f"中文翻譯：{trans_zhHant(text1)}")
st.write(f"日文翻譯：{trans_jp(text1)}")