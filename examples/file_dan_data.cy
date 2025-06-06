# Contoh operasi file dan pengolahan data dalam CodingYok
# File: file_dan_data.cy

tulis("=== OPERASI FILE DAN DATA CODINGYOK ===\n")

# 1. Operasi File Teks
tulis("1. OPERASI FILE TEKS")

# Buat file contoh
konten_contoh = """Ini adalah file contoh CodingYok.
Baris kedua dengan data.
Baris ketiga untuk testing.
Data penting: 12345
Akhir file."""

tulis_file("contoh.txt", konten_contoh)
tulis("File 'contoh.txt' berhasil dibuat")

# Baca file
isi_file = baca_file("contoh.txt")
tulis("Isi file:")
tulis(isi_file)

# Baca per baris
baris_file = baca_baris("contoh.txt")
tulis(str(panjang(baris_file))
untuk i, baris dalam enumerate(baris_file, 1):
    tulis(str(baris)

# Info file
info = info_file("contoh.txt")
tulis("\nInfo file:"
tulis(str(info['ukuran'])
tulis(str(info['adalah_file'])

# 2. Operasi JSON
tulis("\n2. OPERASI JSON")

# Data untuk JSON
data_mahasiswa = {
    "nama": "Ahmad Fauzi",
    "nim": "12345678",
    "jurusan": "Teknik Informatika",
    "semester": 5,
    "nilai": {
        "Algoritma": 85,
        "Database": 90,
        "Web Programming": 88,
        "Mobile Programming": 92
    },
    "hobi": ["coding", "gaming", "membaca"]
}

# Tulis ke JSON
tulis_json("mahasiswa.json", data_mahasiswa)
tulis("Data mahasiswa disimpan ke 'mahasiswa.json'")

# Baca dari JSON
data_terbaca = baca_json("mahasiswa.json")
tulis("Data yang dibaca dari JSON:")
tulis(str(data_terbaca['nama'])
tulis(str(data_terbaca['nim'])
tulis(str(data_terbaca['jurusan'])

tulis("  Nilai:")
untuk mk, nilai dalam data_terbaca['nilai'].items():
    tulis(str(nilai)

# 3. Operasi CSV
tulis("\n3. OPERASI CSV")

# Data untuk CSV
data_csv = [
    ["Nama", "Umur", "Kota", "Gaji"],
    ["Budi Santoso", "25", "Jakarta", "8000000"],
    ["Siti Nurhaliza", "23", "Bandung", "7500000"],
    ["Ahmad Fauzi", "27", "Surabaya", "9000000"],
    ["Dewi Sartika", "24", "Yogyakarta", "7000000"],
    ["Rizki Pratama", "26", "Medan", "8500000"]
]

# Tulis ke CSV
tulis_csv("karyawan.csv", data_csv)
tulis("Data karyawan disimpan ke 'karyawan.csv'")

# Baca dari CSV
data_csv_terbaca = baca_csv("karyawan.csv")
tulis("Data karyawan dari CSV:")

# Tampilkan sebagai tabel
header = data_csv_terbaca[0]
data_rows = data_csv_terbaca[1:]
cetak_tabel(data_rows, header)

# 4. Pengolahan Data dengan Statistik
tulis("\n4. ANALISIS DATA GAJI")

# Ekstrak data gaji
gaji_list = []
untuk row dalam data_rows:
    gaji = int(row[3])  # Kolom gaji
    gaji_list.append(gaji)

# Hitung statistik
stats = hitung_statistik(gaji_list)
tulis("Statistik Gaji Karyawan:")
tulis(str(format_rupiah(stats['rata_rata']))
tulis(str(format_rupiah(stats['median']))
tulis(str(format_rupiah(stats['minimum']))
tulis(str(format_rupiah(stats['maksimum']))
tulis(str(format_rupiah(stats['standar_deviasi']))

# 5. Pattern Matching dan Validasi
tulis("\n5. PATTERN MATCHING DAN VALIDASI")

# Buat file dengan data campuran
data_campuran = """Email: user@example.com
Telepon: 081234567890
Website: https://www.example.com
Email tidak valid: invalid-email
URL tidak valid: not-a-url
Nomor: 08123-456-7890"""

tulis_file("data_campuran.txt", data_campuran)

# Baca dan analisis
isi = baca_file("data_campuran.txt")
baris_data = pisah("\n", isi)

tulis("Analisis data:")
untuk baris dalam baris_data:
    tulis(str(baris)
    
    # Cari email
    email_match = cari_pola(r'[\w\.-]+@[\w\.-]+\.\w+', baris)
    jika email_match:
        valid = validasi_email(email_match)
        status = "Valid" jika valid kalau_tidak "Tidak Valid"
        tulis(str(status)
    
    # Cari URL
    url_match = cari_pola(r'https?://[\w\.-]+', baris)
    jika url_match:
        valid = validasi_url(url_match)
        status = "Valid" jika valid kalau_tidak "Tidak Valid"
        tulis(str(status)
    
    # Cari nomor telepon
    phone_match = cari_pola(r'08\d{8,10}', baris)
    jika phone_match:
        formatted = format_nomor_telepon(phone_match)
        tulis(str(formatted)

# 6. Aplikasi Praktis: Log Analyzer
tulis("\n6. APLIKASI: ANALISIS LOG")

# Buat file log contoh
log_entries = [
    "2024-01-15 10:30:15 INFO User login: admin",
    "2024-01-15 10:31:22 ERROR Database connection failed",
    "2024-01-15 10:32:10 INFO User logout: admin", 
    "2024-01-15 10:35:45 WARNING Low disk space",
    "2024-01-15 10:40:12 ERROR File not found: config.txt",
    "2024-01-15 10:42:33 INFO User login: user123",
    "2024-01-15 10:45:18 INFO Data backup completed",
    "2024-01-15 10:50:25 ERROR Network timeout"
]

tulis_baris("application.log", log_entries)
tulis("File log 'application.log' dibuat")

# Analisis log
log_lines = baca_baris("application.log")
log_stats = {
    "INFO": 0,
    "ERROR": 0,
    "WARNING": 0
}

tulis("\nAnalisis log:")
untuk line dalam log_lines:
    untuk level dalam log_stats.keys():
        jika level dalam line:
            log_stats[level] += 1

untuk level, count dalam log_stats.items():
    tulis(str(count)

# Cari error entries
tulis("\nError entries:")
untuk line dalam log_lines:
    jika "ERROR" dalam line:
        tulis(str(line)

# 7. Cleanup
tulis("\n7. CLEANUP")
files_to_clean = ["contoh.txt", "mahasiswa.json", "karyawan.csv", "data_campuran.txt", "application.log"]

untuk file dalam files_to_clean:
    jika ada_file(file):
        hapus_file(file)
        tulis(str(file)

tulis("\n=== SELESAI ===")
