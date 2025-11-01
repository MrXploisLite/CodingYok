# CodingYok v3.0 - Complete Feature Reference

## 🎉 Overview

CodingYok v3.0 is a major milestone that brings professional-grade features to the Indonesian programming language. This release focuses on advanced language features essential for enterprise development: lambda expressions, comprehensive exception handling, and context managers.

---

## 📊 Feature Comparison

| Feature | v2.0 | v3.0 |
|---------|------|------|
| Lambda Expressions | ❌ | ✅ |
| Exception Handling (coba/kecuali) | ❌ | ✅ |
| Finally Blocks | ❌ | ✅ |
| Raise Statement | ❌ | ✅ |
| Context Managers (dengan) | ❌ | ✅ |
| Custom Exceptions | ❌ | ✅ |
| List Comprehensions | ✅ | ✅ |
| Generators (yield) | ✅ | ✅ |
| Pattern Matching | ✅ | ✅ |
| Module System | ✅ | ✅ |

---

## 🆕 New Keywords

```
# v3.0 now implements:
lambda      - Lambda expressions (anonymous functions)
coba        - Try (exception handling) - NOW IMPLEMENTED
kecuali     - Except (exception handling) - NOW IMPLEMENTED
akhirnya    - Finally (exception handling) - NOW IMPLEMENTED
lempar      - Raise (throw exceptions) - NOW IMPLEMENTED
dengan      - With (context managers) - NOW IMPLEMENTED
```

---

## 📝 Lambda Expressions

### Basic Syntax

```codingyok
lambda parameters: expression
```

### Examples

**Simple Lambda:**
```codingyok
# Single parameter
kuadrat = lambda x: x * x
tulis(kuadrat(5))  # Output: 25

# Multiple parameters
tambah = lambda x, y: x + y
tulis(tambah(3, 4))  # Output: 7

# No parameters
sapa = lambda: tulis("Halo!")
sapa()  # Output: Halo!
```

**Lambda with Higher-Order Functions:**
```codingyok
# Map
angka = [1, 2, 3, 4, 5]
hasil = peta(lambda x: x * 2, angka)
tulis(list(hasil))  # Output: [2, 4, 6, 8, 10]

# Filter
genap = filter(lambda x: x % 2 == 0, angka)
tulis(list(genap))  # Output: [2, 4]

# Sorted with key
data = [
    {"nama": "Budi", "nilai": 85},
    {"nama": "Ani", "nilai": 92},
    {"nama": "Citra", "nilai": 78}
]
sorted_data = sorted(data, key=lambda x: x["nilai"], reverse=benar)
```

**Lambda Closures:**
```codingyok
fungsi buat_penambah(n):
    """Create a function that adds n to its argument"""
    kembalikan lambda x: x + n

tambah_10 = buat_penambah(10)
tambah_5 = buat_penambah(5)

tulis(tambah_10(3))  # Output: 13
tulis(tambah_5(3))   # Output: 8

# Closure with mutable state (using list)
fungsi buat_counter():
    count = [0]
    kembalikan lambda: count.__setitem__(0, count[0] + 1) atau count[0]

counter = buat_counter()
tulis(counter())  # 1
tulis(counter())  # 2
tulis(counter())  # 3
```

**Lambda in List Comprehensions:**
```codingyok
# Create list of functions
operations = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]

nilai = 5
hasil = [op(nilai) untuk op dalam operations]
tulis(hasil)  # Output: [6, 10, 25]
```

---

## 🛡️ Exception Handling

### Try-Except Syntax

```codingyok
coba:
    # Code that might raise exception
kecuali ExceptionType sebagai variable:
    # Handle specific exception
kecuali:
    # Handle any exception
akhirnya:
    # Always executed
```

### Basic Exception Handling

```codingyok
# Simple try-except
coba:
    angka = int("tidak valid")
kecuali:
    tulis("Terjadi error!")

# With exception type
coba:
    hasil = 10 / 0
kecuali ZeroDivisionError:
    tulis("Tidak boleh dibagi nol!")

# Capture exception variable
coba:
    nilai = int("abc")
kecuali ValueError sebagai e:
    tulis(f"Error konversi: {e}")
```

### Multiple Exception Handlers

