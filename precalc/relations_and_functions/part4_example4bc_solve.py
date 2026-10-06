from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class Example4bc(Slide, RelationsFunctionsTemplate):
    """I DO: Example 4b and 4c -- solve for y line by line, then flag the +/-."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_label("Example 4b (I DO)")
        lines_b = self.solve_for_y([
            r"y^2 = x",
            r"y = {{\pm}}\sqrt{x}",
        ])
        self.flag_plus_minus(lines_b[-1])

        self.play(*[FadeOut(m) for m in self.mobjects])

        self.show_label("Example 4c (I DO)")

        original = MathTex(r"{{(x-2)^2}}+(y+1)^2={{9}}", font_size=36)
        original.move_to(UP * 2.4)
        self.play(Write(original))
        self.next_slide()

        term_left = original.get_part_by_tex("(x-2)^2", substring=False)
        term_right = original.get_part_by_tex("9", substring=False)

        # subtract (x-2)^2 from both sides, in red
        inv_left = MathTex(r"-(x-2)^2", color=RED, font_size=36).next_to(term_left, DOWN, buff=0.3)
        inv_right = MathTex(r"-(x-2)^2", color=RED, font_size=36).next_to(term_right, DOWN, buff=0.3)
        self.play(Write(inv_left), Write(inv_right))
        self.next_slide()

        # strike the canceling pair on the left -- stays on screen, not removed
        cancel_group = VGroup(term_left, inv_left)
        strike = Line(
            cancel_group.get_corner(UL) + UP * 0.08 + LEFT * 0.08,
            cancel_group.get_corner(DR) + DOWN * 0.08 + RIGHT * 0.08,
            color=RED, stroke_width=5,
        )
        self.play(Create(strike))
        self.next_slide()

        line2 = MathTex(r"(y+1)^2=9-(x-2)^2", font_size=36)
        line2.next_to(VGroup(original, inv_left, inv_right), DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(line2))
        self.next_slide()

        lines_c = self.solve_for_y([
            r"y+1={{\pm}}\sqrt{9-(x-2)^2}",
            r"y=-1{{\pm}}\sqrt{9-(x-2)^2}",
        ], font_size=36, start_after=line2, line_buff=0.5)
        self.flag_plus_minus(lines_c[-1])
