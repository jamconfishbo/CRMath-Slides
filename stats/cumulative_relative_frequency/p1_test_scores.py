from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import (
    CumulativeFrequencyTemplate, TOTAL_COLOR, ROW_COLOR,
)
from components.theme import ANSWER_COLOR

SPEC = {
    "kind": "cumulative",
    "heading": "Problem 1 (I DO): Frequency → Cumulative Frequency",
    "scenario": "Scenario 1: A high school math class recorded the test scores\nof 40 students grouped into score ranges.",
    "task": "Task: Complete the Cumulative Frequency Table using\nthe completed Frequency Table.",
    "var_header": "Test Score\nRange",
    "classes": ["50–59", "60–69", "70–79", "80–89", "90–99"],
    "freqs": [3, 7, 12, 10, 8],
    "cum_header": "Score\nBoundary",
    "boundaries": ["Less than 60", "Less than 70", "Less than 80", "Less than 90", "Less than 100"],
    "questions": [
        ("a) How many students scored less than 70 on the test?", [
            ("hl", [("cum", 1, None, ANSWER_COLOR)]),
            ("math", [(r"\text{Less than } 70", WHITE), (r"\rightarrow", WHITE), ("10", ANSWER_COLOR)]),
            ("answer", "10 students"),
        ]),
        ("b) How many students scored less than or equal to 89?", [
            ("text", "Scores are whole numbers, so “89 or less” is the same as “less than 90”.", GREY_A),
            ("hl", [("cum", 3, None, ANSWER_COLOR)]),
            ("math", [(r"\le 89", WHITE), ("=", WHITE), (r"\text{Less than } 90", WHITE),
                      (r"\rightarrow", WHITE), ("32", ANSWER_COLOR)]),
            ("answer", "32 students"),
        ]),
        ("c) How many students scored 80 or higher on the test?", [
            ("text", "80 or higher = everyone (Total) − those less than 80", GREY_A),
            ("hl", [("freq", 5, 1, TOTAL_COLOR), ("cum", 2, None, ROW_COLOR)]),
            ("math", [("40", TOTAL_COLOR), ("-", WHITE), ("22", ROW_COLOR), ("=", WHITE), ("18", ANSWER_COLOR)]),
            ("answer", "18 students"),
        ]),
    ],
}


class Problem1TestScores(Slide, CumulativeFrequencyTemplate):
    """Problem 1 (I DO): test scores, frequency -> cumulative frequency."""

    def construct(self):
        self.run_problem(SPEC)
