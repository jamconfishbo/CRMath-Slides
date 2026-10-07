from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.two_way_frequency_table import TwoWayFrequencyTableTemplate, NUMERATOR_COLOR, DENOMINATOR_COLOR

DATA = [
    (3, 30), (8, 65), (2, 55), (7, 40), (10, 70),
    (4, 25), (9, 60), (5, 50), (1, 35), (6, 55),
    (8, 45), (3, 60), (7, 75), (2, 20), (9, 50),
    (4, 40), (6, 30), (1, 65), (10, 55), (5, 35),
]

ROW_LABELS = ["1-5k Steps", "6-10k Steps"]
COL_LABELS = ["20-49 oz Water", "50-79 oz Water"]

COL_X_TALLY = [-1.0, 0.6, 3.0, 5.4]
COL_X_FREQ = [-1.0, 0.6, 3.0, 5.4, 6.8]
ROW_Y_TALLY = [1.8, 0.9, 0.0, -0.9]
ROW_Y_FREQ = [1.8, 0.9, 0.0, -0.9, -1.8]

DATA_CENTER = DOWN * 0.3
DATA_TARGET = np.array([-4.3, -0.5, 0])
DATA_WIDTH = 4.6

LEFT_PANEL_ANCHOR = np.array([-4.3, -0.3, 0])


def row_bucket(steps_thousands):
    return 0 if steps_thousands <= 5 else 1


def col_bucket(water_oz):
    return 0 if water_oz <= 49 else 1


class PracticeStepsWater(Slide, TwoWayFrequencyTableTemplate):
    """Student Practice 2: Daily Steps vs. Daily Water Intake (numerical vs. numerical)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def show_practice(self):
        heading = self.show_heading("Student Practice 2: Daily Steps vs. Daily Water Intake")
        self.show_legend(
            "Row (A): Daily Steps -- 1-5k Steps, 6-10k Steps",
            "Column (B): Daily Water -- 20-49 oz Water, 50-79 oz Water",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=5, font_size=26, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=20, label_font_size=18)
        self.reveal_tags(tally["headers"], tally["row_texts"])

        self.show_timer(300, position=np.array([-6.3, 2.2, 0]))

    def show_solution(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Student Practice 2: Solution -- Tally")
        self.show_legend(
            "Row (A): Daily Steps -- 1-5k Steps, 6-10k Steps",
            "Column (B): Daily Water -- 20-49 oz Water, 50-79 oz Water",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=5, font_size=26, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=20, label_font_size=18)
        self.reveal_tags(tally["headers"], tally["row_texts"])

        cell_indices = [(row_bucket(steps), col_bucket(water)) for steps, water in DATA]
        counts = self.run_tally_phase_stepped(data_mobs, cell_indices, tally["tally_anchors"])

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        heading = self.show_heading("Student Practice 2: Solution -- Frequency Table")
        freq = self.build_frequency_grid(ROW_LABELS, COL_LABELS, COL_X_FREQ, ROW_Y_FREQ, font_size=20, label_font_size=18)
        self.reveal_tags(freq["headers"], freq["row_texts"])

        self.reveal_cell_frequencies(freq["cell_points"], counts, font_size=20)

        row_totals = []
        for i in range(2):
            _, total = self.reveal_total_with_addition(freq["row_total_points"][i], counts[i], font_size=18)
            row_totals.append(total)

        col_totals = []
        for j in range(2):
            _, total = self.reveal_total_with_addition(
                freq["col_total_points"][j], [counts[0][j], counts[1][j]], font_size=18,
            )
            col_totals.append(total)

        self.reveal_total_with_addition(freq["grand_total_point"], row_totals, font_size=18)

        self.play(FadeOut(heading))
        self.next_slide()

        self.show_analysis_questions(freq, counts, row_totals, col_totals)

    def show_analysis_questions(self, freq, counts, row_totals, col_totals):
        self.show_heading("Student Practice 2: Analysis Questions")

        col_x, row_y = freq["col_x"], freq["row_y"]
        grand_total = row_totals[0] + row_totals[1]

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.row_region(col_x, row_y, row_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "a) What percent of all participants take 6-10k Steps daily?",
            denom, numer, "R2 Total", "Grand Total",
            row_totals[1], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.col_region(col_x, row_y, col_idx=1, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=1, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "b) Of those who drink 50-79 oz Water, what percent take 6-10k Steps?",
            denom, numer, "R2C2 Entry", "C2 Total",
            counts[1][1], col_totals[1], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.row_region(col_x, row_y, row_idx=0, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=0, color=NUMERATOR_COLOR)
        self.answer_question(
            "c) Of those who take 1-5k Steps, what percent drink 20-49 oz Water?",
            denom, numer, "R1C1 Entry", "R1 Total",
            counts[0][0], row_totals[0], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "d) What percent take 1-5k Steps AND drink 50-79 oz Water daily?",
            denom, numer, "R1C2 Entry", "Grand Total",
            counts[0][1], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )
