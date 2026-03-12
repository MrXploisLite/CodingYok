"""
Unit tests for CodingYok interpreter
"""

import sys
import os
import asyncio

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from io import StringIO
from codingyok.lexer import CodingYokLexer
from codingyok.parser import CodingYokParser
from codingyok.interpreter import CodingYokInterpreter


class TestCodingYokInterpreter:

    def setup_method(self):
        """Setup for each test"""
        self.interpreter = CodingYokInterpreter()

    async def run_code(self, source_code):
        """Helper to run CodingYok code"""
        lexer = CodingYokLexer(source_code)
        tokens = lexer.tokenize()
        parser = CodingYokParser(tokens)
        ast = parser.parse()
        await self.interpreter.interpret(ast)

    async def capture_output(self, source_code):
        """Helper to capture print output"""
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        try:
            await self.run_code(source_code)
            return captured_output.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    @pytest.mark.asyncio
    async def test_basic_print(self):
        """Test basic print functionality"""
        output = await self.capture_output('tulis("Hello World")')
        assert output == "Hello World"

    @pytest.mark.asyncio
    async def test_print_multiple_args(self):
        """Test print with multiple arguments"""
        output = await self.capture_output('tulis("Hello", "World", 123)')
        assert output == "Hello World 123"

    @pytest.mark.asyncio
    async def test_variables(self):
        """Test variable assignment and access"""
        code = """
        nama = "Budi"
        umur = 25
        tulis(nama, umur)
        """
        output = await self.capture_output(code)
        assert output == "Budi 25"

    @pytest.mark.asyncio
    async def test_arithmetic_operations(self):
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
            output = await self.capture_output(code)
            assert output == expected

    @pytest.mark.asyncio
    async def test_comparison_operations(self):
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
            output = await self.capture_output(code)
            assert output == expected

    @pytest.mark.asyncio
    async def test_logical_operations(self):
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
            output = await self.capture_output(code)
            assert output == expected

    @pytest.mark.asyncio
    async def test_if_statement(self):
        """Test if statements"""
        code = """
        nilai = 85
        jika nilai >= 80:
            tulis("Baik")
        kalau_tidak:
            tulis("Cukup")
        """
        output = await self.capture_output(code)
        assert output == "Baik"

    @pytest.mark.asyncio
    async def test_elif_statement(self):
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
        output = await self.capture_output(code)
        assert output == "C"

    @pytest.mark.asyncio
    async def test_while_loop(self):
        """Test while loops"""
        code = """
        i = 1
        selama i <= 3:
            tulis(i)
            i = i + 1
        """
        output = await self.capture_output(code)
        assert output == "1\n2\n3"

    @pytest.mark.asyncio
    async def test_for_loop(self):
        """Test for loops"""
        code = """
        untuk i dalam rentang(1, 4):
            tulis(i)
        """
        output = await self.capture_output(code)
        assert output == "1\n2\n3"

    @pytest.mark.asyncio
    async def test_for_loop_with_list(self):
        """Test for loops with lists"""
        code = """
        buah = ["apel", "jeruk", "mangga"]
        untuk item dalam buah:
            tulis(item)
        """
        output = await self.capture_output(code)
        assert output == "apel\njeruk\nmangga"

    @pytest.mark.asyncio
    async def test_function_definition_and_call(self):
        """Test function definition and calling"""
        code = """
        fungsi sapa(nama):
            tulis("Halo", nama)
        
        sapa("Budi")
        """
        output = await self.capture_output(code)
        assert output == "Halo Budi"

    @pytest.mark.asyncio
    async def test_function_with_return(self):
        """Test function with return value"""
        code = """
        fungsi tambah(a, b):
            kembalikan a + b
        
        hasil = tambah(5, 3)
        tulis(hasil)
        """
        output = await self.capture_output(code)
        assert output == "8"

    @pytest.mark.asyncio
    async def test_function_with_default_parameters(self):
        """Test function with default parameters"""
        code = """
        fungsi sapa(nama, umur=20):
            tulis(nama, umur)
        
        sapa("Budi")
        sapa("Siti", 25)
        """
        output = await self.capture_output(code)
        assert output == "Budi 20\nSiti 25"

    @pytest.mark.asyncio
    async def test_list_operations(self):
        """Test list operations"""
        code = """
        daftar = [1, 2, 3]
        tulis(daftar[0])
        tulis(panjang(daftar))
        """
        output = await self.capture_output(code)
        assert output == "1\n3"

    @pytest.mark.asyncio
    async def test_dict_operations(self):
        """Test dictionary operations"""
        code = """
        data = {"nama": "Budi", "umur": 25}
        tulis(data["nama"])
        tulis(data["umur"])
        """
        output = await self.capture_output(code)
        assert output == "Budi\n25"

    @pytest.mark.asyncio
    async def test_builtin_functions(self):
        """Test built-in functions"""
        test_cases = [
            ('tulis(panjang("hello"))', "5"),
            ("tulis(tipe(123))", "bilangan_bulat"),
            ('tulis(tipe("text"))', "teks"),
            ("tulis(maksimum([1, 5, 3]))", "5"),
            ("tulis(minimum([1, 5, 3]))", "1"),
            ("tulis(jumlah([1, 2, 3]))", "6"),
        ]

        for code, expected in test_cases:
            output = await self.capture_output(code)
            assert output == expected

    @pytest.mark.asyncio
    async def test_string_operations(self):
        """Test string operations"""
        code = """
        teks = "Hello World"
        tulis(huruf_besar(teks))
        tulis(huruf_kecil(teks))
        """
        output = await self.capture_output(code)
        assert output == "HELLO WORLD\nhello world"

    @pytest.mark.asyncio
    async def test_error_handling(self):
        """Test error handling"""
        # Division by zero - test the expression evaluation directly
        from codingyok.ast_nodes import BinaryExpression, LiteralExpression
        from codingyok.errors import CodingYokZeroDivisionError

        # Create a division by zero expression
        left = LiteralExpression(5)
        right = LiteralExpression(0)
        div_expr = BinaryExpression(left, "/", right)

        with pytest.raises(CodingYokZeroDivisionError):
            await self.interpreter.evaluate(div_expr)

        # Undefined variable - test environment access directly
        from codingyok.ast_nodes import IdentifierExpression
        from codingyok.errors import CodingYokNameError

        undefined_expr = IdentifierExpression("undefined_variable")
        with pytest.raises(CodingYokNameError):
            await self.interpreter.evaluate(undefined_expr)

    @pytest.mark.asyncio
    async def test_nested_scopes(self):
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
        output = await self.capture_output(code)
        assert output == "30"

    @pytest.mark.asyncio
    async def test_recursion(self):
        """Test recursive functions"""
        code = """
        fungsi faktorial(n):
            jika n <= 1:
                kembalikan 1
            kalau_tidak:
                kembalikan n * faktorial(n - 1)
        
        tulis(faktorial(5))
        """
        output = await self.capture_output(code)
        assert output == "120"

    @pytest.mark.asyncio
    async def test_break_continue(self):
        """Test break and continue statements"""
        code = """
        untuk i dalam rentang(5):
            jika i == 2:
                lanjut
            jika i == 4:
                berhenti
            tulis(i)
        """
        output = await self.capture_output(code)
        assert output == "0\n1\n3"
