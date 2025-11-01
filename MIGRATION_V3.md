# Migration Guide: CodingYok v2.0 to v3.0

## Overview

CodingYok v3.0 brings powerful new features while maintaining 100% backward compatibility with v2.0. All existing v2.0 code will run unchanged in v3.0.

## What's New in v3.0

### 1. Lambda Expressions
### 2. Exception Handling (coba/kecuali/akhirnya/lempar)
### 3. Context Managers (dengan statement)

---

## Lambda Expressions

### What Changed
Lambda expressions are now fully supported, allowing you to create anonymous functions.

### Migration Examples

**Before (v2.0):**
```codingyok
fungsi kuadrat(x):
    kembalikan x * x

hasil = peta(kuadrat, [1, 2, 3, 4, 5])
```

**After (v3.0):**
```codingyok
# More concise with lambda
hasil = peta(lambda x: x * x, [1, 2, 3, 4, 5])
```

### When to Use Lambda

**Use Lambda For:**
- Simple, one-line operations
- Functions used once (e.g., as map/filter arguments)
- Callback functions

**Use Regular Functions For:**
- Complex logic
- Functions needing documentation
- Functions used in multiple places
- Recursive functions

---

## Exception Handling

### What Changed
Exception handling was defined in v2.0 but not fully implemented. v3.0 brings complete implementation of `coba`, `kecuali`, `akhirnya`, and `lempar`.

### Migration Examples

**Before (v2.0):**
```codingyok
fungsi bagi(a, b):
    jika b == 0:
        tulis("Error: Tidak boleh dibagi nol")
        kembalikan kosong
    kembalikan a / b

fungsi konversi_angka(text):
    # Manual validation
    jika text.isdigit():
        kembalikan int(text)
    kalau_tidak:
        tulis("Error: Bukan angka valid")
        kembalikan kosong
```

**After (v3.0):**
```codingyok
fungsi bagi(a, b):
    coba:
        kembalikan a / b
    kecuali ZeroDivisionError:
        tulis("Error: Tidak boleh dibagi nol")
        lempar  # Re-raise for caller to handle

fungsi konversi_angka(text):
    coba:
        kembalikan int(text)
    kecuali ValueError:
        tulis("Error: Bukan angka valid")
        kembalikan kosong
```

### Benefits

1. **More Pythonic**: Standard exception handling pattern
2. **Better Error Propagation**: Exceptions bubble up naturally
3. **Cleaner Code**: Separate error handling from business logic
4. **Finally Blocks**: Guaranteed cleanup

### Common Patterns

**Pattern 1: Resource Cleanup**
```codingyok
# Old way
file = buka_file("data.txt")
data = file.baca()
file.tutup()

# New way
coba:
    file = buka_file("data.txt")
    data = file.baca()
akhirnya:
    file.tutup()
```

**Pattern 2: Multiple Error Types**
```codingyok
coba:
    nilai = int(input_data)
    hasil = 100 / nilai
kecuali ValueError:
    tulis("Input bukan angka")
kecuali ZeroDivisionError:
    tulis("Angka tidak boleh nol")
kecuali:
    tulis("Error tidak diketahui")
```

**Pattern 3: Custom Exceptions**
```codingyok
fungsi validasi_email(email):
    jika bukan "@" dalam email:
        lempar ValueError("Email tidak valid")
    kembalikan benar

coba:
    validasi_email("user.example.com")
kecuali ValueError sebagai e:
    tulis(f"Error: {e}")
```

---

## Context Managers

### What Changed
Context managers with `dengan` statement are now fully functional, enabling automatic resource management.

### Migration Examples

**Before (v2.0):**
```codingyok
# Manual file handling
file = buka_file("data.txt")
coba:
    data = file.baca()
    process(data)
akhirnya:
    file.tutup()

# Manual database connection
conn = buat_koneksi_db()
coba:
    cursor = conn.cursor()
    cursor.execute("SELECT ...")
    hasil = cursor.fetchall()
akhirnya:
    conn.tutup()
```

**After (v3.0):**
```codingyok
# Automatic file handling
dengan buka_file("data.txt") sebagai file:
    data = file.baca()
    process(data)
# File automatically closed

# Automatic database connection
dengan buat_koneksi_db() sebagai conn:
    cursor = conn.cursor()
    cursor.execute("SELECT ...")
    hasil = cursor.fetchall()
# Connection automatically closed
```

### Benefits

