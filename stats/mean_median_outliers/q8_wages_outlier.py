from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q8WagesOutlier(Slide, MeanMedianTemplate):
    """Q8: owner adds his own $80/hr wage to Q7's data set (now even, n=8)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q8)} The owner pays himself \$80/hr. Add it to Q7's "
            r"data set. Find the new Mean and Median."
        )
        self.show_headers()

        self.mean_calc([r"\frac{14+15+14+16+16+15+15+80}{8}", r"\frac{185}{8}", "23.125"])

        self.median_calc(
            ["14", "15", "14", "16", "16", "15", "15", "80"],
            ["14", "14", "15", "15", "15", "16", "16", "80"],
        )
