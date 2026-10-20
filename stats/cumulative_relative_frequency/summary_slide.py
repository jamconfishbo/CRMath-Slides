from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.cumulative_frequency import TOTAL_COLOR, ROW_COLOR, RUNNING_COLOR
from templates.summary import SummaryTemplate


def c(color, s):
    return rf"\textcolor[HTML]{{{ManimColor(color).to_hex()[1:]}}}{{{s}}}"


class CumulativeFrequencySummary(Slide, SummaryTemplate):
    """Wrap-up: how each kind of table is filled, row by row."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        head = self.show_key_lines([r"\textbf{Summary: Building Each Table}"], font_size=44)
        self.summary_table(
            ["Table", "Each row", "Check the last row"],
            [
                ["Cumulative Freq.", c(RUNNING_COLOR, "previous cumulative") + " + " + c(ROW_COLOR, "this row's $f$"),
                 "equals the " + c(TOTAL_COLOR, "Total")],
                ["Relative Freq.", c(ROW_COLOR, "$f$") + r" $\div$ " + c(TOTAL_COLOR, "Total") + r" $\to$ \%",
                 r"column adds to 100\%"],
                ["Cumulative Rel. Freq.", c(RUNNING_COLOR, r"previous cum.\ \%") + " + " + c(ROW_COLOR, r"this row's \%"),
                 r"equals 100\%"],
                ["Ogive", r"plot (upper boundary, cum.\ \%), connect",
                 r"read across from 25\%, 50\%, 75\%, then down"],
            ],
            below=head, font_size=28,
        )
