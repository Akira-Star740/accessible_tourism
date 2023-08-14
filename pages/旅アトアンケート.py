import streamlit as st
import pandas as pd

""" 
#### こちらは旅が終わった後にお答えください。
""" 

df = pd.DataFrame(columns=['評価'],
                  index=['満足度','再訪意向','推奨意向'])

option_radio = st.radio("今回の旅行で訪れた観光地にあなたは満足しましたか？", 
                            ('とても満足した','満足した','やや満足した','どちらでもない',
                             'あまり満足していない','満足していない','まったく満足していない'))
st.write('あなたは観光地に満足しましたか：', option_radio)
df.loc['満足度','評価']=option_radio

option_radio = st.radio("今回の旅行で訪れた観光地にまた訪れたいと思いますか？", 
                            ('ぜひ訪れたい','訪れたい','やや訪れたい','どちらでもない',
                             'あまり訪れたくない','訪れたくない','絶対に訪れたくない'))
st.write('あなたは観光地をまた訪れたいですか：', option_radio)
df.loc['再訪意向','評価']=option_radio

option_radio = st.radio("今回の旅行で訪れた観光地を人に薦めたいと思いますか？", 
                            ('ぜひ薦めたい','薦めたい','やや薦めたい','どちらでもない',
                             'あまり薦めたくない','薦めたくない','絶対に薦めたくない'))
st.write('あなたは観光地を人に薦めたいですか：', option_radio)
df.loc['推奨意向','評価']=option_radio

option_button = st.button('回答を送信する')
if option_button == True:
    st.write('回答が送信されました')
    
    df.to_csv('satisfy.csv')
    st.write('あなたの満足度')
    st.write(df)
else:
    st.write('回答を送信してください')