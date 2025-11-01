"""
Standard library functions for CodingYok
Provides built-in functions with Indonesian names
"""

import time
import random
import math
import datetime
from typing import Any, Dict, List, Callable, Optional, Union
from .errors import CodingYokTypeError, CodingYokValueError


def panjang(obj: Any) -> int:
    """Return length of object (len in Python)"""
    try:
        return len(obj)
    except TypeError:
        raise CodingYokTypeError("Objek tidak memiliki panjang")


def tipe(obj: Any) -> str:
    """Return type of object (type in Python)"""
    type_map = {
        int: "bilangan_bulat",
        float: "bilangan_desimal",
        str: "teks",
        list: "daftar",
        dict: "kamus",
        bool: "boolean",
        type(None): "kosong",
    }
    return type_map.get(type(obj), str(type(obj).__name__))


def rentang(*args) -> range:
    """Create range object (range in Python)"""
    if len(args) == 1:
        return range(args[0])
    elif len(args) == 2:
        return range(args[0], args[1])
    elif len(args) == 3:
        return range(args[0], args[1], args[2])
    else:
        raise CodingYokValueError("rentang() membutuhkan 1-3 argumen")


def masukan(prompt: str = "") -> str:
    """Get user input (input in Python)"""
    return input(prompt)


def int_indo(value: Any) -> int:
    """Convert to integer"""
    try:
        return int(value)
    except (ValueError, TypeError):
        raise CodingYokValueError(
            f"Tidak dapat mengkonversi '{value}' ke bilangan bulat"
        )


def float_indo(value: Any) -> float:
    """Convert to float"""
    try:
        return float(value)
    except (ValueError, TypeError):
        raise CodingYokValueError(
            f"Tidak dapat mengkonversi '{value}' ke bilangan desimal"
        )


def str_indo(value: Any) -> str:
    """Convert to string"""
    if value is None:
        return "kosong"
    elif value is True:
        return "benar"
    elif value is False:
        return "salah"
    else:
        return str(value)


def daftar(iterable: Any = None) -> list:
    """Create list (list in Python)"""
    if iterable is None:
        return []
    try:
        return list(iterable)
    except TypeError:
        raise CodingYokTypeError("Objek tidak dapat dikonversi ke daftar")


def kamus(*args, **kwargs) -> dict:
    """Create dictionary (dict in Python)"""
    if len(args) == 0:
        return dict(**kwargs)
    elif len(args) == 1:
        return dict(args[0], **kwargs)
    else:
        raise CodingYokValueError("kamus() membutuhkan maksimal 1 argumen posisi")


def peta(fungsi: Callable, iterable: Any) -> map:
    """Apply function to all items (map in Python)"""
    try:
        return map(fungsi, iterable)
    except TypeError:
        raise CodingYokTypeError("peta() membutuhkan fungsi dan iterable")


def saring(fungsi: Callable, iterable: Any) -> filter:
    """Filter items based on function (filter in Python)"""
    try:
        return filter(fungsi, iterable)
    except TypeError:
        raise CodingYokTypeError("saring() membutuhkan fungsi dan iterable")


def jumlah(iterable: Any) -> float:
    """Sum of iterable (sum in Python)"""
    try:
        return sum(iterable)
    except TypeError:
        raise CodingYokTypeError("Objek tidak dapat dijumlahkan")


def maksimum(iterable: Any) -> Any:
    """Maximum value (max in Python)"""
    try:
        return max(iterable)
    except (ValueError, TypeError):
        raise CodingYokValueError("Tidak dapat mencari nilai maksimum")


def minimum(iterable: Any) -> Any:
    """Minimum value (min in Python)"""
    try:
        return min(iterable)
    except (ValueError, TypeError):
        raise CodingYokValueError("Tidak dapat mencari nilai minimum")


def urutkan(iterable: Any, terbalik: bool = False) -> list:
    """Sort iterable (sorted in Python)"""
    try:
        return sorted(iterable, reverse=terbalik)
    except TypeError:
        raise CodingYokTypeError("Objek tidak dapat diurutkan")


