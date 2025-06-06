"""
Command Line Interface for CodingYok
"""

import sys
import argparse
from pathlib import Path
from typing import Optional

from .lexer import CodingYokLexer
from .parser import CodingYokParser
from .interpreter import CodingYokInterpreter
from .errors import CodingYokError, format_traceback
from . import __version__


def run_file(file_path: str) -> None:
    """Run a CodingYok file"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            source_code = file.read()

        run_code(source_code, file_path)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(
            f"Error: File '{file_path}' tidak dapat dibaca sebagai UTF-8.",
            file=sys.stderr,
        )
        sys.exit(1)


def run_code(source_code: str, filename: str = "<stdin>") -> None:
    """Run CodingYok source code"""
    try:
        # Tokenize
        lexer = CodingYokLexer(source_code)
        tokens = lexer.tokenize()

        # Parse
        parser = CodingYokParser(tokens)
        ast = parser.parse()

        # Interpret
        interpreter = CodingYokInterpreter()
        interpreter.interpret(ast)

    except CodingYokError as error:
        source_lines = source_code.splitlines()
        traceback = format_traceback(error, source_lines)
        print(traceback, file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"Error internal: {error}", file=sys.stderr)
        sys.exit(1)


def run_repl() -> None:
    """Run interactive REPL"""
    print(f"CodingYok v{__version__} - Bahasa Pemrograman Indonesia")
    print("Ketik 'keluar()' atau tekan Ctrl+C untuk keluar.")
    print("=" * 50)

    interpreter = CodingYokInterpreter()

    while True:
        try:
            # Get input
            line = input(">>> ")

            # Check for exit commands
            if line.strip() in ["keluar()", "exit()", "quit()"]:
                print("Sampai jumpa!")
                break

            if not line.strip():
                continue

            # Execute line
            try:
                lexer = CodingYokLexer(line)
                tokens = lexer.tokenize()

                parser = CodingYokParser(tokens)
                ast = parser.parse()

                interpreter.interpret(ast)

            except CodingYokError as error:
                source_lines = [line]
                traceback = format_traceback(error, source_lines)
                print(traceback)

        except KeyboardInterrupt:
            print("\nSampai jumpa!")
            break
        except EOFError:
            print("\nSampai jumpa!")
            break


def show_version() -> None:
    """Show version information"""
    print(f"CodingYok v{__version__}")
    print("Bahasa pemrograman modern dengan keyword bahasa Indonesia")
    print("Dibuat oleh MrXploisLite")


def show_help() -> None:
    """Show help information"""
    help_text = """
CodingYok - Bahasa Pemrograman Indonesia

PENGGUNAAN:
    codingyok [file.cy]          # Jalankan file CodingYok
    codingyok                    # Masuk mode interaktif (REPL)
    codingyok --version          # Tampilkan versi
    codingyok --help             # Tampilkan bantuan ini

CONTOH:
    codingyok hello.cy           # Jalankan file hello.cy
    codingyok                    # Mode interaktif

FITUR UTAMA:
    - Keyword bahasa Indonesia (tulis, jika, untuk, dll.)
    - Syntax familiar seperti Python
    - Built-in functions dengan nama Indonesia
    - Error messages dalam bahasa Indonesia
    - Support untuk tipe data modern

DOKUMENTASI:
    Lihat https://github.com/MrXploisLite/CodingYok untuk dokumentasi lengkap

CONTOH KODE:
    tulis("Halo Dunia!")
    
    nama = masukan("Siapa nama kamu? ")
    tulis(f"Halo {nama}!")
    
    untuk i dalam rentang(5):
        tulis(f"Angka: {i}")
"""
    print(help_text)


def main() -> None:
    """Main entry point"""
    parser = argparse.ArgumentParser(
        prog="codingyok",
        description="CodingYok - Bahasa Pemrograman Indonesia",
        add_help=False,  # We'll handle help ourselves
    )

    parser.add_argument("file", nargs="?", help="File CodingYok (.cy) untuk dijalankan")

    parser.add_argument(
        "--version", "-v", action="store_true", help="Tampilkan informasi versi"
    )

    parser.add_argument("--help", "-h", action="store_true", help="Tampilkan bantuan")

    parser.add_argument(
        "--debug", action="store_true", help="Mode debug (tampilkan token dan AST)"
    )

    args = parser.parse_args()

    # Handle special flags
    if args.version:
        show_version()
        return

    if args.help:
        show_help()
        return

    # Run file or REPL
    if args.file:
        # Validate file extension
        if not args.file.endswith(".cy"):
            print("Warning: File tidak memiliki ekstensi .cy", file=sys.stderr)

        run_file(args.file)
    else:
        run_repl()


if __name__ == "__main__":
    main()
