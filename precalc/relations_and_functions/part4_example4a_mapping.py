from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, THEOREM_COLOR
from templates.relations_functions import RelationsFunctionsTemplate, NOT_FUNCTION_COLOR, IS_FUNCTION_COLOR


class Example4aMapping(Slide, RelationsFunctionsTemplate):
    """I DO: Example 4a -- mapping diagrams. Rule: every input needs exactly one arrow out.
    Shown side by side: a non-example (one input, two arrows), and an example where
    two different inputs share the same output -- which is still fine."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Example 4a (I DO)")

        note = Text("Rule: every input needs exactly ONE arrow out.", font_size=26)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note))

        left_header = Text("NOT a function:", font_size=26, color=NOT_FUNCTION_COLOR, weight=BOLD)
        left_header.move_to(LEFT * 3.5 + UP * 2.6)
        right_header = Text("Still a function:", font_size=26, color=IS_FUNCTION_COLOR, weight=BOLD)
        right_header.move_to(RIGHT * 3.5 + UP * 2.6)
        self.play(FadeIn(left_header), FadeIn(right_header))

        self.mapping_diagram(
            domain_vals=[1, 3, 5],
            range_vals=[2, 4],
            arrows=[(1, 2), (3, 2), (3, 4), (5, 4)],
            repeated_source=3,
            font_size=26, oval_width=1.5, gap=3.0, center=LEFT * 3.5 + DOWN * 0.3,
        )

        two_inputs_note = Text("two inputs, one output -- OK!", font_size=20, color=THEOREM_COLOR)
        two_inputs_note.move_to(RIGHT * 3.5 + UP * 1.95)

        self.mapping_diagram(
            domain_vals=[1, 2, 3],
            range_vals=[5, 6],
            arrows=[(1, 5), (2, 5), (3, 6)],
            repeated_source=None,
            font_size=26, oval_width=1.5, gap=3.0, center=RIGHT * 3.5 + DOWN * 0.3,
        )
        self.play(FadeIn(two_inputs_note))
        self.next_slide()
