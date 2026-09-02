from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, INDICATE_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = GREEN
FILL_COLOR = BLUE


class FactorYSquared9Y14(Slide, DistributionTemplate):
    """Factor y^2 - 9y + 14."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Factor:")

        expr = MathTex(r"{{y}}^2 - 9{{y}} + 14", font_size=64)
        for part in expr.get_parts_by_tex("y", substring=False):
            part.set_color(VAR_COLOR)
        expr.move_to(UP * 2.7)
        self.play(Write(expr))
        self.next_slide()

        template = MathTex(r"({{y}}+\rule{0.4cm}{0.5pt})({{y}}+\rule{0.4cm}{0.5pt})", font_size=64)
        for part in template.get_parts_by_tex("y", substring=False):
            part.set_color(VAR_COLOR)
        template.next_to(expr, DOWN, buff=0.9)
        self.play(Write(template))
        self.next_slide()

        candidates = VGroup(
            MathTex(r"-1 \cdot -14 = 14 \qquad -1+(-14) = -15", font_size=40),
            MathTex(r"-2 \cdot -7 = 14 \qquad -2+(-7) = -9", font_size=40),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        candidates.next_to(template, DOWN, buff=0.8)

        for row in candidates:
            self.play(Write(row))
            self.next_slide()

        self.play(Circumscribe(candidates[1], color=INDICATE_COLOR))
        self.next_slide()

        self.play(FadeOut(candidates))

        filled = MathTex(r"({{y}}{{-2}})({{y}}{{-7}})", font_size=64)
        for part in filled.get_parts_by_tex("y", substring=False):
            part.set_color(VAR_COLOR)
        filled.get_part_by_tex("-2", substring=False).set_color(FILL_COLOR)
        filled.get_part_by_tex("-7", substring=False).set_color(FILL_COLOR)
        filled.move_to(template.get_center())

        self.play(TransformMatchingTex(template, filled))
        self.next_slide()

        self.box_final(filled)
