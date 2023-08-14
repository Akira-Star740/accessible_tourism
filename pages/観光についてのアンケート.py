import streamlit as st
link = '[<span class="hljs-string">バリアフリー観光についてのアンケート</span>](<span class="hljs-link">https://docs.google.com/forms/d/e/1FAIpQLSdtaNwJM1eigr6HvOR1Jz_Lv9paDD32j9d-LgvgkfKFpemGDA/viewform?usp=sf_link</span>)'
st.markdown(link, unsafe_allow_html=True)
st.write('上記リンクからアンケートにお答えください。')