from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, THEOREM_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class ApplySkills2(Slide, RelationsFunctionsTemplate):
    """YOU DO: #2a and 2b side by side -- both shown first, then both answers revealed."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Apply the Skills #2 (YOU DO)")

        instructions = Text(
            "Determine if each relation is a function. Explain why.",
            font_size=28, color=THEOREM_COLOR,
        )
        instructions.to_edge(UP, buff=1.0)
        self.play(FadeIn(instructions))
        self.next_slide()

        label_a = Text("a)", font_size=32, weight=BOLD).move_to(LEFT * 3.4 + UP * 1.9)
        label_b = Text("b)", font_size=32, weight=BOLD).move_to(RIGHT * 3.4 + UP * 1.9)
        self.play(FadeIn(label_a), FadeIn(label_b))

        pairs_a = [(8, 4), (3, -1), (5, 4)]
        pairs_b = [(-3, 2), (9, 5), (1, 0), (-3, 1)]

        relation_a, pair_mobs_a = self.write_relation_pairs(
            pairs_a, font_size=28, anchor=LEFT * 3.4 + UP * 1.1, max_width=5.8, pause=False,
        )
        relation_b, pair_mobs_b = self.write_relation_pairs(
            pairs_b, font_size=28, anchor=RIGHT * 3.4 + UP * 1.1, max_width=5.8, pause=False,
        )
        self.next_slide()

        self.reveal_function_verdict(relation_a, pair_mobs_a, repeat_indices=None)
        self.reveal_function_verdict(relation_b, pair_mobs_b, repeat_indices=(0, 3))
