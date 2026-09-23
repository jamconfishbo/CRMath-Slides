from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class CompletingSquareTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Completing the Square", "Decimal Coefficients & Calculator Practice", title_font_size=48)
        self.next_slide()
