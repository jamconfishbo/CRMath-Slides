from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate, bucket_by_boundaries

SCREEN = [1.5, 2.2, 2.8, 3.1, 3.9, 4.2, 4.5, 5.0, 5.8, 6.4]

CLASS_LABELS = ["1.5 - 3.4", "3.5 - 5.4", "5.5 - 7.4"]
LOWER = ["1.45", "3.45", "5.45"]
UPPER = ["3.45", "5.45", "7.45"]
BOUNDARIES = [(1.45, 3.45), (3.45, 5.45), (5.45, 7.45)]

HEADERS = ["Class Limits", "Class Boundaries", "Tally", "Frequency (f)"]
COL_X = [0.3, 1.6, 3.6, 5.8, 6.9]
TOP_Y = 2.6
ROW_H = 0.6
ROW_Y = [TOP_Y - i * ROW_H for i in range(6)]

RAW_DATA_TARGET = np.array([-3.3, 0.9, 0])
RAW_DATA_WIDTH = 3.2


class Example2ScreenTime(Slide, FrequencyTableTemplate):
    """Example 2 (I DO), Part 3: constructing a frequency distribution from
    scratch -- Range, Bin Width (with rounding), class limits, then
    boundaries/tally/frequency as usual."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Example 2 (I DO): Daily Screen Time (Hours), k = 3")

        data_mobs = self.show_raw_data(SCREEN, per_row=5, font_size=30, center=DOWN * 1.3)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        range_line = MathTex(r"\text{Range} = 6.4 - 1.5 = 4.9", font_size=30)
        range_line.move_to(np.array([-3.3, 2.9, 0]))
        self.play(Write(range_line))
        self.next_slide()

        width_line = MathTex(
            r"\text{Width} = \frac{4.9}{3} \approx 1.63 \rightarrow \text{round UP to } 2",
            font_size=30,
        )
        width_line.move_to(np.array([-3.3, 2.45, 0]))
        self.play(Write(width_line))
        self.next_slide()

        table = self.build_table_grid(
            [" ", " ", " "], HEADERS, COL_X, ROW_Y, font_size=22, label_font_size=20,
        )

        # Class limits weren't given -- reveal the three constructed ranges.
        self.reveal_column(table["col_center"][0], CLASS_LABELS, font_size=22, color=WHITE)

        # Boundaries: lower column, then upper column -- no work shown.
        self.reveal_boundaries(table["col_left"][1], LOWER, UPPER, font_size=22)

        row_indices = bucket_by_boundaries(SCREEN, BOUNDARIES)
        counts = self.run_tally_phase(data_mobs, row_indices, table["col_left"][2])

        total = sum(counts)
        freq_points = table["col_center"][3] + [table["total_center"][3]]
        freq_strs = [str(c) for c in counts] + [str(total)]
        self.reveal_column(freq_points, freq_strs, font_size=22, last_bold=True)
