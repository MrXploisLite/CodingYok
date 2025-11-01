# Test custom user module

tulis("=== Testing Custom User Module ===")
tulis()

# Import the helper module from same directory
impor helper

# Test function from module
pesan = helper.sapa("Budi")
tulis(pesan)
tulis()

# Test module functions
luas = helper.hitung_luas_persegi(5)
tulis(f"Luas persegi (sisi 5) = {luas}")

luas_lingkaran = helper.hitung_luas_lingkaran(7)
tulis(f"Luas lingkaran (radius 7) = {luas_lingkaran}")
tulis()

# Test class from module
calc = helper.Kalkulator()
calc.tambah(10)
calc.tambah(5)
calc.kurang(3)
tulis(f"Hasil kalkulator: {calc.hasil}")
tulis()

# Test module constant
tulis(f"Versi helper module: {helper.VERSI}")
tulis()

tulis("=== Custom module test passed! ===")
