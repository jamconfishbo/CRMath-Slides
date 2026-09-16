from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q1GuidedExample(Slide, MeanMedianTemplate):
    """Q1: guided example -- test scores 15, 12, 100, 14, 18 (odd, one big outlier)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q1)} Guided Example --- unordered test scores: "
            r"15, 12, 100, 14, 18. Find the Mean and Median."
        )
        self.show_headers()

        self.mean_calc([r"\frac{15+12+100+14+18}{5}", r"\frac{159}{5}", "31.8"])

        self.median_calc(
            ["15", "12", "100", "14", "18"],
            ["12", "14", "15", "18", "100"],
        )
