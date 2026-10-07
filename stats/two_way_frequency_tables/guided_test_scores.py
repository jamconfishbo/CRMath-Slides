from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.two_way_frequency_table import TwoWayFrequencyTableTemplate, NUMERATOR_COLOR, DENOMINATOR_COLOR

DATA = [
    (72, "STEM"), (88, "Arts"), (95, "STEM"), (80, "Arts"),
    (78, "STEM"), (91, "Arts"), (84, "Arts"), (98, "STEM"),
    (70, "STEM"), (86, "Arts"), (92, "STEM"), (75, "Arts"),
    (89, "STEM"), (81, "Arts"), (96, "STEM"), (77, "STEM"),
]

ROW_LABELS = ["70-84 Score", "85-100 Score"]
COL_LABELS = ["STEM Subject", "Arts Subject"]

COL_X_TALLY = [-1.0, 0.6, 3.0, 5.4]
COL_X_FREQ = [-1.0, 0.6, 3.0, 5.4, 6.8]
ROW_Y_TALLY = [1.8, 0.9, 0.0, -0.9]
ROW_Y_FREQ = [1.8, 0.9, 0.0, -0.9, -1.8]

DATA_CENTER = ORIGIN
DATA_TARGET = np.array([-4.3, -0.5, 0])
DATA_WIDTH = 4.4

LEFT_PANEL_ANCHOR = np.array([-4.3, -0.3, 0])


def row_bucket(score):
    return 0 if score <= 84 else 1


def col_bucket(subject):
    return 0 if subject == "STEM" else 1


class GuidedTestScores(Slide, TwoWayFrequencyTableTemplate):
    """Guided Example 1: Test Scores vs. Preferred Subject (numerical bin vs. categorical)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Guided Example 1: Test Scores vs. Preferred Subject")
        legend = self.show_legend(
            "Row (A): Test Score Bins -- 70-84 Score, 85-100 Score",
            "Column (B): Preferred Subject -- STEM Subject, Arts Subject",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=4, font_size=28, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=22, label_font_size=22)
        col_tags, row_tags = self.reveal_tags(tally["headers"], tally["row_texts"])

        cell_indices = [(row_bucket(score), col_bucket(subject)) for score, subject in DATA]
        counts = self.run_tally_phase_stepped(data_mobs, cell_indices, tally["tally_anchors"])

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        heading = self.show_heading("Guided Example 1: Frequency Table")
        freq = self.build_frequency_grid(ROW_LABELS, COL_LABELS, COL_X_FREQ, ROW_Y_FREQ, font_size=22, label_font_size=22)
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
        heading = self.show_heading("Guided Example 1: Analysis Questions")

        col_x, row_y = freq["col_x"], freq["row_y"]
        grand_total = row_totals[0] + row_totals[1]

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.row_region(col_x, row_y, row_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "a) What percent of students scored in the 85-100 Score range?",
            denom, numer, "R2 Total", "Grand Total",
            row_totals[1], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.col_region(col_x, row_y, col_idx=0, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=1, col_idx=0, color=NUMERATOR_COLOR)
        self.answer_question(
            "b) Of the students who prefer STEM, what percent scored 85-100?",
            denom, numer, "R2C1 Entry", "C1 Total",
            counts[1][0], col_totals[0], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.row_region(col_x, row_y, row_idx=0, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "c) Of the students who scored 70-84, what percent prefer Arts?",
            denom, numer, "R1C2 Entry", "R1 Total",
            counts[0][1], row_totals[0], anchor=LEFT_PANEL_ANCHOR,
        )
