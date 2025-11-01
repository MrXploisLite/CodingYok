# Test file for v3.0 features

tulis("Testing CodingYok v3.0 Features")
tulis("=" * 40)

# Test 1: Lambda Expressions
tulis("\n1. Testing Lambda:")
tambah = lambda x, y: x + y
tulis("lambda x, y: x + y")
tulis("tambah(5, 3) =", tambah(5, 3))

kuadrat = lambda x: x * x
tulis("lambda x: x * x")
tulis("kuadrat(4) =", kuadrat(4))

# Test 2: Exception Handling
tulis("\n2. Testing Exception Handling:")
tulis("Try-Except:")
coba:
    tulis("  Dalam blok coba")
    hasil = 10 / 2
    tulis("  Hasil:", hasil)
kecuali:
    tulis("  Error terjadi")

tulis("\nTry-Except-Finally:")
coba:
    tulis("  Dalam blok coba")
    x = 5
kecuali:
    tulis("  Dalam blok kecuali")
akhirnya:
    tulis("  Dalam blok akhirnya")

# Test 3: Context Managers
tulis("\n3. Testing Context Managers:")

kelas SimpleContext:
    fungsi __enter__(diri):
        tulis("  Entering context")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        tulis("  Exiting context")
        kembalikan salah

dengan SimpleContext() sebagai ctx:
    tulis("  Inside context")

tulis("\n" + "=" * 40)
tulis("All tests completed!")
