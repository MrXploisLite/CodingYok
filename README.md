# 🇮🇩 CodingYok - Bahasa Pemrograman Indonesia

![CodingYok Logo](https://img.shields.io/badge/CodingYok-v1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**CodingYok** adalah bahasa pemrograman modern yang dirancang khusus untuk programmer Indonesia. Dengan syntax yang familiar seperti Python namun menggunakan kata kunci bahasa Indonesia, CodingYok membuat coding menjadi lebih mudah dan natural bagi developer Indonesia.

## ✨ Fitur Utama

- 🇮🇩 **Keyword Bahasa Indonesia**: `tulis`, `jika`, `untuk`, `selama`, dll.
- 🚀 **Next-Generation Features**: Built-in async/await, modern error handling
- 📅 **Indonesian Localization**: Format tanggal, angka, dan mata uang Indonesia
- 🔧 **Easy to Learn**: Syntax yang familiar bagi pengguna Python
- 📚 **Rich Standard Library**: Library lengkap dengan fokus kebutuhan Indonesia
- 🌐 **Modern Web Support**: Built-in web scraping dan HTTP client

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

### Kelas
```codingyok
kelas Mahasiswa:
    fungsi __init__(diri, nama, nim):
        diri.nama = nama
        diri.nim = nim
        diri.nilai = []
    
    fungsi tambah_nilai(diri, nilai):
        diri.nilai.tambah(nilai)
    
    fungsi rata_rata(diri):
        jika len(diri.nilai) == 0:
            kembalikan 0
        kembalikan sum(diri.nilai) / len(diri.nilai)

mhs = Mahasiswa("Ahmad", "12345")
mhs.tambah_nilai(85)
mhs.tambah_nilai(90)
tulis(f"Rata-rata: {mhs.rata_rata()}")
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
