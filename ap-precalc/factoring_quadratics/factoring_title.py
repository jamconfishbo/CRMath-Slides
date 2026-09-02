from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class FactoringTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Factoring Quadratics")
        self.next_slide()
