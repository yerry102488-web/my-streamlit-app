import streamlit as st
from pages import say_hello, show_data

st.set_page_config(page_title="我的App", layout="wide")

menu = st.sidebar.radio(
    "📱 功能選單",
    ["🏠 首頁", "🔍 Say Hello", "📊 查看資料"]
)

# ✅ 首頁
if menu == "🏠 首頁":
    st.title("🏠 我的 App 首頁")
    st.write("歡迎使用 App 👋")

# ✅ 呼叫 pages
elif menu == "🔍 Say Hello":
    say_hello.show()

elif menu == "📊 查看資料":
    show_data.show()
