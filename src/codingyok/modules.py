"""
Module system for CodingYok language
Handles module loading, caching, and import resolution
"""

import os
import sys
from typing import Dict, Any, Optional, List
from pathlib import Path


class ModuleObject:
    """Represents a loaded module"""

    def __init__(self, name: str, namespace: Dict[str, Any]):
        self.name = name
        self.namespace = namespace

    def get_attribute(self, attr: str) -> Any:
        """Get an attribute from the module namespace"""
        if attr in self.namespace:
            return self.namespace[attr]
        raise AttributeError(f"Module '{self.name}' tidak memiliki atribut '{attr}'")

    def __repr__(self):
        return f"<module '{self.name}'>"


class ModuleLoader:
    """Loads and manages CodingYok modules"""

    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.cache: Dict[str, ModuleObject] = {}
        self.search_paths: List[Path] = []
        self._initialize_search_paths()

    def _initialize_search_paths(self):
        """Initialize module search paths"""
        # Current working directory
        self.search_paths.append(Path.cwd())

        # Directory of the main script being executed (if any)
        if hasattr(self.interpreter, "script_dir") and self.interpreter.script_dir:
            script_path = Path(self.interpreter.script_dir)
            if script_path not in self.search_paths:
                self.search_paths.append(script_path)

        # Standard library modules directory (if exists)
        # Look for stdlib directory relative to the codingyok package
        codingyok_dir = Path(__file__).parent
        stdlib_dir = codingyok_dir / "stdlib_modules"
        if stdlib_dir.exists():
            self.search_paths.append(stdlib_dir)

    def find_module(self, module_name: str) -> Optional[Path]:
        """Find a module file in the search paths"""
        # Convert module name to filename (e.g., "my_module" -> "my_module.cy")
        filename = f"{module_name}.cy"

        for search_path in self.search_paths:
            module_path = search_path / filename
            if module_path.exists() and module_path.is_file():
                return module_path

        return None

    def load_module(
        self, module_name: str, alias: Optional[str] = None
    ) -> ModuleObject:
        """Load a module by name"""
        # Check cache first
        if module_name in self.cache:
            return self.cache[module_name]

        # Find the module file
        module_path = self.find_module(module_name)
        if not module_path:
            raise ModuleNotFoundError(
                f"Modul '{module_name}' tidak ditemukan. "
                f"Pastikan file '{module_name}.cy' ada di salah satu direktori: "
                f"{', '.join(str(p) for p in self.search_paths)}"
            )

        # Read and parse the module
        try:
            with open(module_path, "r", encoding="utf-8") as f:
                source_code = f.read()
        except Exception as e:
            raise RuntimeError(f"Gagal membaca modul '{module_name}': {e}")

        # Parse the module
        from .lexer import CodingYokLexer
        from .parser import CodingYokParser

        try:
            lexer = CodingYokLexer(source_code)
            tokens = lexer.tokenize()
            parser = CodingYokParser(tokens)
            ast = parser.parse()
        except Exception as e:
            raise RuntimeError(f"Gagal mem-parse modul '{module_name}': {e}")

        # Create a new environment for the module
        from .environment import Environment

        module_env = Environment(self.interpreter.global_env)

        # Execute the module in its own environment
        previous_env = self.interpreter.environment
        try:
            self.interpreter.environment = module_env
            for statement in ast.statements:
                self.interpreter.execute(statement)
        except Exception as e:
            # If there's an error during module execution, propagate it
            raise RuntimeError(f"Error saat mengeksekusi modul '{module_name}': {e}")
        finally:
            self.interpreter.environment = previous_env

        # Create module object with the module's namespace
        module_obj = ModuleObject(module_name, module_env.values)

        # Cache the module
        self.cache[module_name] = module_obj

        return module_obj

    def import_module(self, module_name: str, alias: Optional[str] = None):
        """Import a module and add it to the current environment"""
        module_obj = self.load_module(module_name, alias)

        # Add to current environment
        name_to_use = alias if alias else module_name
        self.interpreter.environment.define(name_to_use, module_obj)

    def import_from_module(
        self, module_name: str, names: List[str], aliases: List[Optional[str]]
    ):
        """Import specific names from a module"""
        module_obj = self.load_module(module_name)

        # Import each requested name
        for i, name in enumerate(names):
            try:
                value = module_obj.get_attribute(name)
                alias = aliases[i] if i < len(aliases) and aliases[i] else name
                self.interpreter.environment.define(alias, value)
            except AttributeError:
                raise RuntimeError(
                    f"Tidak dapat mengimpor '{name}' dari modul '{module_name}': "
                    f"nama tidak ditemukan"
                )

    def add_search_path(self, path: Path):
        """Add a new search path for modules"""
        if path not in self.search_paths:
            self.search_paths.append(path)


class ModuleNotFoundError(Exception):
    """Exception raised when a module cannot be found"""

    pass
