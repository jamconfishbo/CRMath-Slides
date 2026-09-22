from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR
from templates.frequency_table import FrequencyTableTemplate

BLANK_COLOR = GRAY


class VocabSlide(Slide, FrequencyTableTemplate):
    """Part 1: Key Concepts & Vocabulary -- fill-in-the-blank reveal."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_heading("Part 1: Key Concepts & Vocabulary", font_size=32)

        intro = Text(
            "Class Limits: the actual values listed in the table that separate classes.",
            font_size=26,
        )
        intro.to_edge(UP, buff=1.0)
        self.play(FadeIn(intro))
        self.next_slide()

        lcl = self._blank_line("Lower Class Limit (LCL): the", "data value in a class.")
        lcl.next_to(intro, DOWN, buff=0.45, aligned_edge=LEFT)
        self.play(FadeIn(lcl))
        self.next_slide()
        self._fill_blank(lcl, "smallest")

        ucl = self._blank_line("Upper Class Limit (UCL): the", "data value in a class.")
        ucl.next_to(lcl, DOWN, buff=0.45, aligned_edge=LEFT)
        self.play(FadeIn(ucl))
        self.next_slide()
        self._fill_blank(ucl, "largest")

        cb = Text(
            "Class Boundaries: numbers used to separate classes so that there are",
            font_size=26,
        )
        cb2 = self._blank_line("", "between the upper limit of one class and the lower limit of the next.")
        cb_group = VGroup(cb, cb2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        cb_group.next_to(ucl, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(FadeIn(cb_group))
        self.next_slide()
        self._fill_blank(cb2, "no gaps")

        formula_heading = Text("How to calculate (for whole-number data):", font_size=26, color=BLUE)
        formula_heading.next_to(cb_group, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(FadeIn(formula_heading))
        self.next_slide()

        lb = self._blank_formula("Lower Class Boundary", "=", "LCL", "-")
        lb.next_to(formula_heading, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(FadeIn(lb))
        self.next_slide()
        self._fill_blank(lb, "0.5")

        ub = self._blank_formula("Upper Class Boundary", "=", "UCL", "+")
        ub.next_to(lb, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(FadeIn(ub))
        self.next_slide()
        self._fill_blank(ub, "0.5")

    def _blank_line(self, prefix, suffix, font_size=26):
        parts = VGroup()
        if prefix:
            parts.add(Text(prefix, font_size=font_size))
        blank = Text("_______", font_size=font_size, color=BLANK_COLOR)
        blank.blank_flag = True
        parts.add(blank)
        parts.add(Text(suffix, font_size=font_size))
        parts.arrange(RIGHT, buff=0.15)
        return parts

    def _blank_formula(self, label, eq, term, op, font_size=26):
        blank = Text("____", font_size=font_size, color=BLANK_COLOR)
        blank.blank_flag = True
        parts = VGroup(
            Text(label, font_size=font_size),
            Text(eq, font_size=font_size),
            Text(term, font_size=font_size),
            Text(op, font_size=font_size),
            blank,
        ).arrange(RIGHT, buff=0.15)
        return parts

    def _fill_blank(self, group, answer_text, font_size=26):
        blank = next(m for m in group if getattr(m, "blank_flag", False))
        answer = Text(answer_text, font_size=font_size, weight=BOLD, color=ANSWER_COLOR)
        answer.move_to(blank)
        self.play(Transform(blank, answer))
        self.next_slide()
