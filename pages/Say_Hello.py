import streamlit as st

def show():
    st.title("📊 技術指標計算")

    st.write("請輸入 High / Low / MA5")

    # ✅ 輸入欄位
    high = st.number_input("High", value=0.0)
    low = st.number_input("Low", value=0.0)
    ma5 = st.number_input("MA5", value=1.0)  # 避免除以 0

    if st.button("✅ 計算"):
        if ma5 == 0:
            st.error("MA5 不能為 0 ❌")
        else:
            result1 = (high - ma5) / ma5
            result2 = (ma5 - low) / ma5

            st.subheader("📈 計算結果")

            st.write(f"(High - MA5) / MA5 = {result1:.4f}")
            st.write(f"(MA5 - Low) / MA5 = {result2:.4f}")

            # ✅ 視覺化提示
            if result1 > 0:
                st.success("價格高於 MA5 ✅")
            else:
                st.warning("價格低於或接近 MA5")

            if result2 > 0:
                st.info("MA5 與 Low 有距離")
