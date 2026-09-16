# templates/mean_median.py

from manim import *

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR

MEAN_COLOR = BLUE
MEDIAN_COLOR = "#FF00FF"  # MAGENTA
STRIKE_COLOR = GRAY

MEAN_X = -3.5
MEDIAN_X = 3.0
COLUMN_HEADER_Y = 2.1


class MeanMedianTemplate:
    """Mixin for "mean & median, side by side, with outliers" worked examples.

    Layout: the packet question stays pinned at the top of the frame for the
    whole slide. Below it, two columns build up left-to-right in time (mean
    first, then median) but sit side by side in space -- mean on the left,
    median on the right.

    Usage:
        class MyProblem(Slide, MeanMedianTemplate):
            def construct(self):
                self.camera.background_color = BACKGROUND_COLOR
                self.show_question(r"\\textbf{Q1)} ...")
                self.show_headers()
                self.mean_calc([r"\\frac{15+12+100+14+18}{5}", r"\\frac{159}{5}", "31.8"])
                self.median_calc(
                    ["15", "12", "100", "14", "18"],
                    ["12", "14", "15", "18", "100"],
                )
    """

    def show_question(self, tex, font_size=30, width=12.0):
        question = Tex(tex, font_size=font_size)
        if question.width > width:
            question.scale_to_fit_width(width)
        question.to_edge(UP, buff=0.35)
        self.play(FadeIn(question))
        self.next_slide()
        return question

    def show_headers(self, mean_label="Mean", median_label="Median", font_size=40, y=COLUMN_HEADER_Y):
        mean_header = Text(mean_label, weight=BOLD, color=MEAN_COLOR, font_size=font_size)
        mean_header.move_to(np.array([MEAN_X, y, 0]))
        median_header = Text(median_label, weight=BOLD, color=MEDIAN_COLOR, font_size=font_size)
        median_header.move_to(np.array([MEDIAN_X, y, 0]))
        self.play(FadeIn(mean_header), FadeIn(median_header))
        self.next_slide()
        return mean_header, median_header

    def mean_calc(self, steps, anchor_y=COLUMN_HEADER_Y - 0.9, font_size=34, buff=0.55):
        """steps: MathTex strings, first = the sum-over-count fraction, last =
        the final value. Every step stays visible, stacked below the last."""
        lines = []
        prev = None
        for s in steps:
            m = MathTex(s, font_size=font_size)
            if prev is None:
                m.move_to(np.array([MEAN_X, anchor_y, 0]))
            else:
                m.next_to(prev, DOWN, buff=buff)
            self.play(Write(m))
            self.next_slide()
            lines.append(m)
            prev = m

        self.play(Circumscribe(lines[-1], color=ANSWER_COLOR))
        self.next_slide()
        return lines

    def median_calc(self, unsorted_values, sorted_values, anchor_y=COLUMN_HEADER_Y - 0.9, font_size=34, row_buff=0.7):
        """
        unsorted_values / sorted_values: parallel lists of the same numbers as
        strings, `sorted_values` given smallest to largest. Animates: write
        the unordered list, arrange it in order below, strike the outer pair
        inward one step at a time, then either box the single middle number
        (odd count) or underline the middle two and compute their average
        (even count). Returns the mobject holding the final median value.
        """
        unsorted_row, _ = self._number_row(unsorted_values, font_size)
        unsorted_row.move_to(np.array([MEDIAN_X, anchor_y, 0]))
        self.play(Write(unsorted_row))
        self.next_slide()

        sorted_row, numbers = self._number_row(sorted_values, font_size)
        sorted_row.next_to(unsorted_row, DOWN, buff=row_buff)
        self.play(TransformFromCopy(unsorted_row, sorted_row))
        self.next_slide()

        left, right = 0, len(numbers) - 1
        while right - left > 1:
            l1 = self._strike_line(numbers[left])
            l2 = self._strike_line(numbers[right])
            self.play(Create(l1), Create(l2))
            self.next_slide()
            left += 1
            right -= 1

        if left == right:
            median_mob = numbers[left]
            self.play(Circumscribe(median_mob, color=ANSWER_COLOR))
            self.next_slide()
            return median_mob

        left_mob, right_mob = numbers[left], numbers[right]
        self.play(Create(Underline(left_mob, color=ANSWER_COLOR)), Create(Underline(right_mob, color=ANSWER_COLOR)))
        self.next_slide()

        avg_setup = MathTex(rf"\frac{{{sorted_values[left]}+{sorted_values[right]}}}{{2}}", font_size=font_size)
        avg_setup.next_to(sorted_row, DOWN, buff=row_buff)
        self.play(Write(avg_setup))
        self.next_slide()

        answer = MathTex(self._average_str(sorted_values[left], sorted_values[right]), font_size=font_size)
        answer.next_to(avg_setup, DOWN, buff=0.4)
        self.play(TransformFromCopy(avg_setup, answer))
        self.play(Circumscribe(answer, color=ANSWER_COLOR))
        self.next_slide()
        return answer

    def show_answer_points(self, points, font_size=34, buff=0.5, width=11):
        """points: Tex strings, revealed one at a time (FadeIn), stacked and
        left-aligned as a centered block."""
        mobs = []
        for p in points:
            m = Tex(p, font_size=font_size)
            if m.width > width:
                m.scale_to_fit_width(width)
            mobs.append(m)
        group = VGroup(*mobs).arrange(DOWN, buff=buff, aligned_edge=LEFT)
        group.move_to(ORIGIN).shift(DOWN * 0.3)

        for m in mobs:
            self.play(FadeIn(m, shift=UP * 0.2))
            self.next_slide()
        return mobs

    @staticmethod
    def _number_row(values, font_size):
        parts = [MathTex(v, font_size=font_size) for v in values]
        row = VGroup()
        for i, p in enumerate(parts):
            row.add(p)
            if i < len(parts) - 1:
                row.add(MathTex(",", font_size=font_size))
        row.arrange(RIGHT, buff=0.22)
        return row, parts

    @staticmethod
    def _strike_line(mob, color=STRIKE_COLOR, pad=0.08, stroke_width=6):
        return Line(
            mob.get_corner(UL) + UP * pad + LEFT * pad,
            mob.get_corner(DR) + DOWN * pad + RIGHT * pad,
            color=color,
            stroke_width=stroke_width,
        )

    @staticmethod
    def _average_str(a, b):
        # Values are plain numbers -- MathTex is already in math mode, so a
        # literal "$" here would break LaTeX. Currency problems show units
        # in the question header/labels instead of inside the number row.
        avg = (float(a) + float(b)) / 2
        return str(int(avg)) if avg == int(avg) else f"{avg:g}"
