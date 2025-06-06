# 🤝 Panduan Kontribusi CodingYok

Terima kasih atas minat Anda untuk berkontribusi pada CodingYok! Dokumen ini akan memandu Anda melalui proses kontribusi.

## 📋 Daftar Isi

- [Code of Conduct](#code-of-conduct)
- [Cara Berkontribusi](#cara-berkontribusi)
- [Setup Development Environment](#setup-development-environment)
- [Panduan Coding](#panduan-coding)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Pelaporan Bug](#pelaporan-bug)
- [Feature Request](#feature-request)

## 🤝 Code of Conduct

Proyek ini mengikuti [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/). Dengan berpartisipasi, Anda diharapkan untuk menjunjung tinggi kode etik ini.

## 🚀 Cara Berkontribusi

Ada beberapa cara untuk berkontribusi pada CodingYok:

1. **Melaporkan Bug** - Temukan dan laporkan bug
2. **Mengusulkan Fitur** - Sarankan fitur baru
3. **Menulis Kode** - Implementasi fitur atau perbaikan bug
4. **Dokumentasi** - Perbaiki atau tambah dokumentasi
5. **Testing** - Tulis atau perbaiki unit tests
6. **Contoh Program** - Buat contoh program CodingYok

## 🛠️ Setup Development Environment

### Prerequisites
- Python 3.8 atau lebih tinggi
- Git
- Virtual environment (recommended)

### Langkah Setup

1. **Fork dan Clone Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CodingYok.git
   cd CodingYok
   ```

2. **Buat Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # atau
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   pip install -e .
   ```

4. **Verifikasi Installation**
   ```bash
   codingyok examples/hello_world.cy
   pytest tests/
   ```

## 📝 Panduan Coding

### Style Guide
- Ikuti [PEP 8](https://pep8.org/) untuk Python code
- Gunakan [Black](https://black.readthedocs.io/) untuk formatting
- Gunakan [mypy](http://mypy-lang.org/) untuk type checking
- Maksimal line length: 88 karakter

### Naming Conventions
- **Variabel dan fungsi**: `snake_case`
- **Kelas**: `PascalCase`
- **Konstanta**: `UPPER_CASE`
- **File**: `snake_case.py`

### Struktur Kode
```python
"""
Module docstring explaining purpose
"""

import standard_library
import third_party_library
from .local_module import LocalClass

# Constants
CONSTANT_VALUE = "value"

class MyClass:
    """Class docstring"""
    
    def __init__(self):
        """Constructor docstring"""
        pass
    
    def public_method(self) -> str:
        """Method docstring"""
        return "result"
    
    def _private_method(self) -> None:
        """Private method docstring"""
        pass
```

### Dokumentasi
- Semua public functions dan classes harus memiliki docstring
- Gunakan format Google-style docstrings
- Komentar dalam bahasa Indonesia untuk CodingYok-specific code
- Komentar dalam bahasa Inggris untuk general programming concepts

## 🧪 Testing

### Menjalankan Tests
```bash
# Semua tests
pytest

# Dengan coverage
pytest --cov=src/codingyok

# Test specific file
pytest tests/test_lexer.py

# Test dengan verbose output
pytest -v
```

### Menulis Tests
- Setiap fitur baru harus memiliki tests
- Test coverage minimal 80%
- Gunakan descriptive test names
- Test both positive dan negative cases

Contoh test:
```python
def test_function_with_return_value(self):
    """Test function that returns a value"""
    code = """
    fungsi tambah(a, b):
        kembalikan a + b
    
    hasil = tambah(5, 3)
    tulis(hasil)
    """
    output = self.capture_output(code)
    assert output == "8"
```

## 📤 Pull Request Process

### Sebelum Membuat PR

1. **Pastikan semua tests pass**
   ```bash
   pytest
   black --check src/ tests/
   mypy src/codingyok/
   flake8 src/
   ```

2. **Update dokumentasi** jika diperlukan

3. **Tambah entry ke CHANGELOG.md** (jika ada)

### Membuat Pull Request

1. **Buat branch baru**
   ```bash
   git checkout -b feature/nama-fitur
   # atau
   git checkout -b fix/nama-bug
   ```

2. **Commit changes**
   ```bash
   git add .
   git commit -m "feat: tambah fitur X"
   # atau
   git commit -m "fix: perbaiki bug Y"
   ```

3. **Push ke fork**
   ```bash
   git push origin feature/nama-fitur
   ```

4. **Buat Pull Request** di GitHub

### Commit Message Format
Gunakan [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` untuk fitur baru
- `fix:` untuk bug fixes
- `docs:` untuk dokumentasi
- `test:` untuk tests
- `refactor:` untuk refactoring
- `style:` untuk formatting changes

## 🐛 Pelaporan Bug

Gunakan [GitHub Issues](https://github.com/MrXploisLite/CodingYok/issues) untuk melaporkan bug.

### Template Bug Report
```markdown
**Deskripsi Bug**
Deskripsi singkat tentang bug.

**Langkah Reproduksi**
1. Buka file '...'
2. Jalankan command '...'
3. Lihat error

**Expected Behavior**
Apa yang seharusnya terjadi.

**Actual Behavior**
Apa yang sebenarnya terjadi.

**Environment**
- OS: [e.g. Windows 10, Ubuntu 20.04]
- Python Version: [e.g. 3.9.0]
- CodingYok Version: [e.g. 1.0.0]

**Kode CodingYok**
```codingyok
# Paste kode yang menyebabkan bug
```

**Error Message**
```
Paste error message di sini
```
```

## 💡 Feature Request

Gunakan [GitHub Issues](https://github.com/MrXploisLite/CodingYok/issues) dengan label "enhancement".

### Template Feature Request
```markdown
**Deskripsi Fitur**
Deskripsi singkat fitur yang diinginkan.

**Motivasi**
Mengapa fitur ini diperlukan? Masalah apa yang akan diselesaikan?

**Contoh Penggunaan**
```codingyok
# Contoh bagaimana fitur akan digunakan
```

**Alternatif**
Apakah ada alternatif yang sudah dipertimbangkan?

**Additional Context**
Informasi tambahan, screenshot, dll.
```

## 🏷️ Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## 🙏 Terima Kasih

Kontribusi Anda sangat berarti untuk pengembangan CodingYok! Setiap kontribusi, sekecil apapun, akan sangat dihargai.

---

**Happy Coding with CodingYok!** 🇮🇩
