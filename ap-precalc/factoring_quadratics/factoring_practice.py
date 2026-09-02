from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR


class FactoringPracticeList(Slide):
    """Practice problems: solve each quadratic by factoring."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Practice: Solve by Factoring", font_size=44, weight=BOLD)
        title.to_edge(UP, buff=0.6)

        label_a = MathTex(r"\textbf{a)}", font_size=40)
        prob_a = MathTex(r"8x^2 + 21 = -59x", font_size=40)
        group_a = VGroup(label_a, prob_a).arrange(RIGHT, buff=0.5)

        label_b = MathTex(r"\textbf{b)}", font_size=40)
        prob_b = MathTex(r"35k^2 - 22k + 7 = 4", font_size=40)
        group_b = VGroup(label_b, prob_b).arrange(RIGHT, buff=0.5)

        label_c = MathTex(r"\textbf{c)}", font_size=40)
        prob_c = MathTex(r"6b^2 - 13b + 3 = -3", font_size=40)
        group_c = VGroup(label_c, prob_c).arrange(RIGHT, buff=0.5)

        label_d = MathTex(r"\textbf{d)}", font_size=40)
        prob_d = MathTex(r"3r^2 - 16r - 7 = 5", font_size=40)
        group_d = VGroup(label_d, prob_d).arrange(RIGHT, buff=0.5)

        problems_group = VGroup(group_a, group_b, group_c, group_d)
        problems_group.arrange(DOWN, buff=0.9, aligned_edge=LEFT)
        problems_group.move_to(ORIGIN)

        self.play(FadeIn(title, shift=UP))
        self.play(LaggedStart(*[FadeIn(g, shift=UP * 0.2) for g in problems_group], lag_ratio=0.3))
        self.next_slide()
