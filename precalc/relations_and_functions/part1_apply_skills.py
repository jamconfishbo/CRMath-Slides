from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, X_COLOR, Y_COLOR, THEOREM_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class ApplySkills1(Slide, RelationsFunctionsTemplate):
    """YOU DO: #1, the sideways table -- relation, domain, range."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Apply the Skills #1 (YOU DO)")

        x_vals = [3, -2, 5, 1]
        y_vals = [-4, 0, 3, 0]

        cells_a, cells_b, table = self.two_row_table(
            "x", "y", x_vals, y_vals, center=UP * 1.8,
        )

        instructions = VGroup(
            Text("a) Write the set of ordered pairs that defines the relation.", font_size=26),
            Text("b) Write the domain.", font_size=26),
            Text("c) Write the range.", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        instructions.set_color(THEOREM_COLOR)
        instructions.next_to(table, DOWN, buff=0.7)
        self.play(FadeIn(instructions, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(instructions))

        self.build_ordered_pairs(cells_a, cells_b, anchor=DOWN * 0.3, max_width=10)
        self.build_set(x_vals, "Domain", X_COLOR, anchor=DOWN * 1.6)
        self.build_set(y_vals, "Range", Y_COLOR, anchor=DOWN * 2.7)
