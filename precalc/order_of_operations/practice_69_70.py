from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.worked_example import WorkedExampleTemplate


class Practice69And70(Slide, WorkedExampleTemplate):
    """Problems 69 and 70: clearing parentheses with exponents inside."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.solve_69()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_70()

    def solve_69(self):
        self.show_label("69)")

        lines = [
            MathTex(r"20 - 12(36 \div {{3^2}} \div 2)"),
            MathTex(r"20 - 12({{36 \div 9}} \div 2)"),
            MathTex(r"20 - 12({{4 \div 2}})"),
            MathTex(r"20 - {{12 \cdot 2}}"),
            MathTex(r"{{20 - 24}}"),
            MathTex(r"-4"),
        ]
        targets = ["3^2", "36 \\div 9", "4 \\div 2", "12 \\cdot 2", "20 - 24", None]

        self.step_through(lines, targets)

    def solve_70(self):
        self.show_label("70)")

        lines = [
            MathTex(r"200 - 2^2({{6 \div \frac{1}{2} }}\cdot 4)"),
            MathTex(r"200 - 2^2({{12 \cdot 4}})"),
            MathTex(r"200 - {{2^2}} \cdot 48"),
            MathTex(r"200 - {{4 \cdot 48}}"),
            MathTex(r"{{200 - 192}}"),
            MathTex(r"8"),
        ]
        targets = [
            "6 \\div \\frac{1}{2}",
            "12 \\cdot 4",
            "2^2",
            "4 \\cdot 48",
            "200 - 192",
            None,
        ]

        self.step_through(lines, targets)