def balik(iterable: Any) -> list:
    """Reverse iterable (reversed in Python)"""
    try:
        return list(reversed(iterable))
    except TypeError:
        raise CodingYokTypeError("Objek tidak dapat dibalik")


def abs_indo(number: Any) -> Any:
    """Absolute value (abs in Python)"""
    try:
        return abs(number)
    except TypeError:
        raise CodingYokTypeError("abs() membutuhkan angka")


def bulat(number: float, ndigits: int = 0) -> float:
    """Round number (round in Python)"""
    try:
        return round(number, ndigits)
    except TypeError:
        raise CodingYokTypeError("bulat() membutuhkan angka")


# Math functions with Indonesian names
def akar(x: float) -> float:
    """Square root (math.sqrt)"""
    try:
        return math.sqrt(x)
    except (TypeError, ValueError):
        raise CodingYokValueError("akar() membutuhkan angka non-negatif")


def pangkat(base: float, exp: float) -> float:
    """Power function (math.pow)"""
    try:
        return math.pow(base, exp)
    except (TypeError, ValueError):
        raise CodingYokValueError("pangkat() membutuhkan dua angka")


def sin_indo(x: float) -> float:
    """Sine function"""
    try:
        return math.sin(x)
    except TypeError:
        raise CodingYokTypeError("sin() membutuhkan angka")


def cos_indo(x: float) -> float:
    """Cosine function"""
    try:
        return math.cos(x)
    except TypeError:
        raise CodingYokTypeError("cos() membutuhkan angka")


def tan_indo(x: float) -> float:
    """Tangent function"""
    try:
        return math.tan(x)
    except TypeError:
        raise CodingYokTypeError("tan() membutuhkan angka")


# Time functions
def waktu_sekarang() -> float:
    """Current time (time.time)"""
    return time.time()


def tidur(detik: float) -> None:
    """Sleep for given seconds (time.sleep)"""
    try:
        time.sleep(detik)
    except (TypeError, ValueError):
        raise CodingYokValueError("tidur() membutuhkan angka detik")


def tanggal_sekarang() -> str:
    """Current date in Indonesian format"""
    now = datetime.datetime.now()
    bulan_indo = [
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember",
    ]
    hari_indo = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

    hari = hari_indo[now.weekday()]
    tanggal = now.day
    bulan = bulan_indo[now.month - 1]
    tahun = now.year

    return f"{hari}, {tanggal} {bulan} {tahun}"


# Random functions
def acak() -> float:
    """Random float between 0 and 1 (random.random)"""
    return random.random()


def acak_int(a: int, b: int) -> int:
    """Random integer between a and b (random.randint)"""
    try:
        return random.randint(a, b)
    except (TypeError, ValueError):
        raise CodingYokValueError("acak_int() membutuhkan dua bilangan bulat")


def pilih_acak(sequence: Any) -> Any:
    """Choose random element from sequence (random.choice)"""
    try:
        return random.choice(sequence)
    except (IndexError, TypeError):
        raise CodingYokValueError("pilih_acak() membutuhkan sequence yang tidak kosong")


def acak_urutan(sequence: list) -> None:
    """Shuffle sequence in place (random.shuffle)"""
    try:
        random.shuffle(sequence)
    except TypeError:
        raise CodingYokTypeError("acak_urutan() membutuhkan list")


# String functions
def huruf_besar(text: str) -> str:
    """Convert to uppercase"""
    try:
        return text.upper()
    except AttributeError:
        raise CodingYokTypeError("huruf_besar() membutuhkan teks")


def huruf_kecil(text: str) -> str:
    """Convert to lowercase"""
    try:
        return text.lower()
    except AttributeError:
        raise CodingYokTypeError("huruf_kecil() membutuhkan teks")


