from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.mean_median import MeanMedianTemplate


class Q11Discussion(Slide, MeanMedianTemplate):
    """Q11: which average should the agent advertise to seem affordable?"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_question(
            r"\textbf{Q11)} To make the neighborhood in Q10 seem affordable "
            r"and typical, which average should the agent advertise? Why?"
        )

        self.show_answer_points([
            r"Median home price: \$220k --- Mean home price: \$672k",
            r"The agent should advertise the \textbf{median}.",
            r"It ignores the \$2.5 million mansion and reflects what a "
            r"typical home actually costs.",
        ])
