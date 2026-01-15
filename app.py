import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Hello, Streamlit!')
st.write('これは最初のStreamlitアプリケーションです。')

input_num = st.number_input('Input a number', value=0)

result = input_num ** 3
st.write('Result: ', result)

st.title('Hello, Streamlit!')
 
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