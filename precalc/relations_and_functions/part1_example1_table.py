from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, X_COLOR, Y_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class Example1Table(Slide, RelationsFunctionsTemplate):
    """I DO: Table 1-1 (hours studied -> test score) -> relation -> domain/range."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Example 1 (I DO)")

        x_vals = [8, 3, 11, 5, 8]
        y_vals = [92, 58, 98, 72, 86]

        cells_a, cells_b, table = self.two_column_table(
            "x", "y", x_vals, y_vals, col_width=1.6, row_height=0.6, center=LEFT * 3.4,
        )

        self.build_ordered_pairs(
            cells_a, cells_b, anchor=RIGHT * 2.1 + UP * 2.2, max_width=6.6,
        )

        self.build_set(x_vals, "Domain", X_COLOR, anchor=RIGHT * 2.1 + DOWN * 0.3)
        self.build_set(y_vals, "Range", Y_COLOR, anchor=RIGHT * 2.1 + DOWN * 1.8)
