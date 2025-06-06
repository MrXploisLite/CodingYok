"""
Abstract Syntax Tree (AST) node definitions for CodingYok
"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union
from dataclasses import dataclass


class ASTNode(ABC):
    """Base class for all AST nodes"""
    
    def __init__(self, line: int = 0, column: int = 0):
        self.line = line
        self.column = column
    
    @abstractmethod
    def accept(self, visitor):
        """Accept a visitor (Visitor pattern)"""
        pass


# Expressions
class Expression(ASTNode):
    """Base class for all expressions"""
    pass


@dataclass
class LiteralExpression(Expression):
    """Literal values (numbers, strings, booleans, None)"""
    value: Any
    
    def accept(self, visitor):
        return visitor.visit_literal(self)


@dataclass
class IdentifierExpression(Expression):
    """Variable or function names"""
    name: str
    
    def accept(self, visitor):
        return visitor.visit_identifier(self)


@dataclass
class BinaryExpression(Expression):
    """Binary operations (a + b, a == b, etc.)"""
    left: Expression
    operator: str
    right: Expression
    
    def accept(self, visitor):
        return visitor.visit_binary(self)


@dataclass
class UnaryExpression(Expression):
    """Unary operations (-a, bukan a, etc.)"""
    operator: str
    operand: Expression
    
    def accept(self, visitor):
        return visitor.visit_unary(self)


@dataclass
class CallExpression(Expression):
    """Function calls"""
    callee: Expression
    arguments: List[Expression]
    
    def accept(self, visitor):
        return visitor.visit_call(self)


@dataclass
class AttributeExpression(Expression):
    """Attribute access (obj.attr)"""
    object: Expression
    attribute: str
    
    def accept(self, visitor):
        return visitor.visit_attribute(self)


@dataclass
class IndexExpression(Expression):
    """Index access (arr[0], dict['key'])"""
    object: Expression
    index: Expression
    
    def accept(self, visitor):
        return visitor.visit_index(self)


@dataclass
class ListExpression(Expression):
    """List literals [1, 2, 3]"""
    elements: List[Expression]
    
    def accept(self, visitor):
        return visitor.visit_list(self)


@dataclass
class DictExpression(Expression):
    """Dictionary literals {'a': 1, 'b': 2}"""
    pairs: List[tuple[Expression, Expression]]
    
    def accept(self, visitor):
        return visitor.visit_dict(self)


# Statements
class Statement(ASTNode):
    """Base class for all statements"""
    pass


@dataclass
class ExpressionStatement(Statement):
    """Expression used as statement"""
    expression: Expression
    
    def accept(self, visitor):
        return visitor.visit_expression_statement(self)


@dataclass
class PrintStatement(Statement):
    """tulis statement"""
    expressions: List[Expression]
    
    def accept(self, visitor):
        return visitor.visit_print(self)


@dataclass
class AssignmentStatement(Statement):
    """Variable assignment"""
    target: str
    value: Expression
    
    def accept(self, visitor):
        return visitor.visit_assignment(self)


@dataclass
class IfStatement(Statement):
    """jika statement"""
    condition: Expression
    then_branch: List[Statement]
    elif_branches: List[tuple[Expression, List[Statement]]]
    else_branch: Optional[List[Statement]]
    
    def accept(self, visitor):
        return visitor.visit_if(self)


@dataclass
class WhileStatement(Statement):
    """selama statement"""
    condition: Expression
    body: List[Statement]
    
    def accept(self, visitor):
        return visitor.visit_while(self)


@dataclass
class ForStatement(Statement):
    """untuk statement"""
    variable: str
    iterable: Expression
    body: List[Statement]
    
    def accept(self, visitor):
        return visitor.visit_for(self)


@dataclass
class FunctionDefinition(Statement):
    """fungsi definition"""
    name: str
    parameters: List[str]
    body: List[Statement]
    defaults: List[Optional[Expression]]
    
    def accept(self, visitor):
        return visitor.visit_function_def(self)


@dataclass
class ReturnStatement(Statement):
    """kembalikan statement"""
    value: Optional[Expression]
    
    def accept(self, visitor):
        return visitor.visit_return(self)


@dataclass
class BreakStatement(Statement):
    """berhenti statement"""
    
    def accept(self, visitor):
        return visitor.visit_break(self)


@dataclass
class ContinueStatement(Statement):
    """lanjut statement"""
    
    def accept(self, visitor):
        return visitor.visit_continue(self)


@dataclass
class PassStatement(Statement):
    """lewati statement"""
    
    def accept(self, visitor):
        return visitor.visit_pass(self)


@dataclass
class ImportStatement(Statement):
    """impor statement"""
    module_name: str
    alias: Optional[str]
    
    def accept(self, visitor):
        return visitor.visit_import(self)


@dataclass
class FromImportStatement(Statement):
    """dari ... impor statement"""
    module_name: str
    names: List[str]
    aliases: List[Optional[str]]
    
    def accept(self, visitor):
        return visitor.visit_from_import(self)


@dataclass
class ClassDefinition(Statement):
    """kelas definition"""
    name: str
    superclass: Optional[str]
    methods: List[FunctionDefinition]
    
    def accept(self, visitor):
        return visitor.visit_class_def(self)


@dataclass
class Program(ASTNode):
    """Root node representing entire program"""
    statements: List[Statement]
    
    def accept(self, visitor):
        return visitor.visit_program(self)
