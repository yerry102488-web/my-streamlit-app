import streamlit as st
import pandas as pd
import os

def show():
    st.title("📊 技術指標計算")
    st.write("請輸入 High / Low / MA5")
    
    # 輸入欄位
    high = st.number_input("High", value=0.0)
    low = st.number_input("Low", value=0.0)
    ma5 = st.number_input("MA5", value=1.0)
    
    if st.button("✅ 計算"):
        if ma5 == 0:
            st.error("MA5 不能為 0 ❌")
        else:
            # 計算
            result1 = (high - ma5) / ma5
            result2 = (low - ma5) / ma5
    
            st.subheader("📈 計算結果（水平排列）")
    
            # 建立 DataFrame（水平一筆資料）
            df = pd.DataFrame({
                "High": [high],
                "Low": [low],
                "MA5": [ma5],
                "Bias_High": [result1],
                "Bias_Low": [result2]
            })
    
            st.dataframe(df, use_container_width=True)
    
            # 額外提示
            if result1 > 0:
                st.success("High 高於 MA5")
            else:
                st.warning("High 低於或接近 MA5")
    
            if result2 > 0:
                st.info("Low 高於 MA5（偏離為正）")
            else:
                st.warning("Low 低於 MA5（偏離為負）")
