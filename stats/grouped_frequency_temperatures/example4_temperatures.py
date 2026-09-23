from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate, bucket_by_boundaries

TEMPS = [
    112, 100, 127, 120, 134, 118, 105, 110, 109, 112,
    110, 118, 117, 116, 118, 122, 114, 114, 105, 109,
    107, 112, 114, 115, 118, 117, 118, 122, 106, 110,
    116, 108, 110, 121, 113, 120, 119, 111, 104, 111,
    120, 113, 120, 117, 105, 110, 118, 112, 114, 114,
]

CLASS_LABELS = ["100-104", "105-109", "110-114", "115-119", "120-124", "125-129", "130-134"]
LOWER = ["99.5", "104.5", "109.5", "114.5", "119.5", "124.5", "129.5"]
UPPER = ["104.5", "109.5", "114.5", "119.5", "124.5", "129.5", "134.5"]
BOUNDARIES = [(99.5, 104.5), (104.5, 109.5), (109.5, 114.5), (114.5, 119.5),
              (119.5, 124.5), (124.5, 129.5), (129.5, 134.5)]

HEADERS = ["Class Limits", "Class Boundaries", "Tally", "Frequency (f)"]
COL_X = [0.3, 1.5, 3.8, 6.1, 7.0]
TOP_Y = 2.9
ROW_H = 0.55
ROW_Y = [TOP_Y - i * ROW_H for i in range(10)]

RAW_DATA_CENTER = DOWN * 0.5
RAW_DATA_TARGET = np.array([-3.9, 0.3, 0])
RAW_DATA_WIDTH = 5.6


class Example4Temperatures(Slide, FrequencyTableTemplate):
    """Example 4: Construct a Grouped Frequency Distribution -- record high
    temperatures for the 50 states, k = 7 classes."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading(
            "Example 4: Construct a Grouped Frequency Distribution (k = 7)", font_size=26
        )

        data_mobs = self.show_raw_data(TEMPS, per_row=10, font_size=26, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        range_line = MathTex(r"\text{Range} = 134 - 100 = 34", font_size=26)
        range_line.move_to(np.array([-3.9, 2.9, 0]))
        self.play(Write(range_line))
        self.next_slide()

        width_line = MathTex(
            r"\text{Width} = \frac{34}{7} \approx 4.857 \rightarrow \text{round UP to } 5",
            font_size=24,
        )
        width_line.move_to(np.array([-3.9, 2.45, 0]))
        self.play(Write(width_line))
        self.next_slide()

        start_line = MathTex(
            r"\text{Start at a convenient integer} \leq \text{min (100)} \rightarrow \text{Start} = 100",
            font_size=22,
        )
        start_line.move_to(np.array([-3.9, 2.05, 0]))
        self.play(Write(start_line))
        self.next_slide()

        table = self.build_table_grid(
            [" "] * 7, HEADERS, COL_X, ROW_Y, font_size=20, label_font_size=18,
        )

        # --- class limits: reveal the 7 constructed ranges ---
        self.reveal_column(table["col_center"][0], CLASS_LABELS, font_size=20, color=WHITE)

        # --- class boundaries: lower column, then upper column -- no work shown ---
        self.reveal_boundaries(table["col_left"][1], LOWER, UPPER, font_size=20)

        # --- tally: one continuous pass over the raw data ---
        row_indices = bucket_by_boundaries(TEMPS, BOUNDARIES)
        counts = self.run_tally_phase(data_mobs, row_indices, table["col_left"][2])

        # --- frequency column, then the total ---
        total = sum(counts)
        freq_points = table["col_center"][3] + [table["total_center"][3]]
        freq_strs = [str(c) for c in counts] + [str(total)]
        self.reveal_column(freq_points, freq_strs, font_size=20, last_bold=True)
