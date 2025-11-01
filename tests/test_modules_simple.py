"""
Simple tests for CodingYok module system (without pytest)
"""

import sys
import os
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

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
    print("Testing basic import...", end=" ")
    code = """
impor matematika
hasil = matematika.tambah(5, 3)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil") == 8
    print("✓")


def test_import_with_alias():
    """Test import with alias"""
    print("Testing import with alias...", end=" ")
    code = """
impor matematika sebagai math
hasil = math.kurang(10, 3)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil") == 7
    print("✓")


def test_from_import():
    """Test from import"""
    print("Testing from import...", end=" ")
    code = """
dari matematika impor tambah, kali
hasil1 = tambah(5, 3)
hasil2 = kali(4, 6)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil1") == 8
    assert interpreter.environment.get("hasil2") == 24
    print("✓")


def test_from_import_with_alias():
    """Test from import with alias"""
    print("Testing from import with alias...", end=" ")
    code = """
dari matematika impor tambah sebagai add
hasil = add(7, 3)
"""
    interpreter = run_code(code)
    assert interpreter.environment.get("hasil") == 10
    print("✓")


def test_import_constant():
    """Test importing constants"""
    print("Testing import constants...", end=" ")
    code = """
dari matematika impor PI
"""
    interpreter = run_code(code)
    pi_value = interpreter.environment.get("PI")
    assert abs(pi_value - 3.141592653589793) < 0.0001
    print("✓")


def test_module_not_found():
    """Test error when module not found"""
    print("Testing module not found error...", end=" ")
    code = """
impor module_yang_tidak_ada
"""
    try:
        import io
        import sys

        old_stderr = sys.stderr
        sys.stderr = io.StringIO()

        try:
            run_code(code)
        except SystemExit:
            pass

        error_output = sys.stderr.getvalue()
        sys.stderr = old_stderr

        # Check if error message contains expected text
        assert (
            "tidak ditemukan" in error_output or "module_yang_tidak_ada" in error_output
        )
        print("✓")
    except Exception as e:
        print(f"✗ - {e}")


def test_custom_module():
    """Test importing custom user module"""
    print("Testing custom module...", end=" ")
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
        print("✓")


def test_module_with_class():
    """Test importing module with class"""
    print("Testing module with class...", end=" ")
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
        print("✓")


def test_module_caching():
    """Test that modules are cached"""
    print("Testing module caching...", end=" ")
    code = """
impor matematika
dari matematika impor PI
impor matematika sebagai math
"""
    interpreter = run_code(code)
    assert "matematika" in interpreter.module_loader.cache
    print("✓")


def test_multiple_imports_same_module():
    """Test multiple imports from same module"""
    print("Testing multiple imports...", end=" ")
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
    print("✓")


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 50)
    print("Running Module System Tests")
    print("=" * 50 + "\n")

    tests = [
        test_basic_import,
        test_import_with_alias,
        test_from_import,
        test_from_import_with_alias,
        test_import_constant,
        test_module_not_found,
        test_custom_module,
        test_module_with_class,
        test_module_caching,
        test_multiple_imports_same_module,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ - {e}")
            failed += 1

    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 50 + "\n")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
