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
tulis("Nama:", nama)
tulis("Umur:", umur, "tahun")
tulis("Tinggi:", tinggi, "cm")
status = "Menikah" jika sudah_menikah kalau_tidak "Belum Menikah"
tulis("Status:", status)

# Menampilkan tipe data
tulis("=== INFORMASI TIPE DATA ===")
tulis("Tipe nama:", tipe(nama))
tulis("Tipe umur:", tipe(umur))
tulis("Tipe tinggi:", tipe(tinggi))
tulis("Tipe hobi:", tipe(hobi))
tulis("Tipe profil:", tipe(profil))

# Operasi dengan variabel
tulis("=== OPERASI MATEMATIKA ===")
tahun_lahir = 2024 - umur
tulis("Tahun lahir:", tahun_lahir)

tinggi_meter = tinggi / 100
tulis("Tinggi dalam meter:", tinggi_meter)

# Bekerja dengan list
tulis("=== HOBI ===")
tulis("Jumlah hobi:", panjang(hobi))
untuk hobby dalam hobi:
    tulis("-", hobby)

# Menambah hobi baru
hobi.append("memasak")
tulis("Hobi setelah ditambah:", hobi)

# Bekerja dengan dictionary
tulis("=== PROFIL LENGKAP ===")
untuk kunci, nilai dalam profil.items():
    tulis(kunci + ":", nilai)
