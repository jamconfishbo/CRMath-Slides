#!/usr/bin/env python3
"""Stitch already-rendered slide scenes into one combined lesson presentation.

Render each slide file first with build_slide.py, then combine the scenes
(in the order you want them to play) with this script. Scenes must live in
the same directory (they must share a `slides/` folder, which is how
manim-slides stores each scene's rendered steps).

Usage:
    python build_course.py <slide_dir> <Scene1> <Scene2> ... [--out name.html]

Example:
    python build_course.py precalc/order_of_operations \\
        OrderOfOperationsTitle ClearingParenthesesTitle Practice69And70 NestedAbsoluteValuePractice \\
        --out order_of_operations_lesson2.html
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_OUT_DIR = REPO_ROOT / "presentations"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slide_dir", help="Directory containing the rendered scenes' slides/ folder")
    parser.add_argument("scenes", nargs="+", help="Scene names, in the order they should play")
    parser.add_argument("--out", default=None, help="Output filename (default: <slide_dir name>.html)")
    parser.add_argument(
        "--to", default="html", help="Output format passed to manim-slides convert (default: html)"
    )
    args = parser.parse_args()

    slide_dir = (REPO_ROOT / args.slide_dir).resolve()
    if not (slide_dir / "slides").exists():
        sys.exit(
            f"No slides/ folder in {slide_dir} -- render each scene with build_slide.py first"
        )

    DEFAULT_OUT_DIR.mkdir(exist_ok=True)
    out_name = args.out or f"{slide_dir.name}.{args.to}"
    out_path = (DEFAULT_OUT_DIR / out_name).resolve()

    convert_cmd = [
        "manim-slides", "convert", *args.scenes, str(out_path),
        "--to", args.to, "--one-file",
    ]
    subprocess.run(convert_cmd, cwd=slide_dir, check=True)
    print(f"Combined presentation written to {out_path}")


if __name__ == "__main__":
    main()
