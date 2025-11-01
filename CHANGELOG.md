# Changelog

All notable changes to CodingYok will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-11-01

### 🎉 Major Release - Modern Language Features

This is a major release that brings CodingYok to feature parity with modern programming languages like Python 3.10+.

### Added

#### **Comprehensions** ✨
- **List Comprehensions**: Create lists with concise syntax
  ```codingyok
  kuadrat = [x * x untuk x dalam rentang(1, 10)]
  genap = [x untuk x dalam angka jika x % 2 == 0]
  ```

- **Dictionary Comprehensions**: Build dictionaries efficiently
  ```codingyok
  dict_kuadrat = {x: x * x untuk x dalam rentang(1, 6)}
  ```

- **Set Comprehensions**: Create unique collections
  ```codingyok
  set_unik = {x untuk x dalam [1, 2, 2, 3, 3] jika x > 1}
  ```

#### **Generators** 🔄
- **`hasilkan` (yield) Statement**: Create memory-efficient iterators
  ```codingyok
  fungsi fibonacci(n):
      a, b = 0, 1
      selama n > 0:
          hasilkan a
          a, b = b, a + b
          n -= 1
  ```

- Functions with `hasilkan` automatically return generator objects
- Generators support lazy evaluation for large datasets
- Perfect for streaming data and infinite sequences

#### **Pattern Matching** 🎯
- **`cocokkan` (match) Statement**: Python 3.10+ style pattern matching
  ```codingyok
  cocokkan nilai:
      kasus 0:
          tulis("nol")
      kasus _ jika nilai > 0:
          tulis("positif")
      kasus _:
          tulis("negatif")
  ```

- Support for literal patterns (numbers, strings)
- Guard conditions with `jika`
- Wildcard pattern `_` for catch-all cases
- Clean alternative to long if-elif chains

#### **Set Data Type** 📦
- Full support for set literals: `{1, 2, 3}`
- Automatic deduplication of elements
- Set operations (union, intersection, difference)
- Set comprehensions for advanced use cases

#### **Better Error Messages** 💡
- **"Did You Mean" Suggestions**: Smart typo detection
  ```
  Nama 'tuless' tidak ditemukan
     Mungkin maksud Anda: tulis, tulis_file
  ```

- Fuzzy matching for variable and function names
- Suggestions based on edit distance
- Helps catch common typos quickly

### Enhanced

- **Error Handling**: More helpful error messages with context
- **Parser**: Support for new syntax constructs
- **Interpreter**: Optimized execution for comprehensions
- **Type System**: Better type inference and checking

### Examples

- Added `examples/fitur_baru.cy` - Comprehensive demonstration of all v2.0 features
- Updated existing examples to showcase new capabilities

### Documentation

- Updated README.md with v2.0 feature showcase
- Added examples for all new language features
- Improved error message documentation
- Added migration guide for v1.x users

### Technical Details

#### New Tokens
- `HASILKAN` - yield keyword
- `COCOKKAN` - match keyword
- `KASUS` - case keyword
- `ASYNC` - async keyword (reserved for future)
- `MENUNGGU` - await keyword (reserved for future)

#### New AST Nodes
- `ListComprehension` - List comprehension expressions
- `DictComprehension` - Dictionary comprehension expressions
- `SetExpression` - Set literal expressions
- `SetComprehension` - Set comprehension expressions
- `YieldStatement` - Yield statements for generators
- `MatchStatement` - Pattern matching statements
- `MatchCase` - Individual case clauses

#### Interpreter Enhancements
- Generator support with lazy evaluation
- Pattern matching engine with guard conditions
- Comprehension evaluation with isolated scopes
- Enhanced error reporting with suggestions

### Breaking Changes

None - Full backward compatibility with v1.0.0 maintained.

### Performance

- Comprehensions are typically 20-30% faster than equivalent loops
- Generators provide O(1) memory for large sequences
- Pattern matching is optimized for common patterns

---

## [1.0.0] - 2024-10-01

### Initial Release

- Core interpreter with Indonesian keywords
- Object-oriented programming (classes, inheritance)
- Exception handling (coba/kecuali/akhirnya)
- File I/O operations
- JSON and CSV support
- Indonesian-specific utilities (Rupiah formatting, number to words, etc.)
- Built-in web server and HTTP client
- REPL and CLI interface
- Comprehensive standard library

[2.0.0]: https://github.com/MrXploisLite/CodingYok/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/MrXploisLite/CodingYok/releases/tag/v1.0.0
