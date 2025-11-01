"""
Tests for CodingYok module system
"""

import sys
import os
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from codingyok.lexer import CodingYokLexer
from codingyok.parser import CodingYokParser
from codingyok.interpreter import CodingYokInterpreter
from codingyok.errors import CodingYokRuntimeError


def run_code(code, script_dir=None):
    """Helper to run CodingYok code"""
    lexer = CodingYokLexer(code)
    tokens = lexer.tokenize()
    parser = CodingYokParser(tokens)
    ast = parser.parse()
    interpreter = CodingYokInterpreter(script_dir=script_dir)
    interpreter.interpret(ast)
    return interpreter


def test_basic_import():
    """Test basic module import"""
    code = """
impor matematika
hasil = matematika.tambah(5, 3)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil") == 8


def test_import_with_alias():
    """Test import with alias"""
    code = """
impor matematika sebagai math
hasil = math.kurang(10, 3)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil") == 7


def test_from_import():
    """Test from import"""
    code = """
dari matematika impor tambah, kali
hasil1 = tambah(5, 3)
hasil2 = kali(4, 6)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil1") == 8
    assert interpreter.environment.get("hasil2") == 24


def test_from_import_with_alias():
    """Test from import with alias"""
    code = """
dari matematika impor tambah sebagai add
hasil = add(7, 3)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil") == 10


def test_import_constant():
    """Test importing constants"""
    code = """
dari matematika impor PI
"""
    interpreter = run_code(code)
    pi_value = interpreter.environment.get("PI")
    assert abs(pi_value - 3.141592653589793) < 0.0001


def test_module_not_found():
    """Test error when module not found"""
    import io
    import sys

    code = """
impor module_yang_tidak_ada
"""
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()

    try:
        run_code(code)
    except SystemExit:
        pass

    error_output = sys.stderr.getvalue()
    sys.stderr = old_stderr

    # Check if error message contains expected text
    assert "tidak ditemukan" in error_output or "module_yang_tidak_ada" in error_output


def test_name_not_found_in_module():
    """Test error when name not found in module"""
    import io
    import sys

    code = """
dari matematika impor fungsi_tidak_ada
"""
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()

    try:
        run_code(code)
    except SystemExit:
        pass

    error_output = sys.stderr.getvalue()
    sys.stderr = old_stderr

    # Check if error message contains expected text
    assert "fungsi_tidak_ada" in error_output or "tidak ditemukan" in error_output


def test_custom_module():
    """Test importing custom user module"""
    # Create a temporary directory with a module
    with tempfile.TemporaryDirectory() as tmpdir:
        module_path = Path(tmpdir) / "my_module.cy"
        module_path.write_text(
            """
fungsi greet(name):
    kembalikan f"Hello, {name}!"

CONSTANT = 42
"""
        )

        code = """
impor my_module
hasil = my_module.greet("Test")
nilai = my_module.CONSTANT
"""
        interpreter = run_code(code, script_dir=tmpdir)
        assert interpreter.environment.get("hasil") == "Hello, Test!"
        assert interpreter.environment.get("nilai") == 42


def test_module_with_class():
    """Test importing module with class"""
    with tempfile.TemporaryDirectory() as tmpdir:
        module_path = Path(tmpdir) / "class_module.cy"
        module_path.write_text(
            """
kelas Calculator:
    fungsi __init__(diri):
        diri.value = 0
    
    fungsi add(diri, n):
        diri.value = diri.value + n
        kembalikan diri.value
"""
        )

        code = """
impor class_module
calc = class_module.Calculator()
hasil = calc.add(5)
"""
        interpreter = run_code(code, script_dir=tmpdir)
        assert interpreter.environment.get("hasil") == 5


def test_module_caching():
    """Test that modules are cached"""
    code = """
impor matematika
dari matematika impor PI
impor matematika sebagai math
"""
    interpreter = run_code(code)
    # Should not raise any errors
    # Module should be loaded only once
    assert "matematika" in interpreter.module_loader.cache


def test_multiple_imports_same_module():
    """Test multiple imports from same module"""
    code = """
dari matematika impor tambah, kurang, kali, bagi
a = tambah(10, 5)
b = kurang(10, 5)
c = kali(10, 5)
d = bagi(10, 5)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("a") == 15
    assert interpreter.environment.get("b") == 5
    assert interpreter.environment.get("c") == 50
    assert interpreter.environment.get("d") == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
