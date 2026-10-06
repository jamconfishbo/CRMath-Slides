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

        prompt = Text("Your turn -- write the relation, domain, and range!",
                       font_size=30, color=THEOREM_COLOR)
        prompt.next_to(table, DOWN, buff=0.8)
        self.play(FadeIn(prompt, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(prompt))

        self.build_ordered_pairs(cells_a, cells_b, anchor=DOWN * 0.3, max_width=10)
        self.build_set(x_vals, "Domain", X_COLOR, anchor=DOWN * 1.6)
        self.build_set(y_vals, "Range", Y_COLOR, anchor=DOWN * 2.7)
