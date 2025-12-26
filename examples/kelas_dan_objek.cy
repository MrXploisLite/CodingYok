# Contoh penggunaan kelas dan objek dalam CodingYok
# File: kelas_dan_objek.cy

tulis("=== SISTEM KELAS CODINGYOK ===")
tulis("")

# Kelas sederhana
kelas Orang:
    fungsi __init__(diri, nama, umur):
        diri.nama = nama
        diri.umur = umur
        diri.hobi = []
    
    fungsi perkenalan(diri):
        tulis(f"Halo, nama saya {diri.nama}, umur {diri.umur} tahun")
    
    fungsi tambah_hobi(diri, hobi):
        diri.hobi.append(hobi)
        tulis(f"Hobi '{hobi}' ditambahkan")
    
    fungsi tampilkan_hobi(diri):
        jika panjang(diri.hobi) == 0:
            tulis(f"{diri.nama} belum punya hobi")
        kalau_tidak:
            tulis(f"Hobi {diri.nama}:")
            untuk hobi dalam diri.hobi:
                tulis(f"  - {hobi}")

# Kelas dengan inheritance
kelas Mahasiswa(Orang):
    fungsi __init__(diri, nama, umur, nim, jurusan):
        diri.nama = nama
        diri.umur = umur
        diri.hobi = []
        diri.nim = nim
        diri.jurusan = jurusan
        diri.nilai = {}
    
    fungsi perkenalan(diri):
        tulis(f"Halo, saya {diri.nama}")
        tulis(f"Jurusan: {diri.jurusan}, Umur: {diri.umur} tahun")
    
    fungsi tambah_nilai(diri, mata_kuliah, nilai):
        diri.nilai[mata_kuliah] = nilai
        tulis(f"Nilai {mata_kuliah}: {nilai}")
    
    fungsi hitung_ipk(diri):
        jika panjang(diri.nilai) == 0:
            kembalikan 0.0
        total_nilai = jumlah(diri.nilai.values())
        kembalikan total_nilai / panjang(diri.nilai)
    
    fungsi tampilkan_transkrip(diri):
        tulis(f"=== Transkrip {diri.nama} ===")
        tulis(f"NIM: {diri.nim}")
        tulis(f"Jurusan: {diri.jurusan}")
        tulis("Nilai:")
        untuk mk dalam diri.nilai.keys():
            tulis(f"  {mk}: {diri.nilai[mk]}")
        ipk = diri.hitung_ipk()
        tulis(f"IPK: {bulat(ipk, 2)}")

# Kelas untuk sistem perpustakaan
kelas Buku:
    fungsi __init__(diri, judul, penulis, tahun):
        diri.judul = judul
        diri.penulis = penulis
        diri.tahun = tahun
        diri.dipinjam = salah
        diri.peminjam = kosong
    
    fungsi info(diri):
        status = "Dipinjam"
        jika bukan diri.dipinjam:
            status = "Tersedia"
        tulis(f"{diri.judul} ({diri.tahun}) - {status}")
    
    fungsi pinjam(diri, peminjam):
        jika diri.dipinjam:
            tulis(f"Buku sudah dipinjam oleh {diri.peminjam}")
            kembalikan salah
        kalau_tidak:
            diri.dipinjam = benar
            diri.peminjam = peminjam
            tulis(f"Buku dipinjam oleh {peminjam}")
            kembalikan benar
    
    fungsi kembalikan_buku(diri):
        jika bukan diri.dipinjam:
            tulis(f"Buku {diri.judul} tidak sedang dipinjam")
        kalau_tidak:
            peminjam_lama = diri.peminjam
            diri.dipinjam = salah
            diri.peminjam = kosong
            tulis(f"Buku dikembalikan oleh {peminjam_lama}")

kelas Perpustakaan:
    fungsi __init__(diri, nama):
        diri.nama = nama
        diri.koleksi = []
    
    fungsi tambah_buku(diri, buku):
        diri.koleksi.append(buku)
        tulis(f"Buku '{buku.judul}' ditambahkan ke {diri.nama}")
    
    fungsi daftar_buku(diri):
        tulis(f"=== Koleksi {diri.nama} ===")
        untuk buku dalam diri.koleksi:
            buku.info()
    
    fungsi cari_buku(diri, judul):
        untuk buku dalam diri.koleksi:
            jika judul.lower() dalam buku.judul.lower():
                kembalikan buku
        kembalikan kosong

# Testing semua kelas
tulis("1. KELAS ORANG")
tulis("-" * 30)
orang1 = Orang("Budi", 25)
orang1.perkenalan()
orang1.tambah_hobi("membaca")
orang1.tambah_hobi("coding")
orang1.tampilkan_hobi()

tulis("")
tulis("2. KELAS MAHASISWA (INHERITANCE)")
tulis("-" * 30)
mhs1 = Mahasiswa("Siti", 20, "12345678", "Teknik Informatika")
mhs1.perkenalan()
mhs1.tambah_hobi("gaming")
mhs1.tambah_nilai("Algoritma", 85)
mhs1.tambah_nilai("Database", 90)
mhs1.tambah_nilai("Web Programming", 88)
mhs1.tampilkan_transkrip()

tulis("")
tulis("3. SISTEM PERPUSTAKAAN")
tulis("-" * 30)
perpus = Perpustakaan("Perpustakaan Universitas")

buku1 = Buku("Belajar Python", "John Doe", 2020)
buku2 = Buku("Algoritma dan Struktur Data", "Jane Smith", 2019)
buku3 = Buku("Web Development", "Bob Johnson", 2021)

perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_buku(buku3)

perpus.daftar_buku()

tulis("")
tulis("4. SIMULASI PEMINJAMAN")
tulis("-" * 30)
buku1.pinjam("Ahmad")
buku2.pinjam("Fatimah")
buku1.pinjam("Rizki")

perpus.daftar_buku()

buku1.kembalikan_buku()
buku1.pinjam("Rizki")

tulis("")
tulis("5. PENCARIAN BUKU")
tulis("-" * 30)
hasil_cari = perpus.cari_buku("python")
jika hasil_cari:
    tulis("Buku ditemukan:")
    hasil_cari.info()
kalau_tidak:
    tulis("Buku tidak ditemukan")

tulis("")
tulis("=== SELESAI ===")
