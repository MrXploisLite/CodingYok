# CodingYok - Complete Feature Reference

## 🎉 Overview

CodingYok adalah bahasa pemrograman Indonesia dengan fitur modern. Dokumen ini mencakup semua fitur dari v1.0 hingga v3.0.

---

## 📊 Feature Summary

| Feature | Description |
|---------|-------------|
| Walrus Operator | `(x := value)` assignment expression |
| Ternary Expression | `x jika kondisi kalau_tidak y` inline conditional |
| Slicing | `arr[start:stop:step]` untuk list dan string |
| Tuple Unpacking | `a, b = [1, 2]` dan `untuk x, y dalam items` |
| List/Dict/Set Comprehensions | Sintaks modern untuk pembuatan koleksi |
| Set Literals | Native set data type `{1, 2, 3}` |
| Generators (`hasilkan`) | Memory-efficient iterators |
| Pattern Matching (`cocokkan/kasus`) | Clean conditional logic |
| Error Suggestions | "Mungkin maksud Anda" untuk typo |
| Module System (`impor`) | Organize code into modules |
| Lambda Expressions | Anonymous functions |
| Exception Handling | `coba/kecuali/akhirnya/lempar` |
| Context Managers | `dengan` statement |
| OOP | Classes dengan inheritance |
| File I/O | JSON, CSV, file operations |
| Web Framework | Built-in HTTP server |

---

## 🆕 Keywords

```
# Core
tulis, jika, kalau_tidak, kalau_tidak_jika, untuk, selama
fungsi, kelas, kembalikan, lewati, berhenti, lanjut

# Module
impor, dari, sebagai

# OOP
diri, kelas

# Boolean/None
benar, salah, kosong

# Logic
dan, atau, bukan, dalam, adalah

# Generators & Pattern Matching
hasilkan, cocokkan, kasus

# Exception Handling
coba, kecuali, akhirnya, lempar

# Context Manager
dengan

# Lambda
lambda

# Others
global, nonlokal, tegas, hapus
```

---

## 📝 Comprehensions

### List Comprehension
```codingyok
# Basic
squares = [x * x untuk x dalam [1, 2, 3, 4, 5]]
# [1, 4, 9, 16, 25]

# With filter
evens = [x untuk x dalam rentang(10) jika x % 2 == 0]
# [0, 2, 4, 6, 8]
```

### Dictionary Comprehension
```codingyok
squares = {x: x * x untuk x dalam rentang(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Set Comprehension
```codingyok
unique = {x untuk x dalam [1, 2, 2, 3, 3, 4]}
# {1, 2, 3, 4}
```

---

## 🔄 Generators

```codingyok
fungsi fibonacci(n):
    a, b = 0, 1
    counter = 0
    selama counter < n:
        hasilkan a
        a, b = b, a + b
        counter += 1

untuk num dalam fibonacci(10):
    tulis(num)
```

---

## 📦 Tuple Unpacking

```codingyok
# Basic unpacking
a, b = [1, 2]
x, y, z = [10, 20, 30]

# Swap values
a, b = [b, a]

# For loop with unpacking
items = [[1, 2], [3, 4], [5, 6]]
untuk x, y dalam items:
    tulis(f"{x} + {y} = {x + y}")

# Dict items iteration
data = {"nama": "Budi", "umur": 25}
untuk key, value dalam data.items():
    tulis(f"{key}: {value}")

# Enumerate with unpacking
buah = ["apel", "jeruk", "mangga"]
untuk i, nama dalam enumerate(buah):
    tulis(f"{i + 1}. {nama}")

# Zip with unpacking
nama_list = ["Budi", "Ani"]
umur_list = [25, 22]
untuk nama, umur dalam zip(nama_list, umur_list):
    tulis(f"{nama} berumur {umur} tahun")
```

---

## 🔪 Slicing

```codingyok
angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
tulis(angka[2:5])    # [2, 3, 4]
tulis(angka[:3])     # [0, 1, 2] - from start
tulis(angka[5:])     # [5, 6, 7, 8, 9] - to end
tulis(angka[:])      # copy entire list

# Negative indices
tulis(angka[-3:])    # [7, 8, 9]
tulis(angka[:-2])    # [0, 1, 2, 3, 4, 5, 6, 7]