```codingyok
fungsi proses_data(data):
    coba:
        nilai = int(data)
        hasil = 100 / nilai
        kembalikan hasil
    kecuali ValueError:
        tulis("Data harus berupa angka")
        kembalikan kosong
    kecuali ZeroDivisionError:
        tulis("Nilai tidak boleh nol")
        kembalikan kosong
    kecuali:
        tulis("Terjadi error yang tidak diketahui")
        kembalikan kosong
```

### Finally Block

```codingyok
# Finally always executes
fungsi baca_file(nama_file):
    file = kosong
    coba:
        file = buka_file(nama_file)
        data = file.baca()
        kembalikan data
    kecuali FileNotFoundError:
        tulis(f"File {nama_file} tidak ditemukan")
        kembalikan kosong
    akhirnya:
        jika file:
            file.tutup()
        tulis("Pembersihan selesai")
```

### Raising Exceptions

```codingyok
# Raise with string message
fungsi validasi_umur(umur):
    jika umur < 0:
        lempar ValueError("Umur tidak boleh negatif")
    jika umur > 150:
        lempar ValueError("Umur tidak wajar")
    kembalikan benar

# Raise in except block
coba:
    nilai = int(input("Masukkan angka: "))
    jika nilai < 0:
        lempar ValueError("Angka harus positif")
kecuali ValueError sebagai e:
    tulis(f"Error: {e}")
    lempar  # Re-raise the exception
```

### Custom Exception Classes

```codingyok
# Define custom exception
kelas EmailTidakValidError(ValueError):
    fungsi __init__(diri, email):
        diri.email = email
        diri.pesan = f"Email tidak valid: {email}"
    
    fungsi __str__(diri):
        kembalikan diri.pesan

# Use custom exception
fungsi validasi_email(email):
    jika bukan "@" dalam email:
        lempar EmailTidakValidError(email)
    kembalikan benar

coba:
    validasi_email("user.example.com")
kecuali EmailTidakValidError sebagai e:
    tulis(e)  # Output: Email tidak valid: user.example.com
```

### Exception Handling Patterns

```codingyok
# Pattern 1: Retry with limit
fungsi fetch_data_with_retry(url, max_retries=3):
    retries = 0
    selama retries < max_retries:
        coba:
            data = http_get(url)
            kembalikan data
        kecuali NetworkError sebagai e:
            retries += 1
            tulis(f"Retry {retries}/{max_retries}")
            jika retries >= max_retries:
                lempar
    kembalikan kosong

# Pattern 2: Resource cleanup
fungsi proses_dengan_cleanup():
    resource = kosong
    coba:
        resource = acquire_resource()
        result = process(resource)
        kembalikan result
    kecuali ProcessingError sebagai e:
        tulis(f"Error processing: {e}")
        kembalikan kosong
    akhirnya:
        jika resource:
            release_resource(resource)

# Pattern 3: Converting exceptions
fungsi safe_division(a, b):
    coba:
        kembalikan a / b
    kecuali ZeroDivisionError:
        lempar ValueError("Divisor tidak boleh nol")
```

---

## 🔐 Context Managers (dengan Statement)

### Basic Syntax

```codingyok
dengan expression sebagai variable:
    # Code block
    # Automatic cleanup after block
```

### File Operations

```codingyok
# Simple file reading
dengan buka_file("data.txt") sebagai f:
    isi = f.baca()
    tulis(isi)
# File automatically closed

# File writing
dengan buka_file("output.txt", "w") sebagai f:
    f.tulis("Hello, World!")
    f.tulis("Ini baris kedua")

# Reading lines
dengan buka_file("data.txt") sebagai f:
    untuk baris dalam f.baca_baris():
        tulis(baris.strip())
```

### Custom Context Managers

```codingyok
# Class-based context manager
kelas Timer:
    fungsi __init__(diri, name):
        diri.name = name
        diri.start_time = kosong
    
    fungsi __enter__(diri):
        diri.start_time = waktu_sekarang()
        tulis(f"Memulai {diri.name}...")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        elapsed = waktu_sekarang() - diri.start_time
        tulis(f"{diri.name} selesai dalam {elapsed} detik")
        kembalikan salah  # Don't suppress exceptions

# Using custom context manager
dengan Timer("Operasi Database") sebagai timer:
    # Perform operations
    tulis("Melakukan query...")
    # Auto-prints elapsed time when done
```

