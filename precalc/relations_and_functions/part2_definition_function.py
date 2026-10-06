from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, X_COLOR, Y_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class DefinitionOfAFunction(Slide, RelationsFunctionsTemplate):
    """Full definition, then the soundbite students write down."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        line1 = Text(
            "Given a relation in x and y, we call y a function of x",
            font_size=26,
        )
        line2 = Text(
            "if every x-value in the domain has exactly one y-value in the range.",
            font_size=26, t2c={"x-value": X_COLOR, "y-value": Y_COLOR},
        )

        self.show_notes("Definition of a Function", [line1, line2])
        self.play(*[FadeOut(m) for m in self.mobjects])

        self.write_soundbite("A function is a relation where every input has only one output.")
