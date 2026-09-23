from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, X_COLOR

VAR_COLOR = X_COLOR
SQUARE_COLOR = RED


class StepsOverview(Slide):
    """Steps for completing the square with decimal coefficients, plus the color legend."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Completing the Square (with Decimals)", font_size=42, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.next_slide()

        steps = VGroup(
            Text("1) Move terms so the equation reads  x² + bx = c", font_size=30),
            Text("2) If a > 1, divide every term by a (use decimals)", font_size=30),
            Text("3) Complete the square: add (b/2)² to both sides", font_size=30),
            Text("4) Factor the left side as a perfect square", font_size=30),
            Text("5) Square root both sides", font_size=30),
            Text("6) Solve for x -- give the answer as a decimal", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        steps.next_to(title, DOWN, buff=0.6)

        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.2) for s in steps], lag_ratio=0.25))
        self.next_slide()

        legend = VGroup(
            MathTex(r"x^2, \ x", color=VAR_COLOR, font_size=40),
            Text("variable terms", font_size=28),
            MathTex(r"(x - h)^2", color=SQUARE_COLOR, font_size=40),
            Text("completing-the-square terms", font_size=28),
        )
        row1 = VGroup(legend[0], legend[1]).arrange(RIGHT, buff=0.3)
        row2 = VGroup(legend[2], legend[3]).arrange(RIGHT, buff=0.3)
        legend_group = VGroup(row1, row2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend_group.next_to(steps, DOWN, buff=0.6)

        self.play(FadeIn(legend_group, shift=UP * 0.2))
        self.next_slide()
