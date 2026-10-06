from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class ApplySkills4(Slide, RelationsFunctionsTemplate):
    """YOU DO: #4a, 4b, 4c together -- mapping diagram, then two solve-for-y checks."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Apply the Skills #4 (YOU DO)")

        label_a = Text("a)", font_size=28, weight=BOLD).move_to(LEFT * 4.3 + UP * 2.6)
        label_b = Text("b)", font_size=26, weight=BOLD).move_to(RIGHT * 3.0 + UP * 3.3)
        label_c = Text("c)", font_size=26, weight=BOLD).move_to(RIGHT * 3.0 + UP * 0.0)
        self.play(FadeIn(label_a), FadeIn(label_b), FadeIn(label_c))

        self.mapping_diagram(
            domain_vals=[2, 3, 8],
            range_vals=[4],
            arrows=[(2, 4), (3, 4), (8, 4)],
            repeated_source=None,
            font_size=26, oval_width=1.4, gap=2.8, center=LEFT * 4.3 + DOWN * 0.2,
        )

        lines_b = self.solve_for_y([
            r"|y+1| = x",
            r"y + 1 = {{\pm}} x",
            r"y = -1 {{\pm}} x",
        ], font_size=24, anchor=RIGHT * 3.0 + UP * 2.7, line_buff=0.2)
        self.flag_plus_minus(lines_b[-1], note_font_size=20, note_buff=0.3)

        lines_c = self.solve_for_y([
            r"x^2+y^2=25",
            r"y^2 = 25-x^2",
            r"y = {{\pm}}\sqrt{25-x^2}",
        ], font_size=24, anchor=RIGHT * 3.0 + DOWN * 0.6, line_buff=0.2)
        self.flag_plus_minus(lines_c[-1], note_font_size=20, note_buff=0.3)
