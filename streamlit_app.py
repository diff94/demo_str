#https://blog.jiatool.com/posts/streamlit_2023/
import time
import streamlit as st
import numpy as np
import pandas as pd 
st.title('我的第一個應用程式')
st.write("嘗試創建**表格**:")
df=pd.DataFrame({
    '1st column': [1,2,3,4],
    '2nd column':[10,20,30,40]

})
df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.6, 120.4],
    columns=['lat', 'lon'])
st.map(map_data)
if st.button('不要按!'):
    st.text("不是叫你不要按了嗎！")
if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.6, 120.4],
        columns=['lat', 'lon'])
    st.map(map_data)
option = st.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
st.text(f'你的答案：{option}')

option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
st.sidebar.text(f'你的答案：{option}')
left_column, right_column = st.columns(2)
left_column.write("這是左邊欄位。")
right_column.write("這是右邊欄位。")

expander = st.expander("點擊來展開...")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")

tab1, tab2 = st.tabs(["Cat 介紹", "Dog 介紹"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


