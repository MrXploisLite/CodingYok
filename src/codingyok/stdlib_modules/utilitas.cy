# Modul utilitas untuk CodingYok
# Module yang menyediakan fungsi-fungsi utilitas umum

fungsi balik_string(s):
    hasil = ""
    untuk i dalam rentang(panjang(s) - 1, -1, -1):
        hasil = hasil + s[i]
    kembalikan hasil

fungsi huruf_besar(s):
    kembalikan s.upper()

fungsi huruf_kecil(s):
    kembalikan s.lower()

fungsi jumlah_kata(s):
    kata = s.split()
    kembalikan panjang(kata)

fungsi hapus_spasi(s):
    kembalikan s.strip()

fungsi ganti_karakter(s, lama, baru):
    kembalikan s.replace(lama, baru)

fungsi cek_palindrom(s):
    s_bersih = s.lower().replace(" ", "")
    panjang_s = panjang(s_bersih)
    untuk i dalam rentang(panjang_s // 2):
        jika s_bersih[i] != s_bersih[panjang_s - 1 - i]:
            kembalikan salah
    kembalikan benar

fungsi gabung_list(separator, items):
    hasil = ""
    untuk i dalam rentang(panjang(items)):
        jika i > 0:
            hasil = hasil + separator
        hasil = hasil + str(items[i])
    kembalikan hasil
