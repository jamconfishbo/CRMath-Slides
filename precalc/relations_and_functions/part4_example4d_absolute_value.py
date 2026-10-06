from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, THEOREM_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class Example4dAbsoluteValue(Slide, RelationsFunctionsTemplate):
    """I DO (NEW): Example 4d -- an absolute-value equation solved for y.
    Preps students for Apply the Skills #4b, which has the same structure."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Example 4d (I DO)")

        note = Text("Isolating absolute value also creates a plus/minus when you solve for y.",
                     font_size=26, color=THEOREM_COLOR)
        note.to_edge(UP, buff=1.1)
        self.play(FadeIn(note))
        self.next_slide()

        lines = self.solve_for_y([
            r"|y-1| = x",
            r"y - 1 = {{\pm}} x",
            r"y = 1 {{\pm}} x",
        ], anchor=UP * 0.6)
        self.flag_plus_minus(lines[-1])
