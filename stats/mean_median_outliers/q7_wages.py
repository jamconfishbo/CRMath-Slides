from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q7Wages(Slide, MeanMedianTemplate):
    """Q7: odd data set, no outlier -- hourly wages 14, 15, 14, 16, 16, 15, 15."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q7)} Odd data set, no outlier --- hourly wages (\$): "
            r"14, 15, 14, 16, 16, 15, 15. Find the Mean and Median."
        )
        self.show_headers()

        self.mean_calc([r"\frac{14+15+14+16+16+15+15}{7}", r"\frac{105}{7}", "15"])

        self.median_calc(
            ["14", "15", "14", "16", "16", "15", "15"],
            ["14", "14", "15", "15", "15", "16", "16"],
        )
