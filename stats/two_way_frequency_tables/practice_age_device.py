from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.two_way_frequency_table import TwoWayFrequencyTableTemplate, NUMERATOR_COLOR, DENOMINATOR_COLOR

DATA = [
    (11, "Tablet"), (16, "Phone"), (13, "Phone"), (17, "Phone"), (10, "Tablet"),
    (15, "Tablet"), (12, "Phone"), (18, "Phone"), (14, "Tablet"), (16, "Phone"),
    (12, "Tablet"), (17, "Phone"), (11, "Phone"), (15, "Tablet"), (13, "Tablet"),
    (18, "Phone"), (10, "Tablet"), (16, "Phone"), (14, "Phone"), (17, "Tablet"),
]

ROW_LABELS = ["10-14 Yrs Age", "15-18 Yrs Age"]
COL_LABELS = ["Phone Device", "Tablet Device"]

COL_X_TALLY = [-1.0, 0.6, 3.0, 5.4]
COL_X_FREQ = [-1.0, 0.6, 3.0, 5.4, 6.8]
ROW_Y_TALLY = [1.8, 0.9, 0.0, -0.9]
ROW_Y_FREQ = [1.8, 0.9, 0.0, -0.9, -1.8]

DATA_CENTER = DOWN * 0.3
DATA_TARGET = np.array([-4.3, -0.5, 0])
DATA_WIDTH = 4.6

LEFT_PANEL_ANCHOR = np.array([-4.3, -0.3, 0])


def row_bucket(age):
    return 0 if age <= 14 else 1


def col_bucket(device):
    return 0 if device == "Phone" else 1


class PracticeAgeDevice(Slide, TwoWayFrequencyTableTemplate):
    """Student Practice 1: Age vs. Primary Tech Device (numerical bin vs. categorical)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def show_practice(self):
        heading = self.show_heading("Student Practice 1: Age vs. Primary Tech Device")
        self.show_legend(
            "Row (A): Age Bins -- 10-14 Yrs Age, 15-18 Yrs Age",
            "Column (B): Primary Device -- Phone Device, Tablet Device",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=5, font_size=26, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=20, label_font_size=20)
        self.reveal_tags(tally["headers"], tally["row_texts"])

        self.show_timer(300, position=np.array([-6.3, 2.2, 0]))

    def show_solution(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Student Practice 1: Solution -- Tally")
        self.show_legend(
            "Row (A): Age Bins -- 10-14 Yrs Age, 15-18 Yrs Age",
            "Column (B): Primary Device -- Phone Device, Tablet Device",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=5, font_size=26, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=20, label_font_size=20)
        self.reveal_tags(tally["headers"], tally["row_texts"])

        cell_indices = [(row_bucket(age), col_bucket(device)) for age, device in DATA]
        counts = self.run_tally_phase_stepped(data_mobs, cell_indices, tally["tally_anchors"])

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        heading = self.show_heading("Student Practice 1: Solution -- Frequency Table")
        freq = self.build_frequency_grid(ROW_LABELS, COL_LABELS, COL_X_FREQ, ROW_Y_FREQ, font_size=20, label_font_size=20)
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
        self.show_heading("Student Practice 1: Analysis Questions")

        col_x, row_y = freq["col_x"], freq["row_y"]
        grand_total = row_totals[0] + row_totals[1]

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.col_region(col_x, row_y, col_idx=0, color=NUMERATOR_COLOR)
        self.answer_question(
            "a) What percent of all respondents prefer a Phone Device?",
            denom, numer, "C1 Total", "Grand Total",
            col_totals[0], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.row_region(col_x, row_y, row_idx=1, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=1, col_idx=0, color=NUMERATOR_COLOR)
        self.answer_question(
            "b) Of the participants aged 15-18, what percent prefer Phone?",
            denom, numer, "R2C1 Entry", "R2 Total",
            counts[1][0], row_totals[1], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.col_region(col_x, row_y, col_idx=1, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "c) Of the respondents who prefer Tablet, what percent are 10-14?",
            denom, numer, "R1C2 Entry", "C2 Total",
            counts[0][1], col_totals[1], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=0, color=NUMERATOR_COLOR)
        self.answer_question(
            "d) What percent are 10-14 Yrs Age AND prefer a Phone Device?",
            denom, numer, "R1C1 Entry", "Grand Total",
            counts[0][0], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )
