"""
CodingYok - Bahasa Pemrograman Indonesia

A modern programming language with Indonesian keywords,
designed to make coding more accessible for Indonesian developers.

Version 3.0.0 - Advanced Features:
- Lambda Expressions (anonymous functions)
- Exception Handling (coba/kecuali/akhirnya/lempar)
- Context Managers (dengan statement)
- Professional error handling infrastructure
- Full backward compatibility with v2.0
"""

__version__ = "3.0.0"
__author__ = "MrXploisLite"
__email__ = "108934584+MrXploisLite@users.noreply.github.com"

from .interpreter import CodingYokInterpreter
from .lexer import CodingYokLexer
from .parser import CodingYokParser
from .errors import CodingYokError, CodingYokSyntaxError, CodingYokRuntimeError

__all__ = [
    "CodingYokInterpreter",
    "CodingYokLexer",
    "CodingYokParser",
    "CodingYokError",
    "CodingYokSyntaxError",
    "CodingYokRuntimeError",
]
