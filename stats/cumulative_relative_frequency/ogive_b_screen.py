from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import CumulativeFrequencyTemplate
from templates.graph import GraphTemplate

SPEC = {
    "practice": True,
    "seconds": 300,
    "heading": "Graph B (YOU DO): Percentile Estimation -- Screen Time",
    "solution_heading": "Graph B: Solution",
    "scenario": "Plot (upper boundary, cumulative %) for each row of Scenario 6,\nconnect the points to form an ogive, then read across from\n25% (Q1), 50% (Median) and 75% (Q3) to the curve and down.",
    "task": "Task: Estimate Q1, the Median, and Q3 for the screen time data.",
    "table_title": "Scenario 6: Cum. Rel. Freq.",
    "xs": [0, 20, 40, 60, 80, 100],
    "ys": [0, 12, 40, 76, 92, 100],
    "unit": "min",
    "labels": ["Start (0 min)", "Less than 20 min", "Less than 40 min", "Less than 60 min",
               "Less than 80 min", "Less than 100 min"],
    "answer_unit": "min",
    "x_label": "Usage (minutes)",
}


class OgiveBScreen(Slide, CumulativeFrequencyTemplate, GraphTemplate):
    """Graph B (YOU DO): ogive + Q1 / median / Q3 for Scenario 6."""

    def construct(self):
        self.run_ogive(SPEC)
