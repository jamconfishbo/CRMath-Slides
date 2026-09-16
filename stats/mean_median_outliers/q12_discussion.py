from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q12Discussion(Slide, MeanMedianTemplate):
    """Q12: which average should the mayor show a luxury brand to seem wealthy?"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q12)} To convince a luxury brand the neighborhood in "
            r"Q10 is wealthy, which average should the mayor show? Why?"
        )

        self.show_answer_points([
            r"Median home price: \$220k --- Mean home price: \$672k",
            r"The mayor should show the \textbf{mean}.",
            r"It is inflated by the mansion, making the neighborhood look "
            r"wealthier than it typically is.",
        ])
