import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Konfigurasi Halaman & Tema Premium (Sesuai Struktur Asli Anda)
st.set_page_config(
    page_title="Script Generator AI",
    page_icon="🪄",
    layout="centered"
)

# Gaya CSS Kustom (Tetap mempertahankan format asli, hanya merapikan kotak hasil)
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
        color: #334155;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Mengambil API Key dari environment variable secara aman
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Catatan: Masukkan Gemini API Key Anda di sidebar jika belum di-deploy.")
    with st.sidebar:
        api_key = st.text_input("Gemini API Key", type="password")

# 3. Menampilkan Logo Resmi yang Sudah Di-upload
logo_path = "logo.png"
if not os.path.exists(logo_path):
    logo_path = "logo.jpg"

if os.path.exists(logo_path):
    col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
    with col_logo2:
        st.image(logo_path, use_container_width=True)
else:
    st.markdown("<h3 style='text-align: center; color: #b30000; letter-spacing: 2px;'>ARAYA CONSULTING</h3>", unsafe_allow_html=True)

# Header Judul Aplikasi
st.markdown("""
    <div style='text-align: center; padding-bottom: 10px;'>
        <h1 style='color: #1e1e1e; margin-top: 5px; font-weight: 800; font-size: 32px;'>🔮 Script Generator AI</h1>
        <p style='color: #666666; font-size: 15px; max-width: 500px; margin: 0 auto;'>
            Platform ceracik skrip video pendek viral untuk TikTok, Reels, dan Shorts dengan pendekatan psikologi audiens.
        </p>
    </div>
""", unsafe_allow_html=True)
st.write("---")

st.subheader("🎬 TikTok Viral Script AI")
st.caption("Lengkapi detail di bawah untuk menghasilkan skrip kustom ber-retensi tinggi.")

# 4. Form Input Terstruktur (100% Memanjang ke Bawah Sesuai Format Asli yang Anda Sukai)
brand = st.text_input("🏷️ Nama Brand / Usaha *wajib*", placeholder="e.g., Seblak Salah, Mie Judes, Araya Consulting...")
niche = st.text_input("🔮 Niche *wajib*", placeholder="e.g., Kuliner, Kecantikan, Finance, Otomotif...")
topic = st.text_input("💡 Topic / Produk *wajib*", placeholder="e.g., Menu pedas baru, Jualan online, Tips kepemimpinan...")
audience = st.text_input("👤 Target Audience *wajib*", placeholder="e.g., Pecinta pedas Lamongan, Gen Z, Pemilik bisnis...")

pain_point = st.text_input("🩸 Pain Point Audience (optional)", placeholder="e.g., Bingung cari makan siang, Pengen berkembang tapi sibuk...")
desire = st.text_input("💖 Desire / Hasrat Audience (optional)", placeholder="e.g., Pengen makan enak kenyang, Pengen jadi leader hebat...")

content_goal = st.selectbox(
    "📢 Content Goal",
    ["Soft Selling (Edukasi + Solusi)", "Hard Selling (Promo Langsung)", "Engagement (Interaksi Komen/Share)", "Brand Awareness"]
)

style = st.selectbox(
    "🎨 Style",
    ["Storytelling / POV (Point of View)", "Edukatif & Profesional", "Kasual / Santai Bicara Depan Kamera", "Komedi Ringan / Satir"]
)

description = st.text_area("📝 Deskripsi ide konten kamu (optional)", placeholder="Ceritakan konsep video kamu, pesan utama, atau hal spesifik yang mau disampaikan...")

# 5. Tombol Aksi & Logika Pemanggilan Gemini API dengan Sistem Dua Tab Output
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
                    "Anda adalah TikTok Viral Script AI dari Araya Consulting. Tugas Anda adalah menghasilkan output skrip dalam DUA FORMAT TERPISAH secara berurutan. "
                    "Gunakan penanda [FORMAT_HUMAN] untuk format pertama dan [FORMAT_AI_VIDEO] untuk format kedua.\n\n"
                    "Ketentuan [FORMAT_HUMAN]:\n"
                    "- Buat skrip kreatif durasi 30-60 detik yang memiliki retensi tinggi.\n"
                    "- Pisahkan jelas per adegan menggunakan struktur teks biasa yang mencantumkan [Visual/Aksi Kamera] dan [Audio/Narasi].\n"
                    "- Harus menyertakan HOOK kuat di awal, isi (BODY), dan Call to Action (CTA) yang jelas.\n\n"
                    "Ketentuan [FORMAT_AI_VIDEO]:\n"
                    "- Hanya berisi teks kalimat narasi/ucapan murni saja dari awal sampai akhir.\n"
                    "- JANGAN sertakan instruksi visual, jangan ada tanda kurung, jangan ada teks 'Hook', 'Visual', 'Audio', atau tanda baca pembatas adegan.\n"
                    "- Format ini harus berupa paragraf teks bersih yang siap di-copy paste langsung ke aplikasi AI Text-to-Video tanpa perlu diedit lagi oleh pengguna.\n\n"
                    "Gaya Bahasa untuk kedua format: Natural, santai, lugas khas praktisi Indonesia, persuasif, tidak kaku, dan tidak lebay."
                )
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.75,
                    ),
                )
                
                raw_text = response.text
                
                # Memisahkan hasil output berdasarkan tag penanda
                human_script = ""
                ai_script = ""
                
                if "[FORMAT_HUMAN]" in raw_text and "[FORMAT_AI_VIDEO]" in raw_text:
                    parts = raw_text.split("[FORMAT_AI_VIDEO]")
                    human_script = parts[0].replace("[FORMAT_HUMAN]", "").strip()
                    ai_script = parts[1].strip()
                else:
                    human_script = raw_text
                    ai_script = raw_text
                
                st.success("✨ Skrip Berhasil Dibuat!")
                
                # 6. Pembuatan Sistem Tab Tampilan Komponen yang Rapi di Bagian Bawah
                tab1, tab2 = st.tabs(["📋 1. Panduan Kreatif (Manusia)", "🤖 2. Narasi Murni (Siap Tempel ke AI Video)"])
                
                with tab1:
                    st.caption("Format terstruktur untuk dibaca langsung oleh Konten Kreator, Narator, atau Editor Video.")
                    st.markdown(f"""
                        <div class="result-box">
                            {human_script.replace('\n', '<br>')}
                        </div>
                    """, unsafe_allow_html=True)
                    st.write("")
                    st.text_area("⬇️ Salin Format Panduan Kreatif:", value=human_script, height=150, key="copy_human")
                
                with tab2:
                    st.caption("Format teks bersih tanpa instruksi kamera. Siap di-copy langsung ke CapCut AI atau web AI video generator.")
                    st.markdown(f"""
                        <div class="result-box" style="border-left-color: #10b981;">
                            {ai_script.replace('\n', '<br>')}
                        </div>
                    """, unsafe_allow_html=True)
                    st.write("")
                    st.text_area("📋 Blok & Salin Teks Murni Ini untuk AI Video Generator Anda:", value=ai_script, height=150, key="copy_ai")
                
            except Exception as e:
                st.error(f"Terjadi kesalahan pada sistem: {str(e)}")
