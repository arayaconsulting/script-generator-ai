import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Konfigurasi Halaman Premium
st.set_page_config(
    page_title="Araya Consulting - Script Generator AI",
    page_icon="🔮",
    layout="centered"
)

# Gaya CSS Premium untuk merombak total tampilan agar sangat elegan
st.markdown("""
    <style>
    /* Mengubah font utama menjadi modern dan bersih */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: #fcfcfc;
    }
    
    /* Mengubah desain kotak input teks dan area teks */
    .stTextInput div div input, .stTextArea div div textarea, .stSelectbox div div div {
        border-radius: 10px !important;
        border: 1px solid #e2e8f0 !important;
        padding: 10px 14px !important;
        background-color: #ffffff !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02) !important;
        transition: all 0.2s ease-in-out !important;
    }
    
    /* Efek fokus saat kolom input diklik */
    .stTextInput div div input:focus, .stTextArea div div textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
    }
    
    /* Tombol Utama Premium (Menggunakan Gradasi Biru-Tua Menyesuaikan Logo Anda) */
    .stButton>button {
        background: linear-gradient(135deg, #1e40af 0%, #0f172a 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 14px 28px !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06) !important;
        transition: all 0.25s ease !important;
        margin-top: 15px;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(30, 64, 175, 0.3) !important;
    }
    
    /* Kotak Hasil Review Skrip Kustom */
    .result-box {
        background-color: #ffffff;
        border-left: 5px solid #1e40af;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-top: 25px;
        color: #334155;
        line-height: 1.6;
    }
    
    /* Merapikan label input */
    label {
        font-weight: 600 !important;
        color: #475569 !important;
        margin-bottom: 6px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Manajemen Akses API Key Aman
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Catatan: Masukkan Gemini API Key Anda di sidebar jika belum di-deploy.")
    with st.sidebar:
        api_key = st.text_input("Gemini API Key", type="password")

# 3. Struktur Header Elegan & Dinamis (Membaca logo yang Anda upload di image_25.png)
logo_path = "logo.png"
if not os.path.exists(logo_path):
    logo_path = "logo.jpg"

if os.path.exists(logo_path):
    # Pengaturan kolom agar ukuran logo simetris di tengah halaman tablet
    col_logo1, col_logo2, col_logo3 = st.columns([1, 1.8, 1])
    with col_logo2:
        st.image(logo_path, use_container_width=True)

# Sub-judul deskriptif dengan tipografi elegan yang rapi
st.markdown("""
    <div style='text-align: center; margin-top: 15px; margin-bottom: 25px;'>
        <h2 style='color: #0f172a; font-weight: 800; font-size: 28px; margin-bottom: 8px;'>🔮 Script Generator AI</h2>
        <p style='color: #64748b; font-size: 15px; max-width: 540px; margin: 0 auto; line-height: 1.5;'>
            Platform cerdas peracik skrip video pendek viral untuk TikTok, Reels, dan Shorts dengan pendekatan psikologi audiens.
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 4. Formulir Formula Konten Terstruktur (Dibuat Grid Baris Berdampingan Agar Elegan)
st.markdown("#### 🎬 Formula Konten Rencana")
st.caption("Isi parameter di bawah untuk menghasilkan skrip kustom dengan tingkat retensi tinggi.")
st.write("")

# Baris 1: Brand & Niche berdampingan
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    brand = st.text_input("🏷️ Nama Brand / Usaha *wajib*", placeholder="e.g., Seblak Salah, Mie Judes")
with row1_col2:
    niche = st.text_input("🔮 Niche *wajib*", placeholder="e.g., Kuliner, Otomotif, Mentorship")

# Baris 2: Topik & Target Audience berdampingan
row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    topic = st.text_input("💡 Topic / Produk *wajib*", placeholder="e.g., Menu pedas baru, Tips bisnis")
with row2_col2:
    audience = st.text_input("👤 Target Audience *wajib*", placeholder="e.g., Pecinta pedas Lamongan, Pemilik bisnis")

# Baris 3: Fitur Psikologi (Pain & Desire) berdampingan
row3_col1, row3_col2 = st.columns(2)
with row3_col1:
    pain_point = st.text_input("🩸 Pain Point Audience (optional)", placeholder="e.g., Bingung cari makan siang, Takut gagal")
with row3_col2:
    desire = st.text_input("💖 Desire / Hasrat Audience (optional)", placeholder="e.g., Pengen kenyang hemat, Pengen tim otomatis")

# Baris 4: Pengaturan Goal & Gaya Bahasa berdampingan
row4_col1, row4_col2 = st.columns(2)
with row4_col1:
    content_goal = st.selectbox(
        "📢 Content Goal",
        ["Soft Selling (Edukasi + Solusi)", "Hard Selling (Promo Langsung)", "Engagement (Interaksi Komen/Share)", "Brand Awareness"]
    )
with row4_col2:
    style = st.selectbox(
        "🎨 Style",
        ["Storytelling / POV (Point of View)", "Edukatif & Profesional", "Kasual / Santai Bicara Depan Kamera", "Komedi Ringan / Satir"]
    )

# Baris 5: Deskripsi Tambahan lebar penuh
description = st.text_area("📝 Deskripsi ide konten kamu (optional)", placeholder="Ceritakan konsep video kamu, pesan utama, atau hal spesifik yang mau disampaikan...")

st.write("")

# 5. Tombol Aksi Premium & Logika Integrasi Gemini API
if st.button("🚀 RACIK SKRIP VIRAL SEKARANG", use_container_width=True):
    if not brand or not niche or not topic or not audience:
        st.error("Mohon isi kolom Brand, Niche, Topic, dan Target Audience terlebih dahulu!")
    elif not api_key:
        st.error("API Key belum dimasukkan!")
    else:
        with st.spinner("Sistem Araya AI sedang merancang skrip terbaik untuk Anda..."):
            try:
                client = genai.Client(api_key=api_key)
                
                prompt = f"""
                Hasilkan skrip video pendek viral berdasarkan data berikut:
                - Nama Brand/Usaha: {brand}
                - Niche: {niche}
                - Topik/Produk: {topic}
                - Target Audiens: {audience}
                - Masalah Utama (Pain Point): {pain_point if pain_point else 'Tidak ditentukan'}
                - Keinginan Terbesar (Desire): {desire if desire else 'Tidak ditentukan'}
                - Goal Konten: {content_goal}
                - Gaya Bahasa/Style: {style}
                - Deskripsi Tambahan: {description if description else 'Tidak ada'}
                """
                
                system_instruction = (
                    "Anda adalah TikTok Viral Script AI, seorang AI strategist ulung untuk konten viral di Indonesia. "
                    "Tugas Anda adalah membuat skrip video pendek berdurasi 30-60 detik yang memiliki retensi tinggi. "
                    "Skrip harus dipisahkan dengan jelas menjadi kolom [Visual/Aksi Kamera] dan [Audio/Narasi].\n"
                    "Wajib menyertakan HOOK kuat di 3 detik pertama, isi (BODY) yang mengalir, dan Call to Action (CTA) yang sesuai dengan goal.\n"
                    "PENTING: Integrasikan nama Brand yang diberikan secara natural ke dalam narasi/audio (misalnya disebut di awal sebagai bagian dari solusi, atau di akhir sebagai bagian dari CTA).\n"
                    "Gunakan gaya bahasa natural, kasual/santai (gunakan saya/kamu jika relevan), scannable, tidak kaku, dan hindari kata-kata berlebihan (lebay)."
                )
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.75,
                    ),
                )
                
                st.success("✨ Skrip Berhasil Dirakit!")
                st.markdown("### 📋 Hasil Rekomendasi Skrip")
                
                # Kontainer keluaran hasil skrip premium menggunakan gaya CSS kustom
                st.markdown(f"""
                    <div class="result-box">
                        {response.text.replace('\n', '<br>')}
                    </div>
                """, unsafe_allow_html=True)
                
                # Kotak ekstraksi instan untuk kemudahan copy-paste di tablet tanpa ribet
                st.write("")
                st.text_area("⬇️ Blok & Salin Teks Skrip di Bawah Ini:", value=response.text, height=180)
                st.caption("💡 Tips Praktis: Tahan atau ketuk dua kali di dalam kotak teks di atas untuk menyalin (*copy*) seluruh skrip langsung ke CapCut tablet Anda.")
                
            except Exception as e:
                st.error(f"Terjadi kesalahan pada sistem: {str(e)}")
