# 🇮🇩 CodingYok - Bahasa Pemrograman Indonesia

![CodingYok Logo](https://img.shields.io/badge/CodingYok-v2.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**CodingYok** adalah bahasa pemrograman modern yang dirancang khusus untuk programmer Indonesia. Dengan syntax yang familiar seperti Python namun menggunakan kata kunci bahasa Indonesia, CodingYok membuat coding menjadi lebih mudah dan natural bagi developer Indonesia.

## 🎉 Apa yang Baru di v2.0?

- ✨ **List/Dict/Set Comprehensions** - Sintaks modern untuk pembuatan koleksi
- 🔄 **Generators dengan `hasilkan`** - Fungsi yang menghasilkan nilai secara lazy
- 🎯 **Pattern Matching `cocokkan/kasus`** - Pattern matching ala Python 3.10+
- 💡 **Error Messages yang Lebih Baik** - Saran "mungkin maksud Anda" untuk typo
- 📦 **Set Data Type** - Dukungan penuh untuk tipe data set

## ✨ Fitur Utama

### 🇮🇩 **Bahasa Indonesia First**
- **Keyword Indonesia**: `tulis`, `jika`, `untuk`, `selama`, `kelas`, `fungsi`, dll.
- **Error Messages**: Pesan error dalam bahasa Indonesia yang mudah dipahami
- **Built-in Indonesian Functions**: Format Rupiah, konversi angka ke kata, tanggal Indonesia

### 🚀 **Next-Generation Features**
- **Object-Oriented Programming**: Sistem kelas dengan inheritance
- **Exception Handling**: `coba`, `kecuali`, `akhirnya` untuk error handling
- **File I/O**: Operasi file dengan nama Indonesia (`baca_file`, `tulis_file`)
- **Web Framework**: Built-in web server dan HTTP client
- **Data Processing**: JSON, CSV, dan regex dengan interface Indonesia

### 📊 **Indonesian-Specific Features**
- **Format Rupiah**: `format_rupiah(1000000)` → "Rp 1.000.000"
- **Angka ke Kata**: `angka_ke_kata(1500)` → "seribu lima ratus"
- **Data Regional**: Database provinsi dan kota besar Indonesia
- **Validasi Indonesia**: NIK, nomor telepon, format Indonesia
- **Konversi Suhu**: Celsius, Fahrenheit, Kelvin dengan nama Indonesia

### 🛠️ **Developer Experience**
- **Rich Standard Library**: 100+ fungsi built-in dengan nama Indonesia
- **Pattern Matching**: Regex dengan interface yang mudah (`cari_pola`, `ganti_pola`)
- **Statistics**: Fungsi statistik built-in (`hitung_statistik`)
- **Table Printing**: Format tabel otomatis (`cetak_tabel`)
- **Modern Syntax**: Type hints dan modern programming patterns

## 🚀 Quick Start

### Instalasi
```bash
git clone https://github.com/MrXploisLite/CodingYok.git
cd CodingYok
pip install -e .
```

### Hello World
Buat file `hello.cy`:
```codingyok
tulis("Halo Dunia!")
tulis("Selamat datang di CodingYok!")
```

Jalankan:
```bash
codingyok hello.cy
```

## 📖 Contoh Kode

### Variabel dan Tipe Data
```codingyok
nama = "Budi"
umur = 25
tinggi = 175.5
sudah_menikah = salah

tulis(f"Nama: {nama}")
tulis(f"Umur: {umur} tahun")
```

### Kondisi
```codingyok
nilai = 85

jika nilai >= 90:
    tulis("Nilai A - Sangat Baik!")
kalau_tidak_jika nilai >= 80:
    tulis("Nilai B - Baik!")
kalau_tidak:
    tulis("Perlu belajar lebih giat!")
```

### Perulangan
```codingyok
# Perulangan untuk
untuk i dalam rentang(1, 6):
    tulis(f"Angka: {i}")

# Perulangan selama
counter = 0
selama counter < 5:
    tulis(f"Counter: {counter}")
    counter += 1
```

### Fungsi
```codingyok
fungsi sapa(nama, umur=20):
    tulis(f"Halo {nama}!")
    tulis(f"Umur kamu {umur} tahun ya?")
    kembalikan f"Salam kenal, {nama}!"

hasil = sapa("Siti", 22)
tulis(hasil)
```

### Kelas dan Inheritance
```codingyok
kelas Hewan:
    fungsi __init__(diri, nama):
        diri.nama = nama

    fungsi suara(diri):
        tulis(f"{diri.nama} membuat suara")

kelas Kucing(Hewan):
    fungsi suara(diri):
        tulis(f"{diri.nama} mengeong: Meow!")

    fungsi main(diri):
        tulis(f"{diri.nama} sedang bermain")

kucing = Kucing("Kitty")
kucing.suara()      # Output: Kitty mengeong: Meow!
kucing.main()       # Output: Kitty sedang bermain
```

### Comprehensions (NEW in v2.0!)
```codingyok
# List comprehension
angka = [1, 2, 3, 4, 5]
kuadrat = [x * x untuk x dalam angka]
tulis(kuadrat)  # Output: [1, 4, 9, 16, 25]

# List comprehension dengan kondisi
genap = [x untuk x dalam angka jika x % 2 == 0]
tulis(genap)  # Output: [2, 4]

# Dictionary comprehension
angka_dict = {x: x * x untuk x dalam rentang(1, 6)}
tulis(angka_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
set_unik = {x untuk x dalam [1, 2, 2, 3, 3, 4]}
tulis(set_unik)  # Output: {1, 2, 3, 4}
```

### Generators (NEW in v2.0!)
```codingyok
# Generator dengan hasilkan
fungsi fibonacci(n):
    a = 0
    b = 1
    counter = 0
    selama counter < n:
        hasilkan a
        temp = a
        a = b
        b = temp + b
        counter += 1

# Menggunakan generator
untuk angka dalam fibonacci(10):
    tulis(angka)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### Pattern Matching (NEW in v2.0!)
```codingyok
# Pattern matching sederhana
fungsi cek_nilai(nilai):
    cocokkan nilai:
        kasus _ jika nilai >= 90:
            tulis("A - Sangat Baik!")
        kasus _ jika nilai >= 80:
            tulis("B - Baik!")
        kasus _ jika nilai >= 70:
            tulis("C - Cukup")
        kasus _:
            tulis("Perlu belajar lebih giat")

cek_nilai(85)  # Output: B - Baik!

# Pattern matching dengan nilai spesifik
fungsi sapa(bahasa):
    cocokkan bahasa:
        kasus "indonesia":
            tulis("Halo!")
        kasus "english":
            tulis("Hello!")
        kasus _:
            tulis("Hi!")

sapa("indonesia")  # Output: Halo!
```

### Fitur Indonesia
```codingyok
# Format mata uang Rupiah
harga = 1500000
tulis(format_rupiah(harga))  # Output: Rp 1.500.000

# Konversi angka ke kata Indonesia
angka = 1500
tulis(angka_ke_kata(angka))  # Output: seribu lima ratus

# Tanggal Indonesia
tulis(tanggal_indonesia())   # Output: Senin, 15 Januari 2024

# Data provinsi Indonesia
tulis(cek_provinsi("jabar")) # Output: Jawa Barat
tulis(daftar_kota_besar()[:3]) # Output: ['Jakarta', 'Surabaya', 'Bandung']

# Validasi data Indonesia
tulis(validasi_nik("1234567890123456"))  # Output: benar
tulis(format_nomor_telepon("081234567890"))  # Output: 0812 3456 7890
```

### File I/O dan Data Processing
```codingyok
# Operasi file
tulis_file("data.txt", "Hello CodingYok!")
isi = baca_file("data.txt")
tulis(isi)  # Output: Hello CodingYok!

# JSON operations
data = {"nama": "Budi", "umur": 25, "kota": "Jakarta"}
tulis_json("person.json", data)
loaded = baca_json("person.json")
tulis(loaded["nama"])  # Output: Budi

# CSV operations
csv_data = [["Nama", "Umur"], ["Budi", "25"], ["Siti", "23"]]
tulis_csv("people.csv", csv_data)
loaded_csv = baca_csv("people.csv")
cetak_tabel(loaded_csv[1:], loaded_csv[0])  # Pretty table output

# Pattern matching
text = "Email: user@example.com, Phone: 081234567890"
email = cari_pola(r'[\w\.-]+@[\w\.-]+\.\w+', text)
tulis(email)  # Output: user@example.com
```

### Web Application
```codingyok
# Buat web server sederhana
server = buat_server_web('localhost', 8080)

@server.route('/')
fungsi halaman_utama(request):
    kembalikan """
    <h1>Selamat Datang di CodingYok Web!</h1>
    <p>Server web dengan bahasa Indonesia</p>
    """

@server.route('/api/data', 'POST')
fungsi handle_data(request):
    data = request.get('json', {})
    kembalikan {
        'status': 'success',
        'message': f"Data diterima: {data}"
    }

# Jalankan server
server.run()  # Akses di http://localhost:8080
```

## 🛠️ Pengembangan

### Setup Development Environment
```bash
# Clone repository
git clone https://github.com/MrXploisLite/CodingYok.git
cd CodingYok

# Install dependencies
pip install -r requirements-dev.txt

# Install in development mode
pip install -e .

# Run tests
pytest tests/
```

### Struktur Project
```
CodingYok/
├── src/codingyok/          # Core interpreter
│   ├── lexer.py           # Tokenizer
│   ├── parser.py          # AST Parser
│   ├── interpreter.py     # Code executor
│   └── stdlib/            # Standard library
├── examples/              # Example .cy files
├── tests/                 # Unit tests
├── docs/                  # Documentation
└── tools/                 # Development tools
```

## 📚 Dokumentasi

- [Tutorial Lengkap](docs/tutorial.md)
- [Referensi Bahasa](docs/language-reference.md)
- [Standard Library](docs/stdlib.md)
- [Panduan Kontribusi](CONTRIBUTING.md)

## 🤝 Kontribusi

Kami sangat welcome kontribusi dari komunitas! Silakan baca [CONTRIBUTING.md](CONTRIBUTING.md) untuk panduan kontribusi.

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Lihat [LICENSE](LICENSE) untuk detail lengkap.

## 🙏 Acknowledgments

- Terinspirasi dari Python dan bahasa pemrograman modern lainnya
- Dibuat dengan ❤️ untuk komunitas developer Indonesia

---

**CodingYok** - *Coding jadi lebih asik dengan bahasa sendiri!* 🇮🇩
