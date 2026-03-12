"""
Interpreter for CodingYok language
Executes the Abstract Syntax Tree (AST)
"""

from typing import Any, Dict, List, Optional, Callable
import sys
import asyncio
import inspect
from .ast_nodes import *
from .errors import *
from .environment import Environment
from .stdlib import get_builtin_functions
from .indonesia import get_indonesian_functions
from .fileio import get_fileio_functions
from .web import get_web_functions
from .classes import (
    CodingYokClass,
    CodingYokInstance,
    CodingYokMethod,
    create_builtin_exceptions,
)
from .modules import ModuleLoader, ModuleObject


class CodingYokFunction:
    """Represents a CodingYok function"""

    def __init__(self, declaration: FunctionDefinition, closure: Environment):
        self.declaration = declaration
        self.closure = closure
        self.is_generator = self._check_if_generator()

    def _check_if_generator(self) -> bool:
        """Check if function contains yield statements"""
        from .ast_nodes import YieldStatement

        def has_yield(statements):
            for stmt in statements:
                if isinstance(stmt, YieldStatement):
                    return True
                for attr_name in dir(stmt):
                    if not attr_name.startswith("_"):
                        attr = getattr(stmt, attr_name)
                        if isinstance(attr, list):
                            if has_yield(attr):
                                return True
            return False

        return has_yield(self.declaration.body)

    async def call(self, interpreter, arguments: List[Any], keyword_args: dict = None) -> Any:
        """Call the function with given arguments"""
        if keyword_args is None:
            keyword_args = {}

        if self.is_generator:
            return await self._create_generator(interpreter, arguments, keyword_args)

        # Create new environment for function execution
        environment = Environment(self.closure)

        # Bind parameters
        params = self.declaration.parameters
        defaults = self.declaration.defaults

        # Handle positional and keyword arguments
        for i, param in enumerate(params):
            if param in keyword_args:
                # Keyword argument provided
                environment.define(param, keyword_args[param])
            elif i < len(arguments):
                # Positional argument provided
                environment.define(param, arguments[i])
            elif i < len(defaults) and defaults[i] is not None:
                # Use default value
                default_value = await interpreter.evaluate(defaults[i])
                environment.define(param, default_value)
            else:
                raise CodingYokRuntimeError(
                    f"Parameter '{param}' tidak memiliki nilai"
                )

        # Execute function body
        try:
            previous = interpreter.environment
            interpreter.environment = environment

            for statement in self.declaration.body:
                await interpreter.execute(statement)

            return None  # No explicit return

        except ReturnValue as return_value:
            return return_value.value
        finally:
            interpreter.environment = previous

    async def _create_generator(self, interpreter, arguments: List[Any], keyword_args: dict = None):
        """Create a generator object"""
        if keyword_args is None:
            keyword_args = {}

        environment = Environment(self.closure)
        params = self.declaration.parameters
        defaults = self.declaration.defaults

        for i, param in enumerate(params):
            if param in keyword_args:
                environment.define(param, keyword_args[param])
            elif i < len(arguments):
                environment.define(param, arguments[i])
            elif i < len(defaults) and defaults[i] is not None:
                default_value = await interpreter.evaluate(defaults[i])
                environment.define(param, default_value)
            else:
                raise CodingYokRuntimeError(
                    f"Parameter '{param}' tidak memiliki nilai"
                )

        async def generator():
            previous = interpreter.environment
            interpreter.environment = environment
            try:
                for statement in self.declaration.body:
                    try:
                        await interpreter.execute(statement)
                    except YieldValue as yv:
                        yield yv.value
            finally:
                interpreter.environment = previous

        return generator()

    def __str__(self) -> str:
        return f"<fungsi {self.declaration.name}>"


