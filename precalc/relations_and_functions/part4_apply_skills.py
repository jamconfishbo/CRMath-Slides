from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class ApplySkills4(Slide, RelationsFunctionsTemplate):
    """YOU DO: #4a (mapping diagram), 4b and 4c (solve for y, absolute value / sqrt)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_label("Apply the Skills #4a (YOU DO)")
        self.mapping_diagram(
            domain_vals=[2, 3, 8],
            range_vals=[4],
            arrows=[(2, 4), (3, 4), (8, 4)],
            repeated_source=None,
        )
        self.play(*[FadeOut(m) for m in self.mobjects])

        self.show_label("Apply the Skills #4b (YOU DO)")
        lines_b = self.solve_for_y([
            r"|y+1| = x",
            r"y + 1 = {{\pm}} x",
            r"y = -1 {{\pm}} x",
        ])
        self.flag_plus_minus(lines_b[-1])
        self.play(*[FadeOut(m) for m in self.mobjects])

        self.show_label("Apply the Skills #4c (YOU DO)")
        lines_c = self.solve_for_y([
            r"x^2+y^2=25",
            r"y^2 = 25-x^2",
            r"y = {{\pm}}\sqrt{25-x^2}",
        ])
        self.flag_plus_minus(lines_c[-1])
