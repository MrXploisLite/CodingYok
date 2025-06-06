"""
Interpreter for CodingYok language
Executes the Abstract Syntax Tree (AST)
"""

from typing import Any, Dict, List, Optional, Callable
import sys
from .ast_nodes import *
from .errors import *
from .environment import Environment
from .stdlib import get_builtin_functions
from .indonesia import get_indonesian_functions
from .fileio import get_fileio_functions
from .web import get_web_functions
from .classes import CodingYokClass, CodingYokInstance, CodingYokMethod, create_builtin_exceptions


class CodingYokFunction:
    """Represents a CodingYok function"""
    
    def __init__(self, declaration: FunctionDefinition, closure: Environment):
        self.declaration = declaration
        self.closure = closure
    
    def call(self, interpreter, arguments: List[Any]) -> Any:
        """Call the function with given arguments"""
        # Create new environment for function execution
        environment = Environment(self.closure)
        
        # Bind parameters
        params = self.declaration.parameters
        defaults = self.declaration.defaults
        
        # Handle default parameters
        for i, param in enumerate(params):
            if i < len(arguments):
                environment.define(param, arguments[i])
            elif i < len(defaults) and defaults[i] is not None:
                default_value = interpreter.evaluate(defaults[i])
                environment.define(param, default_value)
            else:
                raise CodingYokRuntimeError(f"Parameter '{param}' tidak memiliki nilai")
        
        # Execute function body
        try:
            previous = interpreter.environment
            interpreter.environment = environment
            
            for statement in self.declaration.body:
                interpreter.execute(statement)
            
            return None  # No explicit return
            
        except ReturnValue as return_value:
            return return_value.value
        finally:
            interpreter.environment = previous
    
    def __str__(self) -> str:
        return f"<fungsi {self.declaration.name}>"


class ReturnValue(Exception):
    """Exception used for return statements"""
    
    def __init__(self, value: Any):
        self.value = value


class BreakException(Exception):
    """Exception used for break statements"""
    pass


class ContinueException(Exception):
    """Exception used for continue statements"""
    pass


