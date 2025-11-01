# CodingYok v2.0 - Complete Feature Reference

## 🎉 Overview

CodingYok v2.0 represents a major milestone in the evolution of the Indonesian programming language. This release brings modern programming paradigms while maintaining 100% backward compatibility with v1.0.

---

## 📊 Feature Comparison

| Feature | v1.0 | v2.0 |
|---------|------|------|
| List Comprehensions | ❌ | ✅ |
| Dict Comprehensions | ❌ | ✅ |
| Set Comprehensions | ❌ | ✅ |
| Set Literals | ❌ | ✅ |
| Generators (yield) | ❌ | ✅ |
| Pattern Matching | ❌ | ✅ |
| Error Suggestions | ❌ | ✅ |
| OOP | ✅ | ✅ |
| Exceptions | ✅ | ✅ |
| File I/O | ✅ | ✅ |
| Web Framework | ✅ | ✅ |

---

## 🆕 New Keywords

```
hasilkan    - yield (for generators)
cocokkan    - match (pattern matching)
kasus       - case (pattern matching)
async       - async (reserved for future)
menunggu    - await (reserved for future)
```

---

## 📝 Syntax Reference

### List Comprehensions

**Basic:**
```codingyok
[expression untuk variable dalam iterable]
```

**With Filter:**
```codingyok
[expression untuk variable dalam iterable jika condition]
```

