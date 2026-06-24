import streamlit as st

st.set_page_config(page_title="我的App", layout="wide")

# ✅ 側邊欄選單（最推薦🔥）
menu = st.sidebar.radio(
    "📱 功能選單",
    ["🏠 首頁", "🔍 Say Hello", "📊 查看資料"]
)

# ✅ 首頁
if menu == "🏠 首頁":
    st.title("🏠 我的 App 首頁")
    st.write("歡迎使用我的 App 👋")

# ✅ Say Hello 頁
elif menu == "🔍 Say Hello":
    st.title("🔍 Say Hello")

    name = st.text_input("請輸入你的名字")

    if st.button("打招呼"):
        st.success(f"Hello, {name}! 🎉")

# ✅ 查看資料頁
elif menu == "📊 查看資料":
    st.title("📊 查看資料")

    st.write("這裡可以顯示資料")

    # 範例資料
    data = ["Apple", "Banana", "Cherry"]
    st.write(data)
