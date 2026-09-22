from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate, bucket_by_boundaries

COFFEE = [-0.2, 0.8, 1.2, 1.5, 2.1, 2.4, 2.9, 3.2, 3.5, 3.8, 4.1, 4.4, 4.7, 5.0, 5.3, 5.9, -0.49]

CLASS_LABELS = ["0 - 1", "2 - 3", "4 - 5", "6 - 7"]
LOWER = ["-0.5", "1.5", "3.5", "5.5"]
UPPER = ["1.5", "3.5", "5.5", "7.5"]
BOUNDARIES = [(-0.5, 1.5), (1.5, 3.5), (3.5, 5.5), (5.5, 7.5)]

HEADERS = ["Class Limits", "Class Boundaries", "Tally", "Frequency (f)"]
COL_X = [0.3, 1.6, 3.6, 5.8, 6.9]
TOP_Y = 2.4
ROW_H = 0.65
ROW_Y = [TOP_Y - i * ROW_H for i in range(7)]

RAW_DATA_CENTER = DOWN * 0.5
RAW_DATA_TARGET = np.array([-3.3, 0.25, 0])
RAW_DATA_WIDTH = 3.0


class Practice1Coffee(Slide, FrequencyTableTemplate):
    """Practice 1 (YOU DO): Coffee Shop Customer Wait Times."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def show_practice(self):
        self.show_heading("Practice 1 (YOU DO): Coffee Shop Wait Times (min)")

        data_mobs = self.show_raw_data(COFFEE, per_row=6, font_size=28, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        self.build_table_grid(CLASS_LABELS, HEADERS, COL_X, ROW_Y, font_size=22, label_font_size=20)

        self.show_timer(300, position=np.array([-6.0, 2.3, 0]))

    def show_solution(self):
        self.show_heading("Practice 1: Solution")

        data_mobs = self.show_raw_data(COFFEE, per_row=6, font_size=28, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        table = self.build_table_grid(CLASS_LABELS, HEADERS, COL_X, ROW_Y, font_size=22, label_font_size=20)

        self.reveal_boundaries(table["col_left"][1], LOWER, UPPER, font_size=22)

        row_indices = bucket_by_boundaries(COFFEE, BOUNDARIES)
        counts = self.run_tally_phase(data_mobs, row_indices, table["col_left"][2])

        total = sum(counts)
        freq_points = table["col_center"][3] + [table["total_center"][3]]
        freq_strs = [str(c) for c in counts] + [str(total)]
        self.reveal_column(freq_points, freq_strs, font_size=22, last_bold=True)

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_analysis()

    def show_analysis(self):
        self.show_heading("Practice 1: Analysis")

        qa = VGroup(
            Text("a) What is the modal class?", font_size=28),
            Text("4 - 5 minutes has the highest frequency (f = 7)", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        qb = VGroup(
            Text("b) What percent of wait times are less than 3.5 minutes?", font_size=28),
            Text("9 out of 17 wait times", font_size=26, color=BLUE),
            Text("9 / 17 ≈ 52.9%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        qc = VGroup(
            Text("c) What percent of wait times are more than 4.5 minutes?", font_size=28),
            Text("4 out of 17 wait times", font_size=26, color=BLUE),
            Text("4 / 17 ≈ 23.5%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        block = VGroup(qa, qb, qc).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        block.move_to(ORIGIN).shift(DOWN * 0.2)

        for q in block:
            for m in q:
                self.play(FadeIn(m, shift=UP * 0.2))
                self.next_slide()
