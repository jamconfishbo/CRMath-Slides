from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.worked_example import WorkedExampleTemplate


class NestedAbsoluteValuePractice(Slide, WorkedExampleTemplate):
    """Problems 75 and 76: order of operations with nested absolute values."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.solve_75()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_76()

    def solve_75(self):
        self.show_label("75)")

        lines = [
            MathTex(r"9 - (6 + |{{|3-7|}} - 8|) \div \sqrt{25}"),
            MathTex(r"9 - (6 + |{{4 - 8}}|) \div \sqrt{25}"),
            MathTex(r"9 - (6 + {{|-4|}}) \div \sqrt{25}"),
            MathTex(r"9 - ({{6 + 4}}) \div \sqrt{25}"),
            MathTex(r"9 - 10 \div {{\sqrt{25} }}"),
            MathTex(r"9 - {{10 \div 5}}"),
            MathTex(r"{{9 - 2}}"),
            MathTex(r"7"),
        ]
        targets = [
            "|3-7|",
            "4 - 8",
            "|-4|",
            "6 + 4",
            "\\sqrt{25}",
            "10 \\div 5",
            "9 - 2",
            None,
        ]

        self.step_through(lines, targets)

    def solve_76(self):
        self.show_label("76)")

        lines = [
            MathTex(r"8 - 2(4 + |{{|2-5|}} - 5|) \div \sqrt{9}"),
            MathTex(r"8 - 2(4 + |{{3 - 5}}|) \div \sqrt{9}"),
            MathTex(r"8 - 2(4 + {{|-2|}}) \div \sqrt{9}"),
            MathTex(r"8 - 2({{4 + 2}}) \div \sqrt{9}"),
            MathTex(r"8 - 2 \cdot 6 \div {{\sqrt{9} }}"),
            MathTex(r"8 - {{2 \cdot 6}} \div 3"),
            MathTex(r"8 - {{12 \div 3}}"),
            MathTex(r"{{8 - 4}}"),
            MathTex(r"4"),
        ]
        targets = [
            "|2-5|",
            "3 - 5",
            "|-2|",
            "4 + 2",
            "\\sqrt{9}",
            "2 \\cdot 6",
            "12 \\div 3",
            "8 - 4",
            None,
        ]

        self.step_through(lines, targets)
