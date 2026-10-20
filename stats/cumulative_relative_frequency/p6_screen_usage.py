from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import (
    CumulativeFrequencyTemplate, TOTAL_COLOR, ROW_COLOR, RUNNING_COLOR,
)
from components.theme import ANSWER_COLOR

CLASSES = ["0–19", "20–39", "40–59", "60–79", "80–99"]

SPEC = {
    "kind": "combined",
    "practice": True,
    "seconds": 420,
    "heading": "Problem 6 (YOU DO): Combined Frequency Table Conversion",
    "solution_heading": "Problem 6: Solution",
    "scenario": "Scenario 6: Daily screen usage (in minutes) was recorded for\na sample of 50 teenagers.",
    "task": "Task: First, calculate the Relative Frequency column. Then complete\nthe Cumulative Relative Frequency table.",
    "var_header": "Usage\n(min)",
    "classes": CLASSES,
    "work_labels": [f"{c} min" for c in CLASSES],
    "freqs": [6, 14, 18, 8, 4],
    "cum_header": "Usage\nThreshold",
    "boundaries": ["Less than 20", "Less than 40", "Less than 60", "Less than 80", "Less than 100"],
    "questions": [
        ("a) What percentage of teenagers use their screen for less than 60 minutes?", [
            ("hl", [("cum", 2, None, ANSWER_COLOR)]),
            ("math", [(r"\text{Less than } 60", WHITE), (r"\rightarrow", WHITE), (r"76\%", ANSWER_COLOR)]),
            ("answer", "76%"),
        ]),
        ("b) What percentage of teenagers use their screen for 40 minutes or more?", [
            ("text", "40 or more = everyone (100%) − those less than 40", GREY_A),
            ("hl", [("left", 5, 2, TOTAL_COLOR), ("cum", 1, None, ROW_COLOR)]),
            ("math", [(r"100\%", TOTAL_COLOR), ("-", WHITE), (r"40\%", ROW_COLOR), ("=", WHITE), (r"60\%", ANSWER_COLOR)]),
            ("answer", "60%"),
        ]),
        ("c) Which class interval contains the 25th percentile (Q1)?", [
            ("text", "Find where the cumulative % first reaches 25%.", GREY_A),
            ("hl", [("cum", 0, None, RUNNING_COLOR), ("cum", 1, None, ROW_COLOR)]),
            ("math", [(r"12\%", RUNNING_COLOR), ("<", WHITE), (r"25\%", WHITE), (r"\le", WHITE), (r"40\%", ROW_COLOR)]),
            ("hl", [("left", 1, None, ANSWER_COLOR)]),
            ("answer", "20–39 min"),
        ]),
    ],
}


class Problem6ScreenUsage(Slide, CumulativeFrequencyTemplate):
    """Problem 6 (YOU DO): screen usage, relative -> cumulative relative frequency."""

    def construct(self):
        self.run_problem(SPEC)
