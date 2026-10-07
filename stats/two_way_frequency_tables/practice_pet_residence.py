from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.two_way_frequency_table import TwoWayFrequencyTableTemplate, NUMERATOR_COLOR, DENOMINATOR_COLOR

DATA = [
    ("Dog", "House"), ("Cat", "Apartment"), ("Dog", "Apartment"), ("Dog", "House"), ("Cat", "House"),
    ("Cat", "Apartment"), ("Dog", "House"), ("Dog", "Apartment"), ("Cat", "Apartment"), ("Dog", "House"),
    ("Cat", "House"), ("Dog", "House"), ("Cat", "Apartment"), ("Dog", "Apartment"), ("Dog", "House"),
    ("Cat", "Apartment"), ("Dog", "House"), ("Cat", "House"), ("Cat", "Apartment"), ("Dog", "House"),
]

ROW_LABELS = ["Dog Pet", "Cat Pet"]
COL_LABELS = ["House Residence", "Apartment Residence"]

COL_X_TALLY = [-1.0, 0.6, 3.0, 5.4]
COL_X_FREQ = [-1.0, 0.6, 3.0, 5.4, 6.8]
ROW_Y_TALLY = [1.8, 0.9, 0.0, -0.9]
ROW_Y_FREQ = [1.8, 0.9, 0.0, -0.9, -1.8]

DATA_CENTER = DOWN * 0.3
DATA_TARGET = np.array([-4.3, -0.5, 0])
DATA_WIDTH = 4.6

LEFT_PANEL_ANCHOR = np.array([-4.3, -0.3, 0])


def row_bucket(pet):
    return 0 if pet == "Dog" else 1


def col_bucket(residence):
    return 0 if residence == "House" else 1


class PracticePetResidence(Slide, TwoWayFrequencyTableTemplate):
    """Student Practice 3: Pet Type vs. Residence Type (categorical vs. categorical)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def show_practice(self):
        heading = self.show_heading("Student Practice 3: Pet Type vs. Residence Type")
        self.show_legend(
            "Row (A): Pet Preference -- Dog Pet, Cat Pet",
            "Column (B): Residence -- House Residence, Apartment Residence",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=4, font_size=24, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=20, label_font_size=18)
        self.reveal_tags(tally["headers"], tally["row_texts"])

        self.show_timer(300, position=np.array([-6.3, 2.2, 0]))

    def show_solution(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Student Practice 3: Solution -- Tally")
        self.show_legend(
            "Row (A): Pet Preference -- Dog Pet, Cat Pet",
            "Column (B): Residence -- House Residence, Apartment Residence",
            below=heading,
            font_size=20,
        )

        data_mobs = self.show_ordered_pairs(DATA, per_row=4, font_size=24, center=DATA_CENTER)
        self.shrink_ordered_pairs(data_mobs, target_point=DATA_TARGET, width=DATA_WIDTH)

        tally = self.build_tally_grid(ROW_LABELS, COL_LABELS, COL_X_TALLY, ROW_Y_TALLY, font_size=20, label_font_size=18)
        self.reveal_tags(tally["headers"], tally["row_texts"])

        cell_indices = [(row_bucket(pet), col_bucket(residence)) for pet, residence in DATA]
        counts = self.run_tally_phase_stepped(data_mobs, cell_indices, tally["tally_anchors"])

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        heading = self.show_heading("Student Practice 3: Solution -- Frequency Table")
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
        self.show_heading("Student Practice 3: Analysis Questions")

        col_x, row_y = freq["col_x"], freq["row_y"]
        grand_total = row_totals[0] + row_totals[1]

        denom = self.col_region(col_x, row_y, col_idx=0, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=0, color=NUMERATOR_COLOR)
        self.answer_question(
            "a) Of the pet owners who live in a House, what percent own a Dog?",
            denom, numer, "R1C1 Entry", "C1 Total",
            counts[0][0], col_totals[0], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.row_region(col_x, row_y, row_idx=1, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=1, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "b) Of the Cat Pet owners, what percent live in an Apartment?",
            denom, numer, "R2C2 Entry", "R2 Total",
            counts[1][1], row_totals[1], anchor=LEFT_PANEL_ANCHOR,
        )

        denom = self.whole_table_region(col_x, row_y, color=DENOMINATOR_COLOR)
        numer = self.cell_region(col_x, row_y, row_idx=0, col_idx=1, color=NUMERATOR_COLOR)
        self.answer_question(
            "c) What percent own a Dog Pet AND live in an Apartment?",
            denom, numer, "R1C2 Entry", "Grand Total",
            counts[0][1], grand_total, anchor=LEFT_PANEL_ANCHOR,
        )
