import streamlit as st

# 🔹 基本設定
st.set_page_config(
    page_title="個人求職頁",
    layout="wide"
)

# 🔹 自訂CSS（簡約沈穩風）
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #ffffff;
}
h1, h2, h3 {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# ======================
# 個人介紹
# ======================
st.title("個人介紹")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/p1.jpg", use_container_width=True)

with col2:
    st.subheader("勝翔")
    st.write("資料分析 / 資料工程")

st.markdown("---")

st.subheader("自我簡介")
st.write("""
您好，我是勝翔。出生於嘉義縣，目前與妻子定居台中，育有一子一女。  
在家庭與育兒過程中培養了耐心與責任感。

畢業於正修科技大學電機工程系，具備Unity3D、C#、單晶片8051、C語言、PLC基礎。  
目前於職訓局進修「Python人工智慧與數據分析班」。
""")

st.subheader("技術能力")
st.write("""
- Python（爬蟲 / 自動化）
- SQL Server（ETL）
- SSAS / SSRS
- Power BI
""")

st.markdown("[技能樹](https://chengshiang335-web.github.io/)")

st.subheader("專題經驗")

st.markdown("""
### 📊 大型數據資料分析（Power BI 專題）

**專題名稱：大型數據銷售分析與視覺化**

**📌 專題內容：**
- 建立 Power BI 銷售分析儀表板  
- 資料模型設計（Star Schema）  
- KPI 指標分析（營收 / 成長率 / 客戶分析）  
- 大數據資料整合與視覺化呈現  

**🚀 技術應用：**
- Power BI（DAX / 視覺化）
- SQL Server（資料整理 / ETL）
- Azure（資料存放）

**📎 專題連結：**
- 📽️ PPT 簡報  
https://docs.google.com/presentation/d/1vKofcCD7jqhMZdQzVjEwo_z2RVMB3DxbIUQrxneBkX4/edit

- 📊 Power BI Dashboard  
https://app.powerbi.com/view?r=eyJrIjoiNWM4NjQzNTEtMjEyYS00MjI2LThiMmUtMmVhNTM5NjhmZjI1IiwidCI6IjQ3N2JmZWFhLTUyOTEtNGY4My04YjE0LTAzMWMzMDljZDExNyJ9
""")

st.markdown("---")

st.subheader("即時新聞爬蟲 + 情感分析")
st.write("""
- 每 5 分鐘抓取新聞  
- Azure SQL Database 儲存  
- LINE 即時推播  
- NLP 情感分析（正負向判斷）  
""")

st.markdown("---")

st.subheader("工作經歷摘要")
st.write("""
凌發科技（Unity 組長）  
- 博弈平台開發 / 專案管理  

網銀國際（資深工程師）  
- Unity 手機遊戲開發  
- Client 主程  
""")

st.markdown("---")

st.subheader("職涯理念")
st.write("""
重視實作與成果，持續優化系統與流程，  
希望在資料分析與工程領域創造價值。
""")