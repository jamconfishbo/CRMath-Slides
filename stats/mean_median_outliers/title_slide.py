from manim import *
from manim_slides import Slide

from templates.title_slide import TitleSlideTemplate


class MeanMedianTitle(Slide, TitleSlideTemplate):
    def construct(self):
        self.show_title(
            "Mean, Median, and the Power of Outliers",
            "Measures of Center",
            title_font_size=42,
        )
        self.next_slide()
