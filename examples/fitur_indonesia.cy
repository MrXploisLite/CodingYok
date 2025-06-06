# Contoh fitur-fitur khusus Indonesia dalam CodingYok
# File: fitur_indonesia.cy

tulis("=== FITUR KHUSUS INDONESIA CODINGYOK ===\n")

# 1. Format Rupiah
tulis("1. FORMAT RUPIAH")
harga_laptop = 15000000
harga_buku = 75000
harga_kopi = 25000.50

tulis(f"Laptop: {format_rupiah(harga_laptop)}")
tulis(f"Buku: {format_rupiah(harga_buku)}")
tulis(f"Kopi: {format_rupiah(harga_kopi)}")
tulis(f"Total: {format_rupiah(harga_laptop + harga_buku + harga_kopi)}")

# 2. Konversi Angka ke Kata
tulis("\n2. ANGKA KE KATA INDONESIA")
angka_test = [5, 17, 25, 100, 250, 1000, 1500]
untuk angka dalam angka_test:
    tulis(f"{angka} = {angka_ke_kata(angka)}")

# 3. Tanggal dan Waktu Indonesia
tulis("\n3. TANGGAL DAN WAKTU INDONESIA")
tulis(f"Hari ini: {tanggal_indonesia()}")
tulis(f"Tanggal singkat: {tanggal_indonesia(format_panjang=salah)}")
tulis(f"Waktu sekarang: {waktu_indonesia()}")
tulis(f"Waktu 12 jam: {waktu_indonesia(format_24=salah)}")

# 4. Data Provinsi Indonesia
tulis("\n4. DATA PROVINSI INDONESIA")
tulis("Beberapa provinsi di Indonesia:")
provinsi_sample = ["jakarta", "jabar", "jateng", "jatim", "bali"]
untuk prov dalam provinsi_sample:
    nama_lengkap = cek_provinsi(prov)
    tulis(f"  {prov} -> {nama_lengkap}")

tulis(f"\nTotal provinsi: {panjang(daftar_provinsi())}")
tulis("5 provinsi pertama:")
untuk i dalam rentang(5):
    tulis(f"  {i+1}. {daftar_provinsi()[i]}")

# 5. Kota Besar Indonesia
tulis("\n5. KOTA BESAR INDONESIA")
kota_besar = daftar_kota_besar()
tulis(f"Total kota besar: {panjang(kota_besar)}")
tulis("10 kota besar pertama:")
untuk i dalam rentang(10):
    tulis(f"  {i+1}. {kota_besar[i]}")

# 6. Format Nomor Telepon
tulis("\n6. FORMAT NOMOR TELEPON")
nomor_test = [
    "081234567890",
    "6281234567890", 
    "021-12345678",
    "0274-123456"
]

untuk nomor dalam nomor_test:
    formatted = format_nomor_telepon(nomor)
    tulis(f"{nomor} -> {formatted}")

# 7. Validasi NIK
tulis("\n7. VALIDASI NIK")
nik_test = [
    "1234567890123456",  # Valid format
    "3201234567890123",  # Valid Jakarta
    "123456789012345",   # Terlalu pendek
    "abcd567890123456"   # Bukan angka
]

untuk nik dalam nik_test:
    valid = validasi_nik(nik)
    status = "Valid" jika valid kalau_tidak "Tidak Valid"
    tulis(f"NIK {nik}: {status}")

# 8. Konversi Suhu
tulis("\n8. KONVERSI SUHU")
suhu_jakarta = 32  # Celsius
tulis(f"Suhu Jakarta: {suhu_jakarta}°C")
tulis(f"Dalam Fahrenheit: {bulat(konversi_suhu(suhu_jakarta, 'celsius', 'fahrenheit'), 1)}°F")
tulis(f"Dalam Kelvin: {bulat(konversi_suhu(suhu_jakarta, 'celsius', 'kelvin'), 1)}K")

# 9. Jarak Antar Kota
tulis("\n9. JARAK ANTAR KOTA")
rute_test = [
    ("Jakarta", "Bandung"),
    ("Jakarta", "Surabaya"),
    ("Bandung", "Yogyakarta"),
    ("Surabaya", "Denpasar")
]

untuk kota1, kota2 dalam rute_test:
    jarak = jarak_kota(kota1, kota2)
    tulis(f"{kota1} - {kota2}: {jarak}")

# 10. Aplikasi Praktis: Kalkulator Belanja
tulis("\n10. APLIKASI: KALKULATOR BELANJA")

kelas ItemBelanja:
    fungsi __init__(diri, nama, harga, jumlah):
        diri.nama = nama
        diri.harga = harga
        diri.jumlah = jumlah
    
    fungsi total(diri):
        kembalikan diri.harga * diri.jumlah
    
    fungsi info(diri):
        total_harga = diri.total()
        tulis(f"{diri.nama}: {format_rupiah(diri.harga)} x {diri.jumlah} = {format_rupiah(total_harga)}")

kelas KeranjangBelanja:
    fungsi __init__(diri):
        diri.items = []
    
    fungsi tambah_item(diri, item):
        diri.items.append(item)
    
    fungsi total_belanja(diri):
        total = 0
        untuk item dalam diri.items:
            total += item.total()
        kembalikan total
    
    fungsi cetak_struk(diri):
        tulis("\n" + "="*40)
        tulis("           STRUK BELANJA")
        tulis("="*40)
        
        untuk item dalam diri.items:
            item.info()
        
        tulis("-"*40)
        total = diri.total_belanja()
        tulis(f"TOTAL: {format_rupiah(total)}")
        tulis(f"Terbilang: {angka_ke_kata(int(total))} rupiah")
        tulis("="*40)
        tulis(f"Tanggal: {tanggal_indonesia()}")
        tulis(f"Waktu: {waktu_indonesia()}")

# Simulasi belanja
keranjang = KeranjangBelanja()
keranjang.tambah_item(ItemBelanja("Beras 5kg", 65000, 2))
keranjang.tambah_item(ItemBelanja("Minyak Goreng", 25000, 3))
keranjang.tambah_item(ItemBelanja("Gula Pasir", 15000, 1))
keranjang.tambah_item(ItemBelanja("Telur 1kg", 28000, 2))

keranjang.cetak_struk()

tulis("\n=== SELESAI ===")