class CodingYokAsyncFunction:
    """Represents a CodingYok async function"""

    def __init__(self, declaration, closure: Environment):
        self.declaration = declaration
        self.closure = closure
        self.is_async_generator = self._check_if_async_generator()

    def _check_if_async_generator(self) -> bool:
        """Check if function contains async yield statements"""
        from .ast_nodes import YieldStatement

        def has_yield(statements):
            for stmt in statements:
                if isinstance(stmt, YieldStatement):
                    return True
                for attr_name in dir(stmt):
                    if not attr_name.startswith("_"):
                        attr = getattr(stmt, attr_name)
                        if isinstance(attr, list):
                            if has_yield(attr):
                                return True
            return False

        return has_yield(self.declaration.body)

    async def call(self, interpreter, arguments: List[Any], keyword_args: dict = None) -> Any:
        """Call the async function with given arguments"""
        if keyword_args is None:
            keyword_args = {}

        # Create new environment for function execution
        environment = Environment(self.closure)

        # Bind parameters
        params = self.declaration.parameters
        defaults = self.declaration.defaults

        # Handle positional and keyword arguments
        for i, param in enumerate(params):
            if param in keyword_args:
                # Keyword argument provided
                environment.define(param, keyword_args[param])
            elif i < len(arguments):
                # Positional argument provided
                environment.define(param, arguments[i])
            elif i < len(defaults) and defaults[i] is not None:
                # Use default value
                default_value = await interpreter.evaluate(defaults[i])
                environment.define(param, default_value)
            else:
                raise CodingYokRuntimeError(
                    f"Parameter '{param}' tidak memiliki nilai"
                )

        # Return a coroutine that executes the function
        async def async_func():
            previous = interpreter.environment
            interpreter.environment = environment
            try:
                for statement in self.declaration.body:
                    await interpreter.execute(statement)
                return None
            except ReturnValue as return_value:
                return return_value.value
            finally:
                interpreter.environment = previous

        return await async_func()


class CodingYokLambda:
    """Represents a CodingYok lambda (anonymous function)"""

    def __init__(
        self,
        parameters: List[str],
        body: Expression,
        closure: Environment,
        interpreter=None,
    ):
        self.parameters = parameters
        self.body = body
        self.closure = closure
        self.interpreter = interpreter

    async def call(self, interpreter, arguments: List[Any]) -> Any:
        """Call the lambda with given arguments"""
        if len(arguments) != len(self.parameters):
            raise CodingYokRuntimeError(
                f"Lambda mengharapkan {len(self.parameters)} argumen, "
                f"tetapi mendapat {len(arguments)}"
            )

        environment = Environment(self.closure)
        for i, param in enumerate(self.parameters):
            environment.define(param, arguments[i])

        previous = interpreter.environment
        interpreter.environment = environment
        try:
            return await interpreter.evaluate(self.body)
        finally:
            interpreter.environment = previous

    def __call__(self, *args):
        """Make lambda callable for Python's map/filter"""
        if self.interpreter:
            # Note: This will return a coroutine!
            return self.call(self.interpreter, list(args))
        raise CodingYokRuntimeError("Lambda tidak memiliki interpreter")


class ReturnValue(Exception):
    """Exception used for return statements"""

    def __init__(self, value: Any):
        self.value = value


