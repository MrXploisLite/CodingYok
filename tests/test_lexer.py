"""
Unit tests for CodingYok lexer
"""

import pytest
from src.codingyok.lexer import CodingYokLexer
from src.codingyok.tokens import TokenType, Token
from src.codingyok.errors import CodingYokSyntaxError


class TestCodingYokLexer:
    
    def test_simple_tokens(self):
        """Test basic token recognition"""
        source = "tulis(\"Hello\")"
        lexer = CodingYokLexer(source)
        tokens = lexer.tokenize()
        
        expected_types = [
            TokenType.TULIS,
            TokenType.LEFT_PAREN,
            TokenType.STRING,
            TokenType.RIGHT_PAREN,
            TokenType.EOF
        ]
        
        actual_types = [token.type for token in tokens]
        assert actual_types == expected_types
    
    def test_indonesian_keywords(self):
        """Test Indonesian keyword recognition"""
        keywords = {
            'tulis': TokenType.TULIS,
            'jika': TokenType.JIKA,
            'kalau_tidak': TokenType.KALAU_TIDAK,
            'untuk': TokenType.UNTUK,
            'selama': TokenType.SELAMA,
            'fungsi': TokenType.FUNGSI,
            'benar': TokenType.BENAR,
            'salah': TokenType.SALAH,
            'kosong': TokenType.KOSONG,
        }
        
        for keyword, expected_type in keywords.items():
            lexer = CodingYokLexer(keyword)
            tokens = lexer.tokenize()
            assert tokens[0].type == expected_type
    
    def test_numbers(self):
        """Test number tokenization"""
        test_cases = [
            ("123", 123),
            ("45.67", 45.67),
            ("0", 0),
            ("3.14159", 3.14159),
        ]
        
        for source, expected_value in test_cases:
            lexer = CodingYokLexer(source)
            tokens = lexer.tokenize()
            assert tokens[0].type == TokenType.NUMBER
            assert tokens[0].value == expected_value
    
    def test_strings(self):
        """Test string tokenization"""
        test_cases = [
            ('"Hello World"', "Hello World"),
            ("'Single quotes'", "Single quotes"),
            ('"Escape \\n test"', "Escape \n test"),
            ('"Unicode: café"', "Unicode: café"),
        ]
        
        for source, expected_value in test_cases:
            lexer = CodingYokLexer(source)
            tokens = lexer.tokenize()
            assert tokens[0].type == TokenType.STRING
            assert tokens[0].value == expected_value
    
    def test_operators(self):
        """Test operator tokenization"""
        operators = {
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.MULTIPLY,
            '/': TokenType.DIVIDE,
            '==': TokenType.EQUAL,
            '!=': TokenType.NOT_EQUAL,
            '<=': TokenType.LESS_EQUAL,
            '>=': TokenType.GREATER_EQUAL,
            '**': TokenType.POWER,
        }
        
        for op, expected_type in operators.items():
            lexer = CodingYokLexer(op)
            tokens = lexer.tokenize()
            assert tokens[0].type == expected_type
    
    def test_identifiers(self):
        """Test identifier tokenization"""
        test_cases = [
            "variable",
            "nama_panjang",
            "var123",
            "_private",
            "camelCase",
        ]
        
        for identifier in test_cases:
            lexer = CodingYokLexer(identifier)
            tokens = lexer.tokenize()
            assert tokens[0].type == TokenType.IDENTIFIER
            assert tokens[0].value == identifier
    
    def test_comments(self):
        """Test comment handling"""
        source = """
        # This is a comment
        tulis("Hello")  # Another comment
        """
        
        lexer = CodingYokLexer(source)
        tokens = lexer.tokenize()
        
        # Find comment tokens
        comment_tokens = [t for t in tokens if t.type == TokenType.COMMENT]
        assert len(comment_tokens) == 2
        assert "This is a comment" in comment_tokens[0].value
        assert "Another comment" in comment_tokens[1].value
    
    def test_indentation(self):
        """Test indentation handling"""
        source = """
jika benar:
    tulis("Indented")
    jika salah:
        tulis("Double indent")
    tulis("Back to single")
tulis("No indent")
"""
        
        lexer = CodingYokLexer(source)
        tokens = lexer.tokenize()
        
        # Count indent/dedent tokens
        indent_tokens = [t for t in tokens if t.type == TokenType.INDENT]
        dedent_tokens = [t for t in tokens if t.type == TokenType.DEDENT]
        
        assert len(indent_tokens) == 2  # Two levels of indentation
        assert len(dedent_tokens) == 2  # Two dedents back to base level
    
    def test_complex_expression(self):
        """Test complex expression tokenization"""
        source = 'hasil = (a + b) * 2 ** 3 / (c - d)'
        
        lexer = CodingYokLexer(source)
        tokens = lexer.tokenize()
        
        expected_types = [
            TokenType.IDENTIFIER,  # hasil
            TokenType.ASSIGN,      # =
            TokenType.LEFT_PAREN,  # (
            TokenType.IDENTIFIER,  # a
            TokenType.PLUS,        # +
            TokenType.IDENTIFIER,  # b
            TokenType.RIGHT_PAREN, # )
            TokenType.MULTIPLY,    # *
            TokenType.NUMBER,      # 2
            TokenType.POWER,       # **
            TokenType.NUMBER,      # 3
            TokenType.DIVIDE,      # /
            TokenType.LEFT_PAREN,  # (
            TokenType.IDENTIFIER,  # c
            TokenType.MINUS,       # -
            TokenType.IDENTIFIER,  # d
            TokenType.RIGHT_PAREN, # )
            TokenType.EOF
        ]
        
        actual_types = [token.type for token in tokens]
        assert actual_types == expected_types
    
    def test_error_handling(self):
        """Test error handling for invalid characters"""
        with pytest.raises(CodingYokSyntaxError):
            lexer = CodingYokLexer("@invalid_char")
            lexer.tokenize()
    
    def test_unterminated_string(self):
        """Test error for unterminated string"""
        with pytest.raises(CodingYokSyntaxError):
            lexer = CodingYokLexer('"Unterminated string')
            lexer.tokenize()
    
    def test_line_column_tracking(self):
        """Test line and column number tracking"""
        source = """tulis("Line 1")
tulis("Line 2")"""
        
        lexer = CodingYokLexer(source)
        tokens = lexer.tokenize()
        
        # First tulis should be at line 1, column 1
        assert tokens[0].line == 1
        assert tokens[0].column == 1
        
        # Find second tulis token (after newline)
        second_tulis = None
        for token in tokens:
            if token.type == TokenType.TULIS and token.line == 2:
                second_tulis = token
                break
        
        assert second_tulis is not None
        assert second_tulis.line == 2
        assert second_tulis.column == 1
