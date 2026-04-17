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

# 🔹 各頁內容

# ----------------------
if menu == "個人介紹":
    st.title("👤 個人介紹")

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("https://via.placeholder.com/200")

    with col2:
        st.subheader("SHIANG Chen")
        st.write("""
        資料分析 / 資料工程方向  
        擅長 Power BI、Python、SQL  
        專注於資料轉換與商業分析
        """)

# ----------------------
elif menu == "學歷":
    st.title("🎓 學歷")

    st.write("""
    - 國立XXX大學 資訊管理學系  
    - 主修：資料分析、資料庫系統  
    """)

# ----------------------
elif menu == "經歷":
    st.title("💼 經歷")

    st.write("""
    ### 公司A
    - 建立資料ETL流程
    - 使用 Power BI 製作儀表板

    ### 專案
    - H&M 銷售分析
    - 客戶分群模型
    """)

# ----------------------
elif menu == "技能":
    st.title("🛠 技能")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("技術技能")
        st.write("""
        - Python
        - SQL
        - Power BI
        """)

    with col2:
        st.subheader("資料能力")
        st.write("""
        - ETL
        - 資料清洗
        - 視覺化分析
        """)