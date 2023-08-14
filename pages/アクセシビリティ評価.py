import streamlit as st
import pandas as pd

df=pd.read_csv('score.csv')
df=df.set_index('観光スポット')
option_radio = st.sidebar.radio("今回訪れた（訪れようとしている）観光スポットのバリアフリー状況を評価してください。", 
                            (df.index))
st.write('あなたが訪れたスポットは：', option_radio)
#theval=df.loc[option_radio,'アクセス評価']
#st.write(option_radio,theval)
#score = st.slider('アクセシビリティ評価は100点満点中', min_value = 0, max_value = 100, step = 1,value=int(theval))
score = st.slider('アクセシビリティ評価は100点満点中', min_value = 0, max_value = 100, step = 1,
                  value=int(df.loc[option_radio,'アクセス評価']))
st.write(score, '点です！')
#st.write(option_radio,theval)
df.loc[option_radio,'アクセス評価']=score
df.to_csv('score.csv')
st.write('あなたの評価スコア')
st.write(df)

option_button = st.button('リセット')
if option_button == True:
    st.write('回答がリセットされました')
    
    df = pd.DataFrame(columns=['アクセス評価', '情報評価'],
                  index=['偕楽園', '国営ひたち海浜公園', 'アクアワールド', '袋田の滝', '牛久大仏', '大洗磯前神社',
                         '御岩神社','筑波山神社','六角堂','笠間稲荷神社','鹿島神社'])

    df.index.name='観光スポット'
    df.fillna(0, inplace=True)
    df.to_csv('score.csv')
    st.write('あなたの評価スコア')
    st.write(df)
else:
    st.write('回答をリセットします')