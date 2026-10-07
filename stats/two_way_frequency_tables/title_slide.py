from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class TwoWayFrequencyTablesTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("Two-Way Frequency Tables", "Organizing Data, Tallying & Relative Frequency", title_font_size=44)
        self.next_slide()
