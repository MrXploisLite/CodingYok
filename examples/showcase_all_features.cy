# Showcase semua fitur advanced CodingYok
# File: showcase_all_features.cy

tulis("🚀 SHOWCASE FITUR ADVANCED CODINGYOK 🚀")
tulis("=" * 50)

# 1. KELAS DAN INHERITANCE
tulis("\n1. 🏗️ SISTEM KELAS DAN INHERITANCE")

kelas Kendaraan:
    fungsi __init__(diri, merk, tahun):
        diri.merk = merk
        diri.tahun = tahun
        diri.kecepatan = 0
    
    fungsi info(diri):
        tulis(str(diri.kecepatan)
    
    fungsi gas(diri, tambah_kecepatan):
        diri.kecepatan += tambah_kecepatan
        tulis(str(diri.kecepatan)

kelas Mobil(Kendaraan):
    fungsi __init__(diri, merk, tahun, jenis_bahan_bakar):
        diri.merk = merk
        diri.tahun = tahun
        diri.kecepatan = 0
        diri.jenis_bahan_bakar = jenis_bahan_bakar
        diri.pintu = 4
    
    fungsi klakson(diri):
        tulis(str(diri.merk)
    
    fungsi info(diri):
        tulis(str(diri.jenis_bahan_bakar)
        tulis(str(diri.kecepatan)

kelas Motor(Kendaraan):
    fungsi klakson(diri):
        tulis(str(diri.merk)

# Test kelas
mobil = Mobil("Toyota Avanza", 2020, "Bensin")
motor = Motor("Honda Beat", 2019)

mobil.info()
mobil.gas(60)
mobil.klakson()

motor.info()
motor.gas(40)
motor.klakson()

# 2. FITUR INDONESIA ADVANCED
tulis("\n2. 🇮🇩 FITUR KHUSUS INDONESIA")

# Aplikasi Keuangan Indonesia
kelas RekeningBank:
    fungsi __init__(diri, nama_pemilik, saldo_awal=0):
        diri.nama = nama_pemilik
        diri.saldo = saldo_awal
        diri.riwayat = []
        diri.tanggal_buka = tanggal_indonesia()
    
    fungsi setor(diri, jumlah):
        diri.saldo += jumlah
        transaksi = f"Setor {format_rupiah(jumlah)} - {tanggal_indonesia()}"
        diri.riwayat.append(transaksi)
        tulis(str(transaksi)
        tulis(str(format_rupiah(diri.saldo))
    
    fungsi tarik(diri, jumlah):
        jika jumlah <= diri.saldo:
            diri.saldo -= jumlah
            transaksi = f"Tarik {format_rupiah(jumlah)} - {tanggal_indonesia()}"
            diri.riwayat.append(transaksi)
            tulis(str(transaksi)
            tulis(str(format_rupiah(diri.saldo))
            kembalikan benar
        kalau_tidak:
            tulis(str(format_rupiah(diri.saldo))
            kembalikan salah
    
    fungsi info_rekening(diri):
        tulis("\n📊 INFO REKENING"
        tulis(str(diri.nama)
        tulis(str(format_rupiah(diri.saldo))
        tulis(str(angka_ke_kata(int(diri.saldo)))
        tulis(str(diri.tanggal_buka)
        tulis(str(panjang(diri.riwayat))

# Test rekening bank
rekening = RekeningBank("Budi Santoso", 5000000)
rekening.setor(2500000)
rekening.tarik(1000000)
rekening.info_rekening()

# Data regional Indonesia
tulis("\n🗺️ DATA REGIONAL INDONESIA"
provinsi_favorit = ["jakarta", "jabar", "jateng", "jatim", "bali"]
tulis("Provinsi favorit:")
untuk kode dalam provinsi_favorit:
    nama_lengkap = cek_provinsi(kode)
    tulis(str(nama_lengkap)

tulis(str(', '.join(daftar_kota_besar()[:5]))

# Validasi data Indonesia
tulis("\n✅ VALIDASI DATA INDONESIA"
data_test = [
    ("NIK", "1234567890123456", validasi_nik("1234567890123456")),
    ("Email", "user@example.com", validasi_email("user@example.com")),
    ("URL", "https://codingyok.id", validasi_url("https://codingyok.id")),
]

untuk jenis, data, valid dalam data_test:
    status = "✅ Valid" jika valid kalau_tidak "❌ Tidak Valid"
    tulis(str(status)

# Format nomor telepon
nomor_test = ["081234567890", "6281234567890", "021-12345678"]
tulis("\n📞 FORMAT NOMOR TELEPON"
untuk nomor dalam nomor_test:
    formatted = format_nomor_telepon(nomor)
    tulis(str(formatted)

# 3. FILE I/O DAN DATA PROCESSING
tulis("\n3. 📁 FILE I/O DAN DATA PROCESSING")

# Buat data mahasiswa
data_mahasiswa = [
    {"nama": "Ahmad Fauzi", "nim": "12345678", "ipk": 3.75, "jurusan": "Teknik Informatika"},
    {"nama": "Siti Nurhaliza", "nim": "12345679", "ipk": 3.85, "jurusan": "Sistem Informasi"},
    {"nama": "Budi Santoso", "nim": "12345680", "ipk": 3.60, "jurusan": "Teknik Komputer"},
    {"nama": "Dewi Sartika", "nim": "12345681", "ipk": 3.90, "jurusan": "Manajemen Informatika"},
]

# Simpan ke JSON
tulis_json("mahasiswa.json", data_mahasiswa)
tulis("✅ Data mahasiswa disimpan ke mahasiswa.json")

# Baca dan analisis
loaded_data = baca_json("mahasiswa.json")
tulis(str(panjang(loaded_data))

# Hitung statistik IPK
ipk_list = []
untuk mhs dalam loaded_data:
    ipk_list.append(mhs["ipk"])

stats = hitung_statistik(ipk_list)
tulis("\n📈 STATISTIK IPK:"
tulis(str(bulat(stats['rata_rata'], 2))
tulis(str(stats['maksimum'])
tulis(str(stats['minimum'])
tulis(str(stats['median'])

# Buat CSV untuk laporan
csv_data = [["Nama", "NIM", "IPK", "Jurusan"]]
untuk mhs dalam loaded_data:
    csv_data.append([mhs["nama"], mhs["nim"], str(mhs["ipk"]), mhs["jurusan"]])

tulis_csv("laporan_mahasiswa.csv", csv_data)
tulis("✅ Laporan CSV dibuat")

# Tampilkan sebagai tabel
tulis("\n📋 TABEL MAHASISWA:"
cetak_tabel(csv_data[1:], csv_data[0])

# 4. PATTERN MATCHING DAN TEXT PROCESSING
tulis("\n4. 🔍 PATTERN MATCHING DAN TEXT PROCESSING")

# Data teks campuran
teks_data = """
Kontak Mahasiswa:
Ahmad Fauzi - Email: ahmad@student.ac.id, HP: 081234567890
Siti Nurhaliza - Email: siti.nurhaliza@gmail.com, HP: 082345678901
Budi Santoso - Email: budi_santoso@yahoo.com, HP: 083456789012
Website: https://www.university.ac.id
Portal: https://portal.student.ac.id
"""

tulis("📝 Analisis teks:")
tulis(teks_data)

# Ekstrak email
emails = cari_pola(r'[\w\.-]+@[\w\.-]+\.\w+', teks_data, semua=benar)
tulis(str(panjang(emails))
untuk email dalam emails:
    valid = validasi_email(email)
    status = "✅" jika valid kalau_tidak "❌"
    tulis(str(email)

# Ekstrak nomor HP
phones = cari_pola(r'08\d{8,10}', teks_data, semua=benar)
tulis(str(panjang(phones))
untuk phone dalam phones:
    formatted = format_nomor_telepon(phone)
    tulis(str(formatted)

# Ekstrak URL
urls = cari_pola(r'https?://[\w\.-]+', teks_data, semua=benar)
tulis(str(panjang(urls))
untuk url dalam urls:
    valid = validasi_url(url)
    status = "✅" jika valid kalau_tidak "❌"
    tulis(str(url)

# 5. EXCEPTION HANDLING
tulis("\n5. ⚠️ EXCEPTION HANDLING")

fungsi bagi_aman(a, b):
    coba:
        hasil = a / b
        kembalikan hasil
    kecuali ZeroDivisionError:
        tulis("❌ Error: Pembagian dengan nol!")
        kembalikan kosong
    akhirnya:
        tulis(str(b)

# Test exception handling
tulis("Test pembagian normal:")
hasil1 = bagi_aman(10, 2)
tulis(str(hasil1)

tulis("\nTest pembagian dengan nol:")
hasil2 = bagi_aman(10, 0)
tulis(str(hasil2)

# 6. APLIKASI PRAKTIS: SISTEM INVENTORY
tulis("\n6. 📦 APLIKASI PRAKTIS: SISTEM INVENTORY")

kelas Produk:
    fungsi __init__(diri, kode, nama, harga, stok):
        diri.kode = kode
        diri.nama = nama
        diri.harga = harga
        diri.stok = stok
    
    fungsi info(diri):
        kembalikan {
            "kode": diri.kode,
            "nama": diri.nama,
            "harga": diri.harga,
            "stok": diri.stok,
            "nilai_total": diri.harga * diri.stok
        }

kelas Inventory:
    fungsi __init__(diri):
        diri.produk = {}
    
    fungsi tambah_produk(diri, produk):
        diri.produk[produk.kode] = produk
        tulis(str(produk.nama)
    
    fungsi laporan(diri):
        tulis("\n📊 LAPORAN INVENTORY"
        tulis(str(panjang(diri.produk))
        
        data_tabel = []
        total_nilai = 0
        
        untuk kode, produk dalam diri.produk.items():
            info = produk.info()
            data_tabel.append([
                info["kode"],
                info["nama"],
                format_rupiah(info["harga"]),
                str(info["stok"]),
                format_rupiah(info["nilai_total"])
            ])
            total_nilai += info["nilai_total"]
        
        header = ["Kode", "Nama", "Harga", "Stok", "Nilai Total"]
        cetak_tabel(data_tabel, header)
        
        tulis(str(format_rupiah(total_nilai))
        tulis(str(angka_ke_kata(int(total_nilai)))

# Setup inventory
inventory = Inventory()
inventory.tambah_produk(Produk("P001", "Laptop ASUS", 8500000, 5))
inventory.tambah_produk(Produk("P002", "Mouse Wireless", 150000, 20))
inventory.tambah_produk(Produk("P003", "Keyboard Mechanical", 750000, 8))
inventory.tambah_produk(Produk("P004", "Monitor 24 inch", 2500000, 3))

inventory.laporan()

# 7. CLEANUP
tulis("\n7. 🧹 CLEANUP")
files_to_clean = ["mahasiswa.json", "laporan_mahasiswa.csv"]
untuk file dalam files_to_clean:
    jika ada_file(file):
        hapus_file(file)
        tulis(str(file)

tulis("\n" + "=" * 50)
tulis("🎉 SHOWCASE SELESAI! CODINGYOK SIAP DIGUNAKAN! 🎉")
tulis("=" * 50)
