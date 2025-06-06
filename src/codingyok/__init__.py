"""
CodingYok - Bahasa Pemrograman Indonesia

A modern programming language with Indonesian keywords,
designed to make coding more accessible for Indonesian developers.
"""

__version__ = "1.0.0"
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
