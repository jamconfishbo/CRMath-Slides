from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q10RealEstate(Slide, MeanMedianTemplate):
    """Q10: manipulating perception -- home prices (in $1000s) with one mansion."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q10)} Home prices (in \$1000s): 200, 210, 220, 230, and "
            r"a mansion at 2500. Find the Mean and Median."
        )
        self.show_headers()

        self.mean_calc([r"\frac{200+210+220+230+2500}{5}", r"\frac{3360}{5}", "672"])

        self.median_calc(
            ["200", "210", "220", "230", "2500"],
            ["200", "210", "220", "230", "2500"],
        )
