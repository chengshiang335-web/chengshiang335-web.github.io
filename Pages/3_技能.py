import streamlit as st

st.set_page_config(page_title="技能")

st.title("技能")

st.subheader("程式與工具")
st.markdown("""
- Python（爬蟲 / 自動化）
- SQL Server（ETL）
- Power BI（KPI / Dashboard）
- SSAS / SSRS
""")

st.subheader("資料工程能力")
st.markdown("""
- ETL 流程設計
- API / 爬蟲整合
- Azure SQL
""")

st.subheader("專案能力")
st.markdown("""
- 即時新聞爬蟲
- LINE 推播
- 情感分析
""")