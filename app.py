import streamlit as st

st.set_page_config(page_title="我的App", layout="wide")

# ✅ 標題
st.title("🏠 我的 App 首頁")

st.write("請使用左側選單選擇功能 👈")

st.divider()

st.subheader("功能介紹")

st.write("🔍 Say Hello：簡單互動功能")
st.write("📊 查看資料：顯示資料列表")

st.info("👉 請點左上角 ☰ 打開選單")
