from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class ClearingParenthesesTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Order of Operations (cont.)", "Clearing Parentheses")
        self.next_slide()
