"""
Figure generator module.
"""

from pathlib import Path
from typing import Callable, Dict, Optional

# Generator registry
_generators: Dict[str, Callable[[Path, bool], None]] = {}


def register(name: str):
    """Decorator to register a figure generator."""
    def decorator(func: Callable[[Path, bool], None]):
        _generators[name] = func
        return func
    return decorator


def generate(name: str, output_dir: Path, verbose: bool = False) -> None:
    """Execute a specific generator."""
    if name not in _generators:
        available = ", ".join(_generators.keys())
        raise KeyError(
            f"Generator '{name}' not found. "
            f"Available generators: {available}"
        )
    
    if verbose:
        print(f"  → Running generator: {name}")
    
    _generators[name](output_dir, verbose)


def generate_all(output_dir: Path, verbose: bool = False) -> None:
    """Execute all registered generators."""
    if verbose:
        print(f"Generating {len(_generators)} figure(s)...")
    
    for name in sorted(_generators.keys()):
        try:
            generate(name, output_dir, verbose)
        except Exception as e:
            print(f"⚠ Error generating '{name}': {e}", file=__import__("sys").stderr)
            raise


def list_figures() -> list[str]:
    """Return list of all registered generators."""
    return sorted(_generators.keys())
