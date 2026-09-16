from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate

BEVERAGES = list(
    "W J C C J C T W C T "
    "W M M W W M W W M C "
    "T W J M M C J C M W "
    "W C W W J W W M C J".replace(" ", "")
)

CLASS_LABELS = ["W", "M", "J", "C", "T"]
NAMES = {"W": "Water", "M": "Milk", "J": "Juice", "C": "Coffee", "T": "Tea"}

COL_X = [0.5, 1.6, 4.2, 5.3, 6.6]
TOP_Y = 2.2
ROW_H = 0.6
ROW_Y = [TOP_Y - i * ROW_H for i in range(8)]


def bucket(value):
    return CLASS_LABELS.index(value)


class GuidedBeverage(Slide, FrequencyTableTemplate):
    """Guided Example 2: Breakfast Beverage Preference (categorical)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Guided Example 2: Breakfast Beverage Preference")

        legend = Text(
            "W = Water    M = Milk    J = Juice    C = Coffee    T = Tea",
            font_size=22,
            color=BLUE,
        )
        legend.next_to(heading, DOWN, buff=0.25)
        self.play(FadeIn(legend))
        self.next_slide()

        data_mobs = self.show_raw_data(BEVERAGES, per_row=10, font_size=32, center=DOWN * 0.5)
        self.shrink_raw_data(data_mobs, target_point=np.array([-3.9, 0.25, 0]), width=5.6)

        table = self.build_table_skeleton(
            CLASS_LABELS,
            ["Beverage", "Tally", "Freq. (f)", "Percent"],
            COL_X,
            ROW_Y,
            font_size=24,
            label_font_size=22,
        )

        row_indices = [bucket(v) for v in BEVERAGES]
        counts = self.run_tally_phase(data_mobs, row_indices, table["tally_anchors"])

        total = sum(counts)
        rows = []
        for i, c in enumerate(counts):
            pct = c / total * 100
            rows.append((table["freq_slots"][i], str(c), table["percent_slots"][i], f"{pct:.1f}%"))
        self.reveal_row_counts(rows, font_size=24)

        self.reveal_total(
            table["freq_total_slot"], str(total),
            table["percent_total_slot"], "100%",
            font_size=24,
        )