class YieldValue(Exception):
    """Exception used for yield statements"""

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

    def __init__(self, script_dir=None):
        self.globals = Environment()
        self.environment = self.globals
        self.global_env = self.globals
        self.script_dir = script_dir

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

        # Initialize module loader
        self.module_loader = ModuleLoader(self)

    async def interpret(self, program: Program) -> None:
        """Interpret a program"""
        try:
            # Execute statements normally
            for statement in program.statements:
                await self.execute(statement)

            # Check if main was defined in this specific program
            has_main_def = any(
                isinstance(stmt, (FunctionDefinition, AsyncFunctionDefinition))
                and getattr(stmt, "name", None) == "main"
                for stmt in program.statements
            )

            if has_main_def:
                main_func = self.environment.values.get("main")
                if main_func and isinstance(
                    main_func, (CodingYokAsyncFunction, CodingYokFunction)
                ):
                    if isinstance(main_func, CodingYokAsyncFunction):
                        await main_func.call(self, [], {})
                    else:
                        main_func.call(self, [], {})

        except CodingYokRuntimeError as error:
            self.runtime_error(error)

    def runtime_error(self, error: CodingYokRuntimeError) -> None:
        """Handle runtime error"""
        print(f"Kesalahan Runtime: {error}", file=sys.stderr)

    async def execute(self, statement: Statement) -> None:
        """Execute a statement"""
        await statement.accept(self)

    async def evaluate(self, expression: Expression) -> Any:
        """Evaluate an expression"""
        return await expression.accept(self)

    # Visitor methods for statements
    async def visit_program(self, program: Program) -> None:
        """Visit program node"""
        for statement in program.statements:
            await self.execute(statement)

    async def visit_expression_statement(self, stmt: ExpressionStatement) -> None:
        """Visit expression statement"""
        await self.evaluate(stmt.expression)

    async def visit_print(self, stmt: PrintStatement) -> None:
        """Visit print statement"""
        values = []
        for expr in stmt.expressions:
            value = await self.evaluate(expr)
            values.append(self.stringify(value))

        print(" ".join(values))

    async def visit_assignment(self, stmt: AssignmentStatement) -> None:
        """Visit assignment statement"""
        value = await self.evaluate(stmt.value)
        self.environment.define(stmt.target, value)

    async def visit_attribute_assignment(self, stmt) -> None:
        """Visit attribute assignment statement"""
        from .ast_nodes import AttributeAssignmentStatement

        # Type annotation for the parameter
        attr_stmt: AttributeAssignmentStatement = stmt

        obj = await self.evaluate(stmt.target.object)
        value = await self.evaluate(stmt.value)

        if isinstance(obj, CodingYokInstance):
            obj.set(stmt.target.attribute, value)
        else:
            # Try to set attribute on Python object
            try:
                setattr(obj, stmt.target.attribute, value)
            except AttributeError:
                obj_type = type(obj).__name__
                raise CodingYokAttributeError(obj_type, stmt.target.attribute)

    async def visit_index_assignment(self, stmt) -> None:
        """Visit index assignment statement (arr[i] = value, dict[key] = value)"""
        obj = await self.evaluate(stmt.target.object)
        index = await self.evaluate(stmt.target.index)
        value = await self.evaluate(stmt.value)

        try:
            obj[index] = value
        except (TypeError, KeyError, IndexError) as e:
            raise CodingYokRuntimeError(
                f"Tidak dapat menetapkan nilai pada indeks: {e}"
            )

    async def visit_slice_assignment(self, stmt) -> None:
        """Visit slice assignment statement (arr[start:stop] = values)"""
        obj = await self.evaluate(stmt.target.object)
        start = await self.evaluate(stmt.target.start) if stmt.target.start else None
        stop = await self.evaluate(stmt.target.stop) if stmt.target.stop else None
        step = await self.evaluate(stmt.target.step) if stmt.target.step else None
        value = await self.evaluate(stmt.value)

        try:
            obj[start:stop:step] = value
        except TypeError as e:
            raise CodingYokRuntimeError(f"Tidak dapat menetapkan slice: {e}")

    async def visit_if(self, stmt: IfStatement) -> None:
        """Visit if statement"""
        condition_value = await self.evaluate(stmt.condition)

        if self.is_truthy(condition_value):
            for statement in stmt.then_branch:
                await self.execute(statement)
        else:
            # Check elif branches
            for elif_condition, elif_body in stmt.elif_branches:
                elif_value = await self.evaluate(elif_condition)
                if self.is_truthy(elif_value):
                    for statement in elif_body:
                        await self.execute(statement)
                    return

            # Execute else branch if present
            if stmt.else_branch:
                for statement in stmt.else_branch:
                    await self.execute(statement)

    async def visit_while(self, stmt: WhileStatement) -> None:
        """Visit while statement"""
        try:
            while self.is_truthy(await self.evaluate(stmt.condition)):
                try:
                    for statement in stmt.body:
                        await self.execute(statement)
                except ContinueException:
                    continue
        except BreakException:
            pass

    async def visit_for(self, stmt: ForStatement) -> None:
        """Visit for statement"""
        iterable = await self.evaluate(stmt.iterable)

        if not hasattr(iterable, "__iter__") and not hasattr(iterable, "__aiter__"):
            raise CodingYokTypeError("Objek tidak dapat diiterasi")

        async def run_body(item):
            # Handle tuple unpacking in for loop
            if isinstance(stmt.variable, list):
                # Tuple unpacking: untuk a, b dalam items
                if not hasattr(item, "__iter__") or isinstance(item, str):
                    raise CodingYokTypeError(
                        f"Tidak dapat unpack: diharapkan {len(stmt.variable)} "
                        f"nilai"
                    )
                item_list = list(item)
                if len(item_list) != len(stmt.variable):
                    raise CodingYokValueError(
                        f"Tidak dapat unpack: diharapkan {len(stmt.variable)} "
                        f"nilai, mendapat {len(item_list)}"
                    )
                for var, val in zip(stmt.variable, item_list):
                    self.environment.define(var, val)
            else:
                # Single variable
                self.environment.define(stmt.variable, item)

            try:
                for statement in stmt.body:
                    await self.execute(statement)
            except ContinueException:
                pass

        try:
            if hasattr(iterable, "__aiter__"):
                async for item in iterable:
                    try:
                        await run_body(item)
                    except ContinueException:
                        continue
            else:
                for item in iterable:
                    try:
                        await run_body(item)
                    except ContinueException:
                        continue
        except BreakException:
            pass

    async def visit_tuple_unpacking(self, stmt) -> None:
        """Visit tuple unpacking statement (a, b = 1, 2)"""
        value = await self.evaluate(stmt.value)

        # Convert to list if iterable
        if hasattr(value, "__iter__") and not isinstance(value, (str, dict)):
            values = list(value)
        else:
            raise CodingYokTypeError("Nilai harus berupa iterable untuk unpacking")

        if len(values) != len(stmt.targets):
            raise CodingYokValueError(
                f"Tidak dapat unpack: diharapkan {len(stmt.targets)} nilai, "
                f"mendapat {len(values)}"
            )

        for target, val in zip(stmt.targets, values):
            self.environment.define(target, val)

    async def visit_function_def(self, stmt: FunctionDefinition) -> None:
        """Visit function definition"""
        function = CodingYokFunction(stmt, self.environment)
        self.environment.define(stmt.name, function)

    async def visit_async_function_def(self, stmt: AsyncFunctionDefinition) -> None:
        """Visit async function definition"""
        function = CodingYokAsyncFunction(stmt, self.environment)
        self.environment.define(stmt.name, function)

    async def visit_return(self, stmt: ReturnStatement) -> None:
        """Visit return statement"""
        value = None
        if stmt.value:
            value = await self.evaluate(stmt.value)

        raise ReturnValue(value)

    async def visit_break(self, stmt: BreakStatement) -> None:
        """Visit break statement"""
        raise BreakException()

    async def visit_continue(self, stmt: ContinueStatement) -> None:
        """Visit continue statement"""
        raise ContinueException()

    async def visit_pass(self, stmt: PassStatement) -> None:
        """Visit pass statement"""
        pass  # Do nothing

    async def visit_yield(self, stmt: YieldStatement) -> None:
        """Visit yield statement"""
        value = None
        if stmt.value:
            value = await self.evaluate(stmt.value)
        raise YieldValue(value)

    async def visit_match(self, stmt: MatchStatement) -> None:
        """Visit match statement (pattern matching)"""
        match_value = await self.evaluate(stmt.value)

        for case in stmt.cases:
            if await self._match_pattern(match_value, case.pattern):
                if case.guard is None or self.is_truthy(await self.evaluate(case.guard)):
                    for statement in case.body:
                        await self.execute(statement)
                    return

        raise CodingYokRuntimeError(
            f"Tidak ada pola yang cocok untuk nilai: {match_value}"
        )

    async def _match_pattern(self, value: Any, pattern: Any) -> bool:
        """Check if value matches pattern"""
        if isinstance(pattern, IdentifierExpression):
            if pattern.name == "_":
                return True
            return True

        if not hasattr(pattern, "accept"):
            return value == pattern

        pattern_value = await self.evaluate(pattern)

        if isinstance(pattern_value, list):
            if not isinstance(value, list):
                return False
            if len(pattern_value) != len(value):
                return False
            for v, p in zip(value, pattern_value):
                if not await self._match_pattern(v, p):
                    return False
            return True

        return value == pattern_value

    async def visit_import(self, stmt: ImportStatement) -> None:
        """Visit import statement"""
        try:
            await self.module_loader.import_module(stmt.module_name, stmt.alias)
        except Exception as e:
            raise CodingYokRuntimeError(str(e))

    async def visit_from_import(self, stmt: FromImportStatement) -> None:
        """Visit from import statement"""
        try:
            await self.module_loader.import_from_module(
                stmt.module_name, stmt.names, stmt.aliases
            )
        except Exception as e:
            raise CodingYokRuntimeError(str(e))

    async def visit_class_def(self, stmt: ClassDefinition) -> None:
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

    async def visit_try(self, stmt: TryStatement) -> None:
        """Visit try statement"""
        exception_caught = False
        caught_exception = None

        try:
            for statement in stmt.try_block:
                await self.execute(statement)
        except Exception as e:
            exception_caught = True
            caught_exception = e

            for except_clause in stmt.except_clauses:
                if except_clause.exception_type is None:
                    env = Environment(self.environment)
                    if except_clause.exception_name:
                        env.define(except_clause.exception_name, e)

                    prev = self.environment
                    self.environment = env
                    try:
                        for statement in except_clause.body:
                            await self.execute(statement)
                        exception_caught = True
                        caught_exception = None
                        break
                    finally:
                        self.environment = prev
                else:
                    try:
                        exception_class = self.environment.get(
                            except_clause.exception_type
                        )
                    except:
                        exception_class = None

                    # Check if exception matches
                    matches = False
                    if exception_class or except_clause.exception_type:
                        # Check for exception type name matching
                        if except_clause.exception_type in [
                            "ValueError",
                            "TypeError",
                            "ZeroDivisionError",
                            "IndexError",
                            "KeyError",
                            "AttributeError",
                        ]:
                            # Map both Python and CodingYok exceptions
                            exception_type_map = {
                                "ValueError": (ValueError, CodingYokValueError),
                                "TypeError": (TypeError, CodingYokTypeError),
                                "ZeroDivisionError": (
                                    ZeroDivisionError,
                                    CodingYokZeroDivisionError,
                                ),
                                "IndexError": (IndexError, CodingYokIndexError),
                                "KeyError": (KeyError, CodingYokKeyError),
                                "AttributeError": (
                                    AttributeError,
                                    CodingYokAttributeError,
                                ),
                            }
                            exc_types = exception_type_map.get(
                                except_clause.exception_type, ()
                            )
                            if exc_types:
                                matches = isinstance(e, exc_types)
                        elif (
                            exception_class
                            and isinstance(exception_class, CodingYokClass)
                            and isinstance(e, CodingYokInstance)
                        ):
                            matches = e.klass == exception_class
                        elif exception_class and isinstance(e, type(exception_class)):
                            matches = True

                    if matches:
                        env = Environment(self.environment)
                        if except_clause.exception_name:
                            env.define(except_clause.exception_name, e)

                        prev = self.environment
                        self.environment = env
                        try:
                            for statement in except_clause.body:
                                await self.execute(statement)
                            exception_caught = True
                            caught_exception = None
                            break
                        finally:
                            self.environment = prev
        finally:
            if stmt.finally_block:
                for statement in stmt.finally_block:
                    await self.execute(statement)

        if caught_exception:
            raise caught_exception

    async def visit_raise(self, stmt: RaiseStatement) -> None:
        """Visit raise statement"""
        if stmt.exception:
            exception = await self.evaluate(stmt.exception)
            if isinstance(exception, str):
                raise CodingYokRuntimeError(exception)
            elif isinstance(exception, BaseException):
                raise exception
            elif isinstance(exception, CodingYokInstance):
                # Handle CodingYok exception instances
                exc_name = exception.klass.name
                # Get message if available
                msg = ""
                if "pesan" in exception.fields:
                    msg = str(exception.fields["pesan"])
                elif "message" in exception.fields:
                    msg = str(exception.fields["message"])
                # Map to Python exceptions
                exc_map = {
                    "ValueError": ValueError,
                    "TypeError": TypeError,
                    "IndexError": IndexError,
                    "KeyError": KeyError,
                    "ZeroDivisionError": ZeroDivisionError,
                    "AttributeError": AttributeError,
                    "Exception": Exception,
                }
                exc_class = exc_map.get(exc_name, Exception)
                raise exc_class(msg if msg else exc_name)
            else:
                raise CodingYokRuntimeError(
                    f"Objek yang di-raise harus berupa exception: {exception}"
                )
        else:
            raise CodingYokRuntimeError("lempar statement tanpa exception")

    async def visit_with(self, stmt: WithStatement) -> None:
        """Visit with statement"""
        context_manager = await self.evaluate(stmt.context_expr)

        enter_method = None
        exit_method = None

        if isinstance(context_manager, CodingYokInstance):
            try:
                enter_method = context_manager.get("__enter__")
                exit_method = context_manager.get("__exit__")
            except CodingYokAttributeError:
                if stmt.target:
                    self.environment.define(stmt.target, context_manager)
                for statement in stmt.body:
                    await self.execute(statement)
                return
        elif hasattr(context_manager, "__enter__") and hasattr(
            context_manager, "__exit__"
        ):
            enter_method = context_manager.__enter__
            exit_method = context_manager.__exit__
        else:
            if stmt.target:
                self.environment.define(stmt.target, context_manager)
            for statement in stmt.body:
                await self.execute(statement)
            return

        context_value = None
        if enter_method:
            if hasattr(enter_method, "call"):
                context_value = await enter_method.call(self, [])
            elif callable(enter_method):
                if inspect.iscoroutinefunction(enter_method):
                    context_value = await enter_method()
                else:
                    context_value = enter_method()

        if stmt.target:
            self.environment.define(
                stmt.target,
                context_value if context_value is not None else context_manager,
            )

        exception_occurred = None
        try:
            for statement in stmt.body:
                await self.execute(statement)
        except Exception as e:
            exception_occurred = e
        finally:
            if exit_method:
                if hasattr(exit_method, "call"):
                    await exit_method.call(self, [None, None, None])
                elif callable(exit_method):
                    if inspect.iscoroutinefunction(exit_method):
                        await exit_method(None, None, None)
                    else:
                        exit_method(None, None, None)

        if exception_occurred:
            raise exception_occurred

    # Visitor methods for expressions
    async def visit_literal(self, expr: LiteralExpression) -> Any:
        """Visit literal expression"""
        return expr.value

    async def visit_identifier(self, expr: IdentifierExpression) -> Any:
        """Visit identifier expression"""
        return self.environment.get(expr.name)

    async def visit_binary(self, expr: BinaryExpression) -> Any:
        """Visit binary expression"""
        left = await self.evaluate(expr.left)
        right = await self.evaluate(expr.right)

        operator = expr.operator

        # Arithmetic operators
        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            if right == 0:
                raise CodingYokZeroDivisionError()
            return left / right
        elif operator == "//":
            if right == 0:
                raise CodingYokZeroDivisionError()
            return left // right
        elif operator == "%":
            return left % right
        elif operator == "**":
            return left**right

        # Comparison operators
        elif operator == "==":
            return left == right
        elif operator == "!=":
            return left != right
        elif operator == "<":
            return left < right
        elif operator == "<=":
            return left <= right
        elif operator == ">":
            return left > right
        elif operator == ">=":
            return left >= right

        # Membership operator
        elif operator == "dalam":
            return left in right

        # Logical operators
        elif operator == "dan":
            return self.is_truthy(left) and self.is_truthy(right)
        elif operator == "atau":
            return self.is_truthy(left) or self.is_truthy(right)

        else:
            raise CodingYokRuntimeError(f"Operator binary tidak dikenal: {operator}")

    async def visit_ternary(self, expr) -> Any:
        """Visit ternary expression (value jika condition kalau_tidak other)"""
        condition = await self.evaluate(expr.condition)
        if self.is_truthy(condition):
            return await self.evaluate(expr.true_value)
        else:
            return await self.evaluate(expr.false_value)

    async def visit_walrus(self, expr) -> Any:
        """Visit walrus expression (name := value)"""
        value = await self.evaluate(expr.value)
        self.environment.define(expr.name, value)
        return value

    async def visit_unary(self, expr: UnaryExpression) -> Any:
        """Visit unary expression"""
        operand = await self.evaluate(expr.operand)

        if expr.operator == "-":
            return -operand
        elif expr.operator == "bukan":
            return not self.is_truthy(operand)
        else:
            raise CodingYokRuntimeError(
                f"Operator unary tidak dikenal: {expr.operator}"
            )

    async def visit_call(self, expr: CallExpression) -> Any:
        """Visit call expression"""
        callee = await self.evaluate(expr.callee)

        arguments = []
        for arg in expr.arguments:
            arguments.append(await self.evaluate(arg))

        # Evaluate keyword arguments
        keyword_args = {}
        for name, value_expr in expr.keyword_args.items():
            keyword_args[name] = await self.evaluate(value_expr)

        if isinstance(callee, (CodingYokFunction, CodingYokAsyncFunction)):
            res = callee.call(self, arguments, keyword_args)
            if asyncio.iscoroutine(res):
                return await res
            return res
        elif isinstance(callee, CodingYokClass):
            res = callee.call(self, arguments, keyword_args)
            if asyncio.iscoroutine(res):
                return await res
            return res
        elif hasattr(callee, "call"):
            # Check if call method accepts keyword_args
            sig = inspect.signature(callee.call)
            if len(sig.parameters) >= 3:
                res = callee.call(self, arguments, keyword_args)
            else:
                res = callee.call(self, arguments)

            if asyncio.iscoroutine(res):
                return await res
            return res
        elif callable(callee):
            if inspect.iscoroutinefunction(callee):
                return await callee(*arguments, **keyword_args)
            res = callee(*arguments, **keyword_args)
            if asyncio.iscoroutine(res):
                return await res
            return res
        else:
            raise CodingYokTypeError("Objek tidak dapat dipanggil")

    async def visit_attribute(self, expr: AttributeExpression) -> Any:
        """Visit attribute expression"""
        obj = await self.evaluate(expr.object)

        if isinstance(obj, ModuleObject):
            try:
                return obj.get_attribute(expr.attribute)
            except AttributeError as e:
                raise CodingYokAttributeError(obj.name, expr.attribute)
        elif isinstance(obj, CodingYokInstance):
            return obj.get(expr.attribute)
        elif hasattr(obj, expr.attribute):
            return getattr(obj, expr.attribute)
        else:
            obj_type = type(obj).__name__
            if isinstance(obj, CodingYokInstance):
                obj_type = obj.klass.name
            raise CodingYokAttributeError(obj_type, expr.attribute)

    async def visit_index(self, expr: IndexExpression) -> Any:
        """Visit index expression"""
        obj = await self.evaluate(expr.object)
        index = await self.evaluate(expr.index)

        try:
            return obj[index]
        except (IndexError, KeyError, TypeError) as e:
            if isinstance(e, IndexError):
                raise CodingYokIndexError()
            elif isinstance(e, KeyError):
                raise CodingYokKeyError(index)
            else:
                raise CodingYokTypeError("Objek tidak mendukung pengindeksan")

    async def visit_slice(self, expr) -> Any:
        """Visit slice expression (arr[start:stop:step])"""
        obj = await self.evaluate(expr.object)

        start = await self.evaluate(expr.start) if expr.start else None
        stop = await self.evaluate(expr.stop) if expr.stop else None
        step = await self.evaluate(expr.step) if expr.step else None

        try:
            return obj[start:stop:step]
        except TypeError:
            raise CodingYokTypeError("Objek tidak mendukung slicing")

    async def visit_list(self, expr: ListExpression) -> List[Any]:
        """Visit list expression"""
        elements = []
        for element in expr.elements:
            elements.append(await self.evaluate(element))
        return elements

    async def visit_tuple(self, expr) -> tuple:
        """Visit tuple expression"""
        elements = []
        for element in expr.elements:
            elements.append(await self.evaluate(element))
        return tuple(elements)

    async def visit_dict(self, expr: DictExpression) -> Dict[Any, Any]:
        """Visit dictionary expression"""
        result = {}
        for key_expr, value_expr in expr.pairs:
            key = await self.evaluate(key_expr)
            value = await self.evaluate(value_expr)
            result[key] = value
        return result

    async def visit_fstring(self, expr: FStringExpression) -> str:
        """Visit f-string expression"""
        result = ""
        for part in expr.parts:
            if isinstance(part, str):
                result += part
            else:
                # Evaluate the expression and convert to string
                value = await self.evaluate(part)
                result += self.stringify(value)
        return result

    async def visit_list_comprehension(self, expr: ListComprehension) -> List[Any]:
        """Visit list comprehension"""
        result = []
        iterable = await self.evaluate(expr.iterable)

        if not hasattr(iterable, "__iter__"):
            raise CodingYokTypeError("Objek tidak dapat diiterasi dalam comprehension")

        env = Environment(self.environment)
        prev_env = self.environment
        self.environment = env

        try:
            for item in iterable:
                self.environment.define(expr.variable, item)

                if expr.condition is None or self.is_truthy(
                    await self.evaluate(expr.condition)
                ):
                    result.append(await self.evaluate(expr.element))
        finally:
            self.environment = prev_env

        return result

    async def visit_dict_comprehension(self, expr: DictComprehension) -> Dict[Any, Any]:
        """Visit dict comprehension"""
        result = {}
        iterable = await self.evaluate(expr.iterable)

        if not hasattr(iterable, "__iter__"):
            raise CodingYokTypeError("Objek tidak dapat diiterasi dalam comprehension")

        env = Environment(self.environment)
        prev_env = self.environment
        self.environment = env

        try:
            for item in iterable:
                self.environment.define(expr.variable, item)

                if expr.condition is None or self.is_truthy(
                    await self.evaluate(expr.condition)
                ):
                    key = await self.evaluate(expr.key)
                    value = await self.evaluate(expr.value)
                    result[key] = value
        finally:
            self.environment = prev_env

        return result

    async def visit_set(self, expr: SetExpression) -> set:
        """Visit set expression"""
        elements = []
        for element in expr.elements:
            elements.append(await self.evaluate(element))
        return set(elements)

    async def visit_set_comprehension(self, expr: SetComprehension) -> set:
        """Visit set comprehension"""
        result = set()
        iterable = await self.evaluate(expr.iterable)

        if not hasattr(iterable, "__iter__"):
            raise CodingYokTypeError("Objek tidak dapat diiterasi dalam comprehension")

        env = Environment(self.environment)
        prev_env = self.environment
        self.environment = env

        try:
            for item in iterable:
                self.environment.define(expr.variable, item)

                if expr.condition is None or self.is_truthy(
                    await self.evaluate(expr.condition)
                ):
                    result.add(await self.evaluate(expr.element))
        finally:
            self.environment = prev_env

        return result

    async def visit_lambda(self, expr: LambdaExpression) -> CodingYokLambda:
        """Visit lambda expression"""
        return CodingYokLambda(expr.parameters, expr.body, self.environment, self)

    async def visit_await(self, expr: AwaitExpression) -> Any:
        """Visit await expression"""
        value = await self.evaluate(expr.expression)
        if asyncio.iscoroutine(value):
            return await value
        return value

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
