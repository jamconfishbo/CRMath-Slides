from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q5SmallOutlier(Slide, MeanMedianTemplate):
    """Q5: add the small outlier 5 to Q4's data set (now odd, n=7)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q5)} Add the small outlier 5 to Q4's data set: "
            r"42, 38, 45, 40, 35, 46, 5. Find the new Mean and Median."
        )
        self.show_headers()

        self.mean_calc([r"\frac{42+38+45+40+35+46+5}{7}", r"\frac{251}{7}", r"\approx 35.86"])

        self.median_calc(
            ["42", "38", "45", "40", "35", "46", "5"],
            ["5", "35", "38", "40", "42", "45", "46"],
        )
