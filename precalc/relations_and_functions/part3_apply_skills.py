from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, THEOREM_COLOR
from templates.relations_functions import RelationsFunctionsTemplate, IS_FUNCTION_COLOR


class ApplySkills3(Slide, RelationsFunctionsTemplate):
    """YOU DO: #3a, 3b, 3c -- sketch each graph, then check with the vertical line test."""

    def prompt_sketch(self, axes):
        prompt = Text("Sketch this, then try the vertical line test!", font_size=28, color=THEOREM_COLOR)
        prompt.next_to(axes, DOWN, buff=0.5)
        self.play(FadeIn(prompt, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(prompt))

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # --- a) V-shape through the origin: IS a function ---
        self.show_label("Apply the Skills #3a (YOU DO)")
        axes_a = self.show_axes(x_range=(-5, 5, 1), y_range=(-1, 5, 1), length=5.0, center=LEFT * 0.3 + UP * 0.3)
        left_ray = Line(axes_a.c2p(-4, 4), axes_a.c2p(0, 0), color=BLUE, stroke_width=4)
        right_ray = Line(axes_a.c2p(0, 0), axes_a.c2p(4, 4), color=BLUE, stroke_width=4)
        curve_a = VGroup(left_ray, right_ray)
        self.prompt_sketch(axes_a)
        self.vertical_line_test(axes_a, curve_a, test_lines=[(-2, IS_FUNCTION_COLOR)], passes=True,
                                 y_bottom=-1, y_top=5)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # --- b) parabola, vertex (-1, -3): IS a function ---
        self.show_label("Apply the Skills #3b (YOU DO)")
        axes_b = self.show_axes(x_range=(-5, 5, 1), y_range=(-4, 6, 2), length=5.0, center=LEFT * 0.3)
        pts_b = [(x, (x + 1) ** 2 - 3) for x in [-4, -3, -2, -1, 0, 1, 2]]
        curve_b = self.rough_curve(axes_b, pts_b, color=BLUE)
        self.prompt_sketch(axes_b)
        self.vertical_line_test(axes_b, curve_b, test_lines=[(2, IS_FUNCTION_COLOR)], passes=True,
                                 y_bottom=-4, y_top=6)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # --- c) two disjoint rays: IS a function ---
        self.show_label("Apply the Skills #3c (YOU DO)")
        axes_c = self.show_axes(x_range=(-5, 5, 1), y_range=(-5, 5, 1), length=5.0, center=LEFT * 0.3)
        piece1 = self.rough_curve(axes_c, [(-5, 5), (-3, 3)], color=BLUE)
        dot1 = self.endpoint_dot(axes_c, (-3, 3), closed=True, color=BLUE)
        piece2 = self.rough_curve(axes_c, [(-2, 1), (4, -5)], color=BLUE)
        dot2 = self.endpoint_dot(axes_c, (-2, 1), closed=False, color=BLUE)
        curve_c = VGroup(piece1, dot1, piece2, dot2)
        self.prompt_sketch(axes_c)
        self.vertical_line_test(axes_c, curve_c, test_lines=[(1, IS_FUNCTION_COLOR)], passes=True,
                                 y_bottom=-5, y_top=5)
