import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="我的App", layout="wide")

# ✅ 標題
st.title("📱 我的資料記錄 App")
st.caption("像 App 一樣的介面 + 可存資料 ✅")

# ✅ 側邊欄（像 App Menu）
menu = st.sidebar.radio("功能選單", ["➕ 新增資料", "📊 查看資料"])

# ✅ 檔案路徑（用來存資料）
DATA_FILE = "data.csv"

# ✅ 如果沒有檔案就建立
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["姓名", "年齡", "備註"])
    df.to_csv(DATA_FILE, index=False)

# ✅ 讀取資料
df = pd.read_csv(DATA_FILE)

# ✅ 功能 1：新增資料
if menu == "➕ 新增資料":
    st.subheader("新增資料")

    name = st.text_input("姓名")
    age = st.number_input("年齡", 0, 120)
    note = st.text_area("備註")

    if st.button("✅ 儲存"):
        new_data = pd.DataFrame([[name, age, note]], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("✅ 已成功儲存！")

# ✅ 功能 2：查看資料
elif menu == "📊 查看資料":
    st.subheader("所有資料")

    st.dataframe(df, use_container_width=True)

    st.write(f"總筆數：{len(df)}")

    if st.button("🗑 清空資料"):
        df = pd.DataFrame(columns=df.columns)
        df.to_csv(DATA_FILE, index=False)
        st.warning("資料已清空")
