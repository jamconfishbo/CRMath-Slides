from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class FrequencyTablesTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title("One-Way Frequency Tables", "Quantitative & Categorical Data", title_font_size=48)
        self.next_slide()
