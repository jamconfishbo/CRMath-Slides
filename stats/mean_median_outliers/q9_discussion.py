from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q9Discussion(Slide, MeanMedianTemplate):
    """Q9: compare Q7 and Q8 -- which measure resisted the owner's extreme wage?"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q9)} Compare Q7 and Q8 --- which measure of center was "
            r"more resistant to the owner's extreme wage?"
        )

        self.show_answer_points([
            r"Mean: $15 \to 23.125$ --- jumped by $8.125$",
            r"Median: $15 \to 15$ --- did not change at all",
            r"\textbf{The median completely resisted the owner's extreme wage.}",
        ])
