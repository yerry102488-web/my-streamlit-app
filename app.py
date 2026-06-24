import streamlit as st

st.title("🏠 我的 App 首頁")

if st.button("🔍 Say Hellow"):
    st.switch_page("pages/1_Say_Hello.py")

if st.button("📊 查看資料"):
    st.switch_page("pages/2_查看資料.py")