# With step
tulis(angka[::2])    # [0, 2, 4, 6, 8] - every 2nd
tulis(angka[::-1])   # [9, 8, 7, ...] - reverse

# Slice assignment
angka[2:5] = [20, 30, 40]  # replace slice
angka[2:2] = [100, 101]    # insert at position
angka[2:5] = []            # delete slice

# String slicing
teks = "Hello World"
tulis(teks[0:5])     # "Hello"
tulis(teks[::-1])    # "dlroW olleH"
```

---

## ❓ Ternary Expression

```codingyok
# Basic ternary (inline if-else)
hasil = "besar" jika x > 5 kalau_tidak "kecil"

# With numbers
maks = a jika a > b kalau_tidak b

# Nested ternary
grade = "A" jika nilai >= 90 kalau_tidak "B" jika nilai >= 80 kalau_tidak "C"

# In function call
tulis("positif" jika n > 0 kalau_tidak "negatif")

# In list comprehension
hasil = ["genap" jika n % 2 == 0 kalau_tidak "ganjil" untuk n dalam angka]
```

---

## 🦭 Walrus Operator

```codingyok
# Assignment expression - assign and return value
tulis((x := 10))  # prints 10, x is now 10

# In conditions
jika (n := panjang(data)) > 3:
    tulis(f"List punya {n} elemen")

# In while loops
selama (line := baca_baris()):
    tulis(line)

# With calculations
tulis(f"Total: {(total := a + b)}")
tulis(f"Variable: {total}")
```

---

## 🎯 Pattern Matching

```codingyok
fungsi get_grade(score):
    cocokkan score:
        kasus _ jika score >= 90:
            kembalikan "A"
        kasus _ jika score >= 80:
            kembalikan "B"
        kasus _ jika score >= 70:
            kembalikan "C"
        kasus _:
            kembalikan "D"
```

---

## 📦 Module System

```codingyok
# Import entire module
impor matematika
hasil = matematika.tambah(5, 3)

# Import with alias
impor matematika sebagai math
hasil = math.tambah(5, 3)

# Import specific names
dari matematika impor tambah, kali, PI
hasil = tambah(5, 3)
```

### Standard Library Modules
- `matematika` - Math functions (tambah, kurang, kali, bagi, pangkat, akar_kuadrat, faktorial, PI, E)
- `utilitas` - String utilities (balik_string, huruf_besar, huruf_kecil, cek_palindrom)

---

## λ Lambda Expressions

```codingyok
# Simple lambda
kuadrat = lambda x: x * x
tulis(kuadrat(5))  # 25

# Multiple parameters
tambah = lambda x, y: x + y
tulis(tambah(3, 4))  # 7

# With map/filter
angka = [1, 2, 3, 4, 5]
hasil = peta(lambda x: x * 2, angka)
tulis(daftar(hasil))  # [2, 4, 6, 8, 10]

# Closures
fungsi buat_pengali(n):
    kembalikan lambda x: x * n

kali_3 = buat_pengali(3)
tulis(kali_3(10))  # 30
```

---

## 🛡️ Exception Handling

```codingyok
# Basic try-except
coba:
    hasil = 10 / 0
kecuali ZeroDivisionError:
    tulis("Tidak boleh dibagi nol!")

# Multiple handlers
coba:
    nilai = int(data)
    hasil = 100 / nilai
kecuali ValueError:
    tulis("Data harus angka")
kecuali ZeroDivisionError:
    tulis("Tidak boleh nol")

# With finally
coba:
    file = buka_file("data.txt")
    data = file.baca()
kecuali FileNotFoundError:
    tulis("File tidak ditemukan")
akhirnya:
    tulis("Cleanup selesai")

# Raise exception
fungsi validasi_umur(umur):
    jika umur < 0:
        lempar ValueError("Umur tidak boleh negatif")
    kembalikan benar
```

---

## 🔐 Context Managers

```codingyok
# File handling
dengan buka_file("data.txt") sebagai f:
    isi = f.baca()
    tulis(isi)
# File otomatis ditutup

# Custom context manager
kelas Timer:
    fungsi __init__(diri, nama):
        diri.nama = nama
    
    fungsi __enter__(diri):
        tulis(f"Memulai {diri.nama}")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        tulis(f"Selesai {diri.nama}")
        kembalikan salah

