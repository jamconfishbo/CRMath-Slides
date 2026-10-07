from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.two_way_frequency_table import TwoWayFrequencyTableTemplate, NUMERATOR_COLOR, DENOMINATOR_COLOR

DATA = [
    (19, 2), (1, 6), (5, 8), (15, 1), (8, 4), (11, 3),
    (2, 7), (18, 2), (7, 6), (14, 8), (4, 1), (10, 5),
]

ROW_LABELS = ["0-9 Hours Screen", "10-19 Hours Screen"]
COL_LABELS = ["0-4 Hours Study", "5-9 Hours Study"]

COL_X_TALLY = [-1.0, 0.6, 3.0, 5.4]
COL_X_FREQ = [-1.0, 0.6, 3.0, 5.4, 6.8]
ROW_Y_TALLY = [1.8, 0.9, 0.0, -0.9]
ROW_Y_FREQ = [1.8, 0.9, 0.0, -0.9, -1.8]

DATA_CENTER = ORIGIN
DATA_TARGET = np.array([-4.3, -0.5, 0])
DATA_WIDTH = 3.6

LEFT_PANEL_ANCHOR = np.array([-4.3, -0.3, 0])


def row_bucket(screen_hours):
    return 0 if screen_hours <= 9 else 1


def col_bucket(study_hours):
    return 0 if study_hours <= 4 else 1


class GuidedScreenStudy(Slide, TwoWayFrequencyTableTemplate):
    """Guided Example 2: Screen Time vs. Study Time (numerical vs. numerical)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Guided Example 2: Screen Time vs. Study Time")
        self.show_legend(
            "Row (A): Screen Time -- 0-9 Hours Screen, 10-19 Hours Screen",
            "Column (B): Study Time -- 0-4 Hours Study, 5-9 Hours Study",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=4, font_size=30, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=20, label_font_size=20)
        self.reveal_tags(tally["headers"], tally["row_texts"])

        cell_indices = [(row_bucket(screen), col_bucket(study)) for screen, study in DATA]
        counts = self.run_tally_phase_stepped(data_mobs, cell_indices, tally["tally_anchors"])

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        heading = self.show_heading("Guided Example 2: Frequency Table")
        freq = self.build_frequency_grid(ROW_LABELS, COL_LABELS, COL_X_FREQ, ROW_Y_FREQ, font_size=22, label_font_size=20)
        self.reveal_tags(freq["headers"], freq["row_texts"])

        self.reveal_cell_frequencies(freq["cell_points"], counts, font_size=22)

        row_totals = []
        for i in range(2):
            _, total = self.reveal_total_with_addition(freq["row_total_points"][i], counts[i], font_size=20)
            row_totals.append(total)

        col_totals = []
        for j in range(2):
            _, total = self.reveal_total_with_addition(
                freq["col_total_points"][j], [counts[0][j], counts[1][j]], font_size=20,
            )
            col_totals.append(total)

        self.reveal_total_with_addition(freq["grand_total_point"], row_totals, font_size=20)

        self.play(FadeOut(heading))
        heading = self.show_heading("Guided Example 2: Analysis Questions")

        col_x, row_y = freq["col_x"], freq["row_y"]
        grand_total = row_totals[0] + row_totals[1]

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.col_region(col_x, row_y, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "a) What percent of all students study 5-9 Hours Study per week?",
            denom, numer, "C2 Total", "Grand Total",
            col_totals[1], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.row_region(col_x, row_y, row_idx=1, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=1, col_idx=0, color=NUMERATOR_COLOR)
        self.answer_question(
            "b) Of 10-19 Hours Screen students, what percent study 0-4 Hours?",
            denom, numer, "R2C1 Entry", "R2 Total",
            counts[1][0], row_totals[1], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "c) What percent have 0-9 Hours Screen AND 5-9 Hours Study?",
            denom, numer, "R1C2 Entry", "Grand Total",
            counts[0][1], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )
