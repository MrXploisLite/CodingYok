# Contoh penggunaan kontrol alur (if, for, while)
# File: kontrol_alur.cy

tulis("=== CONTOH KONTROL ALUR CODINGYOK ===\n")

# Contoh IF statement
tulis("1. KONDISI IF-ELSE")
nilai = 85

jika nilai >= 90:
    grade = "A"
    keterangan = "Sangat Baik"
kalau_tidak_jika nilai >= 80:
    grade = "B" 
    keterangan = "Baik"
kalau_tidak_jika nilai >= 70:
    grade = "C"
    keterangan = "Cukup"
kalau_tidak_jika nilai >= 60:
    grade = "D"
    keterangan = "Kurang"
kalau_tidak:
    grade = "E"
    keterangan = "Gagal"

tulis(str(nilai))
tulis(str(keterangan))

# Contoh FOR loop
tulis("\n2. PERULANGAN FOR")
tulis("Menghitung dari 1 sampai 5:")
untuk i dalam rentang(1, 6):
    tulis(str(i))

tulis("\nMenampilkan buah-buahan:")
buah_buahan = ["apel", "jeruk", "mangga", "pisang"]
untuk buah dalam buah_buahan:
    tulis(str(huruf_besar(buah)))

# Contoh WHILE loop
tulis("\n3. PERULANGAN WHILE")
tulis("Countdown dari 5:")
countdown = 5
selama countdown > 0:
    tulis(str(countdown))
    countdown -= 1
tulis("  Selesai!")

# Contoh nested loops
tulis("\n4. PERULANGAN BERSARANG")
tulis("Tabel perkalian 3x3:")
untuk i dalam rentang(1, 4):
    baris = ""
    untuk j dalam rentang(1, 4):
        hasil = i * j
        baris += f"{hasil:2} "
    tulis(str(baris))

# Contoh dengan break dan continue
tulis("\n5. BREAK DAN CONTINUE")
tulis("Mencari angka genap dari 1-10 (maksimal 3):")
ditemukan = 0
untuk angka dalam rentang(1, 11):
    jika angka % 2 != 0:
        lanjut  # Skip angka ganjil
    
    tulis(str(angka))
    ditemukan += 1
    
    jika ditemukan >= 3:
        berhenti  # Stop setelah menemukan 3 angka

# Contoh kondisi kompleks
tulis("\n6. KONDISI KOMPLEKS")
umur = 20
punya_sim = benar
punya_mobil = salah

jika umur >= 17 dan punya_sim:
    jika punya_mobil:
        tulis("Anda bisa menyetir mobil sendiri!")
    kalau_tidak:
        tulis("Anda bisa menyetir, tapi perlu pinjam mobil.")
kalau_tidak_jika umur >= 17:
    tulis("Anda perlu SIM dulu untuk menyetir.")
kalau_tidak:
    tulis("Anda belum cukup umur untuk menyetir.")

# Contoh list comprehension style
tulis("\n7. OPERASI LIST")
angka_asli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka_genap = []
angka_kuadrat = []

untuk angka dalam angka_asli:
    jika angka % 2 == 0:
        angka_genap.append(angka)
    angka_kuadrat.append(angka * angka)

tulis(str(angka_asli))
tulis(str(angka_genap))
tulis(str(angka_kuadrat))

tulis("\n=== SELESAI ===")
