import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd. DataFrame({'first column':[1, 2, 3, 4],'second column':[40, 30, 20, 10]})

st. write( df)
st. dataframe( df, width = 200, height = 200)
st. table(df)

st. title('タイトル表示')
st. header('ヘッダーの表示')
st. subheader('サブヘッダーの表示')
st. text('テキストの表示')

#マジックコマンドなどのノート
#https://prog-mcgo.com/streamlit-%E3%83%9E%E3%82%B8%E3%83%83%E3%82%AF%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89/

""" 
# マジックコマンドを使ってみる
文字列を入力
""" 

""" 
```Python
import streamlit as st
print('Hello Streamlit')
```
"""

"""
```Python
import streamlit
df = dataframe({
    '1':[1,2,3,4,5],
    '2':[10,20,30,40,50]
})
```
"""

df = pd.DataFrame(np.random.randn(20,3), columns = ['a', 'b', 'c'])
df
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

fig = plt.figure(figsize =( 10, 5))
ax = plt.axes()
x = [105, 210, 301, 440, 600]
y = [10, 20, 30, 50, 60]
ax.plot( x, y)
st.pyplot(fig)

tokyo_lat = 35.69
tokyo_lon = 139.69
df_tokyo = pd.DataFrame(np.random.randn(1000,2)/[50,50]+[tokyo_lat,tokyo_lon],columns =['lat', 'lon'] )
df_tokyo

st.map(df_tokyo)

import pydeck as pdk
view = pdk.ViewState(latitude = tokyo_lat, longitude = tokyo_lon, pitch = 50, zoom = 11)
hexagon_layer = pdk.Layer('HexagonLayer', data = df_tokyo, get_position =['lon', 'lat'], elevation_scale = 6, radius = 200, extruded = True)
layer_map = pdk.Deck(layers = hexagon_layer, initial_view_state = view)
st.pydeck_chart(layer_map)

from PIL import Image
#import os
#os.chdir('c:/Users/ユーザ名/desktop')
image = Image.open('C:/Users/Akira.Murayama/Pictures/Matsue/20230325_110000.jpg')
st.image(image, caption ='サンプル画像')

option_button = st.button('ボタン')
if option_button == True:
    st.write('ボタンが押されました')
else:
    st.write('ボタンを押してください')

option_radio = st.radio("好きな果物を選んでください", ('りんご', 'バナナ', 'オレンジ', 'その他'))
st.write('あなたが選んだ果物は：', option_radio)

option_check = st.checkbox('DataFrameの表示')
df = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [40, 30, 20, 10]})
if option_check == True:
    st.write(df)

option_select = st.selectbox("どれか一つ選択してください", ('A', 'B', 'C'))
st.write('あなたが選んだのは：', option_select)

option_multi = st.multiselect('好きな色を選択してください', ['緑', '黄色', '赤', '青'], ['黄色', '赤'])

age = st.slider('あなたの年齢を教えて下さい', min_value = 0, max_value = 130, step = 1, value = 20)
st.write('私の年齢は', age, 'です')

height = st.sidebar.slider('あなたの身長(cm)を入力してください', min_value = 0, max_value = 200, step = 1, value = 170)
st.write('私の身長は', height, 'cm です')
gender = st.sidebar.selectbox('あなたの性別を教えて下さい', ['男性', '女性'])
st.write('あなたの性別は：', gender)

import time
progress_button = st.button('プログレスボタン')
if progress_button == True:
    st.write('処理を開始します')
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    st.text('処理が終了しました')
else: st.write('プログレスボタンを押してください')

import plotly.express as px
#import statsmodels as sm
df=px.data.iris()
fig=px.scatter(df,x="sepal_width",y="sepal_length",color="species",marginal_y="violin",marginal_x="box",trendline="ols",template="simple_white")
fig.show()