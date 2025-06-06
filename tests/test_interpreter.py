"""
Unit tests for CodingYok interpreter
"""

import pytest
from io import StringIO
import sys
from src.codingyok.lexer import CodingYokLexer
from src.codingyok.parser import CodingYokParser
from src.codingyok.interpreter import CodingYokInterpreter
from src.codingyok.errors import CodingYokRuntimeError


class TestCodingYokInterpreter:
    
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
    
    def test_basic_print(self):
        """Test basic print functionality"""
        output = self.capture_output('tulis("Hello World")')
        assert output == "Hello World"
    
    def test_print_multiple_args(self):
        """Test print with multiple arguments"""
        output = self.capture_output('tulis("Hello", "World", 123)')
        assert output == "Hello World 123"
    
    def test_variables(self):
        """Test variable assignment and access"""
        code = """
        nama = "Budi"
        umur = 25
        tulis(nama, umur)
        """
        output = self.capture_output(code)
        assert output == "Budi 25"
    
    def test_arithmetic_operations(self):
        """Test arithmetic operations"""
        test_cases = [
            ("tulis(5 + 3)", "8"),
            ("tulis(10 - 4)", "6"),
            ("tulis(6 * 7)", "42"),
            ("tulis(15 / 3)", "5.0"),
            ("tulis(17 // 3)", "5"),
            ("tulis(17 % 3)", "2"),
            ("tulis(2 ** 3)", "8"),
        ]
        
        for code, expected in test_cases:
            output = self.capture_output(code)
            assert output == expected
    
    def test_comparison_operations(self):
        """Test comparison operations"""
        test_cases = [
            ("tulis(5 == 5)", "benar"),
            ("tulis(5 != 3)", "benar"),
            ("tulis(5 > 3)", "benar"),
            ("tulis(3 < 5)", "benar"),
            ("tulis(5 >= 5)", "benar"),
            ("tulis(3 <= 5)", "benar"),
            ("tulis(5 == 3)", "salah"),
        ]
        
        for code, expected in test_cases:
            output = self.capture_output(code)
            assert output == expected
    
    def test_logical_operations(self):
        """Test logical operations"""
        test_cases = [
            ("tulis(benar dan benar)", "benar"),
            ("tulis(benar dan salah)", "salah"),
            ("tulis(benar atau salah)", "benar"),
            ("tulis(salah atau salah)", "salah"),
            ("tulis(bukan benar)", "salah"),
            ("tulis(bukan salah)", "benar"),
        ]
        
        for code, expected in test_cases:
            output = self.capture_output(code)
            assert output == expected
    
    def test_if_statement(self):
        """Test if statements"""
        code = """
        nilai = 85
        jika nilai >= 80:
            tulis("Baik")
        kalau_tidak:
            tulis("Cukup")
        """
        output = self.capture_output(code)
        assert output == "Baik"
    
    def test_elif_statement(self):
        """Test elif statements"""
        code = """
        nilai = 75
        jika nilai >= 90:
            tulis("A")
        kalau_tidak_jika nilai >= 80:
            tulis("B")
        kalau_tidak_jika nilai >= 70:
            tulis("C")
        kalau_tidak:
            tulis("D")
        """
        output = self.capture_output(code)
        assert output == "C"
    
    def test_while_loop(self):
        """Test while loops"""
        code = """
        i = 1
        selama i <= 3:
            tulis(i)
            i = i + 1
        """
        output = self.capture_output(code)
        assert output == "1\n2\n3"
    
    def test_for_loop(self):
        """Test for loops"""
        code = """
        untuk i dalam rentang(1, 4):
            tulis(i)
        """
        output = self.capture_output(code)
        assert output == "1\n2\n3"
    
    def test_for_loop_with_list(self):
        """Test for loops with lists"""
        code = """
        buah = ["apel", "jeruk", "mangga"]
        untuk item dalam buah:
            tulis(item)
        """
        output = self.capture_output(code)
        assert output == "apel\njeruk\nmangga"
    
    def test_function_definition_and_call(self):
        """Test function definition and calling"""
        code = """
        fungsi sapa(nama):
            tulis("Halo", nama)
        
        sapa("Budi")
        """
        output = self.capture_output(code)
        assert output == "Halo Budi"
    
    def test_function_with_return(self):
        """Test function with return value"""
        code = """
        fungsi tambah(a, b):
            kembalikan a + b
        
        hasil = tambah(5, 3)
        tulis(hasil)
        """
        output = self.capture_output(code)
        assert output == "8"
    
    def test_function_with_default_parameters(self):
        """Test function with default parameters"""
        code = """
        fungsi sapa(nama, umur=20):
            tulis(nama, umur)
        
        sapa("Budi")
        sapa("Siti", 25)
        """
        output = self.capture_output(code)
        assert output == "Budi 20\nSiti 25"
    
    def test_list_operations(self):
        """Test list operations"""
        code = """
        daftar = [1, 2, 3]
        tulis(daftar[0])
        tulis(panjang(daftar))
        """
        output = self.capture_output(code)
        assert output == "1\n3"
    
    def test_dict_operations(self):
        """Test dictionary operations"""
        code = """
        data = {"nama": "Budi", "umur": 25}
        tulis(data["nama"])
        tulis(data["umur"])
        """
        output = self.capture_output(code)
        assert output == "Budi\n25"
    
    def test_builtin_functions(self):
        """Test built-in functions"""
        test_cases = [
            ('tulis(panjang("hello"))', "5"),
            ('tulis(tipe(123))', "bilangan_bulat"),
            ('tulis(tipe("text"))', "teks"),
            ('tulis(maksimum([1, 5, 3]))', "5"),
            ('tulis(minimum([1, 5, 3]))', "1"),
            ('tulis(jumlah([1, 2, 3]))', "6"),
        ]
        
        for code, expected in test_cases:
            output = self.capture_output(code)
            assert output == expected
    
    def test_string_operations(self):
        """Test string operations"""
        code = """
        teks = "Hello World"
        tulis(huruf_besar(teks))
        tulis(huruf_kecil(teks))
        """
        output = self.capture_output(code)
        assert output == "HELLO WORLD\nhello world"
    
    def test_error_handling(self):
        """Test error handling"""
        # Division by zero
        with pytest.raises(Exception):  # Should raise CodingYokZeroDivisionError
            self.run_code("tulis(5 / 0)")
        
        # Undefined variable
        with pytest.raises(Exception):  # Should raise CodingYokNameError
            self.run_code("tulis(undefined_variable)")
    
    def test_nested_scopes(self):
        """Test nested function scopes"""
        code = """
        x = 10
        
        fungsi outer():
            y = 20
            
            fungsi inner():
                tulis(x + y)
            
            inner()
        
        outer()
        """
        output = self.capture_output(code)
        assert output == "30"
    
    def test_recursion(self):
        """Test recursive functions"""
        code = """
        fungsi faktorial(n):
            jika n <= 1:
                kembalikan 1
            kalau_tidak:
                kembalikan n * faktorial(n - 1)
        
        tulis(faktorial(5))
        """
        output = self.capture_output(code)
        assert output == "120"
    
    def test_break_continue(self):
        """Test break and continue statements"""
        code = """
        untuk i dalam rentang(5):
            jika i == 2:
                lanjut
            jika i == 4:
                berhenti
            tulis(i)
        """
        output = self.capture_output(code)
        assert output == "0\n1\n3"
