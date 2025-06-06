"""
Token definitions for CodingYok language
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional


class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    
    # Keywords (Indonesian)
    TULIS = auto()          # print
    JIKA = auto()           # if
    KALAU_TIDAK = auto()    # else
    KALAU_TIDAK_JIKA = auto() # elif
    UNTUK = auto()          # for
    SELAMA = auto()         # while
    FUNGSI = auto()         # def
    KELAS = auto()          # class
    IMPOR = auto()          # import
    DARI = auto()           # from
    KEMBALIKAN = auto()     # return
    LEWATI = auto()         # pass
    BERHENTI = auto()       # break
    LANJUT = auto()         # continue
    COBA = auto()           # try
    KECUALI = auto()        # except
    AKHIRNYA = auto()       # finally
    DENGAN = auto()         # with
    SEBAGAI = auto()        # as
    DALAM = auto()          # in
    BUKAN = auto()          # not
    DAN = auto()            # and
    ATAU = auto()           # or
    ADALAH = auto()         # is
    LAMBDA = auto()         # lambda
    GLOBAL = auto()         # global
    NONLOKAL = auto()       # nonlocal
    TEGAS = auto()          # assert
    HAPUS = auto()          # del
    HASIL = auto()          # yield
    
    # Boolean and None
    BENAR = auto()          # True
    SALAH = auto()          # False
    KOSONG = auto()         # None
    
    # Operators
    PLUS = auto()           # +
    MINUS = auto()          # -
    MULTIPLY = auto()       # *
    DIVIDE = auto()         # /
    FLOOR_DIVIDE = auto()   # //
    MODULO = auto()         # %
    POWER = auto()          # **
    
    # Comparison
    EQUAL = auto()          # ==
    NOT_EQUAL = auto()      # !=
    LESS_THAN = auto()      # <
    LESS_EQUAL = auto()     # <=
    GREATER_THAN = auto()   # >
    GREATER_EQUAL = auto()  # >=
    
    # Assignment
    ASSIGN = auto()         # =
    PLUS_ASSIGN = auto()    # +=
    MINUS_ASSIGN = auto()   # -=
    MULTIPLY_ASSIGN = auto() # *=
    DIVIDE_ASSIGN = auto()  # /=
    
    # Delimiters
    LEFT_PAREN = auto()     # (
    RIGHT_PAREN = auto()    # )
    LEFT_BRACKET = auto()   # [
    RIGHT_BRACKET = auto()  # ]
    LEFT_BRACE = auto()     # {
    RIGHT_BRACE = auto()    # }
    COMMA = auto()          # ,
    DOT = auto()            # .
    COLON = auto()          # :
    SEMICOLON = auto()      # ;
    ARROW = auto()          # ->
    
    # Special
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()
    COMMENT = auto()


@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    column: int
    
    def __str__(self) -> str:
        return f"Token({self.type.name}, {repr(self.value)}, {self.line}:{self.column})"
    
    def __repr__(self) -> str:
        return self.__str__()


# Indonesian keyword mapping
INDONESIAN_KEYWORDS = {
    'tulis': TokenType.TULIS,
    'jika': TokenType.JIKA,
    'kalau_tidak': TokenType.KALAU_TIDAK,
    'kalau_tidak_jika': TokenType.KALAU_TIDAK_JIKA,
    'untuk': TokenType.UNTUK,
    'selama': TokenType.SELAMA,
    'fungsi': TokenType.FUNGSI,
    'kelas': TokenType.KELAS,
    'impor': TokenType.IMPOR,
    'dari': TokenType.DARI,
    'kembalikan': TokenType.KEMBALIKAN,
    'lewati': TokenType.LEWATI,
    'berhenti': TokenType.BERHENTI,
    'lanjut': TokenType.LANJUT,
    'coba': TokenType.COBA,
    'kecuali': TokenType.KECUALI,
    'akhirnya': TokenType.AKHIRNYA,
    'dengan': TokenType.DENGAN,
    'sebagai': TokenType.SEBAGAI,
    'dalam': TokenType.DALAM,
    'bukan': TokenType.BUKAN,
    'dan': TokenType.DAN,
    'atau': TokenType.ATAU,
    'adalah': TokenType.ADALAH,
    'lambda': TokenType.LAMBDA,
    'global': TokenType.GLOBAL,
    'nonlokal': TokenType.NONLOKAL,
    'tegas': TokenType.TEGAS,
    'hapus': TokenType.HAPUS,
    'hasil': TokenType.HASIL,
    'benar': TokenType.BENAR,
    'salah': TokenType.SALAH,
    'kosong': TokenType.KOSONG,
}

# Operator mapping
OPERATORS = {
    '+': TokenType.PLUS,
    '-': TokenType.MINUS,
    '*': TokenType.MULTIPLY,
    '/': TokenType.DIVIDE,
    '//': TokenType.FLOOR_DIVIDE,
    '%': TokenType.MODULO,
    '**': TokenType.POWER,
    '==': TokenType.EQUAL,
    '!=': TokenType.NOT_EQUAL,
    '<': TokenType.LESS_THAN,
    '<=': TokenType.LESS_EQUAL,
    '>': TokenType.GREATER_THAN,
    '>=': TokenType.GREATER_EQUAL,
    '=': TokenType.ASSIGN,
    '+=': TokenType.PLUS_ASSIGN,
    '-=': TokenType.MINUS_ASSIGN,
    '*=': TokenType.MULTIPLY_ASSIGN,
    '/=': TokenType.DIVIDE_ASSIGN,
    '->': TokenType.ARROW,
}

# Delimiter mapping
DELIMITERS = {
    '(': TokenType.LEFT_PAREN,
    ')': TokenType.RIGHT_PAREN,
    '[': TokenType.LEFT_BRACKET,
    ']': TokenType.RIGHT_BRACKET,
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    ',': TokenType.COMMA,
    '.': TokenType.DOT,
    ':': TokenType.COLON,
    ';': TokenType.SEMICOLON,
}
