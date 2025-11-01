# CodingYok v3.0 - Showcase All New Features
# Demonstrasi lengkap fitur-fitur baru di v3.0

tulis("=" * 60)
tulis("CodingYok v3.0 - Fitur Baru")
tulis("=" * 60)
tulis()

# ============================================================================
# 1. LAMBDA EXPRESSIONS
# ============================================================================
tulis("1. LAMBDA EXPRESSIONS")
tulis("-" * 60)

# Lambda sederhana
tambah = lambda x, y: x + y
tulis("Lambda tambah(5, 3):", tambah(5, 3))

kuadrat = lambda x: x * x
tulis("Lambda kuadrat(7):", kuadrat(7))

# Lambda dengan peta (map)
angka = [1, 2, 3, 4, 5]
hasil_kali_2 = peta(lambda x: x * 2, angka)
tulis("Peta lambda x*2:", daftar(hasil_kali_2))

# Lambda dengan saring (filter)
genap = saring(lambda x: x % 2 == 0, angka)
tulis("Saring genap:", daftar(genap))

# Lambda dengan closure
fungsi buat_pengali(n):
    kembalikan lambda x: x * n

kali_3 = buat_pengali(3)
kali_5 = buat_pengali(5)
tulis("Closure kali_3(10):", kali_3(10))
tulis("Closure kali_5(10):", kali_5(10))

tulis()

# ============================================================================
# 2. EXCEPTION HANDLING
# ============================================================================
tulis("2. EXCEPTION HANDLING")
tulis("-" * 60)

# Try-Except sederhana
tulis("Demo Try-Except:")
coba:
    hasil = 10 / 2
    tulis("  Pembagian berhasil:", hasil)
kecuali:
    tulis("  Terjadi error!")

# Try-Except dengan tipe exception
tulis("\nDemo ZeroDivisionError:")
coba:
    hasil = 10 / 0
kecuali ZeroDivisionError:
    tulis("  Error: Tidak boleh dibagi nol!")

# Multiple except clauses
tulis("\nDemo Multiple Except:")
fungsi proses_angka(text):
    coba:
        angka = int(text)
        hasil = 100 / angka
        kembalikan hasil
    kecuali ValueError:
        tulis("  Error: Input bukan angka")
        kembalikan kosong
    kecuali ZeroDivisionError:
        tulis("  Error: Angka tidak boleh nol")
        kembalikan kosong

proses_angka("abc")
proses_angka("0")
hasil_valid = proses_angka("5")
tulis("  Hasil valid:", hasil_valid)

# Try-Except-Finally
tulis("\nDemo Finally Block:")
coba:
    tulis("  Memulai operasi...")
    hasil = 5 + 5
    tulis("  Operasi berhasil:", hasil)
kecuali:
    tulis("  Error terjadi")
akhirnya:
    tulis("  Finally: Pembersihan selalu dijalankan")

# Raise exception
tulis("\nDemo Raise Exception:")
fungsi validasi_umur(umur):
    jika umur < 0:
        lempar ValueError("Umur tidak boleh negatif")
    jika umur > 150:
        lempar ValueError("Umur tidak wajar")
    kembalikan benar

coba:
    validasi_umur(25)
    tulis("  Umur 25: Valid")
    validasi_umur(-5)
kecuali ValueError sebagai e:
    tulis(f"  Error validasi: {e}")

tulis()

# ============================================================================
# 3. CONTEXT MANAGERS
# ============================================================================
tulis("3. CONTEXT MANAGERS")
tulis("-" * 60)

# Custom context manager
tulis("Demo Custom Context Manager:")

kelas Timer:
    fungsi __init__(diri, nama):
        diri.nama = nama
    
    fungsi __enter__(diri):
        tulis(f"  [{diri.nama}] Memulai...")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        tulis(f"  [{diri.nama}] Selesai")
        kembalikan salah

dengan Timer("Operasi 1") sebagai timer:
    tulis("    Menjalankan operasi...")
    untuk i dalam rentang(3):
        lewati

tulis("\nDemo Database Context Manager:")

kelas DatabaseConnection:
    fungsi __init__(diri, nama_db):
        diri.nama_db = nama_db
    
    fungsi __enter__(diri):
        tulis(f"  Membuka koneksi ke: {diri.nama_db}")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        tulis(f"  Menutup koneksi ke: {diri.nama_db}")
        kembalikan salah

dengan DatabaseConnection("my_database") sebagai db:
    tulis("    Melakukan query...")
    tulis("    Menyimpan data...")

tulis()

