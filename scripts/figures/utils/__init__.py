"""
Shared utilities for figure generation.

This module contains helper functions common to multiple generators:
- Matplotlib configuration
- Plotting functions
- Data processing
- Mathematical constants
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Matplotlib configuration for academic publication
# Professional style, high resolution, appropriate typography
plt.style.use("seaborn-v0_8-paper")  # Professional base style
matplotlib.rcParams.update({
    # Typography
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Liberation Serif", "Computer Modern Roman", "serif"],
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 12,

    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.titlesize": 12,
    
    # Resolution and format
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.format": "pdf",
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
    
    # Line quality
    "lines.linewidth": 1.5,
    "lines.markersize": 4,
    "axes.linewidth": 1.0,
    
    # Colors
    "axes.prop_cycle": plt.cycler(
        "color",
        ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    ),
})


# Mathematical constants relevant to the paper
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PI = np.pi
E = np.e


def setup_figure(width: float = 6.0, height: float = 4.0, dpi: int = 300) -> tuple[plt.Figure, plt.Axes]:
    """
    Create a figure with standard configuration for the paper.
    
    Args:
        width: Width in inches (default: 6.0, approx. \textwidth/2 in LaTeX)
        height: Height in inches (default: 4.0)
        dpi: Resolution (default: 300, high quality)
    
    Returns:
        Tuple (fig, ax) ready to use
    """
    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    return fig, ax


def save_figure(
    fig: plt.Figure,
    output_path: Path,
    formats: list[str] | None = None,
    verbose: bool = False
) -> None:
    """
    Save a figure in one or more formats.
    
    Args:
        fig: Matplotlib figure
        output_path: Base path (without extension)
        formats: List of formats (default: ["png", "svg", "pdf"])
        verbose: If True, show information
    """
    if formats is None:
        formats = ["pdf", "svg"]
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    for fmt in formats:
        # If output_path already has an extension that matches fmt, use it directly
        # Otherwise, add/replace extension
        if output_path.suffix == f".{fmt}":
            full_path = output_path
        else:
            full_path = output_path.with_suffix(f".{fmt}")
            
        # Use high DPI for raster, vector formats handle themselves
        dpi = 300 if fmt == "png" else None
        
        try:
            fig.savefig(full_path, format=fmt, bbox_inches="tight", dpi=dpi, pad_inches=0.02)
            if verbose:
                print(f"    Saved: {full_path}")
        except Exception as e:
            print(f"    ⚠ Error saving {fmt}: {e}")


def close_all() -> None:
    """Close all open figures (useful for cleanup)."""
    plt.close("all")

