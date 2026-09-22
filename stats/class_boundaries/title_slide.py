from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class ClassBoundariesTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Frequency Distributions", "Class Limits & Class Boundaries", title_font_size=46)
        self.next_slide()
