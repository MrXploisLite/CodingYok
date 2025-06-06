"""
Error handling for CodingYok language
Provides Indonesian error messages
"""

from typing import Optional, Any


class CodingYokError(Exception):
    """Base exception for all CodingYok errors"""

    def __init__(
        self, message: str, line: Optional[int] = None, column: Optional[int] = None
    ):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.format_message())

    def format_message(self) -> str:
        """Format error message with location info"""
        if self.line is not None and self.column is not None:
            return f"Baris {self.line}, Kolom {self.column}: {self.message}"
        elif self.line is not None:
            return f"Baris {self.line}: {self.message}"
        else:
            return self.message


class CodingYokSyntaxError(CodingYokError):
    """Syntax error in CodingYok code"""

    def __init__(
        self, message: str, line: Optional[int] = None, column: Optional[int] = None
    ):
        super().__init__(f"Kesalahan Sintaks: {message}", line, column)


class CodingYokRuntimeError(CodingYokError):
    """Runtime error during CodingYok execution"""

    def __init__(
        self, message: str, line: Optional[int] = None, column: Optional[int] = None
    ):
        super().__init__(f"Kesalahan Runtime: {message}", line, column)


class CodingYokNameError(CodingYokRuntimeError):
    """Name not found error"""

    def __init__(
        self, name: str, line: Optional[int] = None, column: Optional[int] = None
    ):
        super().__init__(f"Nama '{name}' tidak ditemukan", line, column)


class CodingYokTypeError(CodingYokRuntimeError):
    """Type error"""

    def __init__(
        self, message: str, line: Optional[int] = None, column: Optional[int] = None
    ):
        super().__init__(f"Kesalahan Tipe: {message}", line, column)


class CodingYokValueError(CodingYokRuntimeError):
    """Value error"""

    def __init__(
        self, message: str, line: Optional[int] = None, column: Optional[int] = None
    ):
        super().__init__(f"Kesalahan Nilai: {message}", line, column)


class CodingYokIndexError(CodingYokRuntimeError):
    """Index out of range error"""

    def __init__(
        self,
        message: str = "Indeks di luar jangkauan",
        line: Optional[int] = None,
        column: Optional[int] = None,
    ):
        super().__init__(message, line, column)


class CodingYokKeyError(CodingYokRuntimeError):
    """Key not found error"""

    def __init__(
        self, key: Any, line: Optional[int] = None, column: Optional[int] = None
    ):
        super().__init__(f"Kunci '{key}' tidak ditemukan", line, column)


class CodingYokAttributeError(CodingYokRuntimeError):
    """Attribute not found error"""

    def __init__(
        self,
        obj_type: str,
        attr: str,
        line: Optional[int] = None,
        column: Optional[int] = None,
    ):
        super().__init__(
            f"Objek '{obj_type}' tidak memiliki atribut '{attr}'", line, column
        )


class CodingYokZeroDivisionError(CodingYokRuntimeError):
    """Division by zero error"""

    def __init__(self, line: Optional[int] = None, column: Optional[int] = None):
        super().__init__("Pembagian dengan nol tidak diperbolehkan", line, column)


class CodingYokImportError(CodingYokRuntimeError):
    """Import error"""

    def __init__(
        self, module_name: str, line: Optional[int] = None, column: Optional[int] = None
    ):
        super().__init__(f"Tidak dapat mengimpor modul '{module_name}'", line, column)


class CodingYokIndentationError(CodingYokSyntaxError):
    """Indentation error"""

    def __init__(
        self,
        message: str = "Kesalahan indentasi",
        line: Optional[int] = None,
        column: Optional[int] = None,
    ):
        super().__init__(message, line, column)


def format_traceback(error: CodingYokError, source_lines: Optional[list] = None) -> str:
    """Format a nice traceback for CodingYok errors"""
    lines = []

    lines.append("=" * 50)
    lines.append("KESALAHAN CODINGYOK")
    lines.append("=" * 50)

    if error.line is not None and source_lines:
        # Show the problematic line
        if 0 <= error.line - 1 < len(source_lines):
            lines.append(f"Baris {error.line}:")
            lines.append(f"  {source_lines[error.line - 1].rstrip()}")

            # Add pointer to column if available
            if error.column is not None:
                pointer = " " * (error.column + 1) + "^"
                lines.append(f"  {pointer}")

    lines.append("")
    lines.append(str(error))
    lines.append("")

    # Add helpful suggestions based on error type
    if isinstance(error, CodingYokSyntaxError):
        lines.append("💡 Tips:")
        lines.append("   - Periksa tanda kurung, kurung siku, dan kurung kurawal")
        lines.append("   - Pastikan indentasi konsisten")
        lines.append("   - Periksa ejaan kata kunci bahasa Indonesia")
    elif isinstance(error, CodingYokNameError):
        lines.append("💡 Tips:")
        lines.append("   - Pastikan variabel sudah didefinisikan sebelum digunakan")
        lines.append("   - Periksa ejaan nama variabel")
    elif isinstance(error, CodingYokTypeError):
        lines.append("💡 Tips:")
        lines.append("   - Periksa tipe data yang digunakan")
        lines.append("   - Pastikan operasi sesuai dengan tipe data")

    lines.append("=" * 50)

    return "\n".join(lines)
