from manim import *
from manim_slides import Slide

from templates.cumulative_frequency import CumulativeFrequencyTemplate
from templates.graph import GraphTemplate

SPEC = {
    "heading": "Graph A (I DO): Percentile Estimation -- Component Weights",
    "scenario": "Plot (upper boundary, cumulative %) for each row of Scenario 5,\nconnect the points to form an ogive, then read across from\n25% (Q1), 50% (Median) and 75% (Q3) to the curve and down.",
    "task": "Task: Estimate Q1, the Median, and Q3 for the component weights.",
    "table_title": "Scenario 5: Cum. Rel. Freq.",
    "xs": [100, 120, 140, 160, 180, 200],
    "ys": [0, 8, 30, 70, 90, 100],
    "unit": "g",
    "answer_unit": "g",
    "x_label": "Weight (grams)",
}


class OgiveAWeights(Slide, CumulativeFrequencyTemplate, GraphTemplate):
    """Graph A (I DO): ogive + Q1 / median / Q3 for Scenario 5."""

    def construct(self):
        self.run_ogive(SPEC)
