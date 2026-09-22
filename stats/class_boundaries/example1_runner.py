from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate, bucket_by_boundaries

RUNNER = [1.2, 1.8, 2.3, 2.7, 3.1, 3.4, 3.8, 4.2, 4.5, 4.9, 5.2, 5.8]

CLASS_LABELS = ["1 - 2", "3 - 4", "5 - 6", "7 - 8", "9 - 10"]
LOWER = ["0.5", "2.5", "4.5", "6.5", "8.5"]
UPPER = ["2.5", "4.5", "6.5", "8.5", "10.5"]
BOUNDARIES = [(0.5, 2.5), (2.5, 4.5), (4.5, 6.5), (6.5, 8.5), (8.5, 10.5)]

HEADERS = ["Class Limits", "Class Boundaries", "Tally", "Frequency (f)"]
COL_X = [0.3, 1.6, 3.6, 5.8, 6.9]
TOP_Y = 2.6
ROW_H = 0.6
ROW_Y = [TOP_Y - i * ROW_H for i in range(8)]

RAW_DATA_CENTER = DOWN * 0.5
RAW_DATA_TARGET = np.array([-4.0, 0.3, 0])
RAW_DATA_WIDTH = 3.2


class Example1Runner(Slide, FrequencyTableTemplate):
    """Example 1 (I DO): Runner Daily Distances -- class limits given,
    boundaries revealed lower-column-then-upper-column with no arithmetic
    shown, then tallied, then frequency + total."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_heading("Example 1 (I DO): Runner Daily Distances (miles)")

        data_mobs = self.show_raw_data(RUNNER, per_row=6, font_size=32, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        table = self.build_table_grid(CLASS_LABELS, HEADERS, COL_X, ROW_Y, font_size=22, label_font_size=20)

        # Class boundaries: lower column first (all rows), then upper column
        # (all rows) -- no work shown, entry by entry.
        self.reveal_boundaries(table["col_left"][1], LOWER, UPPER, font_size=22)

        # Tally: one continuous pass over the raw data.
        row_indices = bucket_by_boundaries(RUNNER, BOUNDARIES)
        counts = self.run_tally_phase(data_mobs, row_indices, table["col_left"][2])

        # Frequency column, then the total -- one column-major pass.
        total = sum(counts)
        freq_points = table["col_center"][3] + [table["total_center"][3]]
        freq_strs = [str(c) for c in counts] + [str(total)]
        self.reveal_column(freq_points, freq_strs, font_size=22, last_bold=True)

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_analysis()

    def show_analysis(self):
        self.show_heading("Example 1: Analysis")

        qa = VGroup(
            Text("a) What is the modal class (highest frequency)?", font_size=28),
            Text("3 - 4 miles has the highest frequency (f = 5)", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        qb = VGroup(
            Text("b) What percent of data points are less than 3.5 miles?", font_size=28),
            Text("1.2, 1.8, 2.3, 2.7, 3.1, 3.4  =  6 out of 12", font_size=26, color=BLUE),
            Text("6 / 12 = 50%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        qc = VGroup(
            Text("c) What percent of data points are more than 4.5 miles?", font_size=28),
            Text("4.9, 5.2, 5.8  =  3 out of 12", font_size=26, color=BLUE),
            Text("3 / 12 = 25%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        block = VGroup(qa, qb, qc).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        block.move_to(ORIGIN).shift(DOWN * 0.2)

        for q in block:
            for m in q:
                self.play(FadeIn(m, shift=UP * 0.2))
                self.next_slide()
