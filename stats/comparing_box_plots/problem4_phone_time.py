from manim import *
from manim_slides import Slide

from templates.box_plot import BoxPlotTemplate

JUNIORS, SENIORS = 0, 1


def blank(tex, *callouts):
    return {"tex": tex, "callouts": list(callouts)}


SPEC = {
    "heading": "Comparing Box Plots: Problem 4",
    "context": "The box plots show the number of minutes per day that juniors and\n"
               "seniors at a high school spend on their phones.\n"
               "Each small grid line is 15 minutes.",
    "summaries": [
        ("Juniors", 45, 90, 120, 150, 210),
        ("Seniors", 30, 60, 90, 120, 240),
    ],
    "x_range": [0, 240, 15],
    "x_numbers": [0, 30, 60, 90, 120, 150, 180, 210, 240],
    "x_label": "Minutes on Phone per Day",
    "compare_heading": "Compare the groups.",
    "questions": [
        {
            "prompt": "1. Which group has the higher median?",
            "answer": "Juniors",
            "show": "median",
            "follow": "What does this mean?",
            "explain": "A typical junior spends more time on their phone (120 vs. 90 minutes).",
        },
        {
            "prompt": "2. Compare the IQRs. What do you notice? What does this mean?",
            "show": "iqr",
            "explain": "They are the same (60 minutes). The middle 50% of each group\n"
                       "is spread out by the same amount.",
        },
        {
            "prompt": "3. Which group has the larger range?",
            "answer": "Seniors",
            "show": "range",
            "follow": "Why is the range so different when the IQRs are the same?",
            "explain": "Seniors: 210 vs. 165. The range uses the min and max, so a few extreme\n"
                       "seniors (like the one at 240 minutes) make the range larger even\n"
                       "though the middle half has the same spread.",
        },
    ],
    "percents_heading": "Percents and the box plot.",
    "percents_reminder": "Each part of a box plot (whisker, box half, box half, whisker)\n"
                         "contains about 25% of the data.",
    "percents": [
        {"rows": [
            ["4. If a junior spends 150 minutes on their phone,"],
            ["about what percent of juniors spend more time than that?",
             blank(r"25\%", ("mark", JUNIORS, 150, None), ("span", JUNIORS, 150, 210, "25%"))],
        ]},
        {"rows": [
            ["5. If a senior spends 60 minutes on their phone,"],
            ["about what percent of seniors spend less time than that?",
             blank(r"25\%", ("mark", SENIORS, 60, None), ("span", SENIORS, 30, 60, "25%"))],
        ]},
        {"rows": [
            ["6. If a senior spends 120 minutes on their phone,"],
            ["about what percent of seniors spend less time?",
             blank(r"75\%", ("mark", SENIORS, 120, None), ("span", SENIORS, 30, 120, "75%"))],
            ["About what percent spend more time?",
             blank(r"25\%", ("span", SENIORS, 120, 240, "25%"))],
        ]},
        {"rows": [
            ["7. If a junior spends 120 minutes on their phone,"],
            ["about what percent of juniors spend less time?",
             blank(r"50\%", ("mark", JUNIORS, 120, None), ("span", JUNIORS, 45, 120, "50%"))],
        ]},
        {"rows": [
            ["8. About what percent of juniors spend at least 90 minutes"],
            ["on their phone?",
             blank(r"75\%", ("mark", JUNIORS, 90, None), ("span", JUNIORS, 90, 210, "75%"))],
            ["About what percent of seniors spend at least 90 minutes"],
            ["on their phone?",
             blank(r"50\%", ("mark", SENIORS, 90, None), ("span", SENIORS, 90, 240, "50%"))],
        ]},
        {"rows": [
            ["9. About what percent of juniors spend between 45 and 120 minutes"],
            ["on their phone?",
             blank(r"50\%", ("span", JUNIORS, 45, 120, "50%"))],
        ]},
        {"rows": [
            ["10. The middle 50% of juniors spend"],
            ["between", blank("90", ("mark", JUNIORS, 90, None)), "and",
             blank("150", ("mark", JUNIORS, 150, None), ("span", JUNIORS, 90, 150, "middle 50%")),
             "minutes on their phone."],
        ]},
        {"rows": [
            ["11. The middle 50% of seniors spend"],
            ["between", blank("60", ("mark", SENIORS, 60, None)), "and",
             blank("120", ("mark", SENIORS, 120, None), ("span", SENIORS, 60, 120, "middle 50%")),
             "minutes on their phone."],
        ]},
        {
            "rows": [
                ['12. A senior says, "I spend 130 minutes a day on my phone. That puts'],
                ['me in the top 25% of seniors." Is the senior correct? Explain.',
                 blank(r"\text{Yes}", ("mark", SENIORS, 130, "130"), ("span", SENIORS, 120, 240, "top 25%"))],
            ],
            "explain": "130 is greater than the seniors' Q3 of 120, and about 25% of seniors\n"
                       "are above Q3.",
        },
        {
            "rows": [
                ["13. Which group spends more time on their phones?"],
                ["Explain using at least two statistics.", blank(r"\text{Juniors}")],
            ],
            "explain": "Their median is higher (120 vs. 90), and 75% of juniors use their phones\n"
                       "at least 90 minutes compared with only 50% of seniors.\n"
                       "(Seniors do have the single highest value, 240.)",
        },
    ],
}


class P4Read(Slide, BoxPlotTemplate):
    """Read the five-number summaries off the given plots into the table."""

    def construct(self):
        self.run_read_table(SPEC)


class P4Compare(Slide, BoxPlotTemplate):
    """Box plots above, questions 1-3 below."""

    def construct(self):
        self.run_interpretation(SPEC)


class P4Percents(Slide, BoxPlotTemplate):
    """Box plots above, questions 4-13 below."""

    def construct(self):
        self.run_percents(SPEC)
