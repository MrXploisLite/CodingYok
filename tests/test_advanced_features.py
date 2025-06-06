"""
Unit tests for advanced CodingYok features
Tests classes, Indonesian features, file I/O, and web functionality
"""

import pytest
import tempfile
import os
from io import StringIO
import sys
from src.codingyok.lexer import CodingYokLexer
from src.codingyok.parser import CodingYokParser
from src.codingyok.interpreter import CodingYokInterpreter
from src.codingyok.errors import CodingYokRuntimeError
from src.codingyok.indonesia import format_rupiah, angka_ke_kata, tanggal_indonesia
from src.codingyok.fileio import baca_file, tulis_file


class TestAdvancedFeatures:
    
    def setup_method(self):
        """Setup for each test"""
        self.interpreter = CodingYokInterpreter()
    
    def run_code(self, source_code):
        """Helper to run CodingYok code"""
        lexer = CodingYokLexer(source_code)
        tokens = lexer.tokenize()
        parser = CodingYokParser(tokens)
        ast = parser.parse()
        self.interpreter.interpret(ast)
    
    def capture_output(self, source_code):
        """Helper to capture print output"""
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            self.run_code(source_code)
            return captured_output.getvalue().strip()
        finally:
            sys.stdout = old_stdout
    
    def test_class_definition_and_instantiation(self):
        """Test basic class definition and object creation"""
        code = """
        kelas Orang:
            fungsi __init__(diri, nama):
                diri.nama = nama
            
            fungsi sapa(diri):
                tulis(f"Halo, saya {diri.nama}")
        
        orang1 = Orang("Budi")
        orang1.sapa()
        """
        output = self.capture_output(code)
        assert "Halo, saya Budi" in output
    
    def test_class_inheritance(self):
        """Test class inheritance"""
        code = """
        kelas Hewan:
            fungsi __init__(diri, nama):
                diri.nama = nama
            
            fungsi suara(diri):
                tulis(f"{diri.nama} membuat suara")
        
        kelas Kucing(Hewan):
            fungsi suara(diri):
                tulis(f"{diri.nama} mengeong")
        
        kucing = Kucing("Kitty")
        kucing.suara()
        """
        output = self.capture_output(code)
        assert "Kitty mengeong" in output
    
    def test_indonesian_currency_formatting(self):
        """Test Indonesian Rupiah formatting"""
        assert format_rupiah(1000000) == "Rp 1.000.000"
        assert format_rupiah(50000.50) == "Rp 50.000,50"
        assert format_rupiah(123456789) == "Rp 123.456.789"
    
    def test_number_to_indonesian_words(self):
        """Test number to Indonesian words conversion"""
        assert angka_ke_kata(5) == "lima"
        assert angka_ke_kata(17) == "tujuh belas"
        assert angka_ke_kata(100) == "seratus"
        assert angka_ke_kata(1000) == "seribu"
        assert angka_ke_kata(1500) == "seribu lima ratus"
    
    def test_indonesian_date_formatting(self):
        """Test Indonesian date formatting"""
        import datetime
        test_date = datetime.datetime(2024, 1, 15, 10, 30, 0)  # Monday
        result = tanggal_indonesia(test_date)
        assert "Senin" in result
        assert "15" in result
        assert "Januari" in result
        assert "2024" in result
    
    def test_file_operations_integration(self):
        """Test file I/O operations in CodingYok"""
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = os.path.join(temp_dir, "test.txt")
            
            code = f"""
            tulis_file("{test_file}", "Hello CodingYok!")
            content = baca_file("{test_file}")
            tulis(content)
            """
            
            output = self.capture_output(code)
            assert "Hello CodingYok!" in output
    
    def test_json_operations(self):
        """Test JSON file operations"""
        with tempfile.TemporaryDirectory() as temp_dir:
            json_file = os.path.join(temp_dir, "test.json")
            
            code = f"""
            data = {{"nama": "Budi", "umur": 25}}
            tulis_json("{json_file}", data)
            loaded_data = baca_json("{json_file}")
            tulis(loaded_data["nama"])
            tulis(loaded_data["umur"])
            """
            
            output = self.capture_output(code)
            lines = output.split('\n')
            assert "Budi" in lines
            assert "25" in lines
    
    def test_csv_operations(self):
        """Test CSV file operations"""
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_file = os.path.join(temp_dir, "test.csv")
            
            code = f"""
            data = [["Nama", "Umur"], ["Budi", "25"], ["Siti", "23"]]
            tulis_csv("{csv_file}", data)
            loaded_data = baca_csv("{csv_file}")
            tulis(panjang(loaded_data))
            tulis(loaded_data[1][0])  # Budi
            """
            
            output = self.capture_output(code)
            lines = output.split('\n')
            assert "3" in lines  # 3 rows including header
            assert "Budi" in lines
    
    def test_pattern_matching(self):
        """Test regex pattern matching"""
        code = """
        text = "Email: user@example.com dan nomor: 081234567890"
        email = cari_pola(r'[\\w\\.-]+@[\\w\\.-]+\\.\\w+', text)
        phone = cari_pola(r'08\\d{8,10}', text)
        tulis(email)
        tulis(phone)
        """
        
        output = self.capture_output(code)
        lines = output.split('\n')
        assert "user@example.com" in lines
        assert "081234567890" in lines
    
    def test_validation_functions(self):
        """Test validation functions"""
        code = """
        tulis(validasi_email("user@example.com"))
        tulis(validasi_email("invalid-email"))
        tulis(validasi_url("https://www.example.com"))
        tulis(validasi_url("not-a-url"))
        """
        
        output = self.capture_output(code)
        lines = output.split('\n')
        assert "benar" in lines[0]  # Valid email
        assert "salah" in lines[1]  # Invalid email
        assert "benar" in lines[2]  # Valid URL
        assert "salah" in lines[3]  # Invalid URL
    
    def test_indonesian_province_data(self):
        """Test Indonesian province data functions"""
        code = """
        tulis(cek_provinsi("jakarta"))
        tulis(cek_provinsi("jabar"))
        provinsi_list = daftar_provinsi()
        tulis(panjang(provinsi_list) > 30)  # Should have 34+ provinces
        """
        
        output = self.capture_output(code)
        lines = output.split('\n')
        assert "DKI Jakarta" in lines[0]
        assert "Jawa Barat" in lines[1]
        assert "benar" in lines[2]  # More than 30 provinces
    
    def test_temperature_conversion(self):
        """Test temperature conversion"""
        code = """
        celsius_to_f = konversi_suhu(32, "celsius", "fahrenheit")
        tulis(bulat(celsius_to_f, 1))
        
        fahrenheit_to_c = konversi_suhu(89.6, "fahrenheit", "celsius")
        tulis(bulat(fahrenheit_to_c, 1))
        """
        
        output = self.capture_output(code)
        lines = output.split('\n')
        assert "89.6" in lines[0]  # 32°C = 89.6°F
        assert "32.0" in lines[1]  # 89.6°F = 32°C
    
    def test_phone_number_formatting(self):
        """Test Indonesian phone number formatting"""
        code = """
        tulis(format_nomor_telepon("081234567890"))
        tulis(format_nomor_telepon("6281234567890"))
        """
        
        output = self.capture_output(code)
        lines = output.split('\n')
        assert "0812 3456 7890" in lines[0]
        assert "+62 812 3456 7890" in lines[1]
    
    def test_nik_validation(self):
        """Test NIK validation"""
        code = """
        tulis(validasi_nik("1234567890123456"))  # Valid format
        tulis(validasi_nik("123456789012345"))   # Too short
        tulis(validasi_nik("abcd567890123456"))  # Not digits
        """
        
        output = self.capture_output(code)
        lines = output.split('\n')
        assert "benar" in lines[0]  # Valid
        assert "salah" in lines[1]  # Too short
        assert "salah" in lines[2]  # Not digits
    
    def test_statistics_function(self):
        """Test statistics calculation"""
        code = """
        data = [10, 20, 30, 40, 50]
        stats = hitung_statistik(data)
        tulis(stats["rata_rata"])
        tulis(stats["median"])
        tulis(stats["minimum"])
        tulis(stats["maksimum"])
        """
        
        output = self.capture_output(code)
        lines = output.split('\n')
        assert "30.0" in lines[0]  # Average
        assert "30.0" in lines[1]  # Median
        assert "10" in lines[2]    # Minimum
        assert "50" in lines[3]    # Maximum
    
    def test_table_printing(self):
        """Test table printing function"""
        code = """
        data = [["Budi", "25", "Jakarta"], ["Siti", "23", "Bandung"]]
        header = ["Nama", "Umur", "Kota"]
        cetak_tabel(data, header)
        """
        
        output = self.capture_output(code)
        assert "Nama" in output
        assert "Budi" in output
        assert "Siti" in output
        assert "|" in output  # Table formatting
    
    def test_method_binding(self):
        """Test method binding in classes"""
        code = """
        kelas Calculator:
            fungsi __init__(diri):
                diri.value = 0
            
            fungsi add(diri, x):
                diri.value += x
                kembalikan diri.value
            
            fungsi get_value(diri):
                kembalikan diri.value
        
        calc = Calculator()
        calc.add(10)
        calc.add(5)
        tulis(calc.get_value())
        """
        
        output = self.capture_output(code)
        assert "15" in output
    
    def test_complex_class_interaction(self):
        """Test complex class interactions"""
        code = """
        kelas BankAccount:
            fungsi __init__(diri, nama, saldo_awal=0):
                diri.nama = nama
                diri.saldo = saldo_awal
                diri.riwayat = []
            
            fungsi deposit(diri, jumlah):
                diri.saldo += jumlah
                diri.riwayat.append(f"Deposit: {format_rupiah(jumlah)}")
            
            fungsi withdraw(diri, jumlah):
                jika jumlah <= diri.saldo:
                    diri.saldo -= jumlah
                    diri.riwayat.append(f"Withdraw: {format_rupiah(jumlah)}")
                    kembalikan benar
                kalau_tidak:
                    kembalikan salah
            
            fungsi get_saldo(diri):
                kembalikan diri.saldo
        
        account = BankAccount("Budi", 1000000)
        account.deposit(500000)
        account.withdraw(200000)
        tulis(format_rupiah(account.get_saldo()))
        """
        
        output = self.capture_output(code)
        assert "Rp 1.300.000" in output  # 1,000,000 + 500,000 - 200,000
