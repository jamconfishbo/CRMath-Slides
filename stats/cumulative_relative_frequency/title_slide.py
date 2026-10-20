from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class CumulativeFrequencyTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title(
            "Cumulative & Relative Frequency",
            "Constructing Tables, Relative Cumulative Analysis & Ogives",
            title_font_size=46, subtitle_font_size=30,
        )
        self.next_slide()
