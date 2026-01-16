import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Hello, Streamlit!')
st.write('これは最初のStreamlitアプリケーションです。')

input_num = st.number_input('Input a number', value=0)

result = input_num ** 3
st.write('Result: ', result)


df = pd.DataFrame({
    '名前': ['Alice', 'Bob', 'Charlie'],
    'スコア': [85, 90, 78]
})
 
st.write("学生のスコア")
st.dataframe(df)

# データの作成
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
 
# チャートの作成
st.line_chart(df)

counter = 0

if 'counter' not in st.session_state:
    st.session_state.counter = 0
if st.button("カウンターを増やすボタン"):
    st.session_state.counter += 1

st.write("更新されたカウンター：", st.session_state.counter)