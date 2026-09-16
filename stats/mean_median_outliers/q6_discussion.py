from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q6Discussion(Slide, MeanMedianTemplate):
    """Q6: compare Q4 and Q5 -- how did the small outlier pull the mean vs. median?"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q6)} Compare Q4 and Q5 --- how did the small outlier "
            r"pull the mean compared to the median?"
        )

        self.show_answer_points([
            r"Mean: $41 \to 35.86$ --- dropped by about $5.14$",
            r"Median: $41 \to 40$ --- dropped by only $1$",
            r"\textbf{Even a small outlier pulls the mean more than the median.}",
        ])
