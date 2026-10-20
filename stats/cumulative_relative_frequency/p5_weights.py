from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import (
    CumulativeFrequencyTemplate, TOTAL_COLOR, ROW_COLOR, RUNNING_COLOR,
)
from components.theme import ANSWER_COLOR

CLASSES = ["100–119", "120–139", "140–159", "160–179", "180–199"]

SPEC = {
    "kind": "combined",
    "heading": "Problem 5 (I DO): Combined Frequency Table Conversion",
    "scenario": "Scenario 5: A manufacturing lab weighed 50 precision components\n(in grams).",
    "task": "Task: First, calculate the Relative Frequency column. Then convert\nthose values into the Cumulative Relative Frequency table.",
    "var_header": "Weight\n(g)",
    "classes": CLASSES,
    "work_labels": [f"{c} g" for c in CLASSES],
    "freqs": [4, 11, 20, 10, 5],
    "cum_header": "Weight\nThreshold",
    "boundaries": ["Less than 120 g", "Less than 140 g", "Less than 160 g", "Less than 180 g", "Less than 200 g"],
    "questions": [
        ("a) What percentage of components weigh less than 160 g?", [
            ("hl", [("cum", 2, None, ANSWER_COLOR)]),
            ("math", [(r"\text{Less than } 160", WHITE), (r"\rightarrow", WHITE), (r"70\%", ANSWER_COLOR)]),
            ("answer", "70%"),
        ]),
        ("b) What percentage of components weigh 140 g or more?", [
            ("text", "140 g or more = everyone (100%) − those less than 140 g", GREY_A),
            ("hl", [("left", 5, 2, TOTAL_COLOR), ("cum", 1, None, ROW_COLOR)]),
            ("math", [(r"100\%", TOTAL_COLOR), ("-", WHITE), (r"30\%", ROW_COLOR), ("=", WHITE), (r"70\%", ANSWER_COLOR)]),
            ("answer", "70%"),
        ]),
        ("c) Which class interval contains the 50th percentile (median) weight?", [
            ("text", "Find where the cumulative % first reaches 50%.", GREY_A),
            ("hl", [("cum", 1, None, RUNNING_COLOR), ("cum", 2, None, ROW_COLOR)]),
            ("math", [(r"30\%", RUNNING_COLOR), ("<", WHITE), (r"50\%", WHITE), (r"\le", WHITE), (r"70\%", ROW_COLOR)]),
            ("hl", [("left", 2, None, ANSWER_COLOR)]),
            ("answer", "140–159 g"),
        ]),
    ],
}


class Problem5Weights(Slide, CumulativeFrequencyTemplate):
    """Problem 5 (I DO): component weights, relative -> cumulative relative frequency."""

    def construct(self):
        self.run_problem(SPEC)
