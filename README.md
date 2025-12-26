# 🇮🇩 CodingYok

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/MrXploisLite/CodingYok)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

**Bahasa pemrograman modern dengan syntax Indonesia.** Dibuat untuk developer Indonesia yang ingin belajar programming dengan bahasa yang familiar.

## ✨ Highlights

- � 🇩 **Full Indonesian** - Keywords, error messages, dan built-in functions dalam Bahasa Indonesia
- � ***Python-like** - Syntax familiar, mudah dipelajari
- � **Mondern Features** - Lambda, generators, pattern matching, exception handling
- 📦 **Module System** - Organize code dengan `impor` dan `dari...impor`
- 🌐 **Built-in Web** - HTTP server dan client included

## � Quick Stairt

```bash
# Install
git clone https://github.com/MrXploisLite/CodingYok.git
cd CodingYok
pip install -e .

# Run
codingyok hello.cy
```

## 📝 Hello World

```python
# hello.cy
tulis("Halo Dunia!")

nama = masukan("Siapa nama kamu? ")
tulis(f"Selamat datang, {nama}!")
```

## 🎯 Syntax Overview

```python
# Variables
nama = "Budi"
umur = 25
aktif = benar

# Conditions
jika umur >= 18:
    tulis("Dewasa")
kalau_tidak:
    tulis("Anak-anak")

# Loops
untuk i dalam rentang(5):
    tulis(i)

selama aktif:
    tulis("Running...")
    berhenti

# Functions
fungsi sapa(nama):
    kembalikan f"Halo, {nama}!"

# Classes
kelas Orang:
    fungsi __init__(diri, nama):
        diri.nama = nama

# Lambda
kuadrat = lambda x: x * x

# Exception Handling
coba:
    hasil = 10 / 0
kecuali ZeroDivisionError:
    tulis("Error!")
akhirnya:
    tulis("Done")

# Context Manager
dengan buka_file("data.txt") sebagai f:
    data = f.baca()

# List Comprehension
squares = [x * x untuk x dalam rentang(10)]

# Pattern Matching
cocokkan nilai:
    kasus 1:
        tulis("Satu")
    kasus _:
        tulis("Lainnya")
```

## 🇮🇩 Indonesian Features

```python
# Currency
tulis(format_rupiah(1500000))  # Rp 1.500.000

# Number to words
tulis(angka_ke_kata(1500))  # seribu lima ratus

# Date
tulis(tanggal_indonesia())  # Senin, 15 Januari 2024

# Validation
validasi_nik("1234567890123456")
validasi_email("user@email.com")
```

## 📦 Modules

```python
# Import module
impor matematika
hasil = matematika.tambah(5, 3)

# Import specific
dari matematika impor PI, pangkat
tulis(pangkat(2, 10))
```

## 📚 Documentation

- [FEATURES.md](FEATURES.md) - Complete feature reference
- [MODULE_SYSTEM.md](MODULE_SYSTEM.md) - Module system guide
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [examples/](examples/) - Example programs

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

MIT License - see [LICENSE](LICENSE)

---

<p align="center">
  <b>CodingYok</b> - Coding jadi lebih asik! 🇮🇩
</p>
