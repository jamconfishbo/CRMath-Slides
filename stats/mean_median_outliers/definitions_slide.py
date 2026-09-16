from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR


class MeanMedianDefinitions(Slide):
    """Defines Mean and Median before the guided example."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Mean vs. Median", font_size=44, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.next_slide()

        intro = Text(
            '"Average" is ambiguous -- it can mean the Mean or the Median,\n'
            "and outliers can make these two numbers very different.",
            font_size=27,
            line_spacing=1.15,
        )
        intro.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(intro, shift=UP * 0.2))
        self.next_slide()

        mean_def = VGroup(
            Text("Mean", font_size=30, weight=BOLD, color=ANSWER_COLOR),
            Text(
                "The arithmetic average -- add up all the values\n"
                "and divide by how many values there are.",
                font_size=27,
                line_spacing=1.15,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        median_def = VGroup(
            Text("Median", font_size=30, weight=BOLD, color=ANSWER_COLOR),
            Text(
                "The middle value once the data is ordered.\n"
                "Odd count: the exact middle number.\n"
                "Even count: the mean of the two middle numbers.",
                font_size=27,
                line_spacing=1.15,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        defs = VGroup(mean_def, median_def).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        defs.next_to(intro, DOWN, buff=0.55)

        self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.2) for d in defs], lag_ratio=0.4))
        self.next_slide()
