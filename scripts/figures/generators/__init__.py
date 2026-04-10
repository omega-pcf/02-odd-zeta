"""
Figure generator module.

Each generator is responsible for creating one or more specific figures.
The structure is flexible: a generator can create multiple figures,
or multiple generators can collaborate on a complex figure.
"""

from pathlib import Path
from typing import Callable, Dict, Optional

# Generator registry
_generators: Dict[str, Callable[[Path, bool], None]] = {}


def register(name: str):
    """
    Decorator to register a figure generator.
    
    Usage:
        @register("figure_1")
        def generate_figure_1(output_dir: Path, verbose: bool = False):
            # Generate figure...
            pass
    """
    def decorator(func: Callable[[Path, bool], None]):
        _generators[name] = func
        return func
    return decorator


def generate(name: str, output_dir: Path, verbose: bool = False) -> None:
    """
    Execute a specific generator.
    
    Args:
        name: Generator name
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    
    Raises:
        KeyError: If the generator does not exist
    """
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
    """
    Execute all registered generators.
    
    Args:
        output_dir: Directory where to save the figures
        verbose: If True, show additional information
    """
    if verbose:
        print(f"Generating {len(_generators)} figure(s)...")
    
    for name in sorted(_generators.keys()):
        try:
            generate(name, output_dir, verbose)
        except Exception as e:
            print(f"⚠ Error generating '{name}': {e}", file=__import__("sys").stderr)
            if verbose:
                import traceback
                traceback.print_exc()
            raise


def list_figures() -> list[str]:
    """Return list of all registered generators."""
    return sorted(_generators.keys())


# Import generators so they register automatically
# Each module in generators/ must be imported here
# We need to import them after the registry is defined, so we do it at module level
# but we need to ensure the parent directory is in sys.path
import sys
from pathlib import Path

# Ensure parent directory is in path for absolute imports
_parent_dir = Path(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

# Import existing generators (they register automatically via @register)
# These imports must happen after sys.path is set up
import generators.eigenvalues_triangle  # noqa: F401

import generators.orthogonal_views  # noqa: F401
import generators.equilateral_perspective  # noqa: F401
import generators.cylinder_lattice_connection  # noqa: F401
import generators.lattice_hypercube_analysis  # noqa: F401
import generators.tower_expansion  # noqa: F401
import generators.tower_contraction  # noqa: F401
import generators.sierpinski_2d  # noqa: F401
import generators.scale_factors  # noqa: F401
import generators.hypercube_projection  # noqa: F401
import generators.square_rhombus_projection  # noqa: F401
import generators.cylinder_pcf  # noqa: F401
import generators.hausdorff_dimension  # noqa: F401
import generators.top_view_expansion  # noqa: F401
import generators.torus_pcf  # noqa: F401
import generators.towers_comparison  # noqa: F401
import generators.dual_towers  # noqa: F401
import generators.hypercube_complete  # noqa: F401
import generators.hypercube_views  # noqa: F401
import generators.hypercube_tower  # noqa: F401
import generators.lattice_pcf_views  # noqa: F401
import generators.lattice_square_combined  # noqa: F401
import generators.comparative_dimensional_mechanisms  # noqa: F401
import generators.dual_spectrum  # noqa: F401
import generators.gauss_eisenstein_transition  # noqa: F401
import generators.cylinder_lattice_3d  # noqa: F401
import generators.cylinder_lattice_top  # noqa: F401
import generators.cylinder_lattice_lateral  # noqa: F401


