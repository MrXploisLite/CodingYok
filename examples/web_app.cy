# Contoh aplikasi sistem informasi dengan CodingYok
# File: web_app.cy

tulis("=== APLIKASI SISTEM INFORMASI CODINGYOK ===")
tulis("")

# Data storage menggunakan kelas
kelas Database:
    fungsi __init__(diri):
        diri.mahasiswa = []
        diri.counter_id = 0
    
    fungsi generate_id(diri):
        diri.counter_id = diri.counter_id + 1
        kembalikan diri.counter_id
    
    fungsi cari(diri, id_mahasiswa):
        untuk mhs dalam diri.mahasiswa:
            jika mhs["id"] == id_mahasiswa:
                kembalikan mhs
        kembalikan kosong
    
    fungsi tambah(diri, nama, nim, jurusan, semester):
        untuk mhs dalam diri.mahasiswa:
            jika mhs["nim"] == nim:
                tulis(f"Error: NIM {nim} sudah terdaftar!")
                kembalikan kosong
        
        mahasiswa_baru = {
            "id": diri.generate_id(),
            "nama": nama,
            "nim": nim,
            "jurusan": jurusan,
            "semester": semester,
            "tanggal_daftar": tanggal_indonesia()
        }
        
        diri.mahasiswa.append(mahasiswa_baru)
        tulis(f"✓ Mahasiswa {nama} berhasil ditambahkan!")
        kembalikan mahasiswa_baru
    
    fungsi hapus_data(diri, id_mahasiswa):
        untuk i dalam rentang(panjang(diri.mahasiswa)):
            jika diri.mahasiswa[i]["id"] == id_mahasiswa:
                nama = diri.mahasiswa[i]["nama"]
                diri.mahasiswa.pop(i)
                tulis(f"✓ Mahasiswa {nama} berhasil dihapus!")
                kembalikan benar
        tulis(f"Error: Mahasiswa dengan ID {id_mahasiswa} tidak ditemukan!")
        kembalikan salah
    
    fungsi tampilkan_semua(diri):
        tulis("")
        tulis("=" * 60)
        tulis("              DAFTAR MAHASISWA")
        tulis("=" * 60)
        
        jika panjang(diri.mahasiswa) == 0:
            tulis("  Belum ada data mahasiswa.")
        kalau_tidak:
            untuk mhs dalam diri.mahasiswa:
                tulis(f"  ID: {mhs['id']}")
                tulis(f"  Nama: {mhs['nama']}")
                tulis(f"  NIM: {mhs['nim']}")
                tulis(f"  Jurusan: {mhs['jurusan']}")
                tulis(f"  Semester: {mhs['semester']}")
                tulis(f"  Tanggal Daftar: {mhs['tanggal_daftar']}")
                tulis("-" * 60)
        
        tulis(f"  Total: {panjang(diri.mahasiswa)} mahasiswa")
        tulis("=" * 60)
    
    fungsi statistik(diri):
        tulis("")
        tulis("=" * 40)
        tulis("        STATISTIK MAHASISWA")
        tulis("=" * 40)
        
        jika panjang(diri.mahasiswa) == 0:
            tulis("  Belum ada data untuk statistik.")
            kembalikan
        
        per_jurusan = {}
        per_semester = {}
        
        untuk mhs dalam diri.mahasiswa:
            jurusan = mhs["jurusan"]
            semester = mhs["semester"]
            
            jika jurusan dalam per_jurusan:
                per_jurusan[jurusan] = per_jurusan[jurusan] + 1
            kalau_tidak:
                per_jurusan[jurusan] = 1
            
            kunci_semester = f"Semester {semester}"
            jika kunci_semester dalam per_semester:
                per_semester[kunci_semester] = per_semester[kunci_semester] + 1
            kalau_tidak:
                per_semester[kunci_semester] = 1
        
        tulis(f"  Total Mahasiswa: {panjang(diri.mahasiswa)}")
        tulis("")
        tulis("  Per Jurusan:")
        untuk jurusan dalam per_jurusan:
            tulis(f"    - {jurusan}: {per_jurusan[jurusan]}")
        
        tulis("")
        tulis("  Per Semester:")
        untuk sem dalam per_semester:
            tulis(f"    - {sem}: {per_semester[sem]}")
        
        tulis("=" * 40)

# Demo Aplikasi
tulis("🎓 SISTEM INFORMASI MAHASISWA")
tulis("   Dibuat dengan CodingYok")
tulis("")

db = Database()

tulis("Menambahkan data contoh...")
tulis("-" * 40)

db.tambah("Ahmad Fauzi", "12345678", "Teknik Informatika", 5)
db.tambah("Siti Nurhaliza", "12345679", "Sistem Informasi", 3)
db.tambah("Budi Santoso", "12345680", "Teknik Komputer", 7)
db.tambah("Dewi Sartika", "12345681", "Manajemen Informatika", 4)
db.tambah("Rizki Pratama", "12345682", "Teknik Informatika", 6)

db.tampilkan_semua()
db.statistik()

tulis("")
tulis("Test hapus mahasiswa ID 2...")
db.hapus_data(2)

db.tampilkan_semua()

tulis("")
tulis("Test tambah dengan NIM duplikat...")
db.tambah("Test User", "12345678", "Test", 1)

tulis("")
tulis("Test cari mahasiswa ID 3...")
mhs = db.cari(3)
jika mhs != kosong:
    tulis(f"  Ditemukan: {mhs['nama']} ({mhs['nim']})")
kalau_tidak:
    tulis("  Tidak ditemukan")

tulis("")
tulis("=== SELESAI ===")
