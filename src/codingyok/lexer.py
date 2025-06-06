"""
Lexer for CodingYok language
Converts source code into tokens
"""

import re
from typing import List, Optional, Iterator, Union, Any
from .tokens import Token, TokenType, INDONESIAN_KEYWORDS, OPERATORS, DELIMITERS
from .errors import CodingYokSyntaxError


class CodingYokLexer:
    def __init__(self, source_code: str):
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        self.indent_stack = [0]  # Stack to track indentation levels
        self.bracket_depth = 0  # Track nested brackets/braces/parens

    def error(self, message: str) -> None:
        """Raise a syntax error with current position"""
        raise CodingYokSyntaxError(f"Baris {self.line}, Kolom {self.column}: {message}")

    def peek(self, offset: int = 0) -> Optional[str]:
        """Peek at character at current position + offset"""
        pos = self.position + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]

    def advance(self) -> Optional[str]:
        """Move to next character and return current"""
        if self.position >= len(self.source):
            return None

        char = self.source[self.position]
        self.position += 1

        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return char

    def skip_whitespace(self) -> None:
        """Skip whitespace characters except newlines"""
        char = self.peek()
        while char and char in " \t\r":
            self.advance()
            char = self.peek()

    def read_string(self, quote_char: str) -> str:
        """Read string literal"""
        value = ""
        self.advance()  # Skip opening quote

        while True:
            char = self.peek()
            if char is None:
                self.error(f"String tidak ditutup dengan {quote_char}")

            if char == quote_char:
                self.advance()  # Skip closing quote
                break

            if char == "\\":
                self.advance()  # Skip backslash
                escaped = self.advance()
                if escaped is None:
                    self.error("Karakter escape tidak valid")

                # Handle escape sequences
                escape_map = {
                    "n": "\n",
                    "t": "\t",
                    "r": "\r",
                    "\\": "\\",
                    "'": "'",
                    '"': '"',
                }
                if escaped is not None:
                    value += escape_map.get(escaped, escaped)
            else:
                if char is not None:
                    value += char
                self.advance()

        return value

    def read_number(self) -> Union[float, int]:
        """Read numeric literal"""
        value = ""
        has_dot = False

        char = self.peek()
        while char and (char.isdigit() or char == "."):
            if char == ".":
                if has_dot:
                    break  # Second dot, stop here
                has_dot = True
            value += char
            self.advance()
            char = self.peek()

        try:
            return float(value) if has_dot else int(value)
        except ValueError:
            self.error(f"Angka tidak valid: {value}")
            # This line should never be reached due to error() raising an exception
            raise RuntimeError("Unreachable code")

    def read_identifier(self) -> str:
        """Read identifier or keyword"""
        value = ""

        char = self.peek()
        while char and (char.isalnum() or char in "_"):
            char = self.advance()
            if char is not None:
                value += char
            char = self.peek()

        return value

    def read_comment(self) -> str:
        """Read comment until end of line"""
        comment = ""
        self.advance()  # Skip #

        char = self.peek()
        while char and char != "\n":
            char = self.advance()
            if char is not None:
                comment += char
            char = self.peek()

        return comment.strip()

    def read_fstring(self, quote_char: str) -> None:
        """Read f-string literal with basic interpolation support"""
        start_column = self.column
        self.advance()  # Skip quote

        parts = []
        current_text = ""

        while True:
            char = self.peek()
            if char is None:
                self.error(f"F-string tidak ditutup dengan {quote_char}")

            if char == quote_char:
                self.advance()  # Skip closing quote
                if current_text:
                    parts.append(current_text)
                break

            if char == "{":
                # Found interpolation start
                if current_text:
                    parts.append(current_text)
                    current_text = ""

                self.advance()  # Skip {
                expr_text = ""
                brace_count = 1

                # Read until matching }
                while brace_count > 0:
                    char = self.peek()
                    if char is None:
                        self.error("F-string expression tidak ditutup dengan '}'")

                    if char == "{":
                        brace_count += 1
                    elif char == "}":
                        brace_count -= 1

                    if brace_count > 0 and char is not None:
                        expr_text += char

                    self.advance()

                # Store expression text for later parsing
                parts.append(f"{{EXPR:{expr_text}}}")

            elif char == "\\":
                self.advance()  # Skip backslash
                escaped = self.advance()
                if escaped is not None:
                    escape_map = {
                        "n": "\n",
                        "t": "\t",
                        "r": "\r",
                        "\\": "\\",
                        "'": "'",
                        '"': '"',
                    }
                    current_text += escape_map.get(escaped, escaped)
            else:
                if char is not None:
                    current_text += char
                self.advance()

        # Create a special f-string token with the parts
        self.tokens.append(
            Token(TokenType.F_STRING_START, parts, self.line, start_column)
        )

    def read_raw_string(self, quote_char: str) -> None:
        """Read raw string literal (no escape sequences processed)"""
        start_column = self.column
        self.advance()  # Skip quote

        value = ""
        while True:
            char = self.peek()
            if char is None:
                self.error(f"Raw string tidak ditutup dengan {quote_char}")

            if char == quote_char:
                self.advance()  # Skip closing quote
                break

            # In raw strings, backslashes are literal
            if char is not None:
                value += char
            self.advance()

        self.tokens.append(Token(TokenType.STRING, value, self.line, start_column))

    def handle_indentation(self, line_start_pos: int) -> List[Token]:
        """Handle indentation at start of line"""
        indent_tokens = []
        indent_level = 0

        # Count spaces and tabs
        pos = line_start_pos
        while pos < len(self.source) and self.source[pos] in " \t":
            if self.source[pos] == " ":
                indent_level += 1
            else:  # tab
                indent_level += 8  # Treat tab as 8 spaces
            pos += 1

        current_indent = self.indent_stack[-1]

        if indent_level > current_indent:
            # Increased indentation
            self.indent_stack.append(indent_level)
            indent_tokens.append(Token(TokenType.INDENT, indent_level, self.line, 1))
        elif indent_level < current_indent:
            # Decreased indentation
            while self.indent_stack and self.indent_stack[-1] > indent_level:
                self.indent_stack.pop()
                indent_tokens.append(
                    Token(TokenType.DEDENT, indent_level, self.line, 1)
                )

            if not self.indent_stack or self.indent_stack[-1] != indent_level:
                self.error("Indentasi tidak konsisten")

        return indent_tokens

    def tokenize(self) -> List[Token]:
        """Main tokenization method"""
        self.tokens = []
        line_start = True

        while self.position < len(self.source):
            # Handle indentation at start of line
            if line_start:
                line_start_pos = self.position
                self.skip_whitespace()

                # If line is not empty or comment-only
                char = self.peek()
                if char and char not in "\n#":
                    # Only handle indentation when not inside expressions
                    if self.bracket_depth == 0:
                        indent_tokens = self.handle_indentation(line_start_pos)
                        self.tokens.extend(indent_tokens)

                line_start = False

            char = self.peek()

            if char is None:
                break

            # Skip whitespace
            if char in " \t\r":
                self.skip_whitespace()
                continue

            # Newline
            if char == "\n":
                self.tokens.append(
                    Token(TokenType.NEWLINE, "\n", self.line, self.column)
                )
                self.advance()
                line_start = True
                continue

            # Comments
            if char == "#":
                comment = self.read_comment()
                self.tokens.append(
                    Token(TokenType.COMMENT, comment, self.line, self.column)
                )
                continue

            # String literals (including f-strings)
            if char in "\"'":
                start_column = self.column
                string_value = self.read_string(char)
                self.tokens.append(
                    Token(TokenType.STRING, string_value, self.line, start_column)
                )
                continue

            # Numbers
            if char.isdigit():
                start_column = self.column
                number_value = self.read_number()
                self.tokens.append(
                    Token(TokenType.NUMBER, number_value, self.line, start_column)
                )
                continue

            # Identifiers and keywords (including f-strings)
            if char.isalpha() or char == "_":
                start_column = self.column
                identifier = self.read_identifier()

                # Check for f-string or raw string
                next_char = self.peek()
                if identifier == "f" and next_char and next_char in "\"'":
                    self.read_fstring(next_char)
                    continue
                elif identifier == "r" and next_char and next_char in "\"'":
                    self.read_raw_string(next_char)
                    continue

                token_type = INDONESIAN_KEYWORDS.get(identifier, TokenType.IDENTIFIER)

                # Convert boolean and None values
                value: Any
                if token_type == TokenType.BENAR:
                    value = True
                elif token_type == TokenType.SALAH:
                    value = False
                elif token_type == TokenType.KOSONG:
                    value = None
                else:
                    value = identifier

                self.tokens.append(Token(token_type, value, self.line, start_column))
                continue

            # Multi-character operators
            two_char = char + (self.peek(1) or "")
            if two_char in OPERATORS:
                self.tokens.append(
                    Token(OPERATORS[two_char], two_char, self.line, self.column)
                )
                self.advance()
                self.advance()
                continue

            # Single-character operators and delimiters
            if char in OPERATORS:
                self.tokens.append(Token(OPERATORS[char], char, self.line, self.column))
                self.advance()
                continue

            if char in DELIMITERS:
                # Track bracket depth for indentation handling
                if char in "([{":
                    self.bracket_depth += 1
                elif char in ")]}":
                    self.bracket_depth = max(0, self.bracket_depth - 1)

                self.tokens.append(
                    Token(DELIMITERS[char], char, self.line, self.column)
                )
                self.advance()
                continue

            # Unknown character
            self.error(f"Karakter tidak dikenal: '{char}'")

        # Add final DEDENT tokens if needed
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            self.tokens.append(Token(TokenType.DEDENT, 0, self.line, self.column))

        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))

        return self.tokens
