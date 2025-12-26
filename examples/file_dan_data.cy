# Contoh operasi file dan pengolahan data dalam CodingYok
# File: file_dan_data.cy

tulis("=== OPERASI FILE DAN DATA CODINGYOK ===")
tulis("")

# 1. Operasi File Teks
tulis("1. OPERASI FILE TEKS")
tulis("-" * 30)

# Buat file contoh
konten_contoh = "Ini adalah file contoh CodingYok.\nBaris kedua dengan data.\nBaris ketiga untuk testing.\nData penting: 12345\nAkhir file."

tulis_file("contoh.txt", konten_contoh)
tulis("File 'contoh.txt' berhasil dibuat")

# Baca file
isi_file = baca_file("contoh.txt")
tulis("Isi file:")
tulis(isi_file)

# Baca per baris
baris_file = baca_baris("contoh.txt")
tulis(f"Jumlah baris: {panjang(baris_file)}")

# Info file
info = info_file("contoh.txt")
tulis("")
tulis("Info file:")
tulis(f"  Ukuran: {info['ukuran']} bytes")
tulis(f"  Adalah file: {info['adalah_file']}")

# 2. Operasi JSON
tulis("")
tulis("2. OPERASI JSON")
tulis("-" * 30)

# Data untuk JSON
data_mahasiswa = {
    "nama": "Ahmad Fauzi",
    "nim": "12345678",
    "jurusan": "Teknik Informatika",
    "semester": 5,
    "nilai": {
        "Algoritma": 85,
        "Database": 90,
        "Web Programming": 88
    },
    "hobi": ["coding", "gaming", "membaca"]
}

# Tulis ke JSON
tulis_json("mahasiswa.json", data_mahasiswa)
tulis("Data mahasiswa disimpan ke 'mahasiswa.json'")

# Baca dari JSON
data_terbaca = baca_json("mahasiswa.json")
tulis("Data yang dibaca dari JSON:")
tulis(f"  Nama: {data_terbaca['nama']}")
tulis(f"  NIM: {data_terbaca['nim']}")
tulis(f"  Jurusan: {data_terbaca['jurusan']}")

# 3. Operasi CSV
tulis("")
tulis("3. OPERASI CSV")
tulis("-" * 30)

# Data untuk CSV
data_csv = [
    ["Nama", "Umur", "Kota", "Gaji"],
    ["Budi Santoso", "25", "Jakarta", "8000000"],
    ["Siti Nurhaliza", "23", "Bandung", "7500000"],
    ["Ahmad Fauzi", "27", "Surabaya", "9000000"],
    ["Dewi Sartika", "24", "Yogyakarta", "7000000"]
]

# Tulis ke CSV
tulis_csv("karyawan.csv", data_csv)
tulis("Data karyawan disimpan ke 'karyawan.csv'")

# Baca dari CSV
data_csv_terbaca = baca_csv("karyawan.csv")
tulis("Data karyawan dari CSV:")

# Tampilkan header dan data
header = data_csv_terbaca[0]
tulis(f"  Header: {header}")
tulis(f"  Total baris data: {panjang(data_csv_terbaca) - 1}")

# 4. Pengolahan Data dengan Statistik
tulis("")
tulis("4. ANALISIS DATA GAJI")
tulis("-" * 30)

# Ekstrak data gaji
gaji_list = []
untuk i dalam rentang(1, panjang(data_csv_terbaca)):
    row = data_csv_terbaca[i]
    gaji = int(row[3])
    gaji_list.append(gaji)

# Hitung statistik
stats = hitung_statistik(gaji_list)
tulis("Statistik Gaji Karyawan:")
tulis(f"  Rata-rata: {format_rupiah(int(stats['rata_rata']))}")
tulis(f"  Median: {format_rupiah(int(stats['median']))}")
tulis(f"  Minimum: {format_rupiah(stats['minimum'])}")
tulis(f"  Maksimum: {format_rupiah(stats['maksimum'])}")

# 5. Pattern Matching dan Validasi
tulis("")
tulis("5. PATTERN MATCHING DAN VALIDASI")
tulis("-" * 30)

# Test email validation
email_test = ["user@example.com", "invalid-email", "test@domain.co.id"]
tulis("Validasi Email:")
untuk email dalam email_test:
    valid = validasi_email(email)
    status = "Valid"
    jika bukan valid:
        status = "Tidak Valid"
    tulis(f"  {email}: {status}")

# Test URL validation
url_test = ["https://www.example.com", "not-a-url", "http://test.co.id"]
tulis("")
tulis("Validasi URL:")
untuk url dalam url_test:
    valid = validasi_url(url)
    status = "Valid"
    jika bukan valid:
        status = "Tidak Valid"
    tulis(f"  {url}: {status}")

# 6. Aplikasi Praktis: Log Analyzer
tulis("")
tulis("6. APLIKASI: ANALISIS LOG")
tulis("-" * 30)

# Buat file log contoh
log_entries = [
    "2024-01-15 10:30:15 INFO User login: admin",
    "2024-01-15 10:31:22 ERROR Database connection failed",
    "2024-01-15 10:32:10 INFO User logout: admin",
    "2024-01-15 10:35:45 WARNING Low disk space",
    "2024-01-15 10:40:12 ERROR File not found: config.txt",
    "2024-01-15 10:42:33 INFO User login: user123"
]

tulis_baris("application.log", log_entries)
tulis("File log 'application.log' dibuat")

# Analisis log
log_lines = baca_baris("application.log")
info_count = 0
error_count = 0
warning_count = 0

untuk line dalam log_lines:
    jika "INFO" dalam line:
        info_count = info_count + 1
    jika "ERROR" dalam line:
        error_count = error_count + 1
    jika "WARNING" dalam line:
        warning_count = warning_count + 1

tulis("")
tulis("Statistik Log:")
tulis(f"  INFO: {info_count}")
tulis(f"  ERROR: {error_count}")
tulis(f"  WARNING: {warning_count}")

# Cari error entries
tulis("")
tulis("Error entries:")
untuk line dalam log_lines:
    jika "ERROR" dalam line:
        tulis(f"  {line}")

# 7. Cleanup
tulis("")
tulis("7. CLEANUP")
tulis("-" * 30)
files_to_clean = ["contoh.txt", "mahasiswa.json", "karyawan.csv", "application.log"]

untuk file dalam files_to_clean:
    jika ada_file(file):
        hapus_file(file)
        tulis(f"  Dihapus: {file}")

tulis("")
tulis("=== SELESAI ===")
