"""
CodingYok - Bahasa Pemrograman Indonesia

A modern programming language with Indonesian keywords,
designed to make coding more accessible for Indonesian developers.

Version 2.0.0 - Major Update:
- List/Dict/Set Comprehensions
- Generators with yield
- Pattern Matching (cocokkan/kasus)
- Better error messages with suggestions
- Set data type support
"""

__version__ = "2.0.0"
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
