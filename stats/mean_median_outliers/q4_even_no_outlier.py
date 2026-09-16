from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q4EvenNoOutlier(Slide, MeanMedianTemplate):
    """Q4: even data set, no outlier -- 42, 38, 45, 40, 35, 46."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q4)} Even data set, no outlier: 42, 38, 45, 40, 35, 46. "
            r"Find the Mean and Median."
        )
        self.show_headers()

        self.mean_calc([r"\frac{42+38+45+40+35+46}{6}", r"\frac{246}{6}", "41"])

        self.median_calc(
            ["42", "38", "45", "40", "35", "46"],
            ["35", "38", "40", "42", "45", "46"],
        )