class CodingYokInterpreter:
    """Main interpreter class"""
    
    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals
        
        # Add built-in functions
        builtins = get_builtin_functions()
        for name, func in builtins.items():
            self.globals.define(name, func)

        # Add Indonesian-specific functions
        indonesian_funcs = get_indonesian_functions()
        for name, func in indonesian_funcs.items():
            self.globals.define(name, func)

        # Add file I/O functions
        fileio_funcs = get_fileio_functions()
        for name, func in fileio_funcs.items():
            self.globals.define(name, func)

        # Add web functions
        web_funcs = get_web_functions()
        for name, func in web_funcs.items():
            self.globals.define(name, func)

        # Add built-in exception classes
        exceptions = create_builtin_exceptions()
        for name, exc_class in exceptions.items():
            self.globals.define(name, exc_class)
    
    def interpret(self, program: Program) -> None:
        """Interpret a program"""
        try:
            for statement in program.statements:
                self.execute(statement)
        except CodingYokRuntimeError as error:
            self.runtime_error(error)
    
    def runtime_error(self, error: CodingYokRuntimeError) -> None:
        """Handle runtime error"""
        print(f"Kesalahan Runtime: {error}", file=sys.stderr)
    
    def execute(self, statement: Statement) -> None:
        """Execute a statement"""
        statement.accept(self)
    
    def evaluate(self, expression: Expression) -> Any:
        """Evaluate an expression"""
        return expression.accept(self)
    
    # Visitor methods for statements
    def visit_program(self, program: Program) -> None:
        """Visit program node"""
        for statement in program.statements:
            self.execute(statement)
    
    def visit_expression_statement(self, stmt: ExpressionStatement) -> None:
        """Visit expression statement"""
        self.evaluate(stmt.expression)
    
    def visit_print(self, stmt: PrintStatement) -> None:
        """Visit print statement"""
        values = []
        for expr in stmt.expressions:
            value = self.evaluate(expr)
            values.append(self.stringify(value))
        
        print(" ".join(values))
    
    def visit_assignment(self, stmt: AssignmentStatement) -> None:
        """Visit assignment statement"""
        value = self.evaluate(stmt.value)
        self.environment.define(stmt.target, value)
    
    def visit_if(self, stmt: IfStatement) -> None:
        """Visit if statement"""
        condition_value = self.evaluate(stmt.condition)
        
        if self.is_truthy(condition_value):
            for statement in stmt.then_branch:
                self.execute(statement)
        else:
            # Check elif branches
            for elif_condition, elif_body in stmt.elif_branches:
                elif_value = self.evaluate(elif_condition)
                if self.is_truthy(elif_value):
                    for statement in elif_body:
                        self.execute(statement)
                    return
            
            # Execute else branch if present
            if stmt.else_branch:
                for statement in stmt.else_branch:
                    self.execute(statement)
    
    def visit_while(self, stmt: WhileStatement) -> None:
        """Visit while statement"""
        try:
            while self.is_truthy(self.evaluate(stmt.condition)):
                try:
                    for statement in stmt.body:
                        self.execute(statement)
                except ContinueException:
                    continue
        except BreakException:
            pass
    
    def visit_for(self, stmt: ForStatement) -> None:
        """Visit for statement"""
        iterable = self.evaluate(stmt.iterable)
        
        if not hasattr(iterable, '__iter__'):
            raise CodingYokTypeError("Objek tidak dapat diiterasi")
        
        try:
            for item in iterable:
                self.environment.define(stmt.variable, item)
                
                try:
                    for statement in stmt.body:
                        self.execute(statement)
                except ContinueException:
                    continue
        except BreakException:
            pass
    
    def visit_function_def(self, stmt: FunctionDefinition) -> None:
        """Visit function definition"""
        function = CodingYokFunction(stmt, self.environment)
        self.environment.define(stmt.name, function)
    
    def visit_return(self, stmt: ReturnStatement) -> None:
        """Visit return statement"""
        value = None
        if stmt.value:
            value = self.evaluate(stmt.value)
        
        raise ReturnValue(value)
    
    def visit_break(self, stmt: BreakStatement) -> None:
        """Visit break statement"""
        raise BreakException()
    
    def visit_continue(self, stmt: ContinueStatement) -> None:
        """Visit continue statement"""
        raise ContinueException()
    
    def visit_pass(self, stmt: PassStatement) -> None:
        """Visit pass statement"""
        pass  # Do nothing
    
    def visit_import(self, stmt: ImportStatement) -> None:
        """Visit import statement"""
        # TODO: Implement module system
        raise CodingYokRuntimeError("Sistem modul belum diimplementasikan")
    
    def visit_from_import(self, stmt: FromImportStatement) -> None:
        """Visit from import statement"""
        # TODO: Implement module system
        raise CodingYokRuntimeError("Sistem modul belum diimplementasikan")
    
    def visit_class_def(self, stmt: ClassDefinition) -> None:
        """Visit class definition"""
        superclass = None
        if stmt.superclass:
            superclass_value = self.environment.get(stmt.superclass)
            if not isinstance(superclass_value, CodingYokClass):
                raise CodingYokRuntimeError(f"Superclass harus berupa kelas")
            superclass = superclass_value

        # Create methods dictionary
        methods = {}
        for method in stmt.methods:
            methods[method.name] = CodingYokMethod(method, self.environment)

        # Create class
        klass = CodingYokClass(stmt.name, superclass, methods)
        self.environment.define(stmt.name, klass)
    
    # Visitor methods for expressions
    def visit_literal(self, expr: LiteralExpression) -> Any:
        """Visit literal expression"""
        return expr.value
    
    def visit_identifier(self, expr: IdentifierExpression) -> Any:
        """Visit identifier expression"""
        return self.environment.get(expr.name)
    
    def visit_binary(self, expr: BinaryExpression) -> Any:
        """Visit binary expression"""
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        
        operator = expr.operator
        
        # Arithmetic operators
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise CodingYokZeroDivisionError()
            return left / right
        elif operator == '//':
            if right == 0:
                raise CodingYokZeroDivisionError()
            return left // right
        elif operator == '%':
            return left % right
        elif operator == '**':
            return left ** right
        
        # Comparison operators
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '<=':
            return left <= right
        elif operator == '>':
            return left > right
        elif operator == '>=':
            return left >= right
        
        # Logical operators
        elif operator == 'dan':
            return self.is_truthy(left) and self.is_truthy(right)
        elif operator == 'atau':
            return self.is_truthy(left) or self.is_truthy(right)
        
        else:
            raise CodingYokRuntimeError(f"Operator binary tidak dikenal: {operator}")
    
    def visit_unary(self, expr: UnaryExpression) -> Any:
        """Visit unary expression"""
        operand = self.evaluate(expr.operand)
        
        if expr.operator == '-':
            return -operand
        elif expr.operator == 'bukan':
            return not self.is_truthy(operand)
        else:
            raise CodingYokRuntimeError(f"Operator unary tidak dikenal: {expr.operator}")
    
    def visit_call(self, expr: CallExpression) -> Any:
        """Visit call expression"""
        callee = self.evaluate(expr.callee)

        arguments = []
        for arg in expr.arguments:
            arguments.append(self.evaluate(arg))

        if isinstance(callee, CodingYokFunction):
            return callee.call(self, arguments)
        elif isinstance(callee, CodingYokClass):
            return callee.call(self, arguments)
        elif hasattr(callee, 'call'):
            return callee.call(self, arguments)
        elif callable(callee):
            return callee(*arguments)
        else:
            raise CodingYokTypeError("Objek tidak dapat dipanggil")
    
    def visit_attribute(self, expr: AttributeExpression) -> Any:
        """Visit attribute expression"""
        obj = self.evaluate(expr.object)

        if isinstance(obj, CodingYokInstance):
            return obj.get(expr.attribute)
        elif hasattr(obj, expr.attribute):
            return getattr(obj, expr.attribute)
        else:
            obj_type = type(obj).__name__
            if isinstance(obj, CodingYokInstance):
                obj_type = obj.klass.name
            raise CodingYokAttributeError(obj_type, expr.attribute)
    
    def visit_index(self, expr: IndexExpression) -> Any:
        """Visit index expression"""
        obj = self.evaluate(expr.object)
        index = self.evaluate(expr.index)
        
        try:
            return obj[index]
        except (IndexError, KeyError, TypeError) as e:
            if isinstance(e, IndexError):
                raise CodingYokIndexError()
            elif isinstance(e, KeyError):
                raise CodingYokKeyError(index)
            else:
                raise CodingYokTypeError("Objek tidak mendukung pengindeksan")
    
    def visit_list(self, expr: ListExpression) -> List[Any]:
        """Visit list expression"""
        elements = []
        for element in expr.elements:
            elements.append(self.evaluate(element))
        return elements
    
    def visit_dict(self, expr: DictExpression) -> Dict[Any, Any]:
        """Visit dictionary expression"""
        result = {}
        for key_expr, value_expr in expr.pairs:
            key = self.evaluate(key_expr)
            value = self.evaluate(value_expr)
            result[key] = value
        return result
    
    # Helper methods
    def is_truthy(self, value: Any) -> bool:
        """Determine if value is truthy"""
        if value is None or value is False:
            return False
        return True
    
    def stringify(self, value: Any) -> str:
        """Convert value to string representation"""
        if value is None:
            return "kosong"
        elif value is True:
            return "benar"
        elif value is False:
            return "salah"
        else:
            return str(value)
