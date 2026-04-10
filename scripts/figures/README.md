# Figure Generation

This directory contains Python scripts to generate figures.

## Architecture

The structure is designed to be:
- **Modular**: Each generator is independent
- **Flexible**: Does not force 1:1 mapping between files and figures
- **Extensible**: Easy to add new generators
- **Reproducible**: Uses `uv` for dependency management

### Structure

```
scripts/figures/
├── main.py              # Main entry point
├── pyproject.toml       # Python dependencies (uv)
├── generators/          # Generator modules
│   ├── __init__.py      # Generator registry
│   ├── registry.py      # Registry re-export
│   ├── example.py       # Example generator
│   └── ...              # Other generators
└── utils/               # Shared utilities
    └── __init__.py      # Plotting functions, constants, etc.
```

## Usage

### From package.json (recommended)

```bash
# Generate all figures
pnpm run generate:figures

# Full build (figures + PDF)
pnpm run build:full

# PDF build only (without figures)
pnpm run build
```

### Directly with Python

```bash
cd scripts/figures

# Generate all figures
uv run python main.py

# Generate a specific figure
uv run python main.py --figure example

# List available figures
uv run python main.py --list

# Verbose mode
uv run python main.py --verbose

# Specify output directory
uv run python main.py --output-dir ../src/images
```

## Creating a New Generator

1. Create a file in `generators/` (e.g., `generators/figure_1.py`)

2. Use the `@register` decorator:

```python
from pathlib import Path
from ..generators import register
from ..utils import setup_figure, save_figure
import matplotlib.pyplot as plt

@register("figure_1")
def generate_figure_1(output_dir: Path, verbose: bool = False) -> None:
    """Generate figure 1 of the paper."""
    if verbose:
        print("  Generating figure 1...")
    
    fig, ax = setup_figure(width=6.0, height=4.0)
    
    # Your generation code here
    # ...
    
    output_path = output_dir / "figure_1"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
```

3. Import the module in `generators/__init__.py`:

```python
from . import figure_1  # noqa: F401
```

4. Done! The generator will be available automatically.

## Dependencies

Dependencies are managed with `uv` and defined in `pyproject.toml`.

To install/update dependencies:

```bash
cd scripts/figures
uv sync
```

## Output

By default, figures are saved to `images/` (relative to project root).

Each generator can create one or more figures. The default format is PNG at 300 DPI, suitable for academic publication.

## Notes

- Generators register automatically when imported
- A generator can create multiple figures if needed
- Utilities in `utils/` provide standard matplotlib configuration for publication
- The system is error-tolerant: if a generator fails, it's reported but the process continues (unless critical)
