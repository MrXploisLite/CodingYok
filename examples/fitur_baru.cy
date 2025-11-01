# ==========================================
# FITUR BARU CODINGYOK - VERSI 2.0
# ==========================================
# File ini mendemonstrasikan fitur-fitur baru yang ditambahkan:
# 1. List Comprehensions
# 2. Dictionary Comprehensions
# 3. Set Comprehensions
# 4. Generators dengan yield
# 5. Pattern Matching dengan cocokkan/kasus
# ==========================================

tulis("=" * 50)
tulis("FITUR BARU CODINGYOK v2.0")
tulis("=" * 50)
tulis()

# ==========================================
# 1. LIST COMPREHENSIONS
# ==========================================
tulis("1. LIST COMPREHENSIONS")
tulis("-" * 50)

# List comprehension sederhana
angka = [1, 2, 3, 4, 5]
kuadrat = [x * x untuk x dalam angka]
tulis(f"Angka: {angka}")
tulis(f"Kuadrat: {kuadrat}")
tulis()

# List comprehension dengan kondisi
genap = [x untuk x dalam angka jika x % 2 == 0]
tulis(f"Angka genap: {genap}")
tulis()

# List comprehension lebih kompleks
nama_panjang = ["Budi", "Siti", "Ahmad", "Sri", "Rudi"]
nama_panjang_filtered = [nama untuk nama dalam nama_panjang jika panjang(nama) > 3]
tulis(f"Nama dengan lebih dari 3 huruf: {nama_panjang_filtered}")
tulis()

# ==========================================
# 2. DICTIONARY COMPREHENSIONS
# ==========================================
tulis("2. DICTIONARY COMPREHENSIONS")
tulis("-" * 50)

# Dict comprehension sederhana
angka_dict = {x: x * x untuk x dalam rentang(1, 6)}
tulis(f"Dictionary kuadrat: {angka_dict}")
tulis()

# Dict comprehension dengan kondisi
angka_ganjil_dict = {x: x * x untuk x dalam rentang(1, 10) jika x % 2 != 0}
tulis(f"Dictionary kuadrat angka ganjil: {angka_ganjil_dict}")
tulis()

# Membuat dictionary dari dua list
nama = ["Budi", "Siti", "Ahmad"]
umur = [25, 23, 28]
data_combined = [{"nama": n, "umur": u} untuk n, u dalam zip(nama, umur)]
tulis(f"Data gabungan: {data_combined}")
tulis()

# ==========================================
# 3. SET COMPREHENSIONS
# ==========================================
tulis("3. SET COMPREHENSIONS")
tulis("-" * 50)

# Set comprehension (otomatis menghilangkan duplikat)
angka_dengan_duplikat = [1, 2, 2, 3, 3, 4, 4, 5]
set_unik = {x untuk x dalam angka_dengan_duplikat}
tulis(f"Angka dengan duplikat: {angka_dengan_duplikat}")
tulis(f"Set unik: {set_unik}")
tulis()

# Set comprehension dengan kondisi
set_genap = {x untuk x dalam rentang(1, 20) jika x % 2 == 0}
tulis(f"Set angka genap (1-20): {set_genap}")
tulis()

# ==========================================
# 4. GENERATORS DENGAN YIELD
# ==========================================
tulis("4. GENERATORS DENGAN YIELD")
tulis("-" * 50)

# Generator sederhana untuk bilangan Fibonacci
fungsi fibonacci(n):
    a = 0
    b = 1
    counter = 0
    selama counter < n:
        hasilkan a
        temp = a
        a = b
        b = temp + b
        counter += 1

tulis("10 bilangan Fibonacci pertama:")
untuk angka dalam fibonacci(10):
    tulis(angka)
tulis()

# Generator untuk angka genap
fungsi genap_generator(mulai, akhir):
    untuk i dalam rentang(mulai, akhir):
        jika i % 2 == 0:
            hasilkan i

tulis("Angka genap dari 0 sampai 20:")
untuk angka dalam genap_generator(0, 21):
    tulis(angka)
tulis()

# Generator dengan transformasi
fungsi kuadrat_generator(numbers):
    untuk n dalam numbers:
        hasilkan n * n

angka_list = [1, 2, 3, 4, 5]
tulis("Kuadrat dari angka menggunakan generator:")
untuk k dalam kuadrat_generator(angka_list):
    tulis(k)
tulis()

