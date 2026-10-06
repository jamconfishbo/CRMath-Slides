from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class Example4aMapping(Slide, RelationsFunctionsTemplate):
    """I DO: Example 4a -- mapping diagram. Rule: every input needs exactly one arrow out."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Example 4a (I DO)")

        note = Text("Rule: every input needs exactly ONE arrow out.", font_size=26)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))

        self.mapping_diagram(
            domain_vals=[1, 3, 5],
            range_vals=[2, 4],
            arrows=[(1, 2), (3, 2), (3, 4), (5, 4)],
            repeated_source=3,
        )
