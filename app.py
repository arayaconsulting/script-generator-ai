import streamlit as st
from google import genai
from google.genai import types
import os

# Konfigurasi Halaman Dashboard
st.set_page_config(
    page_title="Script Generator AI",
    page_icon="🪄",
    layout="centered"
)

# Mengambil API Key dari environment variable secara aman
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Catatan: Masukkan Gemini API Key Anda di sidebar jika belum di-deploy.")
    with st.sidebar:
        api_key = st.text_input("Gemini API Key", type="password")

# Judul Utama Dashboard
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🔮 Script Generator AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Generate viral scripts for TikTok, Instagram Reels & YouTube Shorts with AI-powered precision.</p>", unsafe_allow_html=True)
st.write("---")

st.subheader("🎬 TikTok Viral Script AI")
st.caption("AI strategist untuk konten viral Indonesia 🇮🇩")

# Form Input Berdasarkan Desain Gambar (Sudah Ditambah Kolom Brand)
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

# Tombol Aksi & Logika Pemanggilan Gemini API
if st.button("🚀 Generate Viral Script", use_container_width=True):
    if not brand or not niche or not topic or not audience:
        st.error("Mohon isi kolom Brand, Niche, Topic, dan Target Audience terlebih dahulu!")
    elif not api_key:
        st.error("API Key belum dimasukkan!")
    else:
        with st.spinner("Sedang meracik skrip viral... Mohon tunggu..."):
            try:
                client = genai.Client(api_key=api_key)
                
                # Memasukkan variabel brand ke dalam prompt
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
                
                st.success("✨ Skrip Berhasil Dibuat!")
                st.markdown("### 📋 Hasil Skrip Konten")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan pada sistem: {str(e)}")