1. **Automatic Cleanup**: Resources always released
2. **Exception Safe**: Cleanup happens even if error occurs
3. **Cleaner Code**: Less boilerplate
4. **Prevents Leaks**: No forgotten cleanup

### Creating Custom Context Managers

```codingyok
kelas Timer:
    fungsi __init__(diri, nama):
        diri.nama = nama
        diri.start_time = kosong
    
    fungsi __enter__(diri):
        diri.start_time = waktu_sekarang()
        tulis(f"Memulai {diri.nama}")
        kembalikan diri
    
    fungsi __exit__(diri, exc_type, exc_val, exc_tb):
        elapsed = waktu_sekarang() - diri.start_time
        tulis(f"{diri.nama} selesai ({elapsed}s)")
        kembalikan salah

# Usage
dengan Timer("Proses Data") sebagai timer:
    # Your code here
    process_data()
```

---

## Upgrading Your Code

### Step 1: Review Current Error Handling

Look for manual error checking:
```codingyok
# Find code like this:
jika error_condition:
    tulis("Error message")
    kembalikan kosong
```

Consider replacing with:
```codingyok
# Replace with:
jika error_condition:
    lempar ValueError("Error message")
```

### Step 2: Identify Resource Management

Look for manual resource cleanup:
```codingyok
# Find code like this:
resource = acquire()
coba:
    use(resource)
akhirnya:
    release(resource)
```

Replace with context managers:
```codingyok
# Replace with:
dengan acquire() sebagai resource:
    use(resource)
```

### Step 3: Simplify Simple Functions

Look for simple helper functions:
```codingyok
# Find code like this:
fungsi tambah_10(x):
    kembalikan x + 10

data = peta(tambah_10, angka)
```

Consider using lambda:
```codingyok
# Consider replacing with:
data = peta(lambda x: x + 10, angka)
```

---

## Breaking Changes

**None** - v3.0 maintains 100% backward compatibility with v2.0.

All v2.0 code will run unchanged in v3.0. The new features are additive only.

---

## Performance Impact

### Lambda Expressions
- Negligible performance difference vs regular functions
- Slightly faster for very simple operations
- Same memory usage

### Exception Handling
- Minimal overhead when no exceptions occur
- Standard Python exception mechanism
- Use for exceptional cases, not control flow

### Context Managers
- Negligible overhead
- Much safer than manual management
- Recommended for all resource operations

---

## Best Practices

### 1. Use Lambda for Simple Cases Only

**Good:**
```codingyok
sorted_users = sorted(users, key=lambda u: u.age)
squares = peta(lambda x: x * x, numbers)
```

**Bad:**
```codingyok
# Too complex for lambda
process = lambda x: x.strip().lower().replace(" ", "_") jika x kalau_tidak ""
```

### 2. Catch Specific Exceptions

**Good:**
```codingyok
coba:
    nilai = int(text)
kecuali ValueError:
    tulis("Invalid number")
```

**Bad:**
```codingyok
coba:
    nilai = int(text)
kecuali:
    lewati  # Silently ignores all errors
```

### 3. Use Context Managers for Resources

**Good:**
```codingyok
dengan buka_file("data.txt") sebagai f:
    data = f.baca()
```

**Bad:**
```codingyok
f = buka_file("data.txt")
data = f.baca()
# Forgot to close!
```

### 4. Document Complex Logic

Lambda expressions can't have docstrings. For anything complex:

**Good:**
```codingyok
fungsi process_user(user):
    """
    Process user data by validating email and normalizing name.
    Returns processed user dict or None on error.
    """
    # Implementation
    pass
```

**Bad:**
```codingyok
# Complex lambda that needs explanation
process = lambda u: {"name": u.name.strip().title(), "email": u.email.lower()} jika validate(u) kalau_tidak kosong
```

---

## Testing Your Migration

### 1. Run Existing Tests
All existing tests should pass without changes.

### 2. Add New Feature Tests
Add tests for new exception handling and context managers.

### 3. Code Review
Review code for opportunities to use new features.

---

## Getting Help

If you encounter issues:

1. Check examples in `examples/v3_showcase.cy`
2. Review `V3_FEATURES.md` for comprehensive documentation
3. Open an issue on GitHub

---

## Summary

v3.0 brings professional-grade features:
- ✅ Lambda expressions for functional programming
- ✅ Complete exception handling infrastructure
- ✅ Context managers for resource safety
- ✅ 100% backward compatible with v2.0
- ✅ No breaking changes

**Recommended**: Gradually adopt new features as you update code.

**Not Required**: Your v2.0 code works as-is in v3.0.
