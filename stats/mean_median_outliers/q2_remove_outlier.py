from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q2RemoveOutlier(Slide, MeanMedianTemplate):
    """Q2: remove the outlier (100) from Q1 -- 15, 12, 14, 18 (even, no outlier)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q2)} Remove the outlier, 100, from Q1's data set: "
            r"15, 12, 14, 18. Recalculate the Mean and Median."
        )
        self.show_headers()

        self.mean_calc([r"\frac{15+12+14+18}{4}", r"\frac{59}{4}", "14.75"])

        self.median_calc(
            ["15", "12", "14", "18"],
            ["12", "14", "15", "18"],
        )