def pisah(text: str, separator: Optional[str] = None) -> list:
    """Split string (str.split)"""
    try:
        return text.split(separator)
    except AttributeError:
        raise CodingYokTypeError("pisah() membutuhkan teks")


def gabung(separator: str, iterable: Any) -> str:
    """Join iterable with separator (str.join)"""
    try:
        return separator.join(str(item) for item in iterable)
    except TypeError:
        raise CodingYokTypeError("gabung() membutuhkan separator teks dan iterable")


def ganti(text: str, old: str, new: str) -> str:
    """Replace substring (str.replace)"""
    try:
        return text.replace(old, new)
    except AttributeError:
        raise CodingYokTypeError("ganti() membutuhkan teks")


def cetak_tabel(data: List[List[Any]], header: Optional[List[str]] = None) -> None:
    """Print data as formatted table"""
    if not data:
        return

    # Calculate column widths
    all_rows = []
    if header:
        all_rows.append([str(h) for h in header])

    for row in data:
        all_rows.append([str(cell) for cell in row])

    if not all_rows:
        return

    # Calculate max width for each column
    col_widths = []
    for col in range(len(all_rows[0])):
        max_width = max(len(row[col]) if col < len(row) else 0 for row in all_rows)
        col_widths.append(max_width)

    # Print header if provided
    if header:
        header_row = all_rows[0]
        print(
            "| "
            + " | ".join(
                cell.ljust(width) for cell, width in zip(header_row, col_widths)
            )
            + " |"
        )
        print("|" + "|".join("-" * (width + 2) for width in col_widths) + "|")
        data_start = 1
    else:
        data_start = 0

    # Print data rows
    for row in all_rows[data_start:]:
        print(
            "| "
            + " | ".join(cell.ljust(width) for cell, width in zip(row, col_widths))
            + " |"
        )


def hitung_statistik(data: List[Union[int, float]]) -> Dict[str, float]:
    """Calculate basic statistics for numerical data"""
    if not data:
        return {}

    n = len(data)
    total = sum(data)
    rata_rata = total / n

    # Calculate variance and standard deviation
    variance = sum((x - rata_rata) ** 2 for x in data) / n
    std_dev = variance**0.5

    # Calculate median
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = float(sorted_data[n // 2])

    return {
        "jumlah": total,
        "rata_rata": rata_rata,
        "median": median,
        "minimum": min(data),
        "maksimum": max(data),
        "varians": variance,
        "standar_deviasi": std_dev,
        "jumlah_data": n,
    }


def get_builtin_functions() -> Dict[str, Any]:
    """Get all built-in functions"""
    return {
        # Basic functions
        "panjang": panjang,
        "tipe": tipe,
        "rentang": rentang,
        "masukan": masukan,
        # Type conversion
        "int": int_indo,
        "float": float_indo,
        "str": str_indo,
        "daftar": daftar,
        "kamus": kamus,
        # Functional programming
        "peta": peta,
        "saring": saring,
        # Math functions
        "jumlah": jumlah,
        "maksimum": maksimum,
        "minimum": minimum,
        "urutkan": urutkan,
        "balik": balik,
        "abs": abs_indo,
        "bulat": bulat,
        "akar": akar,
        "pangkat": pangkat,
        "sin": sin_indo,
        "cos": cos_indo,
        "tan": tan_indo,
        # Time functions
        "waktu_sekarang": waktu_sekarang,
        "tidur": tidur,
        "tanggal_sekarang": tanggal_sekarang,
        # Random functions
        "acak": acak,
        "acak_int": acak_int,
        "pilih_acak": pilih_acak,
        "acak_urutan": acak_urutan,
        # String functions
        "huruf_besar": huruf_besar,
        "huruf_kecil": huruf_kecil,
        "pisah": pisah,
        "gabung": gabung,
        "ganti": ganti,
        # Advanced utilities
        "cetak_tabel": cetak_tabel,
        "hitung_statistik": hitung_statistik,
        # Constants
        "PI": math.pi,
        "E": math.e,
    }
