from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.title_slide import TitleSlideTemplate
from templates.summary import SummaryTemplate


class FunctionTransformationsTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Function Transformations", "Translations, Stretches & Shrinks, Reflections")
        self.next_slide()


class TransformationsDefinition(Slide, SummaryTemplate):
    """Notes: what a function transformation is."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_definition(
            "Function Transformations",
            [
                r"\textbf{Function transformations} are operations that modify",
                r"a parent function $f(x)$ by \textbf{translating},",
                r"\textbf{stretching/shrinking}, or \textbf{reflecting} it.",
            ],
        )
