import streamlit as st

st.set_page_config(page_title="Prompt Generator Realistis", layout="centered")

st.title("🎨 Prompt Generator Ultra-Realistis")
st.markdown("Buat prompt gambar dengan mudah dan realistis untuk generator AI seperti DALL·E, Midjourney, atau Stable Diffusion.")

# --- Input data karakter
st.header("🧍 Karakter")

gender = st.selectbox("Jenis kelamin", ["Pria", "Wanita"])
usia = st.number_input("Usia", min_value=1, max_value=120, value=25)
tinggi = st.number_input("Tinggi badan (cm)", min_value=50, max_value=250, value=170)
berat = st.number_input("Berat badan (kg)", min_value=20, max_value=200, value=60)
kulit = st.text_input("Warna kulit", value="putih terang")
rambut = st.text_input("Gaya & warna rambut", value="hitam lurus dengan poni depan")
wajah = st.text_input("Detail wajah", value="muda, proporsi wajah halus, tanpa jerawat")
pakaian = st.text_input("Pakaian yang dikenakan", value="baju tradisional Bali")

# --- Input latar dan detail artistik
st.header("🌄 Latar & Gaya")

latar = st.text_input("Latar belakang", value="bangunan khas Bali")
gaya = st.text_input("Gaya visual", value="ultra realistic, cinematic lighting, 32k detail")
rasio = st.selectbox("Rasio gambar", ["9:16", "1:1", "16:9", "4:3"], index=0)

# --- Tombol hasilkan prompt
if st.button("🎬 Buat Prompt"):
    hasil = (
        f"A {gender.lower()} berusia {usia} tahun dengan tinggi {tinggi}cm dan berat {berat}kg, "
        f"berkulit {kulit}, rambut {rambut}, wajah {wajah}. "
        f"Mengenakan {pakaian}. "
        f"Berada di {latar}. "
        f"Gaya visual: {gaya}. Rasio gambar {rasio}."
    )
    
    st.subheader("📝 Prompt yang dihasilkan:")
    st.code(hasil, language="text")

    st.success("Salin prompt ini dan gunakan di aplikasi AI favoritmu!")
