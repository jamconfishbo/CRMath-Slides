from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, THEOREM_COLOR
from templates.relations_functions import RelationsFunctionsTemplate, IS_FUNCTION_COLOR, NOT_FUNCTION_COLOR


class ApplySkills3(Slide, RelationsFunctionsTemplate):
    """YOU DO: #3a, 3b, 3c side by side -- sketch each, then apply the vertical line test."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Apply the Skills #3 (YOU DO)")

        instructions = Text(
            "Sketch each graph, then use the vertical line test. Determine if each is a function.",
            font_size=24, color=THEOREM_COLOR,
        )
        instructions.to_edge(UP, buff=1.0)
        self.play(FadeIn(instructions))
        self.next_slide()

        centers = [LEFT * 4.6 + DOWN * 0.3, DOWN * 0.3, RIGHT * 4.6 + DOWN * 0.3]
        sub_labels = ["a)", "b)", "c)"]

        axes_list = []
        for center, text in zip(centers, sub_labels):
            lbl = Text(text, font_size=28, weight=BOLD).move_to(center + UP * 2.1)
            self.play(FadeIn(lbl), run_time=0.3)
            axes = self.show_axes(x_range=(-3, 3, 1), y_range=(-3, 3, 1), length=3.0, center=center)
            axes_list.append(axes)
        self.next_slide()

        axes_a, axes_b, axes_c = axes_list

        # a) V-shape through the origin: IS a function
        left_ray = Line(axes_a.c2p(-2, 2), axes_a.c2p(0, 0), color=BLUE, stroke_width=4)
        right_ray = Line(axes_a.c2p(0, 0), axes_a.c2p(2, 2), color=BLUE, stroke_width=4)
        curve_a = VGroup(left_ray, right_ray)

        # b) parabola, vertex (-1, -1.5): IS a function
        pts_b = [(x, 0.5 * (x + 1) ** 2 - 1.5) for x in [-3, -2, -1, 0, 1, 2]]
        curve_b = self.rough_curve(axes_b, pts_b, color=BLUE)

        # c) two crossing lines (an "X"): NOT a function -- for x = 1.3, the
        # two lines give two different y's, marked with filled dots
        line1 = Line(axes_c.c2p(-2.5, -2.5), axes_c.c2p(2.5, 2.5), color=BLUE, stroke_width=4)
        line2 = Line(axes_c.c2p(-2.5, 2.5), axes_c.c2p(2.5, -2.5), color=BLUE, stroke_width=4)
        curve_c = VGroup(line1, line2)

        self.play(Create(curve_a), Create(curve_b), Create(curve_c))
        self.next_slide()

        vline_a = DashedLine(axes_a.c2p(-1, -3), axes_a.c2p(-1, 3), color=IS_FUNCTION_COLOR, stroke_width=3)
        vline_b = DashedLine(axes_b.c2p(1, -3), axes_b.c2p(1, 3), color=IS_FUNCTION_COLOR, stroke_width=3)
        vline_c = DashedLine(axes_c.c2p(1.3, -3), axes_c.c2p(1.3, 3), color=NOT_FUNCTION_COLOR, stroke_width=3)
        self.play(Create(vline_a), Create(vline_b), Create(vline_c))

        dot_c1 = self.endpoint_dot(axes_c, (1.3, 1.3), closed=True, color=NOT_FUNCTION_COLOR, radius=0.08)
        dot_c2 = self.endpoint_dot(axes_c, (1.3, -1.3), closed=True, color=NOT_FUNCTION_COLOR, radius=0.08)
        self.play(FadeIn(dot_c1), FadeIn(dot_c2))
        self.next_slide()

        verdict_a = self.verdict_text(True, font_size=22).next_to(axes_a, DOWN, buff=0.3)
        verdict_b = self.verdict_text(True, font_size=22).next_to(axes_b, DOWN, buff=0.3)
        verdict_c = self.verdict_text(False, font_size=22).next_to(axes_c, DOWN, buff=0.3)
        self.play(Write(verdict_a), Write(verdict_b), Write(verdict_c))
        self.next_slide()
