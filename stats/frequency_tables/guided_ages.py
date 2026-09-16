from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate

AGES = [
    45, 88, 46, 45, 64, 89, 57, 67, 85, 56,
    92, 81, 51, 58, 71, 55, 54, 62, 48, 38,
    27, 55, 66, 56, 76, 64, 55, 81, 69, 38,
    54, 49, 44, 68, 54, 91, 75, 56, 46, 68,
    61, 46, 68, 47, 78, 83, 61, 71, 83, 62,
]

CLASSES = [(27, 35), (36, 44), (45, 53), (54, 62), (63, 71), (72, 80), (81, 89), (90, 98)]
CLASS_LABELS = [f"{lo}-{hi}" for lo, hi in CLASSES]

COL_X = [0.3, 1.7, 4.3, 5.4, 6.8]
TOP_Y = 2.75
ROW_H = 0.5
ROW_Y = [TOP_Y - i * ROW_H for i in range(11)]


def bucket(value):
    for i, (lo, hi) in enumerate(CLASSES):
        if lo <= value <= hi:
            return i
    raise ValueError(value)


class GuidedAges(Slide, FrequencyTableTemplate):
    """Guided Example 1: Ages of the 50 Wealthiest People (quantitative)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_heading("Guided Example 1: Ages of the 50 Wealthiest People")

        data_mobs = self.show_raw_data(AGES, per_row=10, font_size=30, center=DOWN * 0.5)
        self.shrink_raw_data(data_mobs, target_point=np.array([-3.9, 0.25, 0]), width=6.0)

        table = self.build_table_skeleton(
            CLASS_LABELS,
            ["Class Limits", "Tally", "Freq. (f)", "Percent"],
            COL_X,
            ROW_Y,
            font_size=22,
            label_font_size=22,
        )

        row_indices = [bucket(v) for v in AGES]
        counts = self.run_tally_phase(data_mobs, row_indices, table["tally_anchors"])

        total = sum(counts)
        rows = []
        for i, c in enumerate(counts):
            pct = round(c / total * 100)
            rows.append((table["freq_slots"][i], str(c), table["percent_slots"][i], f"{pct}%"))
        self.reveal_row_counts(rows, font_size=22)

        self.reveal_total(
            table["freq_total_slot"], str(total),
            table["percent_total_slot"], "100%",
            font_size=22,
        )
