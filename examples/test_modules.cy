# Test module system in CodingYok v2.0

tulis("=== Testing Module System ===")
tulis()

# Test 1: Basic import
tulis("Test 1: Basic import")
impor matematika
hasil = matematika.tambah(5, 3)
tulis(f"matematika.tambah(5, 3) = {hasil}")
tulis(f"matematika.PI = {matematika.PI}")
tulis()

# Test 2: Import with alias
tulis("Test 2: Import with alias")
impor utilitas sebagai util
teks = "hello world"
hasil_besar = util.huruf_besar(teks)
tulis(f"util.huruf_besar('{teks}') = {hasil_besar}")
tulis()

# Test 3: From import
tulis("Test 3: From import")
dari matematika impor kurang, kali, PI
hasil_kurang = kurang(10, 4)
hasil_kali = kali(6, 7)
tulis(f"kurang(10, 4) = {hasil_kurang}")
tulis(f"kali(6, 7) = {hasil_kali}")
tulis(f"PI = {PI}")
tulis()

# Test 4: From import with alias
tulis("Test 4: From import with alias")
dari utilitas impor balik_string sebagai reverse
teks_balik = reverse("CodingYok")
tulis(f"reverse('CodingYok') = {teks_balik}")
tulis()

# Test 5: Multiple imports
tulis("Test 5: Multiple imports from same module")
dari matematika impor pangkat, akar_kuadrat, faktorial
tulis(f"pangkat(2, 10) = {pangkat(2, 10)}")
tulis(f"akar_kuadrat(144) = {akar_kuadrat(144)}")
tulis(f"faktorial(5) = {faktorial(5)}")
tulis()

# Test 6: Using constants
tulis("Test 6: Using module constants")
dari matematika impor E
tulis(f"Konstanta E = {E}")
tulis()

tulis("=== All tests passed! ===")
