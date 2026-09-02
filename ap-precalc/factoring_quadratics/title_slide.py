from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class SolvingLinearEquationsTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Solving Linear Equations")
        self.next_slide()
