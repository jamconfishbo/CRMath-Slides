from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate, IS_FUNCTION_COLOR, NOT_FUNCTION_COLOR


class VerticalLineTest(Slide, RelationsFunctionsTemplate):
    """I DO: Example 3a, 3b, 3c -- sketch the graph, then apply the vertical line test."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # --- a) wiggly curve: IS a function ---
        self.show_label("Example 3a (I DO)")
        axes_a = self.show_axes(x_range=(-5, 5, 1), y_range=(-6, 6, 2), length=5.0, center=LEFT * 0.3)
        curve_a = self.rough_curve(
            axes_a,
            [(-5, -5), (-3.2, 3), (-1.5, -1), (0, -3), (1.5, 0.5), (3, 5), (4.2, 6)],
            color=BLUE,
        )
        self.vertical_line_test(
            axes_a, curve_a,
            test_lines=[(-3, IS_FUNCTION_COLOR), (1.5, IS_FUNCTION_COLOR)],
            passes=True, y_bottom=-6, y_top=6,
        )
        self.play(*[FadeOut(m) for m in self.mobjects])

        # --- b) sideways parabola: NOT a function ---
        self.show_label("Example 3b (I DO)")
        axes_b = self.show_axes(x_range=(-5, 5, 1), y_range=(-4, 4, 2), length=5.0, center=LEFT * 0.3)
        pts_b = [(-3 + 0.5 * y * y, y) for y in [-3, -2, -1, 0, 1, 2, 3]]
        curve_b = self.rough_curve(axes_b, pts_b, color=BLUE)
        self.vertical_line_test(
            axes_b, curve_b,
            test_lines=[(-1, NOT_FUNCTION_COLOR)],
            passes=False, y_bottom=-4, y_top=4,
        )
        self.play(*[FadeOut(m) for m in self.mobjects])

        # --- c) jump piecewise: IS a function ---
        self.show_label("Example 3c (I DO)")
        axes_c = self.show_axes(x_range=(-5, 5, 1), y_range=(-4, 6, 2), length=5.0, center=LEFT * 0.3)
        piece1 = self.rough_curve(axes_c, [(-5, 4), (-2, 4), (1, 4)], color=BLUE)
        dot1 = self.endpoint_dot(axes_c, (1, 4), closed=True, color=BLUE)
        piece2 = self.rough_curve(axes_c, [(1, 2), (3, 0), (5, -2)], color=BLUE)
        dot2 = self.endpoint_dot(axes_c, (1, 2), closed=False, color=BLUE)
        curve_c = VGroup(piece1, dot1, piece2, dot2)
        self.vertical_line_test(
            axes_c, curve_c,
            test_lines=[(-2, IS_FUNCTION_COLOR), (3, IS_FUNCTION_COLOR)],
            passes=True, y_bottom=-4, y_top=6,
        )
