"""
File I/O and advanced utilities for CodingYok
Provides Indonesian-named file operations and utilities
"""

import os
import json
import csv
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from .errors import CodingYokRuntimeError, CodingYokValueError


def baca_file(nama_file: str, encoding: str = 'utf-8') -> str:
    """Read file content (Indonesian: read file)"""
    try:
        with open(nama_file, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File '{nama_file}' tidak ditemukan")
    except UnicodeDecodeError:
        raise CodingYokRuntimeError(f"File '{nama_file}' tidak dapat dibaca dengan encoding {encoding}")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error membaca file '{nama_file}': {str(e)}")


def tulis_file(nama_file: str, konten: str, encoding: str = 'utf-8', mode: str = 'w') -> None:
    """Write content to file (Indonesian: write file)"""
    try:
        with open(nama_file, mode, encoding=encoding) as file:
            file.write(konten)
    except Exception as e:
        raise CodingYokRuntimeError(f"Error menulis file '{nama_file}': {str(e)}")


def tambah_ke_file(nama_file: str, konten: str, encoding: str = 'utf-8') -> None:
    """Append content to file (Indonesian: add to file)"""
    tulis_file(nama_file, konten, encoding, 'a')


def baca_baris(nama_file: str, encoding: str = 'utf-8') -> List[str]:
    """Read file lines as list (Indonesian: read lines)"""
    try:
        with open(nama_file, 'r', encoding=encoding) as file:
            return [line.rstrip('\n\r') for line in file.readlines()]
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File '{nama_file}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error membaca baris file '{nama_file}': {str(e)}")


def tulis_baris(nama_file: str, baris_list: List[str], encoding: str = 'utf-8') -> None:
    """Write list of lines to file (Indonesian: write lines)"""
    try:
        with open(nama_file, 'w', encoding=encoding) as file:
            for baris in baris_list:
                file.write(str(baris) + '\n')
    except Exception as e:
        raise CodingYokRuntimeError(f"Error menulis baris ke file '{nama_file}': {str(e)}")


def ada_file(nama_file: str) -> bool:
    """Check if file exists (Indonesian: file exists)"""
    return os.path.exists(nama_file)


def hapus_file(nama_file: str) -> None:
    """Delete file (Indonesian: delete file)"""
    try:
        os.remove(nama_file)
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File '{nama_file}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error menghapus file '{nama_file}': {str(e)}")


def salin_file(sumber: str, tujuan: str) -> None:
    """Copy file (Indonesian: copy file)"""
    try:
        import shutil
        shutil.copy2(sumber, tujuan)
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File sumber '{sumber}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error menyalin file: {str(e)}")


def pindah_file(sumber: str, tujuan: str) -> None:
    """Move/rename file (Indonesian: move file)"""
    try:
        import shutil
        shutil.move(sumber, tujuan)
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File sumber '{sumber}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error memindah file: {str(e)}")


def ukuran_file(nama_file: str) -> int:
    """Get file size in bytes (Indonesian: file size)"""
    try:
        return os.path.getsize(nama_file)
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File '{nama_file}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error mendapatkan ukuran file: {str(e)}")


def info_file(nama_file: str) -> Dict[str, Any]:
    """Get file information (Indonesian: file info)"""
    try:
        stat = os.stat(nama_file)
        return {
            'ukuran': stat.st_size,
            'dibuat': stat.st_ctime,
            'dimodifikasi': stat.st_mtime,
            'diakses': stat.st_atime,
            'adalah_file': os.path.isfile(nama_file),
            'adalah_direktori': os.path.isdir(nama_file),
        }
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File '{nama_file}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error mendapatkan info file: {str(e)}")


# Directory operations
def buat_direktori(nama_dir: str) -> None:
    """Create directory (Indonesian: create directory)"""
    try:
        os.makedirs(nama_dir, exist_ok=True)
    except Exception as e:
        raise CodingYokRuntimeError(f"Error membuat direktori '{nama_dir}': {str(e)}")


def hapus_direktori(nama_dir: str) -> None:
    """Remove directory (Indonesian: delete directory)"""
    try:
        import shutil
        shutil.rmtree(nama_dir)
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"Direktori '{nama_dir}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error menghapus direktori '{nama_dir}': {str(e)}")


