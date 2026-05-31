import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Dashboard Analisis Mobile JKN",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

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

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="banner">

<h1>📊 Dashboard Analisis Mobile JKN Kabupaten Sumedang</h1>

<h4>
Analisis Pengaruh Kemudahan Penggunaan dan Kualitas Sistem
terhadap Efisiensi Penggunaan Mobile JKN Menggunakan PLS-SEM
</h4>

<p>
31 Responden | Kabupaten Sumedang | Tahun 2026
</p>

</div>
""", unsafe_allow_html=True)

# ==================================================
# DESKRIPSI
# ==================================================

st.info("""
Penelitian ini bertujuan menganalisis pengaruh Kemudahan Penggunaan dan
Kualitas Sistem terhadap Efisiensi penggunaan Mobile JKN menggunakan
metode Partial Least Square Structural Equation Modeling (PLS-SEM).

Jumlah responden dalam penelitian ini sebanyak 31 orang.
""")

# ==================================================
# KPI
# ==================================================

st.subheader("📈 Ringkasan Hasil Penelitian")

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.metric(
        "👥 Responden",
        "31 Orang"
    )

with c2:
    st.metric(
        "👍 Kemudahan Penggunaan",
        "4.13",
        "Tinggi"
    )

with c3:
    st.metric(
        "⚙️ Kualitas Sistem",
        "3.95",
        "Baik"
    )

with c4:
    st.metric(
        "⚡ Efisiensi",
        "4.23",
        "Sangat Tinggi"
    )

with c5:
    st.metric(
        "📊 R²",
        "60.5%",
        "Kuat"
    )

st.markdown("---")

# ==================================================
# TEMUAN UTAMA
# ==================================================

st.subheader("🎯 Temuan Utama")

a,b,c = st.columns(3)

with a:
    st.success("""
### Variabel Dominan

**Kualitas Sistem**

β = 0.66

Variabel yang memiliki pengaruh terbesar terhadap Efisiensi penggunaan Mobile JKN.
""")

with b:
    st.info("""
### Efisiensi Pengguna

**4.23**

Kategori Tinggi

Mayoritas responden merasa Mobile JKN membantu proses layanan kesehatan menjadi lebih efisien.
""")

with c:
    st.warning("""
### Kekuatan Model

**R² = 60.5%**

Model mampu menjelaskan 60.5% variasi Efisiensi penggunaan Mobile JKN.
""")

st.markdown("---")

# ==================================================
# PROFIL RESPONDEN
# ==================================================

st.subheader("👥 Profil Responden")

col1,col2 = st.columns(2)

with col1:

    gender = pd.DataFrame({
        "Jenis Kelamin":[
            "Perempuan",
            "Laki-laki"
        ],
        "Jumlah":[
            74.2,
            25.8
        ]
    })

    fig_gender = px.pie(
        gender,
        names="Jenis Kelamin",
        values="Jumlah",
        title="Komposisi Jenis Kelamin"
    )

    st.plotly_chart(
        fig_gender,
        use_container_width=True
    )

with col2:

    st.success("""
### Karakteristik Responden

- Perempuan : 74,2%
- Laki-laki : 25,8%
- Usia dominan : 17–25 tahun
- Profesi dominan : Pelajar/Mahasiswa
- Lama penggunaan dominan : 6 bulan–1 tahun

### Interpretasi

Mayoritas responden merupakan kelompok usia muda yang relatif familiar dengan teknologi digital. Hal ini menunjukkan bahwa Mobile JKN banyak digunakan oleh pengguna yang aktif memanfaatkan layanan berbasis aplikasi.
""")

st.markdown("---")

# ==================================================
# ANALISIS DESKRIPTIF
# ==================================================

st.subheader("📈 Analisis Deskriptif")

df_variabel = pd.DataFrame({
    "Variabel":[
        "Kemudahan Penggunaan",
        "Kualitas Sistem",
        "Efisiensi"
    ],
    "Nilai":[
        4.13,
        3.95,
        4.23
    ]
})

fig_desc = px.bar(
    df_variabel,
    x="Variabel",
    y="Nilai",
    text="Nilai",
    color="Variabel",
    title="Rata-rata Variabel Penelitian"
)

fig_desc.update_layout(
    yaxis_range=[0,5],
    showlegend=False
)

st.plotly_chart(
    fig_desc,
    use_container_width=True
)

st.info("""
Kemudahan Penggunaan memperoleh nilai rata-rata 4.13,
Kualitas Sistem sebesar 3.95, dan Efisiensi sebesar 4.23.

Hasil ini menunjukkan bahwa Efisiensi merupakan variabel dengan nilai tertinggi menurut persepsi responden.
""")

st.markdown("---")

# ==================================================
# VISUALISASI VARIABEL
# ==================================================

st.subheader("📊 Visualisasi Variabel Penelitian")

col3,col4 = st.columns(2)

with col3:

    fig_bar = px.bar(
        df_variabel,
        x="Variabel",
        y="Nilai",
        text="Nilai",
        color="Variabel",
        title="Perbandingan Variabel"
    )

    fig_bar.update_layout(
        yaxis_range=[0,5],
        showlegend=False
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

with col4:

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
        title="Radar Chart Variabel Penelitian",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,5]
            )
        ),
        showlegend=False
    )

    st.plotly_chart(
        radar,
        use_container_width=True
    )

st.markdown("---")

# ==================================================
# HASIL SMARTPLS
# ==================================================

st.subheader("🔬 Hasil SmartPLS")

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

col5,col6 = st.columns(2)

with col5:

    fig_path = px.bar(
        df_path,
        x="Hubungan",
        y="Koefisien",
        text="Koefisien",
        color="Hubungan",
        title="Path Coefficient"
    )

    fig_path.update_layout(
        showlegend=False
    )

    st.plotly_chart(
        fig_path,
        use_container_width=True
    )

with col6:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=60.5,
        title={"text":"Kekuatan Model (R²)"},
        gauge={
            "axis":{"range":[0,100]}
        }
    ))

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

st.markdown("""
### Interpretasi SmartPLS

- KP → EF = 0.13
- KS → EF = 0.66
- R² = 0.605

Kualitas Sistem memiliki pengaruh yang lebih kuat dibandingkan Kemudahan Penggunaan terhadap Efisiensi penggunaan Mobile JKN.
""")

st.markdown("---")

# ==================================================
# KESIMPULAN DAN IMPLIKASI
# ==================================================

st.subheader("📌 Kesimpulan dan Implikasi")

st.markdown("""
### Kesimpulan

1. Kemudahan Penggunaan berpengaruh positif terhadap Efisiensi.

2. Kualitas Sistem berpengaruh positif terhadap Efisiensi.

3. Kualitas Sistem merupakan variabel yang paling dominan.

4. Nilai R² sebesar 0.605 menunjukkan model memiliki kemampuan penjelasan yang cukup kuat.

### Implikasi

Peningkatan kualitas sistem Mobile JKN perlu menjadi prioritas karena memiliki kontribusi terbesar terhadap efisiensi penggunaan aplikasi.

Pengembangan sistem yang lebih stabil, cepat, dan mudah digunakan berpotensi meningkatkan pengalaman pengguna serta efisiensi layanan kesehatan digital.
""")

st.markdown("---")

# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div style='text-align:center;color:gray;'>

Dashboard Analisis Mobile JKN Kabupaten Sumedang<br>
Penelitian PLS-SEM | 2026

</div>
""", unsafe_allow_html=True)
