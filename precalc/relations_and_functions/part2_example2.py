from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class Example2(Slide, RelationsFunctionsTemplate):
    """I DO: Example 2a (not a function) and 2b (is a function)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_label("Example 2a (I DO)")
        pairs_a = [(3, 1), (2, 5), (-4, 2), (-1, 0), (3, -4)]
        self.function_check_pairs(pairs_a, repeat_indices=(0, 4))

        self.play(*[FadeOut(m) for m in self.mobjects])

        self.show_label("Example 2b (I DO)")
        pairs_b = [(-1, 4), (2, 3), (3, 4), (-4, 5)]
        self.function_check_pairs(pairs_b, repeat_indices=None)
