#!/usr/bin/env python3
"""Render and preview a single slide file while workshopping it.

Usage:
    python build_slide.py <path/to/file.py> <SceneName> [-q l|m|h] [--present]

Examples:
    python build_slide.py precalc/order_of_operations/practice_69_70.py Practice69And70
    python build_slide.py precalc/order_of_operations/practice_69_70.py Practice69And70 --present
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Path to the scene file, relative to the repo root")
    parser.add_argument("scene", help="Name of the Scene class to render")
    parser.add_argument(
        "-q", "--quality", default="l", choices=["l", "m", "h", "p", "k"],
        help="Render quality (default: l, for fast iteration)",
    )
    parser.add_argument(
        "--present", action="store_true",
        help="After rendering, open manim-slides' interactive presenter for this scene",
    )
    args = parser.parse_args()

    scene_path = (REPO_ROOT / args.file).resolve()
    if not scene_path.exists():
        sys.exit(f"No such file: {scene_path}")

    slide_dir = scene_path.parent
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")

    render_cmd = [
        "manim-slides", "render", f"-q{args.quality}",
        scene_path.name, args.scene,
    ]
    subprocess.run(render_cmd, cwd=slide_dir, env=env, check=True)

    if args.present:
        present_cmd = ["manim-slides", "present", args.scene]
        subprocess.run(present_cmd, cwd=slide_dir, env=env, check=True)


if __name__ == "__main__":
    main()
