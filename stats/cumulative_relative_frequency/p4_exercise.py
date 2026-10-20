from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import CumulativeFrequencyTemplate, ROW_COLOR
from components.theme import ANSWER_COLOR

CLASSES = ["0–2", "3–5", "6–8", "9–11", "12–14"]

SPEC = {
    "kind": "relative",
    "practice": True,
    "seconds": 300,
    "heading": "Problem 4 (YOU DO): Relative Frequency Analysis",
    "solution_heading": "Problem 4: Solution",
    "scenario": "Scenario 4: A wellness program tracked weekly physical exercise\nhours for 100 adult participants.",
    "task": "Task: Calculate and complete the Relative Frequency Table\nbased on the Frequency Table.",
    "var_header": "Exercise\n(hrs)",
    "classes": CLASSES,
    "work_labels": [f"{c} hrs" for c in CLASSES],
    "freqs": [10, 25, 40, 18, 7],
    "questions": [
        ("a) What percentage of participants exercise 6–8 hours per week?", [
            ("hl", [("rel", 2, None, ANSWER_COLOR)]),
            ("math", [(r"6\text{--}8 \text{ hrs}", WHITE), (r"\rightarrow", WHITE), (r"40\%", ANSWER_COLOR)]),
            ("answer", "40%"),
        ]),
        ("b) What percentage of participants exercise less than 6 hours per week?", [
            ("text", "Less than 6 = the 0–2 row + the 3–5 row", GREY_A),
            ("hl", [("rel", 0, None, ROW_COLOR), ("rel", 1, None, ROW_COLOR)]),
            ("math", [(r"10\%", ROW_COLOR), ("+", WHITE), (r"25\%", ROW_COLOR), ("=", WHITE), (r"35\%", ANSWER_COLOR)]),
            ("answer", "35%"),
        ]),
        ("c) What percentage of participants exercise more than 8 hours per week?", [
            ("text", "More than 8 = the 9–11 row + the 12–14 row", GREY_A),
            ("hl", [("rel", 3, None, ROW_COLOR), ("rel", 4, None, ROW_COLOR)]),
            ("math", [(r"18\%", ROW_COLOR), ("+", WHITE), (r"7\%", ROW_COLOR), ("=", WHITE), (r"25\%", ANSWER_COLOR)]),
            ("answer", "25%"),
        ]),
    ],
}


class Problem4Exercise(Slide, CumulativeFrequencyTemplate):
    """Problem 4 (YOU DO): exercise hours, frequency -> relative frequency."""

    def construct(self):
        self.run_problem(SPEC)
