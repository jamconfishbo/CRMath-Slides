from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q3Discussion(Slide, MeanMedianTemplate):
    """Q3: how did removing the outlier affect the mean vs. the median?"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q3)} How did removing the outlier impact the mean and "
            r"median? Which measure changed more?"
        )

        self.show_answer_points([
            r"Mean: $31.8 \to 14.75$ --- dropped by $17.05$",
            r"Median: $15 \to 14.5$ --- dropped by only $0.5$",
            r"\textbf{The mean changed far more than the median.}",
        ])
