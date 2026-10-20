from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import CumulativeFrequencyTemplate, ROW_COLOR
from components.theme import ANSWER_COLOR

CLASSES = ["0–9", "10–19", "20–29", "30–39", "40–49"]

SPEC = {
    "kind": "relative",
    "heading": "Problem 3 (I DO): Relative Frequency Analysis",
    "scenario": "Scenario 3: A city transit authority surveyed 100 commuters\nabout their daily one-way commute times in minutes.",
    "task": "Task: Calculate and complete the Relative Frequency Table\nusing the Frequency Table.",
    "var_header": "Commute\n(min)",
    "classes": CLASSES,
    "work_labels": [f"{c} min" for c in CLASSES],
    "freqs": [15, 30, 35, 12, 8],
    "questions": [
        ("a) What percentage of commuters have a commute time of 10–19 minutes?", [
            ("hl", [("rel", 1, None, ANSWER_COLOR)]),
            ("math", [(r"10\text{--}19 \text{ min}", WHITE), (r"\rightarrow", WHITE), (r"30\%", ANSWER_COLOR)]),
            ("answer", "30%"),
        ]),
        ("b) What percentage of commuters have a commute time less than 20 minutes?", [
            ("text", "Less than 20 = the 0–9 row + the 10–19 row", GREY_A),
            ("hl", [("rel", 0, None, ROW_COLOR), ("rel", 1, None, ROW_COLOR)]),
            ("math", [(r"15\%", ROW_COLOR), ("+", WHITE), (r"30\%", ROW_COLOR), ("=", WHITE), (r"45\%", ANSWER_COLOR)]),
            ("answer", "45%"),
        ]),
        ("c) What percentage of commuters have a commute time of more than 29 minutes?", [
            ("text", "More than 29 = the 30–39 row + the 40–49 row", GREY_A),
            ("hl", [("rel", 3, None, ROW_COLOR), ("rel", 4, None, ROW_COLOR)]),
            ("math", [(r"12\%", ROW_COLOR), ("+", WHITE), (r"8\%", ROW_COLOR), ("=", WHITE), (r"20\%", ANSWER_COLOR)]),
            ("answer", "20%"),
        ]),
    ],
}


class Problem3Commute(Slide, CumulativeFrequencyTemplate):
    """Problem 3 (I DO): commute times, frequency -> relative frequency."""

    def construct(self):
        self.run_problem(SPEC)
