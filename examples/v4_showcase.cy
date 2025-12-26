# CodingYok v4 Showcase - Fitur Baru
# Demonstrasi Lambda, Dict Comprehension, dan F-String

tulis("=" * 50)
tulis("🚀 CodingYok v4 - Fitur Baru!")
tulis("=" * 50)

# ============================================
# 1. LAMBDA (Fungsi Anonim)
# ============================================
tulis("\n📌 1. LAMBDA (Fungsi Anonim)")
tulis("-" * 30)

# Lambda sederhana
kali_dua = lambda x: x * 2
tulis(f"kali_dua(5) = {kali_dua(5)}")

# Lambda dengan multiple parameter
tambah = lambda a, b: a + b
tulis(f"tambah(3, 7) = {tambah(3, 7)}")

# Lambda tanpa parameter
salam = lambda: "Halo Dunia!"
tulis(f"salam() = {salam()}")

# Lambda dalam list
operasi = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
tulis(f"operasi[0](5) = {operasi[0](5)}")
tulis(f"operasi[1](5) = {operasi[1](5)}")
tulis(f"operasi[2](5) = {operasi[2](5)}")

# Lambda dengan map
angka = [1, 2, 3, 4, 5]
hasil_map = daftar(peta(lambda x: x * 3, angka))
tulis(f"peta(lambda x: x * 3, [1,2,3,4,5]) = {hasil_map}")

# Lambda dengan filter
genap = daftar(saring(lambda x: x % 2 == 0, angka))
tulis(f"saring(lambda x: x % 2 == 0, [1,2,3,4,5]) = {genap}")

# ============================================
# 2. DICTIONARY COMPREHENSION
# ============================================
tulis("\n📌 2. DICTIONARY COMPREHENSION")
tulis("-" * 30)

# Dict comprehension sederhana
kuadrat_dict = {x: x ** 2 untuk x dalam rentang(1, 6)}
tulis(f"{{x: x**2 untuk x dalam rentang(1,6)}} = {kuadrat_dict}")

# Dict comprehension dengan kondisi
genap_dict = {x: x * 2 untuk x dalam rentang(1, 11) jika x % 2 == 0}
tulis(f"Dict genap: {genap_dict}")

# Dict dari list
buah = ["apel", "jeruk", "mangga"]
panjang_buah = {b: panjang(b) untuk b dalam buah}
tulis(f"Panjang nama buah: {panjang_buah}")

# ============================================
# 3. F-STRING (String Interpolation)
# ============================================
tulis("\n📌 3. F-STRING (String Interpolation)")
tulis("-" * 30)

nama = "Budi"
umur = 25
kota = "Jakarta"

# F-string sederhana
tulis(f"Nama: {nama}, Umur: {umur}, Kota: {kota}")

# F-string dengan ekspresi
tulis(f"Tahun lahir: {2024 - umur}")
tulis(f"Umur 5 tahun lagi: {umur + 5}")

# F-string dengan method
pesan = "halo dunia"
tulis(f"Uppercase: {pesan.upper()}")

# F-string dengan list
nilai = [85, 90, 78, 92]
tulis(f"Nilai: {nilai}, Rata-rata: {jumlah(nilai) / panjang(nilai)}")

# F-string nested
items = ["buku", "pensil", "penghapus"]
tulis(f"Jumlah item: {panjang(items)}, Item pertama: {items[0]}")

# ============================================
# 4. SET (Himpunan)
# ============================================
tulis("\n📌 4. SET (Himpunan)")
tulis("-" * 30)

# Set literal
angka_set = {1, 2, 3, 4, 5}
tulis(f"Set angka: {angka_set}")

# Set dari list (menghilangkan duplikat)
duplikat = [1, 2, 2, 3, 3, 3, 4]
unik = {x untuk x dalam duplikat}
tulis(f"Set dari {duplikat} = {unik}")

# Set comprehension dengan kondisi
ganjil_set = {x untuk x dalam rentang(1, 11) jika x % 2 != 0}
tulis(f"Set ganjil 1-10: {ganjil_set}")

# ============================================
# 5. KOMBINASI FITUR
# ============================================
tulis("\n📌 5. KOMBINASI FITUR")
tulis("-" * 30)

# Lambda + Dict Comprehension
transform = lambda x: x ** 2 + 1
hasil_transform = {x: transform(x) untuk x dalam rentang(1, 6)}
tulis(f"Transform x**2+1: {hasil_transform}")

# F-string + Lambda
operasi_str = lambda op, a, b: f"{a} {op} {b} = {a + b jika op == '+' kalau_tidak a - b}"
tulis(operasi_str("+", 10, 5))
tulis(operasi_str("-", 10, 5))

# Dict comprehension + F-string
siswa = ["Andi", "Budi", "Citra"]
nilai_siswa = [85, 90, 78]
rapor = {siswa[i]: f"Nilai: {nilai_siswa[i]}" untuk i dalam rentang(panjang(siswa))}
tulis(f"Rapor: {rapor}")

tulis("\n" + "=" * 50)
tulis("✅ Semua fitur v4 berjalan dengan baik!")
tulis("=" * 50)
