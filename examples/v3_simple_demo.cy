# CodingYok v3.0 - Simple Demo
# Demonstrasi sederhana fitur-fitur v3.0

tulis("=" * 50)
tulis("CodingYok v3.0 - Fitur Baru")
tulis("=" * 50)
tulis()

# 1. Lambda Expressions
tulis("1. LAMBDA EXPRESSIONS")
tulis("-" * 50)

# Lambda sederhana
tambah = lambda x, y: x + y
tulis("Lambda tambah(5, 3) =", tambah(5, 3))

kuadrat = lambda x: x * x
tulis("Lambda kuadrat(7) =", kuadrat(7))

# Lambda dengan closure
fungsi buat_pengali(n):
    kembalikan lambda x: x * n

kali_3 = buat_pengali(3)
tulis("Lambda dengan closure kali_3(10) =", kali_3(10))

tulis()

# 2. Exception Handling
tulis("2. EXCEPTION HANDLING")
tulis("-" * 50)

tulis("Try-Except sederhana:")
coba:
    hasil = 10 / 2
    tulis("  Berhasil: 10 / 2 =", hasil)
kecuali:
    tulis("  Error terjadi")

tulis("\nTry-Except dengan ZeroDivisionError:")
coba:
    hasil = 10 / 0
kecuali ZeroDivisionError:
    tulis("  Error ditangkap: Tidak boleh dibagi nol!")

tulis("\nTry-Except-Finally:")
coba:
    tulis("  Blok coba dijalankan")
kecuali:
    tulis("  Blok kecuali dijalankan")
akhirnya:
    tulis("  Blok akhirnya selalu dijalankan")

tulis()

# 3. Context Managers
tulis("3. CONTEXT MANAGERS")
tulis("-" * 50)

kelas SimpleTimer:
    fungsi __init__(diri, nama):
        diri.nama = nama
    
    fungsi __enter__(diri):
        tulis(f"  Memulai: {diri.nama}")
        kembalikan diri
    
    fungsi __exit__(diri, a, b, c):
        tulis(f"  Selesai: {diri.nama}")
        kembalikan salah

dengan SimpleTimer("Operasi") sebagai timer:
    tulis("    Menjalankan operasi...")
    untuk i dalam rentang(3):
        lewati

tulis()

# 4. Kombinasi Fitur
tulis("4. KOMBINASI FITUR")
tulis("-" * 50)

# Lambda dengan exception handling
tulis("Lambda dengan exception handling:")

fungsi apply_safe(func, nilai):
    coba:
        kembalikan func(nilai)
    kecuali ZeroDivisionError:
        tulis(f"  Error: Pembagian dengan nol")
        kembalikan kosong

divide_by_2 = lambda x: x / 2
divide_by_0 = lambda x: x / 0

tulis(f"  10 / 2 = {apply_safe(divide_by_2, 10)}")
apply_safe(divide_by_0, 10)

tulis()

# Summary
tulis("=" * 50)
tulis("RINGKASAN:")
tulis("  ✓ Lambda - Fungsi anonim")
tulis("  ✓ Exception Handling - coba/kecuali/akhirnya")
tulis("  ✓ Context Managers - dengan statement")
tulis("=" * 50)
