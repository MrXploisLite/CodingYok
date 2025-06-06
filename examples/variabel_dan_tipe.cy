# Contoh penggunaan variabel dan tipe data
# File: variabel_dan_tipe.cy

# Variabel dengan berbagai tipe data
nama = "Budi Santoso"
umur = 25
tinggi = 175.5
sudah_menikah = salah
hobi = ["membaca", "coding", "traveling"]
profil = {
    "nama": nama,
    "umur": umur,
    "kota": "Jakarta"
}

# Menampilkan informasi
tulis("=== PROFIL PENGGUNA ===")
tulis(f"Nama: {nama}")
tulis(f"Umur: {umur} tahun")
tulis(f"Tinggi: {tinggi} cm")
tulis(f"Status: {'Menikah' jika sudah_menikah kalau_tidak 'Belum Menikah'}")

# Menampilkan tipe data
tulis("\n=== INFORMASI TIPE DATA ===")
tulis(f"Tipe nama: {tipe(nama)}")
tulis(f"Tipe umur: {tipe(umur)}")
tulis(f"Tipe tinggi: {tipe(tinggi)}")
tulis(f"Tipe hobi: {tipe(hobi)}")
tulis(f"Tipe profil: {tipe(profil)}")

# Operasi dengan variabel
tulis("\n=== OPERASI MATEMATIKA ===")
tahun_lahir = 2024 - umur
tulis(f"Tahun lahir: {tahun_lahir}")

tinggi_meter = tinggi / 100
tulis(f"Tinggi dalam meter: {tinggi_meter}")

# Bekerja dengan list
tulis("\n=== HOBI ===")
tulis(f"Jumlah hobi: {panjang(hobi)}")
untuk hobby dalam hobi:
    tulis(f"- {hobby}")

# Menambah hobi baru
hobi.append("memasak")
tulis(f"Hobi setelah ditambah: {hobi}")

# Bekerja dengan dictionary
tulis("\n=== PROFIL LENGKAP ===")
untuk kunci, nilai dalam profil.items():
    tulis(f"{kunci}: {nilai}")