# ==========================================
# 5. PATTERN MATCHING (COCOKKAN/KASUS)
# ==========================================
tulis("5. PATTERN MATCHING")
tulis("-" * 50)

# Pattern matching sederhana dengan angka
fungsi cek_kategori_angka(angka):
    cocokkan angka:
        kasus 0:
            tulis("Ini adalah nol")
        kasus 1:
            tulis("Ini adalah satu")
        kasus 2:
            tulis("Ini adalah dua")
        kasus _:
            tulis(f"Ini adalah angka lain: {angka}")

tulis("Testing pattern matching dengan angka:")
cek_kategori_angka(0)
cek_kategori_angka(1)
cek_kategori_angka(5)
tulis()

# Pattern matching dengan string
fungsi sapa_berdasarkan_bahasa(bahasa):
    cocokkan bahasa:
        kasus "indonesia":
            tulis("Halo!")
        kasus "english":
            tulis("Hello!")
        kasus "spanish":
            tulis("Hola!")
        kasus _:
            tulis("Hi there!")

tulis("Testing pattern matching dengan string:")
sapa_berdasarkan_bahasa("indonesia")
sapa_berdasarkan_bahasa("english")
sapa_berdasarkan_bahasa("french")
tulis()

# Pattern matching dengan guard condition
fungsi kategori_nilai(nilai):
    cocokkan nilai:
        kasus _ jika nilai >= 90:
            kembalikan "A - Sangat Baik"
        kasus _ jika nilai >= 80:
            kembalikan "B - Baik"
        kasus _ jika nilai >= 70:
            kembalikan "C - Cukup"
        kasus _ jika nilai >= 60:
            kembalikan "D - Kurang"
        kasus _:
            kembalikan "E - Gagal"

tulis("Testing pattern matching dengan guard conditions:")
nilai_list = [95, 85, 75, 65, 55]
untuk n dalam nilai_list:
    hasil = kategori_nilai(n)
    tulis(f"Nilai {n}: {hasil}")
tulis()

# ==========================================
# KOMBINASI FITUR
# ==========================================
tulis("6. KOMBINASI FITUR BARU")
tulis("-" * 50)

# Generator + Comprehension
fungsi range_generator(n):
    untuk i dalam rentang(n):
        hasilkan i

hasil = [x * 2 untuk x dalam range_generator(5)]
tulis(f"Generator + Comprehension: {hasil}")
tulis()

# Pattern matching + Comprehension
fungsi proses_data(items):
    hasil = []
    untuk item dalam items:
        cocokkan item:
            kasus _ jika item < 0:
                hasil.append("negatif")
            kasus 0:
                hasil.append("nol")
            kasus _:
                hasil.append("positif")
    kembalikan hasil

data = [-5, 0, 3, -2, 10]
hasil_kategori = proses_data(data)
tulis(f"Data: {data}")
tulis(f"Kategori: {hasil_kategori}")
tulis()

# ==========================================
# CONTOH PRAKTIS
# ==========================================
tulis("7. CONTOH PRAKTIS")
tulis("-" * 50)

# Membersihkan dan memproses data
data_kotor = [1, 2, kosong, 3, kosong, 4, 5]
data_bersih = [x untuk x dalam data_kotor jika x != kosong]
tulis(f"Data kotor: {data_kotor}")
tulis(f"Data bersih: {data_bersih}")
tulis()

# Membuat lookup dictionary
produk = ["Laptop", "Mouse", "Keyboard", "Monitor"]
harga = [10000000, 150000, 500000, 3000000]
katalog = {p: h untuk p, h dalam zip(produk, harga)}
tulis("Katalog produk:")
untuk nama, harga dalam katalog.items():
    tulis(f"  {nama}: {format_rupiah(harga)}")
tulis()

# Generator untuk membaca data besar (simulasi)
fungsi baca_data_besar(jumlah):
    untuk i dalam rentang(jumlah):
        hasilkan {"id": i, "nilai": i * 100}

tulis("Membaca 5 item pertama dari data besar:")
counter = 0
untuk item dalam baca_data_besar(1000):
    tulis(f"  ID: {item['id']}, Nilai: {item['nilai']}")
    counter += 1
    jika counter >= 5:
        berhenti
tulis()

tulis("=" * 50)
tulis("SELESAI - Semua fitur baru telah didemonstrasikan!")
tulis("=" * 50)
