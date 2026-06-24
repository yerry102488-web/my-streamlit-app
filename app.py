import streamlit as st

st.set_page_config(page_title="我的App", layout="wide")

st.title("🏠 我的 App 首頁")

st.write("請選擇功能：")

# ✅ 按鈕式跳頁（安全）
st.page_link("pages/Say_Hello.py", label="🔍 Say Hello")
st.page_link("pages/Show_Data.py", label="📊 查看資料")
