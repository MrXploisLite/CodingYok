# 🚀 Migration Guide: CodingYok v1.0 → v2.0

Welcome to CodingYok v2.0! This guide will help you understand the new features and how to upgrade your codebase.

## 📋 Table of Contents

1. [What's New](#whats-new)
2. [Backward Compatibility](#backward-compatibility)
3. [New Features Guide](#new-features-guide)
4. [Best Practices](#best-practices)
5. [Performance Tips](#performance-tips)

---

## What's New

CodingYok v2.0 introduces powerful modern programming features:

### Major Features

✨ **Comprehensions** - Concise syntax for creating collections  
🔄 **Generators** - Memory-efficient iterators with `hasilkan`  
🎯 **Pattern Matching** - Clean conditional logic with `cocokkan/kasus`  
💡 **Better Errors** - "Did you mean" suggestions for typos  
📦 **Sets** - Native set data type with literals and comprehensions  

---

## Backward Compatibility

✅ **100% Backward Compatible** - All v1.0 code runs unchanged in v2.0

No breaking changes were introduced. Your existing code will continue to work exactly as before.

---

## New Features Guide

### 1. List Comprehensions

**Before (v1.0):**
```codingyok
# Creating a list of squares
angka = [1, 2, 3, 4, 5]
kuadrat = []
untuk x dalam angka:
    kuadrat.append(x * x)
```

**After (v2.0):**
```codingyok
# More concise with comprehension
angka = [1, 2, 3, 4, 5]
kuadrat = [x * x untuk x dalam angka]
```

**With Conditions:**
```codingyok
# Filter even numbers and square them
genap_kuadrat = [x * x untuk x dalam angka jika x % 2 == 0]
# Result: [4, 16]
```

**Use When:**
- ✅ Creating lists from existing iterables
- ✅ Filtering and transforming data in one step
- ✅ Code readability is improved

**Avoid When:**
- ❌ Logic is too complex (use regular loops)
- ❌ Need multiple statements per iteration
- ❌ Side effects are needed (use for loops)

---

### 2. Dictionary Comprehensions

**Before (v1.0):**
```codingyok
# Creating a mapping
angka = [1, 2, 3, 4, 5]
kuadrat_dict = {}
untuk x dalam angka:
    kuadrat_dict[x] = x * x
```

**After (v2.0):**
```codingyok
# Cleaner with dict comprehension
kuadrat_dict = {x: x * x untuk x dalam angka}
```

**Practical Examples:**
```codingyok
# Convert list of tuples to dict
data = [("a", 1), ("b", 2), ("c", 3)]
dict_data = {k: v untuk k, v dalam data}

# Create lookup table
produk = ["Laptop", "Mouse", "Keyboard"]
harga = [10000000, 150000, 500000]
katalog = {p: h untuk p, h dalam zip(produk, harga)}

# Filter and transform
data = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v * 2 untuk k, v dalam data.items() jika v > 2}
```

---

### 3. Set Comprehensions

**New in v2.0:**
```codingyok
# Create set of unique squares
angka = [1, 2, 2, 3, 3, 4, 4, 5]
squares_set = {x * x untuk x dalam angka}
# Result: {1, 4, 9, 16, 25}

# Remove duplicates with filtering
words = ["hello", "world", "hello", "python", "world"]
unique_long = {w untuk w dalam words jika panjang(w) > 4}
# Result: {"hello", "world", "python"}
```

**Set Literals:**
```codingyok
# Before: Had to use set() function
my_set = set([1, 2, 3])

# After: Direct literal syntax
my_set = {1, 2, 3}
```

---

### 4. Generators

**Before (v1.0):**
```codingyok
# Return entire list (memory intensive)
fungsi get_numbers(n):
    result = []
    untuk i dalam rentang(n):
        result.append(i * i)
    kembalikan result

# Memory: O(n)
numbers = get_numbers(1000000)  # Uses a lot of memory!
```

**After (v2.0):**
```codingyok
# Generator yields values one at a time
fungsi get_numbers(n):
    untuk i dalam rentang(n):
        hasilkan i * i

# Memory: O(1) - values generated on demand
numbers = get_numbers(1000000)  # Minimal memory!
untuk num dalam numbers:
    tulis(num)
```

**Real-World Examples:**

```codingyok
# Reading large files
fungsi read_large_file(filename):
    file = buka_file(filename, "r")
    selama benar:
        line = file.readline()
        jika bukan line:
            berhenti
        hasilkan line.strip()

# Infinite sequence
fungsi fibonacci():
    a, b = 0, 1
    selama benar:
        hasilkan a
        a, b = b, a + b

# Take first 10 fibonacci numbers
counter = 0
untuk num dalam fibonacci():
    tulis(num)
    counter += 1
    jika counter >= 10:
        berhenti

# Data pipeline
fungsi process_data(data):
    untuk item dalam data:
        jika item > 0:
            hasilkan item * 2

fungsi filter_large(data):
    untuk item dalam data:
        jika item > 100:
            hasilkan item

# Chain generators
raw_data = [-5, 10, 50, 200, -3, 150]
processed = process_data(raw_data)
filtered = filter_large(processed)
hasil = list(filtered)  # [400, 300]
```

**When to Use Generators:**
- ✅ Processing large datasets
- ✅ Infinite sequences
- ✅ Pipeline processing
- ✅ Memory-constrained environments

---

### 5. Pattern Matching

**Before (v1.0):**
```codingyok
# Long if-elif chains
fungsi get_grade(score):
    jika score >= 90:
        kembalikan "A"
    kalau_tidak_jika score >= 80:
        kembalikan "B"
    kalau_tidak_jika score >= 70:
        kembalikan "C"
    kalau_tidak_jika score >= 60:
        kembalikan "D"
    kalau_tidak:
        kembalikan "F"
```

**After (v2.0):**
```codingyok
# Cleaner with pattern matching
fungsi get_grade(score):
    cocokkan score:
        kasus _ jika score >= 90:
            kembalikan "A"
        kasus _ jika score >= 80:
            kembalikan "B"
        kasus _ jika score >= 70:
            kembalikan "C"
        kasus _ jika score >= 60:
            kembalikan "D"
        kasus _:
            kembalikan "F"
```

**Matching Specific Values:**
```codingyok
fungsi process_command(cmd):
    cocokkan cmd:
        kasus "start":
            tulis("Starting...")
        kasus "stop":
            tulis("Stopping...")
        kasus "restart":
            tulis("Restarting...")
        kasus _:
            tulis("Unknown command")
```

**With Guards:**
```codingyok
fungsi categorize(value):
    cocokkan value:
        kasus 0:
            kembalikan "zero"
        kasus _ jika value < 0:
            kembalikan "negative"
        kasus _ jika value % 2 == 0:
            kembalikan "even positive"
        kasus _:
            kembalikan "odd positive"
```

---

### 6. Better Error Messages

**Before (v1.0):**
```
Kesalahan Runtime: Nama 'tuless' tidak ditemukan
```

**After (v2.0):**
```
Kesalahan Runtime: Nama 'tuless' tidak ditemukan
   Mungkin maksud Anda: tulis, tulis_file
```

The interpreter now suggests similar names when you make a typo!

---

## Best Practices

### Comprehensions

✅ **DO:**
```codingyok
# Simple, readable transformations
squares = [x * x untuk x dalam numbers]
even_only = [x untuk x dalam numbers jika x % 2 == 0]
```

❌ **DON'T:**
```codingyok
# Too complex - use regular loop instead
complex = [func1(func2(x, y), func3(z)) untuk x, y, z dalam data jika condition1(x) dan condition2(y) atau condition3(z)]
```

### Generators

✅ **DO:**
```codingyok
# Use for large datasets
fungsi read_logs(filename):
    untuk line dalam read_file_lines(filename):
        hasilkan parse_log(line)

# Chain generators for pipelines
hasil = process_stage3(process_stage2(process_stage1(data)))
```

❌ **DON'T:**
```codingyok
# Don't use for small lists (overhead)
fungsi get_three_numbers():
    hasilkan 1
    hasilkan 2
    hasilkan 3
# Better: kembalikan [1, 2, 3]
```

### Pattern Matching

✅ **DO:**
```codingyok
# Use for clear categorization
cocokkan user_type:
    kasus "admin":
        grant_admin_access()
    kasus "user":
        grant_user_access()
    kasus _:
        deny_access()
```

❌ **DON'T:**
```codingyok
# Don't use for simple if-else
cocokkan x:
    kasus _ jika x > 0:
        do_something()
    kasus _:
        do_other()
# Better: jika x > 0: do_something() kalau_tidak: do_other()
```

---

## Performance Tips

### List Comprehensions vs Loops

```codingyok
# Comprehensions are typically 20-30% faster
import time

# Method 1: Loop
start = time.time()
result = []
untuk i dalam rentang(1000000):
    result.append(i * 2)
tulis(f"Loop: {time.time() - start}")

# Method 2: Comprehension (FASTER!)
start = time.time()
result = [i * 2 untuk i dalam rentang(1000000)]
tulis(f"Comprehension: {time.time() - start}")
```

### Generator Memory Efficiency

```codingyok
# List: Stores all items (high memory)
import sys
big_list = [i untuk i dalam rentang(1000000)]
tulis(f"List size: {sys.getsizeof(big_list)} bytes")

# Generator: Stores state only (low memory)
big_gen = (i untuk i dalam rentang(1000000))
tulis(f"Generator size: {sys.getsizeof(big_gen)} bytes")
# Generator is ~200x smaller!
```

---

## Summary

✅ **All v1.0 code works in v2.0**  
✅ **New features are optional but recommended**  
✅ **Better performance with comprehensions**  
✅ **Lower memory with generators**  
✅ **Clearer code with pattern matching**  
✅ **Fewer typos with better errors**  

Start adopting v2.0 features incrementally. Happy coding! 🎉

---

**Questions?** Check the [documentation](docs/) or [examples](examples/fitur_baru.cy)
