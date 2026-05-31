import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Mobile JKN Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main{
    background-color:#f4f8fc;
}

[data-testid="metric-container"]{
    background:white;
    border-radius:18px;
    padding:18px;
    border-left:5px solid #0d6efd;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.banner{
    background: linear-gradient(135deg,#0d6efd,#36a2ff);
    padding:35px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="banner">

<h1>📊 Mobile JKN Analytics Dashboard</h1>

<h4>
Analisis Kemudahan Penggunaan, Kualitas Sistem,
dan Efisiensi Mobile JKN di Kabupaten Sumedang
</h4>

<p>
Metode PLS-SEM | Responden 31 Orang
</p>

</div>
""", unsafe_allow_html=True)

# =====================================
# DESKRIPSI PENELITIAN
# =====================================

st.info("""
Penelitian ini bertujuan untuk menganalisis pengaruh
Kemudahan Penggunaan dan Kualitas Sistem terhadap
Efisiensi penggunaan Mobile JKN menggunakan metode
PLS-SEM dengan jumlah responden sebanyak 31 orang.
""")

# =====================================
# KPI
# =====================================

st.subheader("📈 Ringkasan Hasil Penelitian")

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("👥 Responden","31")
c2.metric("👍 Kemudahan Penggunaan","4.13")
c3.metric("⚙️ Kualitas Sistem","3.95")
c4.metric("⚡ Efisiensi","4.23")
c5.metric("📊 R²","60.5%")

st.markdown("---")

# =====================================
# TEMUAN UTAMA
# =====================================

st.subheader("🎯 Temuan Utama")

a,b,c = st.columns(3)

with a:
    st.success("""
### Variabel Dominan

**Kualitas Sistem**

β = 0.66

Memiliki pengaruh terbesar terhadap Efisiensi.
""")

with b:
    st.info("""
### Efisiensi Pengguna

**4.23**

Kategori Tinggi

Mayoritas pengguna merasa Mobile JKN membantu proses layanan kesehatan menjadi lebih efisien.
""")

with c:
    st.warning("""
### Kekuatan Model

**R² = 60.5%**

Model mampu menjelaskan 60.5% variasi Efisiensi.
""")

st.markdown("---")

# =====================================
# DATA
# =====================================

df_variabel = pd.DataFrame({
    "Variabel":[
        "Kemudahan Penggunaan",
        "Kualitas Sistem",
        "Efisiensi"
    ],
    "Nilai":[4.13,3.95,4.23]
})

df_path = pd.DataFrame({
    "Hubungan":[
        "KP → EF",
        "KS → EF"
    ],
    "Koefisien":[
        0.13,
        0.66
    ]
})

# =====================================
# GRAFIK BAR + RADAR
# =====================================

col1,col2 = st.columns(2)

with col1:

    fig = px.bar(
        df_variabel,
        x="Variabel",
        y="Nilai",
        text="Nilai",
        color="Variabel",
        title="Perbandingan Variabel Penelitian"
    )

    fig.update_layout(
        yaxis_range=[0,5],
        showlegend=False
    )

    st.plotly_chart(fig,use_container_width=True)

with col2:

    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
        r=[4.13,3.95,4.23],
        theta=[
            "Kemudahan Penggunaan",
            "Kualitas Sistem",
            "Efisiensi"
        ],
        fill="toself"
    ))

    radar.update_layout(
        title="Profil Variabel Penelitian",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,5]
            )
        ),
        showlegend=False
    )

    st.plotly_chart(radar,use_container_width=True)

# =====================================
# SMARTPLS + R²
# =====================================

col3,col4 = st.columns(2)

with col3:

    fig2 = px.bar(
        df_path,
        x="Hubungan",
        y="Koefisien",
        text="Koefisien",
        color="Hubungan",
        title="Path Coefficient SmartPLS"
    )

    fig2.update_layout(showlegend=False)

    st.plotly_chart(fig2,use_container_width=True)

with col4:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=60.5,
        title={"text":"Kekuatan Model (R²)"},
        gauge={
            "axis":{"range":[0,100]}
        }
    ))

    st.plotly_chart(gauge,use_container_width=True)

st.markdown("---")

# =====================================
# INSIGHT
# =====================================

st.subheader("📖 Insight Penelitian")

st.markdown("""
### Pengaruh Kemudahan Penggunaan terhadap Efisiensi

Kemudahan penggunaan memiliki pengaruh positif terhadap Efisiensi
dengan koefisien sebesar **0.13**.

### Pengaruh Kualitas Sistem terhadap Efisiensi

Kualitas sistem memiliki pengaruh terbesar terhadap Efisiensi
dengan koefisien sebesar **0.66**.

### Interpretasi R²

Nilai **R² sebesar 0.605** menunjukkan bahwa Kemudahan Penggunaan
dan Kualitas Sistem mampu menjelaskan **60.5% variasi Efisiensi**
penggunaan Mobile JKN.
""")

st.markdown("---")

# =====================================
# FOOTER
# =====================================

st.markdown("""
<div style='text-align:center;color:gray;'>

Mobile JKN Analytics Dashboard<br>
Penelitian PLS-SEM | Kabupaten Sumedang | 2026

</div>
""", unsafe_allow_html=True)