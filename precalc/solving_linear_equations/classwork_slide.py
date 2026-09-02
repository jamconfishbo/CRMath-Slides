from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, THEOREM_COLOR


class ClassworkSlide(Slide):
    """Final slide: classwork assignment."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Classwork", font_size=56, weight=BOLD)

        assignment = Text(
            "Page R94  #9-12 and #23-26",
            font_size=44,
            color=THEOREM_COLOR,
        )
        assignment.next_to(title, DOWN, buff=0.7)

        group = VGroup(title, assignment).move_to(ORIGIN)

        self.play(Write(title))
        self.play(FadeIn(assignment, shift=UP * 0.3))
        self.next_slide()
