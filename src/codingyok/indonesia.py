"""
Indonesian-specific features for CodingYok
Includes Rupiah formatting, regional data, calendar, and text processing
"""

import datetime
import locale
from typing import Dict, List, Optional, Union
from .errors import CodingYokValueError


# Indonesian regional data
PROVINSI_INDONESIA = {
    "aceh": "Aceh",
    "sumut": "Sumatera Utara",
    "sumbar": "Sumatera Barat",
    "riau": "Riau",
    "kepri": "Kepulauan Riau",
    "jambi": "Jambi",
    "sumsel": "Sumatera Selatan",
    "babel": "Bangka Belitung",
    "bengkulu": "Bengkulu",
    "lampung": "Lampung",
    "jakarta": "DKI Jakarta",
    "jabar": "Jawa Barat",
    "jateng": "Jawa Tengah",
    "yogya": "DI Yogyakarta",
    "jatim": "Jawa Timur",
    "banten": "Banten",
    "bali": "Bali",
    "ntb": "Nusa Tenggara Barat",
    "ntt": "Nusa Tenggara Timur",
    "kalbar": "Kalimantan Barat",
    "kalteng": "Kalimantan Tengah",
    "kalsel": "Kalimantan Selatan",
    "kaltim": "Kalimantan Timur",
    "kaltara": "Kalimantan Utara",
    "sulut": "Sulawesi Utara",
    "sulteng": "Sulawesi Tengah",
    "sulsel": "Sulawesi Selatan",
    "sultra": "Sulawesi Tenggara",
    "gorontalo": "Gorontalo",
    "sulbar": "Sulawesi Barat",
    "maluku": "Maluku",
    "malut": "Maluku Utara",
    "papua": "Papua",
    "papbar": "Papua Barat",
}

KOTA_BESAR_INDONESIA = [
    "Jakarta",
    "Surabaya",
    "Bandung",
    "Medan",
    "Semarang",
    "Makassar",
    "Palembang",
    "Tangerang",
    "Depok",
    "Bekasi",
    "Bogor",
    "Batam",
    "Pekanbaru",
    "Bandar Lampung",
    "Malang",
    "Yogyakarta",
    "Solo",
    "Denpasar",
    "Balikpapan",
    "Samarinda",
    "Pontianak",
    "Manado",
    "Mataram",
    "Kupang",
    "Jayapura",
]

# Indonesian number words
ANGKA_INDONESIA = {
    0: "nol",
    1: "satu",
    2: "dua",
    3: "tiga",
    4: "empat",
    5: "lima",
    6: "enam",
    7: "tujuh",
    8: "delapan",
    9: "sembilan",
    10: "sepuluh",
    11: "sebelas",
    12: "dua belas",
    13: "tiga belas",
    14: "empat belas",
    15: "lima belas",
    16: "enam belas",
    17: "tujuh belas",
    18: "delapan belas",
    19: "sembilan belas",
    20: "dua puluh",
    30: "tiga puluh",
    40: "empat puluh",
    50: "lima puluh",
    60: "enam puluh",
    70: "tujuh puluh",
    80: "delapan puluh",
    90: "sembilan puluh",
    100: "seratus",
    1000: "seribu",
}

# Indonesian month names
BULAN_INDONESIA = [
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

# Indonesian day names
HARI_INDONESIA = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]


def format_rupiah(amount: Union[int, float], include_symbol: bool = True) -> str:
    """Format number as Indonesian Rupiah currency"""
    try:
        # Convert to integer if it's a whole number
        if isinstance(amount, float) and amount.is_integer():
            amount = int(amount)

        # Format with thousand separators
        if isinstance(amount, int):
            formatted = f"{amount:,}".replace(",", ".")
        else:
            formatted = f"{amount:,.2f}".replace(",", ".")

        if include_symbol:
            return f"Rp {formatted}"
        else:
            return formatted
    except (TypeError, ValueError):
        raise CodingYokValueError("format_rupiah() membutuhkan angka")


