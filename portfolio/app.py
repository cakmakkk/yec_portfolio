import streamlit as st
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Yunus Emre Çakmak | Portfolio", layout="wide")
st.header("👨‍💻 Yunus Emre Çakmak")

# Sidebar
st.sidebar.title("Menü")
menu = st.sidebar.radio("Git:", ["Hakkımda", "Projeler"])

st.sidebar.markdown("---")
st.sidebar.markdown("**İletişim**")
st.sidebar.markdown("""
📧 emreyunuscakmakk4@gmail.com  
📱 +90 554 173 0459  
📍 Ankara, Yenimahalle  

[![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?style=flat&logo=github&logoColor=white&color=black)](https://github.com/cakmakkk)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0A66C2)](https://www.linkedin.com/in/yunus-emre-%C3%A7akmak-0a850b256/)
""")
with open("cv/YunusEmreCakmak_cvTrk.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.sidebar.download_button(label="📄 CV'yi İndir", data=PDFbyte, file_name="YunusEmreCakmak_cvTrk.pdf", mime='application/pdf')

st.sidebar.markdown("**Yetenekler**")
st.sidebar.markdown("""
- Python  
- C++  
- Java  
- Dart & Flutter  
- SQL  
- Git
""")

# --- HAKKIMDA --- #
if menu == "Hakkımda":
    col1, col2 = st.columns([1,6])
    with col1:
        st.image("photos/ves1.png", width=140)
    with col2:
        st.markdown("""
        Gazi Üniversitesi Bilgisayar Mühendisliği 3. sınıf öğrencisiyim.
        Aynı zamanda Anadolu Üniversitesi'nde açık öğretim olarak İşletme Yönetimi önlisans programına devam ediyorum.
        Yapay zeka, veri bilimi ve görüntü işleme alanlarında kendimi geliştiriyorum. 
        Python ve C++ dillerinde kendimi geliştirmeye devam edip NumPy,
        Pandas, TensorFlow, PyTorch ve Scikit-Learn kütüphaneleriyle de
        çalışıyorum. Ayrıca mobil geliştirme web alanında da çeşitli uygulamalar geliştirdim. Ekip çalışmasına
        yatkınlığım sayesinde yazılım projelerinde koordinasyon ve iletişim
        süreçlerinde aktif rol alıyorum. Sürekli öğrenme ve araştırma
        prensibimle teknik bilgi birikimimi artırmaya devam ediyorum.
        """)
    st.subheader("🎓 Eğitimler")
    st.markdown("""
    - Gazi Üniversitesi — Bilgisayar Mühendisliği (Lisans)
    - Anadolu Üniversitesi — İşletme Yönetimi (Açıköğretim, Önlisans)
    """)

    st.subheader("💼 Deneyimler")
    st.markdown("""
    - **Gazi Üniversitesi Ölçme ve Değerlendirme Merkezi** — Python Yazılım Geliştiricisi (Part-time)
    - **Mehmet Emin Resulzade Anadolu Lisesi** — Python Eğitmeni (10 Hafta)(Gönüllülük Esaslı Sosyal Sorumluluk Projesi)
    """)
    
    st.subheader("📜 Sertifikalar")
    st.markdown("""
    - Yapay Zeka Bootcamp — 60 saat — Pupilica
    - Python 401 — Turkcell Geleceği Yazanlar
    - OpenCV 501 — Turkcell Geleceği Yazanlar
    - A'dan Z'ye Yapay Zeka Eğitimi — Gazi Üni. Yapay Zeka Topluluğu
    """)

# --- PROJELER --- #
elif menu == "Projeler":
    st.title("📁 Projeler")

    projects = [
        {
            "title": "Araç Sayma ve Takip Uygulaması",
            "tools": "YOLOv8, OpenCV, ByteTrack",
            "desc": "Gerçek zamanlı araç sayımı ve takibi yaptım."
        },
        {
            "title": "CNN ile Beyin Tümörü Tespiti",
            "tools": "CNN, Python",
            "desc": "Görüntü sınıflandırma ile beyin tümörlerinin tespitini gerçekleştirdim."
        },
        {
            "title": "Coğrafi Bilgi Sistemi (GIS) Web Uygulaması",
            "tools": "Python, GeoPandas, Html/Css/Js, OpenStreetMap",
            "desc": "CSV dosyalarından koordinat bilgileri alarak nokta ve poligon haritaları oluşturan, konum verilerini görselleştiren bir web uygulaması geliştirdim."
        },
        {
            "title": "Mobil Sudoku Uygulaması",
            "tools": "Flutter, Firebase",
            "desc": "Gerçek zamanlı kullanıcı verisiyle çalışan Sudoku oyunu geliştirdim."
        },
        {
            "title": "Drone Tabanlı Nesne Takip Sistemi",
            "tools": "YOLOv8, OpenCV",
            "desc": "Drone görüntülerinden nesne takibi yaptım. Optik akışla hassasiyet artırıldı."
        },
        {
            "title": "Obezite Tahmini",
            "tools": "PCA, Makine Öğrenmesi",
            "desc": "Sınıflandırıcı algoritmalarla obezite tahmini yaptım."
        },        
        {
            "title": "Müşteri Segmentasyonu",
            "tools": "KMeans, Matplotlib",
            "desc": "Titanic veri seti üzerinde müşteri kümeleleri oluşturup görselleştirdim."
        },
        
    ]

    kategori = st.selectbox("📌 Kategoriye göre filtrele:", ["Tümü"] + [p["title"] for p in projects])

    for project in projects:
        if kategori != "Tümü" and kategori != project["title"]:
            continue

        with st.expander(project["title"]):
            st.markdown(f"**Kullanılan Teknolojiler:** {project['tools']}")
            st.markdown(f"{project['desc']}")

            if project["title"] == "Müşteri Segmentasyonu":
                st.subheader("📊 Kümeleme Görselleri")

                st.image("photos/must1.png", caption="Kümeleme Skorları", use_column_width=True)

                images = [
                    ("photos/must2.png", "PCA Görselleştirme"),
                    ("photos/must3.png", "t-SNE Görselleştirme"),
                    ("photos/must4.png", "SIBSP vs Cluster"),
                    ("photos/must5.png", "AGE vs Cluster"),
                    ("photos/must6.png", "FARE vs Cluster"),
                    ("photos/must7.png", "PCLASS vs Cluster"),
                ]

                for i in range(0, len(images), 3):
                    cols = st.columns(3)
                    for j in range(3):
                        if i + j < len(images):
                            with cols[j]:
                                img = Image.open(images[i + j][0])
                                img = img.resize((300, 300))
                                st.image(img, caption=images[i + j][1])

            if project["title"] == "Coğrafi Bilgi Sistemi (GIS) Web Uygulaması":
                st.image("photos/gis.png", caption="GIS Web Uygulaması Görseli", use_column_width=True)

            if project["title"] == "Obezite Tahmini":
                st.image("photos/obz1.png", caption="Obezite Tahmin Sonuçları", width=400)

            if project["title"] == "CNN ile Beyin Tümörü Tespiti":
                st.image("photos/mri1.png", caption="Beyin Tumor mri", width=400)

            if project["title"] == "Araç Sayma ve Takip Uygulaması":
                st.image("photos/obj1.png", caption="Car Detection", use_column_width=True)

            st.markdown("---")
