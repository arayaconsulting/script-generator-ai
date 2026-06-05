import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Konfigurasi Halaman & Tema Premium (Menggunakan Judul Araya Consulting)
st.set_page_config(
    page_title="Araya Consulting - Script Generator AI",
    page_icon="🔮",
    layout="centered"
)

# Gaya CSS Kustom untuk membuat tampilan sangat elegan dan bersih
st.markdown("""
    <style>
    /* Mengubah font utama dan background soft */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Desain Kotak Input */
    .stTextInput div div input, .stTextArea div div textarea {
        border-radius: 8px !important;
        border: 1px solid #e0e0e0 !important;
    }
    
    /* Desain Tombol Utama Premium Merah Gelap Elegan */
    .stButton>button {
        background: linear-gradient(135deg, #ff4b4b 0%, #b30000 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(211, 47, 47, 0.3) !important;
    }
    
    /* Kotak Hasil Skrip yang Elegan */
    .result-box {
        background-color: #f8f9fa;
        border-left: 5px solid #ff4b4b;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Mengambil API Key dari environment variable secara aman
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Catatan: Masukkan Gemini API Key Anda di sidebar jika belum di-deploy.")
    with st.sidebar:
        api_key = st.text_input("Gemini API Key", type="password")

# 3. Header Landing Page Elegan dengan Branding Araya Consulting
st.markdown("""
    <div style='text-align: center; padding-bottom: 10px;'>
        <p style='color: #888888; font-weight: bold; letter-spacing: 2px; margin-bottom: 0; font-size: 14px;'>ARAYA CONSULTING</p>
        <h1 style='color: #1e1e1e; margin-top: 5px; font-weight: 800; font-size: 32px;'>🔮 Script Generator AI</h1>
        <p style='color: #666666; font-size: 15px; max-width: 500px; margin: 0 auto;'>
            Platform cerdas peracik skrip video pendek viral untuk TikTok, Reels, dan Shorts dengan pendekatan psikologi audiens.
        </p>
    </div>
""", unsafe_allow_html=True)
st.write("---")

st.subheader("🎬 TikTok Viral Script AI")
st.caption("Lengkapi detail di bawah untuk menghasilkan skrip kustom ber-retensi tinggi.")

# 4. Form Input Terstruktur (Mempertahankan Struktur Kolom Anda)
brand = st.text_input("🏷️ Nama Brand / Usaha *wajib*", placeholder="e.g., Seblak Salah, Mie Judes, Araya Consulting...")
niche = st.text_input("🔮 Niche *wajib*", placeholder="e.g., Kuliner, Kecantikan, Finance, Otomotif...")
topic = st.text_input("💡 Topic / Produk *wajib*", placeholder="e.g., Menu pedas baru, Jualan online, Tips kepemimpinan...")
audience = st.text_input("👤 Target Audience *wajib*", placeholder="e.g., Pecinta pedas Lamongan, Gen Z, Pemilik bisnis...")

pain_point = st.text_input("🩸 Pain Point Audience (optional)", placeholder="e.g., Bingung cari makan siang, Pengen berkembang tapi sibuk...")
desire = st.text_input("💖 Desire / Hasrat Audience (optional)", placeholder="e.g., Pengen makan enak kenyang, Pengen jadi leader hebat...")

col1, col2 = st.columns(2)
with col1:
    content_goal = st.selectbox(
        "📢 Content Goal",
        ["Soft Selling (Edukasi + Solusi)", "Hard Selling (Promo Langsung)", "Engagement (Interaksi Komen/Share)", "Brand Awareness"]
    )
with col2:
    style = st.selectbox(
        "🎨 Style",
        ["Storytelling / POV (Point of View)", "Edukatif & Profesional", "Kasual / Santai Bicara Depan Kamera", "Komedi Ringan / Satir"]
    )

description = st.text_area("📝 Deskripsi ide konten kamu (optional)", placeholder="Ceritakan konsep video kamu, pesan utama, atau hal spesifik yang mau disampaikan...")

# 5. Tombol Aksi & Logika Pemanggilan Gemini API (Menggunakan Model Stabil)
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
                
                # Menampilkan Hasil dengan Desain Premium & Wadah Salin Instan
                st.success("✨ Skrip Berhasil Dibuat!")
                st.markdown("### 📋 Hasil Rekomendasi Skrip")
                
                st.markdown(f"""
                    <div class="result-box">
                        {response.text.replace('\n', '<br>')}
                    </div>
                """, unsafe_allow_html=True)
                
                # Mempermudah copy-paste langsung di tablet tanpa block manual
                st.write("")
                st.text_area("⬇️ Blok & Salin Teks Skrip di Bawah Ini:", value=response.text, height=180)
                st.caption("💡 Tips Praktis: Tahan atau ketuk dua kali di dalam kotak teks di atas untuk menyalin (*copy*) seluruh skrip ke CapCut tablet Anda.")
                
            except Exception as e:
                st.error(f"Terjadi kesalahan pada sistem: {str(e)}")