### Database Connection Example

```codingyok
kelas DatabaseConnection:
    fungsi __init__(diri, host, port):
        diri.host = host
        diri.port = port
        diri.connection = kosong
    
    fungsi __enter__(diri):
        tulis(f"Menghubungkan ke {diri.host}:{diri.port}...")
        diri.connection = connect_to_db(diri.host, diri.port)
        kembalikan diri.connection
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        jika diri.connection:
            tulis("Menutup koneksi database...")
            diri.connection.close()
        kembalikan salah

# Usage
dengan DatabaseConnection("localhost", 5432) sebagai conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
# Connection automatically closed
```

### Nested Context Managers

```codingyok
# Multiple context managers
dengan buka_file("input.txt") sebagai input_file:
    dengan buka_file("output.txt", "w") sebagai output_file:
        untuk baris dalam input_file.baca_baris():
            output_file.tulis(baris.upper())

# Complex nesting
dengan DatabaseConnection("localhost", 5432) sebagai db:
    dengan db.transaction() sebagai trans:
        dengan Timer("Batch Insert") sebagai timer:
            untuk item dalam data:
                db.insert(item)
            trans.commit()
```

### Context Manager for Temporary State

```codingyok
kelas TemporaryDirectory:
    fungsi __init__(diri, prefix="tmp"):
        diri.prefix = prefix
        diri.path = kosong
    
    fungsi __enter__(diri):
        diri.path = buat_temp_dir(diri.prefix)
        tulis(f"Created temp dir: {diri.path}")
        kembalikan diri.path
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        jika diri.path:
            hapus_dir(diri.path)
            tulis(f"Removed temp dir: {diri.path}")
        kembalikan salah

# Usage
dengan TemporaryDirectory() sebagai temp_dir:
    temp_file = f"{temp_dir}/data.txt"
    tulis_file(temp_file, "temporary data")
    # Process file...
# Temp directory automatically deleted
```

---

## 🎯 Use Cases

### Lambda Expressions

**Good For:**
- ✅ Short, one-line functions
- ✅ Higher-order functions (map, filter, sorted)
- ✅ Functional programming patterns
- ✅ Callback functions
- ✅ Simple transformations

**Avoid For:**
- ❌ Complex logic requiring multiple statements
- ❌ Functions needing documentation
- ❌ Recursive functions
- ❌ Functions used in multiple places

### Exception Handling

**Good For:**
- ✅ File I/O operations
- ✅ Network requests
- ✅ Database operations
- ✅ User input validation
- ✅ Resource allocation
- ✅ External API calls

**Best Practices:**
```codingyok
# DO: Catch specific exceptions
coba:
    nilai = int(input_data)
kecuali ValueError:
    tulis("Invalid number")

# DON'T: Catch all exceptions without reason
coba:
    risky_operation()
kecuali:
    lewati  # Bad: silently ignores all errors

# DO: Use finally for cleanup
coba:
    file = buka_file("data.txt")
    process(file)
akhirnya:
    file.tutup()

# DO: Re-raise when appropriate
coba:
    critical_operation()
kecuali DatabaseError sebagai e:
    log_error(e)
    lempar  # Re-raise for caller to handle
```

### Context Managers

**Good For:**
- ✅ File operations
- ✅ Database connections
- ✅ Network sockets
- ✅ Locks and synchronization
- ✅ Temporary state changes
- ✅ Resource pooling

**Real-World Examples:**
```codingyok
# File operations
dengan buka_file("config.json") sebagai f:
    config = json_decode(f.baca())

# Database transactions
dengan database.transaction() sebagai trans:
    trans.execute("INSERT INTO ...")
    trans.execute("UPDATE ...")
    trans.commit()

# Timing operations
dengan Timer("API Call"):
    response = http_get("https://api.example.com")

# Temporary configuration
dengan override_config({"debug": benar}):
    run_tests()
# Original config restored
```

---

## 💡 Advanced Patterns

### Combining Features

