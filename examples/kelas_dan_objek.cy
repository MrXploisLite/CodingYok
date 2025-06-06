# Contoh penggunaan kelas dan objek dalam CodingYok
# File: kelas_dan_objek.cy

tulis("=== SISTEM KELAS CODINGYOK ===\n")

# Kelas sederhana
kelas Orang:
    fungsi __init__(diri, nama, umur):
        diri.nama = nama
        diri.umur = umur
        diri.hobi = []
    
    fungsi perkenalan(diri):
        tulis(str(diri.umur)
    
    fungsi tambah_hobi(diri, hobi):
        diri.hobi.append(hobi)
        tulis(str(hobi)
    
    fungsi tampilkan_hobi(diri):
        jika panjang(diri.hobi) == 0:
            tulis(str(diri.nama)
        kalau_tidak:
            tulis(str(diri.nama)
            untuk hobi dalam diri.hobi:
                tulis(str(hobi)

# Kelas dengan inheritance
kelas Mahasiswa(Orang):
    fungsi __init__(diri, nama, umur, nim, jurusan):
        # Panggil constructor parent class
        diri.nama = nama
        diri.umur = umur
        diri.hobi = []
        
        # Atribut khusus mahasiswa
        diri.nim = nim
        diri.jurusan = jurusan
        diri.nilai = {}
    
    fungsi perkenalan(diri):
        tulis(str(diri.jurusan)
        tulis(str(diri.umur)
    
    fungsi tambah_nilai(diri, mata_kuliah, nilai):
        diri.nilai[mata_kuliah] = nilai
        tulis(str(nilai)
    
    fungsi hitung_ipk(diri):
        jika panjang(diri.nilai) == 0:
            kembalikan 0.0
        
        total_nilai = jumlah(diri.nilai.values())
        kembalikan total_nilai / panjang(diri.nilai)
    
    fungsi tampilkan_transkrip(diri):
        tulis(str(diri.nama)
        tulis(str(diri.nim)
        tulis(str(diri.jurusan)
        tulis("Nilai:")
        
        untuk mk, nilai dalam diri.nilai.items():
            tulis(str(nilai)
        
        ipk = diri.hitung_ipk()
        tulis(str(bulat(ipk, 2))

# Kelas untuk sistem perpustakaan
kelas Buku:
    fungsi __init__(diri, judul, penulis, tahun):
        diri.judul = judul
        diri.penulis = penulis
        diri.tahun = tahun
        diri.dipinjam = salah
        diri.peminjam = kosong
    
    fungsi info(diri):
        status = "Dipinjam" jika diri.dipinjam kalau_tidak "Tersedia"
        tulis(str(status)
    
    fungsi pinjam(diri, peminjam):
        jika diri.dipinjam:
            tulis(str(diri.peminjam)
            kembalikan salah
        kalau_tidak:
            diri.dipinjam = benar
            diri.peminjam = peminjam
            tulis(str(peminjam)
            kembalikan benar
    
    fungsi kembalikan_buku(diri):
        jika bukan diri.dipinjam:
            tulis(str(diri.judul)
        kalau_tidak:
            peminjam_lama = diri.peminjam
            diri.dipinjam = salah
            diri.peminjam = kosong
            tulis(str(peminjam_lama)

kelas Perpustakaan:
    fungsi __init__(diri, nama):
        diri.nama = nama
        diri.koleksi = []
        diri.anggota = []
    
    fungsi tambah_buku(diri, buku):
        diri.koleksi.append(buku)
        tulis(str(diri.nama)
    
    fungsi daftar_buku(diri):
        tulis(str(diri.nama)
        untuk i, buku dalam enumerate(diri.koleksi, 1):
            tulis(f"{i}. ", end="")
            buku.info()
    
    fungsi cari_buku(diri, judul):
        untuk buku dalam diri.koleksi:
            jika judul.lower() dalam buku.judul.lower():
                kembalikan buku
        kembalikan kosong

# Testing semua kelas
tulis("1. KELAS ORANG")
orang1 = Orang("Budi", 25)
orang1.perkenalan()
orang1.tambah_hobi("membaca")
orang1.tambah_hobi("coding")
orang1.tampilkan_hobi()

tulis("\n2. KELAS MAHASISWA (INHERITANCE)")
mhs1 = Mahasiswa("Siti", 20, "12345678", "Teknik Informatika")
mhs1.perkenalan()
mhs1.tambah_hobi("gaming")
mhs1.tambah_nilai("Algoritma", 85)
mhs1.tambah_nilai("Database", 90)
mhs1.tambah_nilai("Web Programming", 88)
mhs1.tampilkan_transkrip()

tulis("\n3. SISTEM PERPUSTAKAAN")
perpus = Perpustakaan("Perpustakaan Universitas")

# Tambah buku-buku
buku1 = Buku("Belajar Python", "John Doe", 2020)
buku2 = Buku("Algoritma dan Struktur Data", "Jane Smith", 2019)
buku3 = Buku("Web Development", "Bob Johnson", 2021)

perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_buku(buku3)

perpus.daftar_buku()

tulis("\n4. SIMULASI PEMINJAMAN BUKU")
# Simulasi peminjaman
buku1.pinjam("Ahmad")
buku2.pinjam("Fatimah")
buku1.pinjam("Rizki")  # Gagal karena sudah dipinjam

perpus.daftar_buku()

# Kembalikan buku
buku1.kembalikan_buku()
buku1.pinjam("Rizki")  # Sekarang berhasil

tulis("\n5. PENCARIAN BUKU")
hasil_cari = perpus.cari_buku("python")
jika hasil_cari:
    tulis("Buku ditemukan:")
    hasil_cari.info()
kalau_tidak:
    tulis("Buku tidak ditemukan")

tulis("\n=== SELESAI ===")
