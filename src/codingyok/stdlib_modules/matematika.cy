# Modul matematika untuk CodingYok
# Module matematika yang menyediakan fungsi-fungsi matematika dasar

fungsi tambah(a, b):
    kembalikan a + b

fungsi kurang(a, b):
    kembalikan a - b

fungsi kali(a, b):
    kembalikan a * b

fungsi bagi(a, b):
    jika b == 0:
        lempar Kesalahan("Tidak dapat membagi dengan nol")
    kembalikan a / b

fungsi pangkat(base, exp):
    kembalikan base ** exp

fungsi akar_kuadrat(n):
    jika n < 0:
        lempar Kesalahan("Tidak dapat menghitung akar kuadrat dari angka negatif")
    kembalikan n ** 0.5

fungsi faktorial(n):
    jika n < 0:
        lempar Kesalahan("Faktorial tidak didefinisikan untuk angka negatif")
    jika n == 0 atau n == 1:
        kembalikan 1
    hasil = 1
    untuk i dalam rentang(2, n + 1):
        hasil = hasil * i
    kembalikan hasil

fungsi absolut(n):
    jika n < 0:
        kembalikan -n
    kembalikan n

# Konstanta matematika
PI = 3.141592653589793
E = 2.718281828459045
