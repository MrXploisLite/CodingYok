# 📚 CodingYok Module System

## Overview

CodingYok v2.0 introduces a powerful module system that allows you to organize your code into reusable modules. The module system supports:

- Basic imports with `impor`
- Aliased imports with `sebagai`
- Selective imports with `dari...impor`
- Module caching for performance
- Custom user modules
- Standard library modules

---

## 🎯 Basic Usage

### Import Entire Module

```codingyok
impor matematika

hasil = matematika.tambah(5, 3)
tulis(hasil)  # Output: 8

tulis(matematika.PI)  # Output: 3.141592653589793
```

### Import with Alias

```codingyok
impor utilitas sebagai util

teks = "hello world"
teks_besar = util.huruf_besar(teks)
tulis(teks_besar)  # Output: HELLO WORLD
```

### Import Specific Names

```codingyok
dari matematika impor tambah, kurang, PI

hasil1 = tambah(10, 5)
hasil2 = kurang(10, 5)
tulis(hasil1)  # Output: 15
tulis(hasil2)  # Output: 5
tulis(PI)      # Output: 3.141592653589793
```

### Import with Alias (Selective)

```codingyok
dari utilitas impor balik_string sebagai reverse

teks = reverse("CodingYok")
tulis(teks)  # Output: koYgnidoC
```

### Multiple Imports

```codingyok
dari matematika impor tambah, kurang, kali, bagi

tulis(tambah(10, 5))   # Output: 15
tulis(kurang(10, 5))   # Output: 5
tulis(kali(10, 5))     # Output: 50
tulis(bagi(10, 5))     # Output: 2
```

---

## 📦 Standard Library Modules

CodingYok comes with several built-in modules in the standard library:

### `matematika` Module

Mathematical functions and constants.

**Functions:**
- `tambah(a, b)` - Addition
- `kurang(a, b)` - Subtraction
- `kali(a, b)` - Multiplication
- `bagi(a, b)` - Division
- `pangkat(base, exp)` - Power/exponentiation
- `akar_kuadrat(n)` - Square root
- `faktorial(n)` - Factorial
- `absolut(n)` - Absolute value

**Constants:**
- `PI` - 3.141592653589793
- `E` - 2.718281828459045

**Example:**
```codingyok
dari matematika impor pangkat, akar_kuadrat, PI

tulis(pangkat(2, 10))      # Output: 1024
tulis(akar_kuadrat(144))   # Output: 12.0
tulis(PI * 2)              # Output: 6.283185307179586
```

### `utilitas` Module

String and text manipulation utilities.

**Functions:**
- `balik_string(s)` - Reverse a string
- `huruf_besar(s)` - Convert to uppercase
- `huruf_kecil(s)` - Convert to lowercase
- `jumlah_kata(s)` - Count words in string
- `hapus_spasi(s)` - Trim whitespace
- `ganti_karakter(s, lama, baru)` - Replace characters
- `cek_palindrom(s)` - Check if string is palindrome
- `gabung_list(separator, items)` - Join list items

**Example:**
```codingyok
dari utilitas impor huruf_besar, cek_palindrom

tulis(huruf_besar("hello"))        # Output: HELLO
tulis(cek_palindrom("radar"))      # Output: benar
tulis(cek_palindrom("hello"))      # Output: salah
```

---

## 🛠️ Creating Your Own Modules

### Step 1: Create a Module File

Create a file with `.cy` extension (e.g., `helper.cy`):

```codingyok
# file: helper.cy

fungsi sapa(nama):
    kembalikan f"Halo, {nama}! Selamat datang di CodingYok!"

fungsi hitung_luas_persegi(sisi):
    kembalikan sisi * sisi

fungsi hitung_luas_lingkaran(radius):
    PI = 3.14159
    kembalikan PI * radius * radius

kelas Kalkulator:
    fungsi __init__(diri):
        diri.hasil = 0
    
    fungsi tambah(diri, nilai):
        diri.hasil = diri.hasil + nilai
        kembalikan diri.hasil
    
    fungsi kurang(diri, nilai):
        diri.hasil = diri.hasil - nilai
        kembalikan diri.hasil

VERSI = "1.0.0"
```

### Step 2: Import and Use the Module

Create another file in the same directory (e.g., `main.cy`):

```codingyok
# file: main.cy

impor helper

# Use function from module
pesan = helper.sapa("Budi")
tulis(pesan)

# Use class from module
calc = helper.Kalkulator()
calc.tambah(10)
calc.tambah(5)
tulis(f"Hasil: {calc.hasil}")  # Output: Hasil: 15

# Use constant from module
tulis(f"Versi: {helper.VERSI}")  # Output: Versi: 1.0.0
```

### Step 3: Run the Main File

```bash
codingyok main.cy
```

---

## 🔍 Module Search Paths

CodingYok searches for modules in the following order:

1. **Current working directory** - Where you run the `codingyok` command
2. **Script directory** - Directory containing the main script
3. **Standard library** - Built-in modules in `src/codingyok/stdlib_modules/`

### Example Directory Structure

```
my_project/
├── main.cy          # Main script
├── helper.cy        # Custom module (same directory)
└── utils/
    └── tools.cy     # Module in subdirectory (not yet supported)
```

When you run `codingyok main.cy`, it can import `helper.cy` directly:

```codingyok
impor helper
```

---

## 💡 Best Practices

### 1. Module Naming

Use lowercase names with underscores for module files:

