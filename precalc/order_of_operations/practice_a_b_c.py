from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.worked_example import WorkedExampleTemplate


class PracticeProblems(Slide, WorkedExampleTemplate):
    """Problems a, b, and c: order of operations and clearing parentheses."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.solve_a()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_b()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
        
        self.solve_c()

    def solve_a(self):
        self.show_label("a)")

        lines = [
            MathTex(r"30 - 24 \div ({{4^2}} \div 2^2 \cdot 3)"),
            MathTex(r"30 - 24 \div (16 \div {{2^2}} \cdot 3)"),
            MathTex(r"30 - 24 \div ({{16 \div 4}} \cdot 3)"),
            MathTex(r"30 - 24 \div ({{4 \cdot 3}})"),
            MathTex(r"30 - {{24 \div 12}}"),
            MathTex(r"{{30 - 2}}"),
            MathTex(r"28"),
        ]
        targets = [
            "4^2",
            "2^2",
            "16 \\div 4",
            "4 \\cdot 3",
            "24 \\div 12",
            "30 - 2",
            None,
        ]

        self.step_through(lines, targets)

    def solve_b(self):
        self.show_label("b)")

        # Using standard brackets [ ] instead of \left[ \right] for cleaner MathTex parsing
        lines = [
            MathTex(r"15 - [-4 + 2[({{2-5}})^2 - 4]]"),
            MathTex(r"15 - [-4 + 2[{{(-3)^2}} - 4]]"),
            MathTex(r"15 - [-4 + 2[{{9 - 4}}]]"),
            MathTex(r"15 - [-4 + {{2(5)}}]"),
            MathTex(r"15 - [{{-4 + 10}}]"),
            MathTex(r"{{15 - 6}}"),
            MathTex(r"9"),
        ]
        targets = [
            "2-5",
            "(-3)^2",
            "9 - 4",
            "2(5)",
            "-4 + 10",
            "15 - 6",
            None,
        ]

        self.step_through(lines, targets)

    def solve_c(self):
        self.show_label("c)")

        lines = [
            MathTex(r"12 - [{{3(2y+5)}} - 4(y-3)] - 5"),
            MathTex(r"12 - [6y + 15 {{ - 4(y-3)}}] - 5"),
            MathTex(r"12 - [{{6y + 15 - 4y + 12}}] - 5"),
            MathTex(r"12 - {{[2y + 27]}} - 5"),
            MathTex(r"{{12 - 2y - 27 - 5}}"),
            MathTex(r"-2y - 20"),
        ]
        targets = [
            "3(2y+5)",
            " - 4(y-3)",
            "6y + 15 - 4y + 12",
            "[2y + 27]",
            "12 - 2y - 27 - 5",
            None,
        ]

        self.step_through(lines, targets)