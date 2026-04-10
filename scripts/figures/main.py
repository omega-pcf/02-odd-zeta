#!/usr/bin/env python3
"""
Entry point for figure generation

This module coordinates the execution of all figure generators.
It can be run individually or as part of the build pipeline.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from generators.registry import (
    generate,
    generate_all,
    list_figures,
)


def main(args: Optional[list[str]] = None) -> int:
    """
    Main function that executes figure generators.
    
    Args:
        args: Command line arguments (optional, for testing)
    
    Returns:
        Exit code (0 = success, >0 = error)
    """
    parser = argparse.ArgumentParser(
        description="Generate figures for the Ω_PCF paper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all figures
  python main.py
  
  # Generate a specific figure
  python main.py --figure figure_1
  
  # List available figures
  python main.py --list
        """
    )
    
    parser.add_argument(
        "--figure",
        "-f",
        type=str,
        help="Generate only a specific figure (by name)"
    )
    
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List all available figures"
    )
    
    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        default="images",
        help="Output directory for figures (default: images)"
    )
    
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose mode (show more information)"
    )
    
    parsed_args = parser.parse_args(args)
    
    # Resolve absolute path for output directory
    project_root = Path(__file__).parent.parent.parent
    output_dir = project_root / parsed_args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if parsed_args.list:
        print("Available figures:")
        for name in list_figures():
            print(f"  - {name}")
        return 0
    
    try:
        if parsed_args.figure:
            # Generate a specific figure
            if parsed_args.verbose:
                print(f"Generating figure: {parsed_args.figure}")
            generate(parsed_args.figure, output_dir, verbose=parsed_args.verbose)
        else:
            # Generate all figures
            if parsed_args.verbose:
                print(f"Generating all figures in: {output_dir}")
            generate_all(output_dir, verbose=parsed_args.verbose)
        
        if parsed_args.verbose:
            print(f"\n✓ Figures generated successfully in: {output_dir}")
        
        return 0
    
    except Exception as e:
        print(f"❌ Error generating figures: {e}", file=sys.stderr)
        if parsed_args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
