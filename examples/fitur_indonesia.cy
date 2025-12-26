# Contoh fitur-fitur khusus Indonesia dalam CodingYok
# File: fitur_indonesia.cy

tulis("=== FITUR KHUSUS INDONESIA CODINGYOK ===")
tulis("")

# 1. Format Rupiah
tulis("1. FORMAT RUPIAH")
tulis("-" * 30)
harga_laptop = 15000000
harga_buku = 75000
harga_kopi = 25000

tulis(f"Laptop: {format_rupiah(harga_laptop)}")
tulis(f"Buku: {format_rupiah(harga_buku)}")
tulis(f"Kopi: {format_rupiah(harga_kopi)}")
tulis(f"Total: {format_rupiah(harga_laptop + harga_buku + harga_kopi)}")

# 2. Konversi Angka ke Kata
tulis("")
tulis("2. ANGKA KE KATA INDONESIA")
tulis("-" * 30)
angka_test = [5, 17, 25, 100, 250, 1000, 1500]
untuk angka dalam angka_test:
    tulis(f"{angka} = {angka_ke_kata(angka)}")

# 3. Tanggal dan Waktu Indonesia
tulis("")
tulis("3. TANGGAL DAN WAKTU INDONESIA")
tulis("-" * 30)
tulis(f"Hari ini: {tanggal_indonesia()}")
tulis(f"Waktu sekarang: {waktu_indonesia()}")

# 4. Data Provinsi Indonesia
tulis("")
tulis("4. DATA PROVINSI INDONESIA")
tulis("-" * 30)
tulis("Beberapa provinsi di Indonesia:")
provinsi_sample = ["jakarta", "jabar", "jateng", "jatim", "bali"]
untuk prov dalam provinsi_sample:
    nama_lengkap = cek_provinsi(prov)
    tulis(f"  {prov} -> {nama_lengkap}")

semua_provinsi = daftar_provinsi()
tulis(f"Total provinsi: {panjang(semua_provinsi)}")

# 5. Kota Besar Indonesia
tulis("")
tulis("5. KOTA BESAR INDONESIA")
tulis("-" * 30)
kota_besar = daftar_kota_besar()
tulis(f"Total kota besar: {panjang(kota_besar)}")
tulis("5 kota besar pertama:")
untuk i dalam rentang(5):
    tulis(f"  {i + 1}. {kota_besar[i]}")

# 6. Format Nomor Telepon
tulis("")
tulis("6. FORMAT NOMOR TELEPON")
tulis("-" * 30)
nomor_test = ["081234567890", "6281234567890", "021-12345678"]
untuk nomor dalam nomor_test:
    formatted = format_nomor_telepon(nomor)
    tulis(f"  {nomor} -> {formatted}")

# 7. Validasi NIK
tulis("")
tulis("7. VALIDASI NIK")
tulis("-" * 30)
nik_test = ["1234567890123456", "123456789012345", "abcd567890123456"]
untuk nik dalam nik_test:
    valid = validasi_nik(nik)
    status = "Valid"
    jika bukan valid:
        status = "Tidak Valid"
    tulis(f"  {nik}: {status}")

# 8. Konversi Suhu
tulis("")
tulis("8. KONVERSI SUHU")
tulis("-" * 30)
suhu_jakarta = 32
tulis(f"Suhu Jakarta: {suhu_jakarta}°C")
fahrenheit = konversi_suhu(suhu_jakarta, "celsius", "fahrenheit")
kelvin = konversi_suhu(suhu_jakarta, "celsius", "kelvin")
tulis(f"  Fahrenheit: {bulat(fahrenheit, 1)}°F")
tulis(f"  Kelvin: {bulat(kelvin, 1)}K")

# 9. Aplikasi Praktis: Kalkulator Belanja
tulis("")
tulis("9. APLIKASI: KALKULATOR BELANJA")
tulis("-" * 30)

kelas ItemBelanja:
    fungsi __init__(diri, nama, harga, jumlah):
        diri.nama = nama
        diri.harga = harga
        diri.jumlah = jumlah
    
    fungsi total(diri):
        kembalikan diri.harga * diri.jumlah
    
    fungsi info(diri):
        total_harga = diri.total()
        tulis(f"  {diri.nama} x{diri.jumlah}: {format_rupiah(total_harga)}")

kelas KeranjangBelanja:
    fungsi __init__(diri):
        diri.items = []
    
    fungsi tambah_item(diri, item):
        diri.items.append(item)
    
    fungsi total_belanja(diri):
        total = 0
        untuk item dalam diri.items:
            total = total + item.total()
        kembalikan total
    
    fungsi cetak_struk(diri):
        tulis("")
        tulis("=" * 40)
        tulis("           STRUK BELANJA")
        tulis("=" * 40)
        
        untuk item dalam diri.items:
            item.info()
        
        tulis("-" * 40)
        total = diri.total_belanja()
        tulis(f"TOTAL: {format_rupiah(total)}")
        tulis(f"Terbilang: {angka_ke_kata(int(total))} rupiah")
        tulis("=" * 40)
        tulis(f"Tanggal: {tanggal_indonesia()}")
        tulis(f"Waktu: {waktu_indonesia()}")

# Simulasi belanja
keranjang = KeranjangBelanja()
keranjang.tambah_item(ItemBelanja("Beras 5kg", 65000, 2))
keranjang.tambah_item(ItemBelanja("Minyak Goreng", 25000, 3))
keranjang.tambah_item(ItemBelanja("Gula Pasir", 15000, 1))
keranjang.tambah_item(ItemBelanja("Telur 1kg", 28000, 2))

keranjang.cetak_struk()

tulis("")
tulis("=== SELESAI ===")
