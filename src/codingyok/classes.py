"""
Class system implementation for CodingYok
Supports inheritance, method resolution, and instance management
"""

from typing import Any, Dict, List, Optional, TYPE_CHECKING
from .errors import CodingYokRuntimeError, CodingYokAttributeError
from .environment import Environment

if TYPE_CHECKING:
    from .interpreter import CodingYokInterpreter
    from .ast_nodes import FunctionDefinition


class CodingYokClass:
    """Represents a CodingYok class"""

    def __init__(
        self, name: str, superclass: Optional["CodingYokClass"], methods: Dict[str, Any]
    ):
        self.name = name
        self.superclass = superclass
        self.methods = methods

    def call(
        self, interpreter: "CodingYokInterpreter", arguments: List[Any]
    ) -> "CodingYokInstance":
        """Create new instance of the class"""
        instance = CodingYokInstance(self)

        # Call __init__ if it exists
        initializer = self.find_method("__init__")
        if initializer:
            initializer.bind(instance).call(interpreter, arguments)

        return instance

    def find_method(self, name: str) -> Optional[Any]:
        """Find method in this class or superclass"""
        if name in self.methods:
            return self.methods[name]

        if self.superclass:
            return self.superclass.find_method(name)

        return None

    def __str__(self) -> str:
        return f"<kelas {self.name}>"


class CodingYokInstance:
    """Represents an instance of a CodingYok class"""

    def __init__(self, klass: CodingYokClass):
        self.klass = klass
        self.fields: Dict[str, Any] = {}

    def get(self, name: str) -> Any:
        """Get attribute from instance"""
        if name in self.fields:
            return self.fields[name]

        method = self.klass.find_method(name)
        if method:
            return method.bind(self)

        raise CodingYokAttributeError(self.klass.name, name)

    def set(self, name: str, value: Any) -> None:
        """Set attribute on instance"""
        self.fields[name] = value

    def __str__(self) -> str:
        return f"<instance {self.klass.name}>"


class CodingYokBoundMethod:
    """Represents a method bound to an instance"""

    def __init__(self, instance: CodingYokInstance, method: Any):
        self.instance = instance
        self.method = method

    def call(self, interpreter: "CodingYokInterpreter", arguments: List[Any]) -> Any:
        """Call the bound method"""
        # Add 'diri' (self) as first argument
        return self.method.call(interpreter, [self.instance] + arguments)

    def __str__(self) -> str:
        return f"<bound method {self.method.declaration.name}>"


# Enhanced CodingYokFunction to support method binding
class CodingYokMethod:
    """Represents a method that can be bound to instances"""

    def __init__(self, declaration: "FunctionDefinition", closure: Environment):
        self.declaration = declaration
        self.closure = closure

    def bind(self, instance: CodingYokInstance) -> CodingYokBoundMethod:
        """Bind this method to an instance"""
        return CodingYokBoundMethod(instance, self)

    def call(self, interpreter: "CodingYokInterpreter", arguments: List[Any]) -> Any:
        """Call the method (unbound)"""
        from .interpreter import ReturnValue

        # Create new environment for method execution
        environment = Environment(self.closure)

        # Bind parameters
        params = self.declaration.parameters
        defaults = self.declaration.defaults

        # Handle default parameters
        for i, param in enumerate(params):
            if i < len(arguments):
                environment.define(param, arguments[i])
            elif i < len(defaults) and defaults[i] is not None:
                default_value = interpreter.evaluate(defaults[i])  # type: ignore
                environment.define(param, default_value)
            else:
                raise CodingYokRuntimeError(f"Parameter '{param}' tidak memiliki nilai")

        # Execute method body
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
        return f"<method {self.declaration.name}>"


# Built-in exception classes for CodingYok
class CodingYokException:
    """Base exception class for CodingYok"""

    def __init__(self, message: str = ""):
        self.message = message

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.message}"


class CodingYokValueException(CodingYokException):
    """Value error exception"""

    pass


class CodingYokTypeException(CodingYokException):
    """Type error exception"""

    pass


class CodingYokIndexException(CodingYokException):
    """Index error exception"""

    pass


class CodingYokKeyException(CodingYokException):
    """Key error exception"""

    pass


class CodingYokAttributeException(CodingYokException):
    """Attribute error exception"""

    pass


class CodingYokZeroDivisionException(CodingYokException):
    """Zero division error exception"""

    pass


# Exception handling utilities
def create_builtin_exceptions() -> Dict[str, CodingYokClass]:
    """Create built-in exception classes"""
    exceptions: Dict[str, CodingYokClass] = {}

    # Base Exception class (simplified for now)
    base_exception = CodingYokClass("Exception", None, {})
    exceptions["Exception"] = base_exception

    # Specific exception types
    exception_types = [
        "ValueError",
        "TypeError",
        "IndexError",
        "KeyError",
        "AttributeError",
        "ZeroDivisionError",
    ]

    for exc_type in exception_types:
        exc_class = CodingYokClass(exc_type, base_exception, {})
        exceptions[exc_type] = exc_class

    return exceptions
