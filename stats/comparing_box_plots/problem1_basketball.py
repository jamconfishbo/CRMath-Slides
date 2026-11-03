from manim import *
from manim_slides import Slide

from templates.box_plot import BoxPlotTemplate

SPEC = {
    "heading": "Comparing Box Plots: Problem 1",
    "context": "The points scored by two basketball players over their recent games are shown below.",
    "data": [
        ("Player A", [21, 8, 30, 15, 24, 12, 18, 27, 11, 33, 22, 14, 25, 17], "Player A (14 games)"),
        ("Player B", [25, 14, 30, 22, 12, 28, 19, 34, 21, 16, 24, 20, 23], "Player B (13 games)"),
    ],
    "x_range": [5, 35, 1],
    "x_numbers": [5, 10, 15, 20, 25, 30, 35],
    "x_label": "Points Scored",
    "questions": [
        {
            "prompt": "a) Which player has the higher median?",
            "answer": "Player B",
            "show": "median",
            "follow": "What does this tell us about the two players?",
            "explain": "Player B usually scores more points in a typical game (22 vs. 19.5).",
        },
        {
            "prompt": "b) Which player has the larger IQR?",
            "answer": "Player A",
            "show": "iqr",
            "follow": "What does this tell us?",
            "explain": "The middle 50% of Player A's scores are more spread out (11 vs. 9).\n"
                       "Player B's typical games are more consistent.",
        },
        {
            "prompt": "c) Which player has the larger range?",
            "answer": "Player A",
            "show": "range",
            "follow": "What does this tell us?",
            "explain": "Player A's scores vary more overall, from a low of 8 to a high of 33\n"
                       "(range 25 vs. 22).",
        },
        {
            "prompt": "d) If you were the coach and needed a player who scores consistently,\n"
                       "which player would you choose? Use the median, IQR, and range to explain.",
            "answer": "Player B",
            "explain": "Player B has a higher median, a smaller IQR, and a smaller range,\n"
                       "so Player B scores more points and is more consistent.",
        },
    ],
}


class P1Order(Slide, BoxPlotTemplate):
    """Step 1: order Player A, then Player B, one number per click."""

    def construct(self):
        self.run_ordering(SPEC)


class P1PlayerA(Slide, BoxPlotTemplate):
    """Step 2, even count: median between two values, odd halves."""

    def construct(self):
        self.run_step2(SPEC, 0)


class P1PlayerB(Slide, BoxPlotTemplate):
    """Step 2, odd count: median is a data value, even halves."""

    def construct(self):
        self.run_step2(SPEC, 1)


class P1Table(Slide, BoxPlotTemplate):
    """Step 3: five-number summary, IQR and range."""

    def construct(self):
        self.run_table(SPEC)


class P1BoxPlots(Slide, BoxPlotTemplate):
    """Step 4: filled table above, both box plots drawn below it."""

    def construct(self):
        self.run_box_plots(SPEC)


class P1Interpret(Slide, BoxPlotTemplate):
    """Step 5: box plots above, interpretation questions below."""

    def construct(self):
        self.run_interpretation(SPEC)