def angka_ke_kata(number: int) -> str:
    """Convert number to Indonesian words"""
    if not isinstance(number, int):
        raise CodingYokValueError("angka_ke_kata() membutuhkan bilangan bulat")

    if number < 0:
        return f"minus {angka_ke_kata(-number)}"

    if number in ANGKA_INDONESIA:
        return ANGKA_INDONESIA[number]

    if number < 100:
        if number < 20:
            return ANGKA_INDONESIA[number]
        else:
            tens = (number // 10) * 10
            ones = number % 10
            if ones == 0:
                return ANGKA_INDONESIA[tens]
            else:
                return f"{ANGKA_INDONESIA[tens]} {ANGKA_INDONESIA[ones]}"

    if number < 1000:
        hundreds = number // 100
        remainder = number % 100

        if hundreds == 1:
            result = "seratus"
        else:
            result = f"{ANGKA_INDONESIA[hundreds]} ratus"

        if remainder > 0:
            result += f" {angka_ke_kata(remainder)}"

        return result

    if number < 1000000:
        thousands = number // 1000
        remainder = number % 1000

        if thousands == 1:
            result = "seribu"
        else:
            result = f"{angka_ke_kata(thousands)} ribu"

        if remainder > 0:
            result += f" {angka_ke_kata(remainder)}"

        return result

    # For larger numbers, use basic conversion
    return str(number)


def tanggal_indonesia(
    date: Optional[datetime.datetime] = None, format_panjang: bool = True
) -> str:
    """Format date in Indonesian format"""
    if date is None:
        date = datetime.datetime.now()

    hari = HARI_INDONESIA[date.weekday()]
    tanggal = date.day
    bulan = BULAN_INDONESIA[date.month - 1]
    tahun = date.year

    if format_panjang:
        return f"{hari}, {tanggal} {bulan} {tahun}"
    else:
        return f"{tanggal} {bulan} {tahun}"


def waktu_indonesia(
    time: Optional[datetime.datetime] = None, format_24: bool = True
) -> str:
    """Format time in Indonesian format"""
    if time is None:
        time = datetime.datetime.now()

    if format_24:
        return f"{time.hour:02d}:{time.minute:02d}:{time.second:02d} WIB"
    else:
        hour = time.hour
        period = "pagi" if hour < 12 else "sore"
        if hour == 0:
            hour = 12
        elif hour > 12:
            hour -= 12

        return f"{hour}:{time.minute:02d}:{time.second:02d} {period}"


def cek_provinsi(nama_provinsi: str) -> Optional[str]:
    """Check if province name is valid and return full name"""
    nama_lower = nama_provinsi.lower()

    # Check by code
    if nama_lower in PROVINSI_INDONESIA:
        return PROVINSI_INDONESIA[nama_lower]

    # Check by full name
    for code, full_name in PROVINSI_INDONESIA.items():
        if full_name.lower() == nama_lower:
            return full_name

    return None


def daftar_provinsi() -> List[str]:
    """Get list of all Indonesian provinces"""
    return list(PROVINSI_INDONESIA.values())


def daftar_kota_besar() -> List[str]:
    """Get list of major Indonesian cities"""
    return KOTA_BESAR_INDONESIA.copy()


def format_nomor_telepon(nomor: str) -> str:
    """Format Indonesian phone number"""
    # Remove all non-digit characters
    digits = "".join(filter(str.isdigit, nomor))

    # Handle different formats
    if digits.startswith("62"):
        # International format
        if len(digits) >= 10:
            return f"+62 {digits[2:5]} {digits[5:9]} {digits[9:]}"
    elif digits.startswith("0"):
        # Domestic format
        if len(digits) >= 10:
            return f"{digits[:4]} {digits[4:8]} {digits[8:]}"

    return nomor  # Return original if can't format


def validasi_nik(nik: str) -> bool:
    """Validate Indonesian NIK (Nomor Induk Kependudukan)"""
    # Remove spaces and check if all digits
    nik_clean = nik.replace(" ", "")

    if not nik_clean.isdigit() or len(nik_clean) != 16:
        return False

    # Basic validation - check if province code is valid
    province_code = nik_clean[:2]
    try:
        province_num = int(province_code)
        return 11 <= province_num <= 94  # Valid province codes
    except ValueError:
        return False


def konversi_suhu(suhu: float, dari: str, ke: str) -> float:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin"""
    dari = dari.lower()
    ke = ke.lower()

    # Convert to Celsius first
    if dari == "fahrenheit" or dari == "f":
        celsius = (suhu - 32) * 5 / 9
    elif dari == "kelvin" or dari == "k":
        celsius = suhu - 273.15
    elif dari == "celsius" or dari == "c":
        celsius = suhu
    else:
        raise CodingYokValueError(
            "Unit suhu tidak valid. Gunakan: celsius, fahrenheit, kelvin"
        )

    # Convert from Celsius to target
    if ke == "fahrenheit" or ke == "f":
        return celsius * 9 / 5 + 32
    elif ke == "kelvin" or ke == "k":
        return celsius + 273.15
    elif ke == "celsius" or ke == "c":
        return celsius
    else:
        raise CodingYokValueError(
            "Unit suhu tidak valid. Gunakan: celsius, fahrenheit, kelvin"
        )


def jarak_kota(kota1: str, kota2: str) -> Optional[str]:
    """Get approximate distance between Indonesian cities (placeholder)"""
    # This is a simplified implementation
    # In a real implementation, this would use a proper distance database

    if kota1.lower() == kota2.lower():
        return "0 km"

    # Some example distances
    distances = {
        ("jakarta", "bandung"): "150 km",
        ("jakarta", "surabaya"): "800 km",
        ("jakarta", "medan"): "1,400 km",
        ("bandung", "yogyakarta"): "450 km",
        ("surabaya", "denpasar"): "350 km",
    }

    key1 = (kota1.lower(), kota2.lower())
    key2 = (kota2.lower(), kota1.lower())

    return distances.get(key1) or distances.get(key2) or "Jarak tidak tersedia"


def get_indonesian_functions() -> Dict[str, callable]:
    """Get all Indonesian-specific functions"""
    return {
        # Currency and number formatting
        "format_rupiah": format_rupiah,
        "angka_ke_kata": angka_ke_kata,
        # Date and time
        "tanggal_indonesia": tanggal_indonesia,
        "waktu_indonesia": waktu_indonesia,
        # Regional data
        "cek_provinsi": cek_provinsi,
        "daftar_provinsi": daftar_provinsi,
        "daftar_kota_besar": daftar_kota_besar,
        # Utilities
        "format_nomor_telepon": format_nomor_telepon,
        "validasi_nik": validasi_nik,
        "konversi_suhu": konversi_suhu,
        "jarak_kota": jarak_kota,
        # Constants
        "PROVINSI": PROVINSI_INDONESIA,
        "KOTA_BESAR": KOTA_BESAR_INDONESIA,
        "BULAN": BULAN_INDONESIA,
        "HARI": HARI_INDONESIA,
    }
