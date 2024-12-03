import re
import streamlit as st

# Data prefix operator
operator_prefix = {
    "Telkomsel": ["0811", "0812", "0813", "0821", "0822", "0852", "0853"],
    "Indosat Ooredoo": ["0814", "0815", "0816", "0855", "0856", "0857", "0858"],
    "XL Axiata": ["0817", "0818", "0819", "0859", "0877", "0878"],
    "3": ["0895", "0896", "0897", "0898", "0899"],
    "Smartfren": ["0881", "0882", "0883", "0884", "0885", "0886", "0887", "0888", "0889"]
}

# Fungsi untuk memvalidasi nomor telepon
def validate_phone_number(number):
    # Pola untuk nomor telepon internasional
    pattern = r'^\+?62[-.\s]?\d{3,4}[-.\s]?\d{3,4}[-.\s]?\d{3,4}$'
    return re.match(pattern, number) is not None

# Fungsi untuk menentukan operator
def get_operator(number):
    # Hapus karakter selain angka
    cleaned_number = re.sub(r"[^\d]", "", number)
    
    # Pastikan nomor dimulai dengan +62 atau 62 atau 0
    if cleaned_number.startswith("62"):
        cleaned_number = "0" + cleaned_number[2:]
    elif cleaned_number.startswith("+62"):
        cleaned_number = "0" + cleaned_number[3:]
    
    # Ambil 4 digit pertama
    prefix = cleaned_number[:4]
    
    # Cari operator berdasarkan prefix
    for operator, prefixes in operator_prefix.items():
        if prefix in prefixes:
            return operator
    
    return "Tidak Diketahui"

# Judul aplikasi
st.title("Validasi Nomor Telepon dan Deteksi Operator")
st.write("Masukkan nomor telepon untuk memeriksa apakah valid atau tidak, serta mengetahui operatornya.")

# Input dari pengguna
number = st.text_input("Masukkan nomor telepon:")

# Tombol untuk memvalidasi dan mendeteksi operator
if st.button("Validasi"):
    if validate_phone_number(number):
        operator = get_operator(number)
        if operator != "Tidak Diketahui":
            st.success(f"'{number}' adalah nomor telepon yang Valid dan menggunakan operator **{operator}**.")
        else:
            st.warning(f"'{number}' adalah nomor telepon yang Valid, tetapi operator tidak dapat ditemukan.")
    else:
        st.error(f"'{number}' adalah nomor telepon yang Tidak Valid.")

# Catatan tambahan
st.info("Nomor telepon harus dalam format internasional dengan awalan +62 atau 62.")
