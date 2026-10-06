from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class RelationsFunctionsTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Relations & Functions", "Ordered Pairs, Domain, Range, and the Vertical Line Test")
        self.next_slide()
