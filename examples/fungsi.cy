# Contoh penggunaan fungsi dalam CodingYok
# File: fungsi.cy

tulis("=== CONTOH FUNGSI CODINGYOK ===\n")

# Fungsi sederhana tanpa parameter
fungsi sapa():
    tulis("Halo! Selamat datang di CodingYok!")

# Fungsi dengan parameter
fungsi sapa_nama(nama):
    tulis(f"Halo {nama}! Senang bertemu dengan Anda.")

# Fungsi dengan parameter default
fungsi perkenalan(nama, umur=20, kota="Jakarta"):
    tulis(f"Nama saya {nama}, umur {umur} tahun, tinggal di {kota}.")

# Fungsi yang mengembalikan nilai
fungsi tambah(a, b):
    hasil = a + b
    kembalikan hasil

# Fungsi matematika
fungsi luas_persegi_panjang(panjang, lebar):
    kembalikan panjang * lebar

fungsi luas_lingkaran(radius):
    kembalikan PI * radius * radius

# Fungsi dengan logika kondisional
fungsi cek_ganjil_genap(angka):
    jika angka % 2 == 0:
        kembalikan "genap"
    kalau_tidak:
        kembalikan "ganjil"

# Fungsi rekursif
fungsi faktorial(n):
    jika n <= 1:
        kembalikan 1
    kalau_tidak:
        kembalikan n * faktorial(n - 1)

# Fungsi untuk bekerja dengan list
fungsi cari_maksimum(daftar_angka):
    jika panjang(daftar_angka) == 0:
        kembalikan kosong
    
    maks = daftar_angka[0]
    untuk angka dalam daftar_angka:
        jika angka > maks:
            maks = angka
    kembalikan maks

# Fungsi untuk validasi
fungsi validasi_email(email):
    jika "@" dalam email dan "." dalam email:
        kembalikan benar
    kalau_tidak:
        kembalikan salah

# Fungsi dengan multiple return values (menggunakan list)
fungsi statistik_dasar(angka_list):
    jika panjang(angka_list) == 0:
        kembalikan [0, 0, 0]  # min, max, rata-rata
    
    minimum_val = minimum(angka_list)
    maksimum_val = maksimum(angka_list)
    rata_rata = jumlah(angka_list) / panjang(angka_list)
    
    kembalikan [minimum_val, maksimum_val, rata_rata]

# Testing semua fungsi
tulis("1. FUNGSI SEDERHANA")
sapa()
sapa_nama("Budi")
perkenalan("Siti", 25, "Bandung")
perkenalan("Ahmad")  # Menggunakan default values

tulis("\n2. FUNGSI DENGAN RETURN VALUE")
hasil_tambah = tambah(15, 25)
tulis(f"15 + 25 = {hasil_tambah}")

luas_pp = luas_persegi_panjang(10, 5)
tulis(f"Luas persegi panjang (10x5): {luas_pp}")

luas_l = luas_lingkaran(7)
tulis(f"Luas lingkaran (r=7): {bulat(luas_l, 2)}")

tulis("\n3. FUNGSI KONDISIONAL")
untuk angka dalam [4, 7, 12, 15]:
    jenis = cek_ganjil_genap(angka)
    tulis(f"Angka {angka} adalah {jenis}")

tulis("\n4. FUNGSI REKURSIF")
untuk n dalam [3, 5, 6]:
    hasil_faktorial = faktorial(n)
    tulis(f"Faktorial {n} = {hasil_faktorial}")

tulis("\n5. FUNGSI DENGAN LIST")
data_angka = [3, 7, 2, 9, 1, 8, 5]
maks_angka = cari_maksimum(data_angka)
tulis(f"Data: {data_angka}")
tulis(f"Nilai maksimum: {maks_angka}")

tulis("\n6. FUNGSI VALIDASI")
email_list = ["user@example.com", "invalid-email", "test@domain.org"]
untuk email dalam email_list:
    valid = validasi_email(email)
    status = "valid" jika valid kalau_tidak "tidak valid"
    tulis(f"Email '{email}' adalah {status}")

tulis("\n7. FUNGSI DENGAN MULTIPLE RETURNS")
data_test = [10, 5, 8, 12, 3, 15, 7]
min_val, max_val, avg_val = statistik_dasar(data_test)
tulis(f"Data: {data_test}")
tulis(f"Minimum: {min_val}")
tulis(f"Maksimum: {max_val}")
tulis(f"Rata-rata: {bulat(avg_val, 2)}")

# Fungsi sebagai parameter (higher-order function concept)
fungsi terapkan_operasi(daftar, operasi_func):
    hasil = []
    untuk item dalam daftar:
        hasil.append(operasi_func(item))
    kembalikan hasil

fungsi kuadrat(x):
    kembalikan x * x

fungsi kali_dua(x):
    kembalikan x * 2

tulis("\n8. FUNGSI SEBAGAI PARAMETER")
angka_awal = [1, 2, 3, 4, 5]
hasil_kuadrat = terapkan_operasi(angka_awal, kuadrat)
hasil_kali_dua = terapkan_operasi(angka_awal, kali_dua)

tulis(f"Angka awal: {angka_awal}")
tulis(f"Hasil kuadrat: {hasil_kuadrat}")
tulis(f"Hasil kali dua: {hasil_kali_dua}")

tulis("\n=== SELESAI ===")
