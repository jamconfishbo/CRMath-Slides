from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class ApplySkills2(Slide, RelationsFunctionsTemplate):
    """YOU DO: #2a (is a function) and 2b (not a function)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_label("Apply the Skills #2a (YOU DO)")
        pairs_a = [(8, 4), (3, -1), (5, 4)]
        self.function_check_pairs(pairs_a, repeat_indices=None)

        self.play(*[FadeOut(m) for m in self.mobjects])

        self.show_label("Apply the Skills #2b (YOU DO)")
        pairs_b = [(-3, 2), (9, 5), (1, 0), (-3, 1)]
        self.function_check_pairs(pairs_b, repeat_indices=(0, 3))
