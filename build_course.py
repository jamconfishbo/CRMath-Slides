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

# Reveal hides the old clip the moment a slide changes, before the new clip has
# painted, so the screen flashes dark. A restarted clip can also show its old
# last frame until the rewind lands. Cover the deck with a still of the outgoing
# frame until the new clip has painted a frame from its start.
STEADY_PLAYBACK = """
<style>
  #steady-frame {
    position: absolute; inset: 0; width: 100%; height: 100%; z-index: 10;
    object-fit: contain; display: none;
  }
</style>
<script>
  (function () {
    var still = document.createElement("canvas");
    still.id = "steady-frame";
    document.querySelector(".reveal .backgrounds").appendChild(still);
    var change = 0;

    function videoOf(slide) {
      var background = slide && Reveal.getSlideBackground(slide);
      return background && background.querySelector("video");
    }

    Reveal.on("slidechanged", function (event) {
      var thisChange = ++change;
      var outgoing = videoOf(event.previousSlide);
      var incoming = videoOf(event.currentSlide);
      if (outgoing && outgoing.readyState >= 2) {
        still.width = outgoing.videoWidth;
        still.height = outgoing.videoHeight;
        still.getContext("2d").drawImage(outgoing, 0, 0);
        still.style.display = "block";
      }
      if (!incoming) { still.style.display = "none"; return; }

      function reveal() {
        if (thisChange === change) still.style.display = "none";
      }
      setTimeout(reveal, 1500);
      if (incoming.requestVideoFrameCallback) {
        incoming.requestVideoFrameCallback(function check(now, frame) {
          if (thisChange !== change) return;
          if (frame.mediaTime < 0.25) {
            requestAnimationFrame(function () { requestAnimationFrame(reveal); });
          } else {
            incoming.requestVideoFrameCallback(check);
          }
        });
      } else {
        incoming.addEventListener("playing", reveal, { once: true });
      }
    });
  })();
</script>
"""


def add_steady_playback(html_path):
    html = html_path.read_text()
    html_path.write_text(html.replace("</body>", STEADY_PLAYBACK + "</body>", 1))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slide_dir", help="Directory containing the rendered scenes' slides/ folder")
    parser.add_argument("scenes", nargs="+", help="Scene names, in the order they should play")
    parser.add_argument("--out", default=None, help="Output filename (default: <slide_dir name>.html)")
    parser.add_argument(
        "--to", default="html", help="Output format passed to manim-slides convert (default: html)"
    )
    parser.add_argument(
        "--split", action="store_true",
        help="Write the videos to a <name>_assets/ folder beside the page instead of embedding "
             "them in one file (needed once a deck passes GitHub's 100 MB file limit, e.g. HD renders)",
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
        "--to", args.to,
    ]
    if not args.split:
        convert_cmd.append("--one-file")
    subprocess.run(convert_cmd, cwd=slide_dir, check=True)
    if args.to == "html":
        add_steady_playback(out_path)
    print(f"Combined presentation written to {out_path}")


if __name__ == "__main__":
    main()
