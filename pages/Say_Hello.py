import streamlit as st

def show():
    st.title("🔍 Say Hello")

    name = st.text_input("請輸入名字")

    if st.button("打招呼"):
        st.success(f"Hello {name} 👋")
