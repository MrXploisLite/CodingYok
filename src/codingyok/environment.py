"""
Environment for variable scope management in CodingYok
"""

from typing import Any, Dict, Optional
from .errors import CodingYokNameError


class Environment:
    """Represents a scope for variables"""

    def __init__(self, enclosing: Optional["Environment"] = None):
        self.enclosing = enclosing
        self.values: Dict[str, Any] = {}

    def define(self, name: str, value: Any) -> None:
        """Define a variable in this environment"""
        self.values[name] = value

    def get(self, name: str) -> Any:
        """Get a variable value"""
        if name in self.values:
            return self.values[name]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise CodingYokNameError(name)

    def assign(self, name: str, value: Any) -> None:
        """Assign to an existing variable"""
        if name in self.values:
            self.values[name] = value
            return

        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return

        raise CodingYokNameError(name)

    def get_at(self, distance: int, name: str) -> Any:
        """Get variable at specific distance in scope chain"""
        return self.ancestor(distance).values[name]

    def assign_at(self, distance: int, name: str, value: Any) -> None:
        """Assign variable at specific distance in scope chain"""
        self.ancestor(distance).values[name] = value

    def ancestor(self, distance: int) -> "Environment":
        """Get ancestor environment at given distance"""
        environment = self
        for _ in range(distance):
            if environment.enclosing is not None:
                environment = environment.enclosing
            else:
                raise RuntimeError(f"Cannot access ancestor at distance {distance}")
        return environment

    def __str__(self) -> str:
        """String representation for debugging"""
        result = f"Environment({list(self.values.keys())})"
        if self.enclosing:
            result += f" -> {self.enclosing}"
        return result
