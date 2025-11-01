# Helper module - custom user module

fungsi sapa(nama):
    kembalikan f"Halo, {nama}! Selamat datang di CodingYok!"

fungsi hitung_luas_persegi(sisi):
    kembalikan sisi * sisi

fungsi hitung_luas_lingkaran(radius):
    PI = 3.14159
    kembalikan PI * radius * radius

kelas Kalkulator:
    fungsi __init__(diri):
        diri.hasil = 0
    
    fungsi reset(diri):
        diri.hasil = 0
    
    fungsi tambah(diri, nilai):
        diri.hasil = diri.hasil + nilai
        kembalikan diri.hasil
    
    fungsi kurang(diri, nilai):
        diri.hasil = diri.hasil - nilai
        kembalikan diri.hasil

VERSI = "1.0.0"
