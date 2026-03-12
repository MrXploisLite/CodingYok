"""
Tests for CodingYok async/await features
"""

import sys
import os
import asyncio
import pytest
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from codingyok.lexer import CodingYokLexer
from codingyok.parser import CodingYokParser
from codingyok.interpreter import CodingYokInterpreter

class TestAsyncAwait:
    def setup_method(self):
        self.interpreter = CodingYokInterpreter()

    async def run_code(self, source_code):
        lexer = CodingYokLexer(source_code)
        tokens = lexer.tokenize()
        parser = CodingYokParser(tokens)
        ast = parser.parse()
        await self.interpreter.interpret(ast)

    async def capture_output(self, source_code):
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        try:
            await self.run_code(source_code)
            return captured_output.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    @pytest.mark.asyncio
    async def test_simple_async_call(self):
        code = """
        async fungsi halo():
            tulis("Halo dari async")

        menunggu halo()
        """
        output = await self.capture_output(code)
        assert output == "Halo dari async"

    @pytest.mark.asyncio
    async def test_async_await_chain(self):
        code = """
        async fungsi satu():
            kembalikan 1

        async fungsi dua():
            nilai = menunggu satu()
            kembalikan nilai + 1

        tulis(menunggu dua())
        """
        output = await self.capture_output(code)
        assert output == "2"

    @pytest.mark.asyncio
    async def test_async_tidur(self):
        import time
        code = """
        tulis("Mulai")
        menunggu async_tidur(0.1)
        tulis("Selesai")
        """
        start = time.time()
        output = await self.capture_output(code)
        end = time.time()
        assert "Mulai\nSelesai" in output
        assert end - start >= 0.1

    @pytest.mark.asyncio
    async def test_async_main_auto_run(self):
        code = """
        async fungsi main():
            tulis("Async main berjalan")
        """
        output = await self.capture_output(code)
        assert output == "Async main berjalan"

    @pytest.mark.asyncio
    async def test_async_loop(self):
        code = """
        async fungsi get_items():
            kembalikan [1, 2, 3]

        async fungsi main():
            items = menunggu get_items()
            untuk item dalam items:
                tulis(item)
        """
        output = await self.capture_output(code)
        assert output == "1\n2\n3"

    @pytest.mark.asyncio
    async def test_async_builtin_functions(self):
        # We need a small file for test
        with open("test_async_read.txt", "w") as f:
            f.write("Halo Async File!")

        code = """
        isi = menunggu async_baca_file("test_async_read.txt")
        tulis(isi)
        """
        try:
            output = await self.capture_output(code)
            assert "Halo Async File!" in output
        finally:
            if os.path.exists("test_async_read.txt"):
                os.remove("test_async_read.txt")
