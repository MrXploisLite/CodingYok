"""
Parser for CodingYok language
Converts tokens into Abstract Syntax Tree (AST)
"""

from typing import List, Optional
from .tokens import Token, TokenType
from .ast_nodes import *
from .errors import CodingYokSyntaxError


class CodingYokParser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def error(self, message: str) -> None:
        """Raise syntax error at current token"""
        token = self.peek()
        raise CodingYokSyntaxError(message, token.line, token.column)

    def peek(self, offset: int = 0) -> Token:
        """Look at token at current position + offset"""
        pos = self.current + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]  # Return EOF token
        return self.tokens[pos]

    def advance(self) -> Token:
        """Move to next token and return current"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def previous(self) -> Token:
        """Return previous token"""
        return self.tokens[self.current - 1]

    def is_at_end(self) -> bool:
        """Check if we're at end of tokens"""
        return self.peek().type == TokenType.EOF

    def check(self, token_type: TokenType) -> bool:
        """Check if current token is of given type"""
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def match(self, *types: TokenType) -> bool:
        """Check if current token matches any of the given types"""
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def consume(self, token_type: TokenType, message: str) -> Token:
        """Consume token of expected type or raise error"""
        if self.check(token_type):
            return self.advance()

        current_token = self.peek()
        self.error(f"{message}. Ditemukan: {current_token.type.name}")
        # This line should never be reached due to error() raising an exception
        raise RuntimeError("Unreachable code")

    def skip_newlines(self) -> None:
        """Skip newline tokens"""
        while self.match(TokenType.NEWLINE):
            pass

    def parse(self) -> Program:
        """Parse tokens into AST"""
        statements = []

        self.skip_newlines()

        while not self.is_at_end():
            if self.check(TokenType.NEWLINE):
                self.advance()
                continue

            stmt = self.statement()
            if stmt:
                statements.append(stmt)

            self.skip_newlines()

        return Program(statements)

    def statement(self) -> Optional[Statement]:
        """Parse a statement"""
        try:
            # Skip comments
            if self.match(TokenType.COMMENT):
                return None

            # Skip indentation tokens at statement level
            if self.match(TokenType.INDENT, TokenType.DEDENT):
                return None

            # Function definition
            if self.match(TokenType.FUNGSI):
                return self.function_definition()

            # Class definition
            if self.match(TokenType.KELAS):
                return self.class_definition()

            # Control flow
            if self.match(TokenType.JIKA):
                return self.if_statement()

            if self.match(TokenType.SELAMA):
                return self.while_statement()

            if self.match(TokenType.UNTUK):
                return self.for_statement()

            # Jump statements
            if self.match(TokenType.KEMBALIKAN):
                return self.return_statement()

            if self.match(TokenType.HASILKAN):
                return self.yield_statement()

            if self.match(TokenType.BERHENTI):
                return BreakStatement()

            if self.match(TokenType.LANJUT):
                return ContinueStatement()

            if self.match(TokenType.LEWATI):
                return PassStatement()

            # Pattern matching
            if self.match(TokenType.COCOKKAN):
                return self.match_statement()

            # Exception handling
            if self.match(TokenType.COBA):
                return self.try_statement()

            if self.match(TokenType.LEMPAR):
                return self.raise_statement()

            # Context manager
            if self.match(TokenType.DENGAN):
                return self.with_statement()

            # Import statements
            if self.match(TokenType.IMPOR):
                return self.import_statement()

            if self.match(TokenType.DARI):
                return self.from_import_statement()

            # Print statement
            if self.match(TokenType.TULIS):
                return self.print_statement()

            # Expression statement or assignment
            return self.expression_statement()

        except CodingYokSyntaxError:
            # Synchronize on error
            self.synchronize()
            raise

    def synchronize(self) -> None:
        """Recover from parse error by finding next statement"""
        self.advance()

        while not self.is_at_end():
            if self.previous().type == TokenType.NEWLINE:
                return

            if self.peek().type in [
                TokenType.KELAS,
                TokenType.FUNGSI,
                TokenType.JIKA,
                TokenType.UNTUK,
                TokenType.SELAMA,
                TokenType.TULIS,
                TokenType.KEMBALIKAN,
            ]:
                return

            self.advance()

    def print_statement(self) -> PrintStatement:
        """Parse tulis statement"""
        expressions = []

        self.consume(TokenType.LEFT_PAREN, "Diharapkan '(' setelah 'tulis'")

        if not self.check(TokenType.RIGHT_PAREN):
            expressions.append(self.expression())

            while self.match(TokenType.COMMA):
                expressions.append(self.expression())

        self.consume(TokenType.RIGHT_PAREN, "Diharapkan ')' setelah argumen tulis")

        return PrintStatement(expressions)

    def expression_statement(self) -> Statement:
        """Parse expression statement or assignment"""
        expr = self.expression()

        # Check for tuple unpacking (a, b = 1, 2)
        if isinstance(expr, IdentifierExpression) and self.check(TokenType.COMMA):
            # Could be tuple unpacking
            targets = [expr.name]
            while self.match(TokenType.COMMA):
                if self.check(TokenType.IDENTIFIER):
                    targets.append(self.advance().value)
                else:
                    break

            if self.match(TokenType.ASSIGN):
                value = self.expression()
                return TupleUnpackingStatement(targets, value)
            else:
                # Not an assignment, revert - this shouldn't happen normally
                self.error("Diharapkan '=' setelah tuple unpacking")

        # Check for assignment (including compound assignments)
        if self.match(
            TokenType.ASSIGN,
            TokenType.PLUS_ASSIGN,
            TokenType.MINUS_ASSIGN,
            TokenType.MULTIPLY_ASSIGN,
            TokenType.DIVIDE_ASSIGN,
        ):
            operator = self.previous().value

            if isinstance(expr, IdentifierExpression):
                value = self.expression()

                # Handle compound assignment by converting to regular assignment
                if operator != "=":
                    # Convert += to = var + value, etc.
                    op_map = {"+=": "+", "-=": "-", "*=": "*", "/=": "/"}
                    binary_op = op_map[operator]
                    value = BinaryExpression(expr, binary_op, value)

                return AssignmentStatement(expr.name, value)
            elif isinstance(expr, AttributeExpression):
                # Handle attribute assignment (e.g., diri.nama = value)
                value = self.expression()

                # Handle compound assignment for attributes
                if operator != "=":
                    op_map = {"+=": "+", "-=": "-", "*=": "*", "/=": "/"}
                    binary_op = op_map[operator]
                    value = BinaryExpression(expr, binary_op, value)

                return AttributeAssignmentStatement(expr, value)
            elif isinstance(expr, IndexExpression):
                # Handle index assignment (e.g., arr[0] = value, dict["key"] = value)
                value = self.expression()

                # Handle compound assignment for index
                if operator != "=":
                    op_map = {"+=": "+", "-=": "-", "*=": "*", "/=": "/"}
                    binary_op = op_map[operator]
                    value = BinaryExpression(expr, binary_op, value)

                return IndexAssignmentStatement(expr, value)
            elif isinstance(expr, SliceExpression):
                # Handle slice assignment (e.g., arr[1:3] = [10, 20])
                value = self.expression()
                return SliceAssignmentStatement(expr, value)
            else:
                self.error("Target assignment tidak valid")

        return ExpressionStatement(expr)

    def expression(self) -> Expression:
        """Parse expression"""
        return self.logical_or()

    def logical_or(self) -> Expression:
        """Parse logical OR expression"""
        expr = self.logical_and()

        while self.match(TokenType.ATAU):
            operator = self.previous().value
            right = self.logical_and()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def logical_and(self) -> Expression:
        """Parse logical AND expression"""
        expr = self.equality()

        while self.match(TokenType.DAN):
            operator = self.previous().value
            right = self.equality()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def equality(self) -> Expression:
        """Parse equality expression"""
        expr = self.comparison()

        while self.match(TokenType.EQUAL, TokenType.NOT_EQUAL):
            operator = self.previous().value
            right = self.comparison()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def comparison(self) -> Expression:
        """Parse comparison expression"""
        expr = self.term()

        while self.match(
            TokenType.GREATER_THAN,
            TokenType.GREATER_EQUAL,
            TokenType.LESS_THAN,
            TokenType.LESS_EQUAL,
            TokenType.DALAM,
        ):
            operator = self.previous().value
            right = self.term()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def term(self) -> Expression:
        """Parse addition/subtraction"""
        expr = self.factor()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous().value
            right = self.factor()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def factor(self) -> Expression:
        """Parse multiplication/division"""
        expr = self.unary()

        while self.match(
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
            TokenType.FLOOR_DIVIDE,
            TokenType.MODULO,
        ):
            operator = self.previous().value
            right = self.unary()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def unary(self) -> Expression:
        """Parse unary expression"""
        if self.match(TokenType.BUKAN, TokenType.MINUS):
            operator = self.previous().value
            right = self.unary()
            return UnaryExpression(operator, right)

        return self.power()

    def power(self) -> Expression:
        """Parse power expression"""
        expr = self.call()

        if self.match(TokenType.POWER):
            operator = self.previous().value
            right = self.unary()  # Right associative
            expr = BinaryExpression(expr, operator, right)

        return expr

    def call(self) -> Expression:
        """Parse function call or attribute access"""
        expr = self.primary()

        while True:
            if self.match(TokenType.LEFT_PAREN):
                expr = self.finish_call(expr)
            elif self.match(TokenType.DOT):
                name = self.consume(
                    TokenType.IDENTIFIER, "Diharapkan nama atribut setelah '.'"
                )
                expr = AttributeExpression(expr, name.value)
            elif self.match(TokenType.LEFT_BRACKET):
                # Check for slice or index
                expr = self.parse_index_or_slice(expr)
            else:
                break

        return expr

    def parse_index_or_slice(self, obj: Expression) -> Expression:
        """Parse index access or slice expression"""
        start = None
        stop = None
        step = None

        # Parse start (optional)
        is_colon = self.check(TokenType.COLON)
        is_bracket = self.check(TokenType.RIGHT_BRACKET)
        if not is_colon and not is_bracket:
            start = self.expression()

        # Check for slice
        if self.match(TokenType.COLON):
            # Parse stop (optional)
            is_colon = self.check(TokenType.COLON)
            is_bracket = self.check(TokenType.RIGHT_BRACKET)
            if not is_colon and not is_bracket:
                stop = self.expression()

            # Parse step (optional)
            if self.match(TokenType.COLON):
                if not self.check(TokenType.RIGHT_BRACKET):
                    step = self.expression()

            self.consume(TokenType.RIGHT_BRACKET, "Diharapkan ']' setelah slice")
            return SliceExpression(obj, start, stop, step)
        else:
            self.consume(TokenType.RIGHT_BRACKET, "Diharapkan ']' setelah indeks")
            return IndexExpression(obj, start)

    def finish_call(self, callee: Expression) -> CallExpression:
        """Parse function call arguments"""
        arguments = []

        if not self.check(TokenType.RIGHT_PAREN):
            arguments.append(self.expression())

            while self.match(TokenType.COMMA):
                arguments.append(self.expression())

        self.consume(TokenType.RIGHT_PAREN, "Diharapkan ')' setelah argumen")

        return CallExpression(callee, arguments)

    def primary(self) -> Expression:
        """Parse primary expression"""
        if self.match(TokenType.LAMBDA):
            return self.lambda_expression()

        if self.match(TokenType.BENAR, TokenType.SALAH, TokenType.KOSONG):
            return LiteralExpression(self.previous().value)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return LiteralExpression(self.previous().value)

        if self.match(TokenType.F_STRING_START):
            return self.parse_fstring(self.previous().value)

        if self.match(TokenType.IDENTIFIER, TokenType.DIRI):
            return IdentifierExpression(self.previous().value)

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Diharapkan ')' setelah ekspresi")
            return expr

        if self.match(TokenType.LEFT_BRACKET):
            return self.list_expression()

        if self.match(TokenType.LEFT_BRACE):
            return self.dict_expression()

        self.error("Diharapkan ekspresi")
        # This line should never be reached due to error() raising an exception
        raise RuntimeError("Unreachable code")

    def list_expression(self) -> Expression:
        """Parse list literal or list comprehension"""
        # Skip newlines after opening bracket
        self.skip_newlines()

        if self.check(TokenType.RIGHT_BRACKET):
            self.consume(TokenType.RIGHT_BRACKET, "Diharapkan ']'")
            return ListExpression([])

        first_element = self.expression()

        if self.match(TokenType.UNTUK):
            variable = self.consume(
                TokenType.IDENTIFIER, "Diharapkan nama variabel"
            ).value
            self.consume(TokenType.DALAM, "Diharapkan 'dalam' dalam comprehension")
            iterable = self.expression()

            condition = None
            if self.match(TokenType.JIKA):
                condition = self.expression()

            self.skip_newlines()
            self.consume(
                TokenType.RIGHT_BRACKET, "Diharapkan ']' setelah comprehension"
            )
            return ListComprehension(first_element, variable, iterable, condition)

        elements = [first_element]
        while self.match(TokenType.COMMA):
            self.skip_newlines()
            if self.check(TokenType.RIGHT_BRACKET):
                break
            elements.append(self.expression())

        self.skip_newlines()
        self.consume(TokenType.RIGHT_BRACKET, "Diharapkan ']' setelah elemen list")

        return ListExpression(elements)

    def dict_expression(self) -> Expression:
        """Parse dictionary literal, dict comprehension, or set"""
        self.skip_newlines()

        if self.check(TokenType.RIGHT_BRACE):
            self.consume(TokenType.RIGHT_BRACE, "Diharapkan '}'")
            return DictExpression([])

        first_key = self.expression()

        if self.match(TokenType.COLON):
            value = self.expression()

            if self.match(TokenType.UNTUK):
                variable = self.consume(
                    TokenType.IDENTIFIER, "Diharapkan nama variabel"
                ).value
                self.consume(TokenType.DALAM, "Diharapkan 'dalam' dalam comprehension")
                iterable = self.expression()

                condition = None
                if self.match(TokenType.JIKA):
                    condition = self.expression()

                self.skip_newlines()
                self.consume(
                    TokenType.RIGHT_BRACE, "Diharapkan '}' setelah dict comprehension"
                )
                return DictComprehension(
                    first_key, value, variable, iterable, condition
                )

            pairs = [(first_key, value)]
            while self.match(TokenType.COMMA):
                self.skip_newlines()
                if self.check(TokenType.RIGHT_BRACE):
                    break
                key = self.expression()
                self.consume(TokenType.COLON, "Diharapkan ':' setelah kunci dictionary")
                val = self.expression()
                pairs.append((key, val))

            self.skip_newlines()
            self.consume(TokenType.RIGHT_BRACE, "Diharapkan '}' setelah dictionary")
            return DictExpression(pairs)

        if self.match(TokenType.UNTUK):
            variable = self.consume(
                TokenType.IDENTIFIER, "Diharapkan nama variabel"
            ).value
            self.consume(TokenType.DALAM, "Diharapkan 'dalam' dalam comprehension")
            iterable = self.expression()

            condition = None
            if self.match(TokenType.JIKA):
                condition = self.expression()

            self.skip_newlines()
            self.consume(
                TokenType.RIGHT_BRACE, "Diharapkan '}' setelah set comprehension"
            )
            return SetComprehension(first_key, variable, iterable, condition)

        elements = [first_key]
        while self.match(TokenType.COMMA):
            self.skip_newlines()
            if self.check(TokenType.RIGHT_BRACE):
                break
            elements.append(self.expression())

        self.skip_newlines()
        self.consume(TokenType.RIGHT_BRACE, "Diharapkan '}' setelah set")
        return SetExpression(elements)

    def parse_fstring(self, parts: List[str]) -> FStringExpression:
        """Parse f-string parts into expressions"""
        from typing import Union

        parsed_parts: List[Union[str, Expression]] = []

        for part in parts:
            if part.startswith("{EXPR:") and part.endswith("}"):
                # Extract expression text
                expr_text = part[6:-1]  # Remove {EXPR: and }

                # Create a mini-parser for the expression
                from .lexer import CodingYokLexer

                expr_lexer = CodingYokLexer(expr_text)
                expr_tokens = expr_lexer.tokenize()

                # Create a mini-parser for the expression
                expr_parser = CodingYokParser(expr_tokens)
                expr = expr_parser.expression()
                parsed_parts.append(expr)
            else:
                # Regular string part
                parsed_parts.append(part)

        return FStringExpression(parsed_parts)

    def function_definition(self) -> FunctionDefinition:
        """Parse function definition"""
        name = self.consume(TokenType.IDENTIFIER, "Diharapkan nama fungsi").value

        self.consume(TokenType.LEFT_PAREN, "Diharapkan '(' setelah nama fungsi")

        parameters: List[str] = []
        defaults: List[Optional[Expression]] = []

        if not self.check(TokenType.RIGHT_PAREN):
            # Parse parameters (allow 'diri' as special case)
            if self.check(TokenType.DIRI):
                param = self.advance().value
            else:
                param = self.consume(
                    TokenType.IDENTIFIER, "Diharapkan nama parameter"
                ).value
            parameters.append(param)

            # Check for default value
            if self.match(TokenType.ASSIGN):
                defaults.append(self.expression())
            else:
                defaults.append(None)

            while self.match(TokenType.COMMA):
                if self.check(TokenType.DIRI):
                    param = self.advance().value
                else:
                    param = self.consume(
                        TokenType.IDENTIFIER, "Diharapkan nama parameter"
                    ).value
                parameters.append(param)

                if self.match(TokenType.ASSIGN):
                    defaults.append(self.expression())
                else:
                    defaults.append(None)

        self.consume(TokenType.RIGHT_PAREN, "Diharapkan ')' setelah parameter")
        self.consume(TokenType.COLON, "Diharapkan ':' setelah definisi fungsi")

        body = self.block()

        return FunctionDefinition(name, parameters, body, defaults)

    def class_definition(self) -> ClassDefinition:
        """Parse class definition"""
        name = self.consume(TokenType.IDENTIFIER, "Diharapkan nama kelas").value

        superclass = None
        if self.match(TokenType.LEFT_PAREN):
            superclass = self.consume(
                TokenType.IDENTIFIER, "Diharapkan nama superclass"
            ).value
            self.consume(TokenType.RIGHT_PAREN, "Diharapkan ')' setelah superclass")

        self.consume(TokenType.COLON, "Diharapkan ':' setelah definisi kelas")

        methods = []

        # Skip newlines before indent
        self.skip_newlines()
        self.consume(TokenType.INDENT, "Diharapkan indentasi setelah definisi kelas")

        while not self.check(TokenType.DEDENT) and not self.is_at_end():
            if self.check(TokenType.NEWLINE):
                self.advance()
                continue

            if self.match(TokenType.FUNGSI):
                methods.append(self.function_definition())
            else:
                self.error("Hanya definisi fungsi yang diperbolehkan dalam kelas")

            self.skip_newlines()

        self.consume(TokenType.DEDENT, "Diharapkan dedent setelah blok kelas")

        return ClassDefinition(name, superclass, methods)

    def if_statement(self) -> IfStatement:
        """Parse if statement"""
        condition = self.expression()
        self.consume(TokenType.COLON, "Diharapkan ':' setelah kondisi jika")

        then_branch = self.block()

        elif_branches = []
        while self.match(TokenType.KALAU_TIDAK_JIKA):
            elif_condition = self.expression()
            self.consume(
                TokenType.COLON, "Diharapkan ':' setelah kondisi kalau_tidak_jika"
            )
            elif_body = self.block()
            elif_branches.append((elif_condition, elif_body))

        else_branch = None
        if self.match(TokenType.KALAU_TIDAK):
            self.consume(TokenType.COLON, "Diharapkan ':' setelah kalau_tidak")
            else_branch = self.block()

        return IfStatement(condition, then_branch, elif_branches, else_branch)

    def while_statement(self) -> WhileStatement:
        """Parse while statement"""
        condition = self.expression()
        self.consume(TokenType.COLON, "Diharapkan ':' setelah kondisi selama")

        body = self.block()

        return WhileStatement(condition, body)

    def for_statement(self) -> ForStatement:
        """Parse for statement"""
        # Check for tuple unpacking (untuk a, b dalam items)
        variable = self.consume(TokenType.IDENTIFIER, "Diharapkan nama variabel").value

        if self.match(TokenType.COMMA):
            # Tuple unpacking in for loop
            variables = [variable]
            variables.append(
                self.consume(TokenType.IDENTIFIER, "Diharapkan nama variabel").value
            )
            while self.match(TokenType.COMMA):
                variables.append(
                    self.consume(
                        TokenType.IDENTIFIER, "Diharapkan nama variabel"
                    ).value
                )
            variable = variables

        self.consume(TokenType.DALAM, "Diharapkan 'dalam' setelah variabel untuk")

        iterable = self.expression()
        self.consume(TokenType.COLON, "Diharapkan ':' setelah iterable")

        body = self.block()

        return ForStatement(variable, iterable, body)

    def return_statement(self) -> ReturnStatement:
        """Parse return statement"""
        value = None

        if not self.check(TokenType.NEWLINE) and not self.is_at_end():
            value = self.expression()

        return ReturnStatement(value)

    def yield_statement(self) -> YieldStatement:
        """Parse yield statement (for generators)"""
        value = None

        if not self.check(TokenType.NEWLINE) and not self.is_at_end():
            value = self.expression()

        return YieldStatement(value)

    def match_statement(self) -> MatchStatement:
        """Parse match statement (pattern matching)"""
        value = self.expression()
        self.consume(TokenType.COLON, "Diharapkan ':' setelah ekspresi cocokkan")

        cases = []

        self.skip_newlines()
        self.consume(TokenType.INDENT, "Diharapkan indentasi setelah cocokkan")

        while not self.check(TokenType.DEDENT) and not self.is_at_end():
            if self.check(TokenType.NEWLINE):
                self.advance()
                continue

            if self.match(TokenType.KASUS):
                pattern = self.expression()

                guard = None
                if self.match(TokenType.JIKA):
                    guard = self.expression()

                self.consume(TokenType.COLON, "Diharapkan ':' setelah pola kasus")
                body = self.block()

                cases.append(MatchCase(pattern, guard, body))
            else:
                self.error("Diharapkan 'kasus' dalam blok cocokkan")

            self.skip_newlines()

        self.consume(TokenType.DEDENT, "Diharapkan dedent setelah blok cocokkan")

        return MatchStatement(value, cases)

    def import_statement(self) -> ImportStatement:
        """Parse import statement"""
        module_name = self.consume(TokenType.IDENTIFIER, "Diharapkan nama modul").value

        alias = None
        if self.match(TokenType.SEBAGAI):
            alias = self.consume(
                TokenType.IDENTIFIER, "Diharapkan alias setelah 'sebagai'"
            ).value

        return ImportStatement(module_name, alias)

    def from_import_statement(self) -> FromImportStatement:
        """Parse from import statement"""
        module_name = self.consume(TokenType.IDENTIFIER, "Diharapkan nama modul").value
        self.consume(TokenType.IMPOR, "Diharapkan 'impor' setelah nama modul")

        names = []
        aliases = []

        names.append(
            self.consume(TokenType.IDENTIFIER, "Diharapkan nama untuk diimpor").value
        )

        if self.match(TokenType.SEBAGAI):
            aliases.append(self.consume(TokenType.IDENTIFIER, "Diharapkan alias").value)
        else:
            aliases.append(None)

        while self.match(TokenType.COMMA):
            names.append(
                self.consume(
                    TokenType.IDENTIFIER, "Diharapkan nama untuk diimpor"
                ).value
            )

            if self.match(TokenType.SEBAGAI):
                aliases.append(
                    self.consume(TokenType.IDENTIFIER, "Diharapkan alias").value
                )
            else:
                aliases.append(None)

        return FromImportStatement(module_name, names, aliases)

    def block(self) -> List[Statement]:
        """Parse indented block of statements"""
        statements = []

        self.skip_newlines()
        self.consume(TokenType.INDENT, "Diharapkan indentasi")

        while not self.check(TokenType.DEDENT) and not self.is_at_end():
            if self.check(TokenType.NEWLINE):
                self.advance()
                continue

            stmt = self.statement()
            if stmt:
                statements.append(stmt)

            self.skip_newlines()

        self.consume(TokenType.DEDENT, "Diharapkan dedent setelah blok")

        return statements

    def try_statement(self) -> TryStatement:
        """Parse try statement"""
        self.consume(TokenType.COLON, "Diharapkan ':' setelah 'coba'")
        try_block = self.block()

        except_clauses = []
        while self.match(TokenType.KECUALI):
            exception_type = None
            exception_name = None

            # Optional exception type
            if self.check(TokenType.IDENTIFIER):
                exception_type = self.advance().value

                # Optional 'sebagai' name
                if self.match(TokenType.SEBAGAI):
                    exception_name = self.consume(
                        TokenType.IDENTIFIER, "Diharapkan nama exception"
                    ).value

            self.consume(TokenType.COLON, "Diharapkan ':' setelah kecuali")
            except_body = self.block()

            except_clauses.append(
                ExceptClause(exception_type, exception_name, except_body)
            )

        finally_block = None
        if self.match(TokenType.AKHIRNYA):
            self.consume(TokenType.COLON, "Diharapkan ':' setelah 'akhirnya'")
            finally_block = self.block()

        return TryStatement(try_block, except_clauses, finally_block)

    def raise_statement(self) -> RaiseStatement:
        """Parse raise statement"""
        exception = None

        if not self.check(TokenType.NEWLINE) and not self.is_at_end():
            exception = self.expression()

        return RaiseStatement(exception)

    def with_statement(self) -> WithStatement:
        """Parse with statement"""
        context_expr = self.expression()

        target = None
        if self.match(TokenType.SEBAGAI):
            target = self.consume(
                TokenType.IDENTIFIER, "Diharapkan nama variabel setelah 'sebagai'"
            ).value

        self.consume(TokenType.COLON, "Diharapkan ':' setelah ekspresi dengan")
        body = self.block()

        return WithStatement(context_expr, target, body)

    def lambda_expression(self) -> LambdaExpression:
        """Parse lambda expression"""
        parameters = []

        if not self.check(TokenType.COLON):
            parameters.append(
                self.consume(TokenType.IDENTIFIER, "Diharapkan nama parameter").value
            )

            while self.match(TokenType.COMMA):
                parameters.append(
                    self.consume(
                        TokenType.IDENTIFIER, "Diharapkan nama parameter"
                    ).value
                )

        self.consume(TokenType.COLON, "Diharapkan ':' setelah parameter lambda")
        body = self.expression()

        return LambdaExpression(parameters, body)