# ============================================================================
# 4. COMBINING FEATURES
# ============================================================================
tulis("4. MENGGABUNGKAN FITUR")
tulis("-" * 60)

# Lambda + Exception Handling
tulis("Demo Lambda + Exception Handling:")

fungsi apply_safe(func, nilai):
    coba:
        kembalikan func(nilai)
    kecuali Exception sebagai e:
        tulis(f"  Error pada fungsi: {e}")
        kembalikan kosong

operasi = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x / 2
]

i = 0
untuk op dalam operasi:
    hasil = apply_safe(op, 20)
    tulis(f"  Operasi {i + 1}: {hasil}")
    i += 1

# Context Manager + Exception Handling
tulis("\nDemo Context Manager + Exception:")

kelas SafeOperation:
    fungsi __init__(diri, nama):
        diri.nama = nama
    
    fungsi __enter__(diri):
        tulis(f"  Memulai {diri.nama}")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        jika exc_type:
            tulis(f"  Error di {diri.nama}: {exc_val}")
        tulis(f"  Cleanup {diri.nama}")
        kembalikan salah

dengan SafeOperation("Operasi Berisiko") sebagai op:
    tulis("    Melakukan operasi...")
    coba:
        hasil = 10 / 1
        tulis(f"    Hasil: {hasil}")
    kecuali ZeroDivisionError:
        tulis("    Error: Pembagian dengan nol")

tulis()

# ============================================================================
# 5. ADVANCED PATTERNS
# ============================================================================
tulis("5. POLA LANJUTAN")
tulis("-" * 60)

# Functional programming pattern
tulis("Demo Functional Programming:")

# Function composition
fungsi compose(f, g):
    kembalikan lambda x: f(g(x))

tambah_1 = lambda x: x + 1
kali_2 = lambda x: x * 2

# Compose: (x * 2) + 1
transform = compose(tambah_1, kali_2)
tulis("  Compose (5*2)+1:", transform(5))

# Pipeline processing
tulis("\nDemo Processing Pipeline:")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pipeline: filter even -> square -> sum
genap = saring(lambda x: x % 2 == 0, data)
kuadrat = peta(lambda x: x * x, genap)
total = jumlah(daftar(kuadrat))
tulis("  Pipeline hasil:", total)

tulis()

# ============================================================================
# 6. PRACTICAL EXAMPLE
# ============================================================================
tulis("6. CONTOH PRAKTIS: Manajemen User")
tulis("-" * 60)

kelas User:
    fungsi __init__(diri, nama, email, umur):
        diri.nama = nama
        diri.email = email
        diri.umur = umur
    
    fungsi validate(diri):
        jika bukan "@" dalam diri.email:
            lempar ValueError(f"Email tidak valid: {diri.email}")
        jika diri.umur < 0 atau diri.umur > 150:
            lempar ValueError(f"Umur tidak valid: {diri.umur}")
        kembalikan benar

kelas UserManager:
    fungsi __init__(diri):
        diri.users = []
    
    fungsi __enter__(diri):
        tulis("  UserManager: Inisialisasi")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        tulis(f"  UserManager: Cleanup ({panjang(diri.users)} users)")
        kembalikan salah
    
    fungsi add_user(diri, user):
        coba:
            user.validate()
            diri.users.append(user)
            tulis(f"    User ditambahkan: {user.nama}")
            kembalikan benar
        kecuali ValueError sebagai e:
            tulis(f"    Error: {e}")
            kembalikan salah
    
    fungsi get_adult_users(diri):
        kembalikan saring(lambda u: u.umur >= 18, diri.users)

tulis("Menggunakan UserManager:")
dengan UserManager() sebagai um:
    um.add_user(User("Budi", "budi@email.com", 25))
    um.add_user(User("Ani", "ani@email.com", 22))
    um.add_user(User("Citra", "citra.email.com", 20))
    um.add_user(User("Doni", "doni@email.com", -5))
    
    adults = daftar(um.get_adult_users())
    tulis(f"\n    Total user dewasa: {panjang(adults)}")
    untuk user dalam adults:
        tulis(f"      - {user.nama} ({user.umur} tahun)")

tulis()

# ============================================================================
# SUMMARY
# ============================================================================
tulis("=" * 60)
tulis("RINGKASAN FITUR v3.0:")
tulis("  ✓ Lambda Expressions - Fungsi anonim dengan closure")
tulis("  ✓ Exception Handling - coba/kecuali/akhirnya/lempar")
tulis("  ✓ Context Managers - dengan statement untuk resource")
tulis("  ✓ Advanced Patterns - Kombinasi fitur untuk kode profesional")
tulis("=" * 60)