def daftar_file(direktori: str = '.') -> List[str]:
    """List files in directory (Indonesian: list files)"""
    try:
        return [f for f in os.listdir(direktori) if os.path.isfile(os.path.join(direktori, f))]
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"Direktori '{direktori}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error membaca direktori '{direktori}': {str(e)}")


def daftar_direktori(direktori: str = '.') -> List[str]:
    """List directories (Indonesian: list directories)"""
    try:
        return [d for d in os.listdir(direktori) if os.path.isdir(os.path.join(direktori, d))]
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"Direktori '{direktori}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error membaca direktori '{direktori}': {str(e)}")


# JSON operations
def baca_json(nama_file: str) -> Any:
    """Read JSON file (Indonesian: read JSON)"""
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File JSON '{nama_file}' tidak ditemukan")
    except json.JSONDecodeError as e:
        raise CodingYokRuntimeError(f"Error parsing JSON: {str(e)}")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error membaca JSON: {str(e)}")


def tulis_json(nama_file: str, data: Any, indent: int = 2) -> None:
    """Write data to JSON file (Indonesian: write JSON)"""
    try:
        with open(nama_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)
    except Exception as e:
        raise CodingYokRuntimeError(f"Error menulis JSON: {str(e)}")


# CSV operations
def baca_csv(nama_file: str, delimiter: str = ',') -> List[List[str]]:
    """Read CSV file (Indonesian: read CSV)"""
    try:
        with open(nama_file, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file, delimiter=delimiter)
            return list(reader)
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"File CSV '{nama_file}' tidak ditemukan")
    except Exception as e:
        raise CodingYokRuntimeError(f"Error membaca CSV: {str(e)}")


def tulis_csv(nama_file: str, data: List[List[Any]], delimiter: str = ',') -> None:
    """Write data to CSV file (Indonesian: write CSV)"""
    try:
        with open(nama_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerows(data)
    except Exception as e:
        raise CodingYokRuntimeError(f"Error menulis CSV: {str(e)}")


# Regular expressions with Indonesian interface
def cari_pola(pola: str, teks: str, semua: bool = False) -> Union[str, List[str], None]:
    """Search pattern in text (Indonesian: search pattern)"""
    try:
        if semua:
            matches = re.findall(pola, teks)
            return matches if matches else []
        else:
            match = re.search(pola, teks)
            return match.group() if match else None
    except re.error as e:
        raise CodingYokValueError(f"Pola regex tidak valid: {str(e)}")


def ganti_pola(pola: str, pengganti: str, teks: str, semua: bool = True) -> str:
    """Replace pattern in text (Indonesian: replace pattern)"""
    try:
        if semua:
            return re.sub(pola, pengganti, teks)
        else:
            return re.sub(pola, pengganti, teks, count=1)
    except re.error as e:
        raise CodingYokValueError(f"Pola regex tidak valid: {str(e)}")


def pisah_pola(pola: str, teks: str) -> List[str]:
    """Split text by pattern (Indonesian: split pattern)"""
    try:
        return re.split(pola, teks)
    except re.error as e:
        raise CodingYokValueError(f"Pola regex tidak valid: {str(e)}")


def validasi_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validasi_url(url: str) -> bool:
    """Validate URL format"""
    pattern = r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$'
    return bool(re.match(pattern, url))


def get_fileio_functions() -> Dict[str, callable]:
    """Get all file I/O and utility functions"""
    return {
        # File operations
        'baca_file': baca_file,
        'tulis_file': tulis_file,
        'tambah_ke_file': tambah_ke_file,
        'baca_baris': baca_baris,
        'tulis_baris': tulis_baris,
        'ada_file': ada_file,
        'hapus_file': hapus_file,
        'salin_file': salin_file,
        'pindah_file': pindah_file,
        'ukuran_file': ukuran_file,
        'info_file': info_file,
        
        # Directory operations
        'buat_direktori': buat_direktori,
        'hapus_direktori': hapus_direktori,
        'daftar_file': daftar_file,
        'daftar_direktori': daftar_direktori,
        
        # JSON operations
        'baca_json': baca_json,
        'tulis_json': tulis_json,
        
        # CSV operations
        'baca_csv': baca_csv,
        'tulis_csv': tulis_csv,
        
        # Pattern matching
        'cari_pola': cari_pola,
        'ganti_pola': ganti_pola,
        'pisah_pola': pisah_pola,
        
        # Validation
        'validasi_email': validasi_email,
        'validasi_url': validasi_url,
    }