```codingyok
# Lambda + Exception Handling
safe_operations = [
    lambda x: x / 2,
    lambda x: x ** 2,
    lambda x: 1 / x  # Might raise ZeroDivisionError
]

fungsi apply_safe(operations, nilai):
    hasil = []
    untuk op dalam operations:
        coba:
            hasil.append(op(nilai))
        kecuali ZeroDivisionError:
            hasil.append(kosong)
    kembalikan hasil

# Context Manager + Exception Handling
dengan DatabaseConnection("localhost", 5432) sebagai conn:
    coba:
        dengan conn.transaction() sebagai trans:
            trans.execute("UPDATE users SET ...")
            trans.commit()
    kecuali DatabaseError sebagai e:
        tulis(f"Transaction failed: {e}")
        # Transaction auto-rolled back by context manager

# Lambda + Context Manager
dengan TemporaryFile() sebagai temp:
    processor = lambda data: temp.tulis(encrypt(data))
    untuk chunk dalam large_file:
        processor(chunk)
```

### Functional Programming with Lambda

```codingyok
# Composition
compose = lambda f, g: lambda x: f(g(x))

tambah_1 = lambda x: x + 1
kali_2 = lambda x: x * 2

# Create new function: (x * 2) + 1
transform = compose(tambah_1, kali_2)
tulis(transform(5))  # Output: 11

# Pipeline processing
pipeline = [
    lambda x: x.strip(),
    lambda x: x.lower(),
    lambda x: x.replace(" ", "_")
]

fungsi apply_pipeline(data, pipeline):
    result = data
    untuk func dalam pipeline:
        result = func(result)
    kembalikan result

slug = apply_pipeline("  Hello World  ", pipeline)
tulis(slug)  # Output: "hello_world"
```

---

## 🚀 Performance Considerations

### Lambda Performance
- Lambda functions have minimal overhead
- Similar performance to regular functions for simple operations
- Slightly slower for complex closures due to variable capture
- Best for short-lived, simple operations

### Exception Handling Performance
- Try-except blocks have negligible cost when no exception occurs
- Raising and catching exceptions is expensive
- Use exceptions for exceptional cases, not control flow
- Consider validation before expensive operations

### Context Manager Performance
- Minimal overhead for resource management
- Much safer than manual cleanup
- Prevents resource leaks
- Recommended for all resource operations

---

## 📚 Migration from v2.0

### What Changed
- **Lambda**: New feature, no breaking changes
- **Exception Handling**: Previously defined but not implemented, now fully functional
- **Context Managers**: Previously defined but not implemented, now fully functional

### Updating Existing Code
```codingyok
# v2.0: Manual resource cleanup
file = buka_file("data.txt")
data = file.baca()
file.tutup()

# v3.0: Automatic cleanup with context manager
dengan buka_file("data.txt") sebagai file:
    data = file.baca()

# v2.0: Manual error checking
fungsi divide(a, b):
    jika b == 0:
        tulis("Error: division by zero")
        kembalikan kosong
    kembalikan a / b

# v3.0: Exception handling
fungsi divide(a, b):
    coba:
        kembalikan a / b
    kecuali ZeroDivisionError:
        tulis("Error: division by zero")
        lempar

# v2.0: Named function for simple operation
fungsi kuadrat(x):
    kembalikan x * x

data = peta(kuadrat, angka)

# v3.0: Lambda for simple operation
data = peta(lambda x: x * x, angka)
```

---

## ✅ Best Practices

1. **Use Lambda for Simple Functions**
   - One-line expressions only
   - No complex logic
   - Clear and readable

2. **Catch Specific Exceptions**
   - Don't use bare `kecuali:`
   - Catch only what you can handle
   - Re-raise when appropriate

3. **Always Use Context Managers for Resources**
   - Files, connections, locks
   - Prevents resource leaks
   - Cleaner code

4. **Use Finally for Critical Cleanup**
   - Release locks
   - Close connections
   - Log completion

5. **Don't Suppress Exceptions Silently**
   - Log errors
   - Provide feedback
   - Handle appropriately

---

## 🔍 Examples and Testing

See the `examples/` directory for complete working examples:
- `lambda_examples.cy` - Lambda expression patterns
- `exception_handling.cy` - Error handling patterns
- `context_managers.cy` - Resource management
- `v3_showcase.cy` - All v3.0 features together

---

**CodingYok v3.0** - *Professional Indonesian Programming Language* 🇮🇩
