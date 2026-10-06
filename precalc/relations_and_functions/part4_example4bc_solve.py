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
        lines_c = self.solve_for_y([
            r"(x-2)^2+(y+1)^2=9",
            r"(y+1)^2=9-(x-2)^2",
            r"y+1={{\pm}}\sqrt{9-(x-2)^2}",
            r"y=-1{{\pm}}\sqrt{9-(x-2)^2}",
        ])
        self.flag_plus_minus(lines_c[-1])