✅ Good:
- `matematika.cy`
- `utilitas_teks.cy`
- `helper.cy`

❌ Avoid:
- `Matematika.cy` (uppercase)
- `utilitas-teks.cy` (hyphens)
- `helper module.cy` (spaces)

### 2. Module Organization

Keep related functions together in a module:

```codingyok
# Good: file_utils.cy
fungsi baca_file(path):
    # ...

fungsi tulis_file(path, content):
    # ...

fungsi hapus_file(path):
    # ...
```

### 3. Selective Imports

Import only what you need:

```codingyok
# Better
dari matematika impor tambah, kurang

# Instead of
impor matematika
```

### 4. Module Documentation

Document your modules with comments:

```codingyok
# Module: helper
# Deskripsi: Fungsi-fungsi pembantu umum
# Versi: 1.0.0

fungsi sapa(nama):
    """Memberikan salam kepada pengguna"""
    kembalikan f"Halo, {nama}!"
```

---

## 🚨 Error Handling

### Module Not Found

```codingyok
impor module_tidak_ada
```

**Error:**
```
Kesalahan Runtime: Modul 'module_tidak_ada' tidak ditemukan.
Pastikan file 'module_tidak_ada.cy' ada di salah satu direktori: ...
```

**Solution:** Check that the module file exists and is in the correct location.

### Name Not Found in Module

```codingyok
dari matematika impor fungsi_tidak_ada
```

**Error:**
```
Kesalahan Runtime: Tidak dapat mengimpor 'fungsi_tidak_ada' dari modul 'matematika': 
nama tidak ditemukan
```

**Solution:** Check the module's available functions and names.

### Syntax Error in Module

If a module has syntax errors, you'll see:

```
Kesalahan Runtime: Gagal mem-parse modul 'my_module': [syntax error details]
```

**Solution:** Fix the syntax errors in the module file.

---

## 🎓 Advanced Examples

### Example 1: Math Library

```codingyok
# Create: math_lib.cy
fungsi rata_rata(numbers):
    total = 0
    untuk n dalam numbers:
        total = total + n
    kembalikan total / panjang(numbers)

fungsi median(numbers):
    sorted_nums = sorted(numbers)
    n = panjang(sorted_nums)
    jika n % 2 == 0:
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        kembalikan (mid1 + mid2) / 2
    kalau_tidak:
        kembalikan sorted_nums[n // 2]

# Use: main.cy
dari math_lib impor rata_rata, median

data = [1, 2, 3, 4, 5]
tulis(f"Rata-rata: {rata_rata(data)}")  # Output: Rata-rata: 3.0
tulis(f"Median: {median(data)}")        # Output: Median: 3
```

### Example 2: Text Processing

```codingyok
# Create: text_tools.cy
fungsi count_char(text, char):
    count = 0
    untuk c dalam text:
        jika c == char:
            count = count + 1
    kembalikan count

fungsi remove_duplicates(text):
    seen = {}
    result = ""
    untuk char dalam text:
        jika char bukan dalam seen:
            seen[char] = benar
            result = result + char
    kembalikan result

# Use: main.cy
impor text_tools sebagai tt

text = "hello world"
tulis(tt.count_char(text, "l"))       # Output: 3
tulis(tt.remove_duplicates(text))     # Output: helo wrd
```

### Example 3: Calculator Module with Classes

```codingyok
# Create: calculator.cy
kelas ScientificCalculator:
    fungsi __init__(diri):
        diri.memory = 0
    
    fungsi store(diri, value):
        diri.memory = value
    
    fungsi recall(diri):
        kembalikan diri.memory
    
    fungsi clear(diri):
        diri.memory = 0
    
    fungsi compute(diri, operation, a, b=0):
        cocokkan operation:
            kasus "add":
                kembalikan a + b
            kasus "subtract":
                kembalikan a - b
            kasus "multiply":
                kembalikan a * b
            kasus "divide":
                jika b == 0:
                    lempar Kesalahan("Division by zero")
                kembalikan a / b
            kasus _:
                lempar Kesalahan("Unknown operation")

# Use: main.cy
dari calculator impor ScientificCalculator

calc = ScientificCalculator()
hasil = calc.compute("multiply", 5, 3)
calc.store(hasil)
tulis(f"Hasil: {calc.recall()}")  # Output: Hasil: 15
```

---

## 📝 Module Caching

CodingYok caches modules after first import for performance. A module is only executed once, even if imported multiple times:

```codingyok
# This only executes module_x once
impor module_x
dari module_x impor func1
impor module_x sebagai mx
```

This means:
- ✅ Faster subsequent imports
- ✅ Shared state across imports
- ⚠️ Module initialization code runs only once

---

## 🔮 Future Enhancements

The following features are planned for future versions:

- **Package support** - Import modules from subdirectories
- **Relative imports** - Import from relative paths
- **Module reloading** - Reload modules during development
- **Binary modules** - Import Python modules
- **Module search path configuration** - Custom search paths

---

## 📚 Summary

The CodingYok module system provides:

- ✅ Clean code organization
- ✅ Code reusability
- ✅ Standard library modules
- ✅ Custom user modules
- ✅ Multiple import styles
- ✅ Module caching
- ✅ Indonesian-style syntax

Start organizing your code with modules today! 🎉

---

**For more information:**
- See `examples/test_modules.cy` for comprehensive examples
- See `examples/test_custom_module.cy` for custom module examples
- Check `src/codingyok/stdlib_modules/` for standard library modules
