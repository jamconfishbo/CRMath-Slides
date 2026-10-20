from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import (
    CumulativeFrequencyTemplate, TOTAL_COLOR, ROW_COLOR,
)
from components.theme import ANSWER_COLOR

SPEC = {
    "kind": "cumulative",
    "practice": True,
    "seconds": 300,
    "heading": "Problem 2 (YOU DO): Frequency → Cumulative Frequency",
    "solution_heading": "Problem 2: Solution",
    "scenario": "Scenario 2: A survey recorded the daily study time (in minutes)\nfor 40 high school seniors.",
    "task": "Task: Construct the Cumulative Frequency Table based on\nthe provided Frequency Table.",
    "var_header": "Study Time\n(min)",
    "classes": ["10–19", "20–29", "30–39", "40–49", "50–59"],
    "freqs": [5, 8, 14, 9, 4],
    "cum_header": "Time\nBoundary",
    "boundaries": ["Less than 20", "Less than 30", "Less than 40", "Less than 50", "Less than 60"],
    "questions": [
        ("a) How many students study for less than 30 minutes per day?", [
            ("hl", [("cum", 1, None, ANSWER_COLOR)]),
            ("math", [(r"\text{Less than } 30", WHITE), (r"\rightarrow", WHITE), ("13", ANSWER_COLOR)]),
            ("answer", "13 students"),
        ]),
        ("b) How many students study for less than or equal to 49 minutes?", [
            ("text", "Times are whole minutes, so “49 or less” is the same as “less than 50”.", GREY_A),
            ("hl", [("cum", 3, None, ANSWER_COLOR)]),
            ("math", [(r"\le 49", WHITE), ("=", WHITE), (r"\text{Less than } 50", WHITE),
                      (r"\rightarrow", WHITE), ("36", ANSWER_COLOR)]),
            ("answer", "36 students"),
        ]),
        ("c) How many students study for 40 minutes or more?", [
            ("text", "40 or more = everyone (Total) − those less than 40", GREY_A),
            ("hl", [("freq", 5, 1, TOTAL_COLOR), ("cum", 2, None, ROW_COLOR)]),
            ("math", [("40", TOTAL_COLOR), ("-", WHITE), ("27", ROW_COLOR), ("=", WHITE), ("13", ANSWER_COLOR)]),
            ("answer", "13 students"),
        ]),
    ],
}


class Problem2StudyTime(Slide, CumulativeFrequencyTemplate):
    """Problem 2 (YOU DO): study time, frequency -> cumulative frequency."""

    def construct(self):
        self.run_problem(SPEC)
