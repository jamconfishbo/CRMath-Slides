from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, X_COLOR, Y_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class DefinitionOfARelation(Slide, RelationsFunctionsTemplate):
    """Notes: definition of a relation, domain, and range."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        line1 = Text(
            "A set of ordered pairs (x, y) is called a relation.",
            font_size=28, t2c={"x": X_COLOR, "y": Y_COLOR},
        )
        line2 = Text(
            "The x-values are the domain.",
            font_size=28, t2c={"x": X_COLOR, "domain": X_COLOR},
        )
        line3 = Text(
            "The y-values are the range.",
            font_size=28, t2c={"y": Y_COLOR, "range": Y_COLOR},
        )

        self.show_notes("Definition of a Relation", [line1, line2, line3])
