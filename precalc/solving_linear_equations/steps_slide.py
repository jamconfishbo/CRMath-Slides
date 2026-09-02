from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR

NO_SOLUTION_COLOR = RED
INFINITE_COLOR = BLUE


class SolvingStepsList(Slide):
    """Steps for solving a linear equation, then the three possible outcomes."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Solving Linear Equations", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        steps = VGroup(
            Text("1) Distribute and combine like terms", font_size=32),
            Text(
                "2) Get variables on one side and constants on the other\n"
                "    (add or subtract)",
                font_size=32,
                line_spacing=1.2,
            ),
            Text(
                "3) Apply the multiplicative inverse so the coefficient\n"
                "    of the variable is 1",
                font_size=32,
                line_spacing=1.2,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        steps.next_to(title, DOWN, buff=0.9)

        self.play(Write(title))
        self.play(LaggedStart(*[FadeIn(step, shift=UP * 0.2) for step in steps], lag_ratio=0.3))
        self.next_slide()

        self.play(FadeOut(steps))

        subtitle = Text("How Many Solutions?", font_size=40, weight=BOLD)
        subtitle.next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(subtitle))

        row1 = VGroup(
            MathTex(r"x = \#", font_size=44),
            Text("one solution", font_size=32, color=ANSWER_COLOR),
        ).arrange(RIGHT, buff=0.8)

        row2 = VGroup(
            MathTex(r"3 = 5", font_size=44),
            Text("contradiction  →  no solution", font_size=32, color=NO_SOLUTION_COLOR),
        ).arrange(RIGHT, buff=0.8)

        row3 = VGroup(
            MathTex(r"3 = 3", font_size=44),
            Text("identity  →  infinitely many solutions", font_size=32, color=INFINITE_COLOR),
        ).arrange(RIGHT, buff=0.8)

        rows = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        rows.next_to(subtitle, DOWN, buff=0.9)

        self.play(LaggedStart(*[FadeIn(row, shift=UP * 0.2) for row in rows], lag_ratio=0.3))
        self.next_slide()