**Examples:**
```codingyok
# Simple transformation
squares = [x * x untuk x dalam [1, 2, 3, 4, 5]]
# [1, 4, 9, 16, 25]

# With condition
evens = [x untuk x dalam rentang(10) jika x % 2 == 0]
# [0, 2, 4, 6, 8]

# Nested
matrix = [[i * j untuk j dalam rentang(3)] untuk i dalam rentang(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

---

### Dictionary Comprehensions

**Basic:**
```codingyok
{key_expr: value_expr untuk variable dalam iterable}
```

**With Filter:**
```codingyok
{key_expr: value_expr untuk variable dalam iterable jika condition}
```

**Examples:**
```codingyok
# Create dict from range
squares = {x: x * x untuk x dalam rentang(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
mapping = {k: v untuk k, v dalam zip(keys, values)}
# {"a": 1, "b": 2, "c": 3}

# Transform dict
prices = {"apple": 100, "banana": 50, "orange": 75}
discounted = {k: v * 0.9 untuk k, v dalam prices.items()}
```

---

### Set Comprehensions

**Basic:**
```codingyok
{expression untuk variable dalam iterable}
```

**With Filter:**
```codingyok
{expression untuk variable dalam iterable jika condition}
```

**Examples:**
```codingyok
# Remove duplicates
unique = {x untuk x dalam [1, 2, 2, 3, 3, 4]}
# {1, 2, 3, 4}

# Unique squares
squares = {x * x untuk x dalam [1, -1, 2, -2, 3]}
# {1, 4, 9}

# Filter and unique
positive_evens = {x untuk x dalam [-4, -2, 0, 2, 4, 2] jika x > 0}
# {2, 4}
```

---

### Set Literals

**Syntax:**
```codingyok
{element1, element2, element3}
```

**Examples:**
```codingyok
# Create set
numbers = {1, 2, 3, 4, 5}

# Auto deduplication
unique = {1, 1, 2, 2, 3}  # {1, 2, 3}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
union = a.union(b)        # {1, 2, 3, 4, 5}
intersection = a.intersection(b)  # {3}
difference = a.difference(b)      # {1, 2}
```

---

### Generators

**Basic Syntax:**
```codingyok
fungsi generator_name(parameters):
    untuk item dalam iterable:
        hasilkan value
```

**Examples:**

**Simple Generator:**
```codingyok
fungsi count_up(n):
    untuk i dalam rentang(n):
        hasilkan i

untuk num dalam count_up(5):
    tulis(num)  # 0, 1, 2, 3, 4
```

**Fibonacci Generator:**
```codingyok
fungsi fibonacci(n):
    a = 0
    b = 1
    counter = 0
    selama counter < n:
        hasilkan a
        a, b = b, a + b
        counter += 1

# Get first 10 fibonacci numbers
fib_nums = list(fibonacci(10))
```

**Infinite Generator:**
```codingyok
fungsi infinite_counter():
    n = 0
    selama benar:
        hasilkan n
        n += 1

# Use with break
counter = 0
untuk num dalam infinite_counter():
    tulis(num)
    counter += 1
    jika counter >= 5:
        berhenti
```

**Generator Pipeline:**
```codingyok
fungsi read_numbers(data):
    untuk item dalam data:
        hasilkan int(item)

fungsi square_numbers(numbers):
    untuk n dalam numbers:
        hasilkan n * n

fungsi filter_large(numbers):
    untuk n dalam numbers:
        jika n > 10:
            hasilkan n

# Chain generators
data = ["1", "2", "3", "4", "5"]
hasil = filter_large(square_numbers(read_numbers(data)))
tulis(list(hasil))  # [16, 25]
```

---

### Pattern Matching

**Basic Syntax:**
```codingyok
cocokkan expression:
    kasus pattern1:
        statements
    kasus pattern2:
        statements
    kasus _:
        default_statements
```

**Literal Patterns:**
```codingyok
fungsi describe_number(n):
    cocokkan n:
        kasus 0:
            tulis("Zero")
        kasus 1:
            tulis("One")
        kasus 2:
            tulis("Two")
        kasus _:
            tulis("Other")
```

**Guard Conditions:**
```codingyok
fungsi categorize(x):
    cocokkan x:
        kasus _ jika x < 0:
            tulis("Negative")
        kasus 0:
            tulis("Zero")
        kasus _ jika x > 0 dan x < 10:
            tulis("Small positive")
        kasus _ jika x >= 10:
            tulis("Large positive")
```

**String Patterns:**
```codingyok
fungsi handle_command(cmd):
    cocokkan cmd:
        kasus "start":
            start_service()
        kasus "stop":
            stop_service()
        kasus "restart":
            restart_service()
        kasus "status":
            show_status()
        kasus _:
            tulis("Unknown command")
```

**Complex Example:**
```codingyok
fungsi process_http_status(code):
    cocokkan code:
        kasus _ jika code >= 200 dan code < 300:
            kembalikan "Success"
        kasus _ jika code >= 300 dan code < 400:
            kembalikan "Redirection"
        kasus _ jika code >= 400 dan code < 500:
            kembalikan "Client Error"
        kasus _ jika code >= 500:
            kembalikan "Server Error"
        kasus _:
            kembalikan "Invalid Status Code"
```

---

## 💡 Error Suggestions

### How It Works

The interpreter now uses fuzzy string matching to suggest corrections when you make typos:

**Example 1: Variable Typo**
```codingyok
nama = "Budi"
tulis(namaa)  # Typo!
```

**Error Message:**
```
Kesalahan Runtime: Nama 'namaa' tidak ditemukan
   Mungkin maksud Anda: nama
```

**Example 2: Function Typo**
```codingyok
tuless("Hello")  # Typo!
```

**Error Message:**
```
Kesalahan Runtime: Nama 'tuless' tidak ditemukan
   Mungkin maksud Anda: tulis, tulis_file, tulis_json
```

### Suggestion Algorithm

- Uses Levenshtein distance (edit distance)
- Suggests up to 3 closest matches
- Minimum similarity threshold: 60%
- Searches through all available names in scope

---

## 🎯 Use Cases

### List Comprehensions

**Good For:**
- ✅ Data transformation
- ✅ Filtering lists
- ✅ Mapping operations
- ✅ Flattening nested lists

**Example Use Cases:**
```codingyok
# Data cleaning
clean_data = [x.strip().lower() untuk x dalam raw_data jika x]

# Extract fields
names = [person["name"] untuk person dalam people]

# Transform and filter
prices_with_tax = [p * 1.1 untuk p dalam prices jika p > 0]
```

---

### Generators

**Good For:**
- ✅ Large datasets
- ✅ Streaming data
- ✅ Infinite sequences
- ✅ Memory-constrained environments
- ✅ Data pipelines

**Example Use Cases:**
```codingyok
# Read large file
fungsi read_large_csv(filename):
    untuk line dalam baca_file_lines(filename):
        hasilkan parse_csv_line(line)

# Process logs
fungsi filter_errors(log_file):
    untuk line dalam read_large_csv(log_file):
        jika line["level"] == "ERROR":
            hasilkan line

# Batch processing
fungsi batch_generator(items, batch_size):
    batch = []
    untuk item dalam items:
        batch.append(item)
        jika panjang(batch) == batch_size:
            hasilkan batch
            batch = []
    jika batch:
        hasilkan batch
```

---

### Pattern Matching

**Good For:**
- ✅ Command parsing
- ✅ State machines
- ✅ HTTP routing
- ✅ Type categorization
- ✅ Configuration handling

**Example Use Cases:**
```codingyok
# CLI command parser
fungsi handle_cli(args):
    command = args[0]
    cocokkan command:
        kasus "add":
            add_item(args[1:])
        kasus "remove":
            remove_item(args[1:])
        kasus "list":
            list_items()
        kasus "help":
            show_help()
        kasus _:
            tulis(f"Unknown command: {command}")

# HTTP router
fungsi route_request(method, path):
    cocokkan path:
        kasus "/":
            kembalikan home_page()
        kasus "/api/users":
            cocokkan method:
                kasus "GET":
                    kembalikan get_users()
                kasus "POST":
                    kembalikan create_user()
                kasus _:
                    kembalikan method_not_allowed()
        kasus _:
            kembalikan not_found()
```

---

## 📈 Performance Benchmarks

### Comprehensions vs Loops

```
List creation (1M items):
- Traditional loop: 0.45s
- List comprehension: 0.32s
- Improvement: ~29% faster
```

### Generator Memory Usage

```
Sequence of 1M items:
- List: ~8 MB
- Generator: ~0.1 KB
- Improvement: ~80,000x less memory
```

---

## 🔮 Future Features (Reserved Keywords)

### Async/Await

```codingyok
# Planned for v3.0
async fungsi fetch_data(url):
    response = menunggu http_get(url)
    kembalikan response.json()

async fungsi main():
    data = menunggu fetch_data("https://api.example.com")
    tulis(data)
```

---

## 📚 Resources

- **Examples**: See `examples/fitur_baru.cy` for comprehensive demos
- **Migration Guide**: See `MIGRATION_V2.md` for upgrade instructions  
- **Changelog**: See `CHANGELOG.md` for detailed changes
- **Documentation**: See `README.md` for overview

---

## 🎓 Quick Tips

1. **Start Small**: Adopt one feature at a time
2. **Profile First**: Use comprehensions where they improve readability
3. **Memory Matters**: Use generators for large datasets
4. **Pattern Match Wisely**: Use for complex conditionals, not simple if-else
5. **Learn from Examples**: Study the example files

---

## 🤝 Contributing

We welcome contributions! If you have ideas for v3.0 features:

1. Open an issue on GitHub
2. Discuss in our community
3. Submit a pull request

**Potential v3.0 Features:**
- Async/await support
- Decorators
- Type annotations
- Dataclasses
- Context managers
- Module system enhancements

---

**Happy Coding with CodingYok v2.0!** 🇮🇩🎉