dengan Timer("Operasi") sebagai t:
    tulis("Menjalankan...")
```

---

## 🏗️ Classes & OOP

```codingyok
kelas Hewan:
    fungsi __init__(diri, nama):
        diri.nama = nama
    
    fungsi suara(diri):
        tulis(f"{diri.nama} membuat suara")

kelas Kucing(Hewan):
    fungsi suara(diri):
        tulis(f"{diri.nama} mengeong")

kucing = Kucing("Kitty")
kucing.suara()  # Kitty mengeong
```

---

## 🇮🇩 Indonesian Features

```codingyok
# Currency formatting
tulis(format_rupiah(1500000))  # Rp 1.500.000

# Number to words
tulis(angka_ke_kata(1500))  # seribu lima ratus

# Date formatting
tulis(tanggal_indonesia())  # Senin, 15 Januari 2024

# Province data
tulis(cek_provinsi("jabar"))  # Jawa Barat

# Validation
tulis(validasi_nik("1234567890123456"))
tulis(validasi_email("user@example.com"))
```

---

## 📁 File I/O

```codingyok
# Text files
tulis_file("data.txt", "Hello!")
isi = baca_file("data.txt")

# JSON
data = {"nama": "Budi", "umur": 25}
tulis_json("data.json", data)
loaded = baca_json("data.json")

# CSV
csv_data = [["Nama", "Umur"], ["Budi", "25"]]
tulis_csv("data.csv", csv_data)
loaded = baca_csv("data.csv")

# Pattern matching
email = cari_pola(r'[\w\.-]+@[\w\.-]+\.\w+', text)
```

---

## 🌐 Web Framework

```codingyok
server = buat_server_web('localhost', 8080)

@server.route('/')
fungsi home(request):
    kembalikan "<h1>Hello CodingYok!</h1>"

@server.route('/api/data', 'POST')
fungsi api(request):
    kembalikan {"status": "success"}

server.run()
```

---

## 💡 Error Suggestions

```codingyok
nama = "Budi"
tulis(namaa)  # Typo!
```

Output:
```
Kesalahan Runtime: Nama 'namaa' tidak ditemukan
   Mungkin maksud Anda: nama
```

---

## 📚 Built-in Functions

| Function | Description |
|----------|-------------|
| `panjang(obj)` | Length of object |
| `tipe(obj)` | Type of object |
| `rentang(n)` | Range iterator |
| `masukan(prompt)` | User input |
| `int(val)`, `float(val)`, `str(val)` | Type conversion |
| `daftar(iter)`, `kamus()` | Create list/dict |
| `peta(func, iter)` | Map function |
| `saring(func, iter)` | Filter function |
| `jumlah(iter)` | Sum of iterable |
| `maksimum(iter)`, `minimum(iter)` | Max/min value |
| `urutkan(iter)` | Sort iterable |
| `balik(iter)` | Reverse iterable |
| `enumerate(iter)` | Enumerate with index |
| `zip(iter1, iter2)` | Zip iterables together |
| `abs(n)`, `bulat(n)` | Absolute/round |
| `akar(n)`, `pangkat(a, b)` | Math functions |
| `acak()`, `acak_int(a, b)` | Random numbers |
| `huruf_besar(s)`, `huruf_kecil(s)` | String case |
| `pisah(s)`, `gabung(sep, iter)` | String split/join |
| `waktu_sekarang()`, `tidur(s)` | Time functions |
| `cetak_tabel(data, header)` | Print table |
| `hitung_statistik(data)` | Statistics |

---

## 🔍 Examples

See `examples/` directory:
- `hello_world.cy` - Basic example
- `variabel_dan_tipe.cy` - Variables and types
- `kontrol_alur.cy` - Control flow
- `fungsi.cy` - Functions
- `kelas_dan_objek.cy` - OOP
- `v3_showcase.cy` - All v3 features
- `fitur_indonesia.cy` - Indonesian features
- `file_dan_data.cy` - File I/O
- `web_app.cy` - Web framework

---

**CodingYok** - *Coding jadi lebih asik dengan bahasa sendiri!* 🇮🇩
