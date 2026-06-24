import streamlit as st
import pandas as pd
import numpy as np

def show():
    # 標題
    st.title("🎉 我的第一個 Streamlit 網站")
    st.write("歡迎使用我的 Web App 🚀")

    # 使用者輸入
    name = st.text_input("請輸入你的名字：")

    if st.button("打招呼"):
        st.success(f"你好，{name}！很高興見到你 😊")

    # 分隔線
    st.divider()

    # 資料顯示
    st.subheader("📊 隨機資料")

    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )

    st.dataframe(data)

    # 圖表
    st.subheader("📈 折線圖")
    st.line_chart(data)

    # 側邊欄（⚠️注意這裡）
    st.sidebar.title("⚙️ 設定")

    rows = st.sidebar.slider("選擇資料筆數", 10, 100, 20)

    new_data = pd.DataFrame(
        np.random.randn(rows, 2),
        columns=['X', 'Y']
    )

    st.subheader("📉 可調整圖表")
    st.line_chart(new_data)
