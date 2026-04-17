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

# 🔹 Sidebar 選單
menu = st.sidebar.radio(
    "導覽",
    ["個人介紹", "學歷", "經歷", "技能"]
)

# ----------------------
if menu == "個人介紹":
    st.title("個人介紹")

    col1, col2 = st.columns([1,2])

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

    **🔹 專題名稱：大型數據銷售分析與視覺化**

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
    - 📽️ PPT 簡報：  
    [查看簡報](https://docs.google.com/presentation/d/1vKofcCD7jqhMZdQzVjEwo_z2RVMB3DxbIUQrxneBkX4/edit?pli=1&slide=id.g3de6d4d23ec_1_85)

    - 📊 Power BI Dashboard：  
    [查看儀表板](https://app.powerbi.com/view?r=eyJrIjoiNWM4NjQzNTEtMjEyYS00MjI2LThiMmUtMmVhNTM5NjhmZjI1IiwidCI6IjQ3N2JmZWFhLTUyOTEtNGY4My04YjE0LTAzMWMzMDljZDExNyJ9)

    ---

    ### 📡 即時新聞爬蟲 + 情感分析
    - 每 5 分鐘抓取新聞  
    - Azure SQL Database 儲存  
    - LINE 即時推播  
    - NLP 情感分析（正負向判斷）  
    """)

    st.subheader("工作經歷摘要")
    st.write("""
凌發科技（Unity 組長）  
- 博弈平台開發 / 專案管理  

網銀國際（資深工程師）  
- Unity 手機遊戲開發  
- Client 主程  
""")

    st.subheader("職涯理念")
    st.write("""
重視實作與成果，持續優化系統與流程，  
希望在資料分析與工程領域創造價值。
""")

# ----------------------
elif menu == "學歷":
    st.title("學歷")

    st.markdown("### 正修科技大學｜電機工程系（二技）")
    st.write("2002 / 09 ～ 2004 / 06")

    st.markdown("### 高苑技術學院｜電機工程系（二專）")
    st.write("2000 / 09 ～ 2002 / 06")

    st.markdown("### 省立民雄農工｜電工科（高職）")
    st.write("1997 / 09 ～ 2000 / 06")

# ----------------------
elif menu == "經歷":
    st.title("經歷")

    st.markdown("""
### 凌發科技｜Unity 主任  
109 / 05 ～ 114 / 07  

- Unity3D 博弈平台開發  
- Addressable Bundle 導入  
- UGUI 前端開發與上線  
- 團隊管理（組長 / 主任）  

專案：
- 博彩遊戲
- 元宇宙（銀行）
- 直播系統  

---

### 網銀國際｜資深工程師 / 組長  
101 / 04 ～ 109 / 04  

- Unity 手機遊戲開發  
- Client 主程（世界大亨）  
- 架構設計與優化  
- Facebook 數據分析  

代表作品：
- 星城 Online  
- 勇士2014  
- 世界大亨  

---

### 早期經歷

海德威電子｜韌體工程師  
- RF Protocol / 工業設備  

博敦電子｜遊戲工程師  
- Slot Game 開發  

鼎威研發｜應用工程師  
- PCB / 8051 韌體  

奇美電子｜設備工程  
- 產線維護與故障排除  

---

### 職涯特質
- 跨領域（硬體 → 軟體 → 遊戲 → 資料）  
- 具備開發與管理能力  
- 重視效率與成果  
""")

# ----------------------
elif menu == "技能":
    st.title("技能")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("程式與工具")
        st.markdown("""
**Python**  
- 爬蟲（Requests / BeautifulSoup）  
- 自動化處理  
- 資料分析  

**SQL Server**  
- ETL（資料清洗 / 轉換 / 載入）  
- 查詢效能優化  

**Power BI**  
- 資料建模（Star Schema）  
- DAX 計算（YoY / KPI）  
- 視覺化儀表板  

**SSAS / SSRS**  
- 多維度分析  
- 報表建置  
""")

    with col2:
        st.subheader("資料與系統能力")
        st.markdown("""
**資料工程**
- ETL 流程設計  
- 資料清洗與轉換  
- API / 爬蟲資料整合  

**雲端與資料庫**
- Azure SQL Database  
- 即時資料寫入與查詢  

**數據分析**
- 銷售分析（Power BI）  
- 客戶行為分析  
- KPI 指標設計  

**專案實作**
- 即時新聞爬蟲（5分鐘更新）  
- LINE 推播整合  
- 情感分析（AI應用）  
""")