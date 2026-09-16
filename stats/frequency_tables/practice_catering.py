from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate

MEALS = "F F C F B F F F C F F B F F C F F F B F F F F C F F F F C F".split()

CLASS_LABELS = ["B", "C", "F"]

COL_X = [0.5, 1.6, 4.2, 5.3, 6.6]
TOP_Y = 1.8
ROW_H = 0.7
ROW_Y = [TOP_Y - i * ROW_H for i in range(6)]

RAW_DATA_CENTER = DOWN * 0.5
RAW_DATA_TARGET = np.array([-3.1, 0.25, 0])
RAW_DATA_WIDTH = 3.8


def bucket(value):
    return CLASS_LABELS.index(value)


class PracticeCatering(Slide, FrequencyTableTemplate):
    """Student Practice 2: Catering Preferences at a Reception (categorical)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def _legend(self, heading):
        legend = Text("B = Beef    C = Chicken    F = Fish", font_size=22, color=BLUE)
        legend.next_to(heading, DOWN, buff=0.25)
        self.play(FadeIn(legend))
        self.next_slide()
        return legend

    def show_practice(self):
        heading = self.show_heading("Student Practice 2: Catering Preferences at a Reception")
        self._legend(heading)

        data_mobs = self.show_raw_data(MEALS, per_row=10, font_size=32, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        self.build_table_skeleton(
            CLASS_LABELS,
            ["Meal Choice", "Tally", "Freq. (f)", "Percent"],
            COL_X,
            ROW_Y,
            font_size=24,
            label_font_size=22,
        )

        self.show_timer(240, position=np.array([-6.0, 1.8, 0]))

    def show_solution(self):
        heading = self.show_heading("Student Practice 2: Solution")
        self._legend(heading)

        data_mobs = self.show_raw_data(MEALS, per_row=10, font_size=32, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        table = self.build_table_skeleton(
            CLASS_LABELS,
            ["Meal Choice", "Tally", "Freq. (f)", "Percent"],
            COL_X,
            ROW_Y,
            font_size=24,
            label_font_size=22,
        )

        row_indices = [bucket(v) for v in MEALS]
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

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_analysis_questions()

    def show_analysis_questions(self):
        self.show_heading("Student Practice 2: Analysis")

        qb = VGroup(
            Text("b) What proportion of guests selected Fish (F)?", font_size=28),
            Text("22 / 30 = 73.3%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        qb.move_to(UP * 1.6)

        for m in qb:
            self.play(FadeIn(m, shift=UP * 0.2))
            self.next_slide()

        qc = VGroup(
            Text("c) Cultural Context: why did guests overwhelmingly choose Fish?", font_size=28),
            Text(
                "The reception was held on a Friday. In traditional Catholic\n"
                "custom, the faithful abstain from meat on Fridays as a form of\n"
                "penance, so guests chose fish instead of beef or chicken.",
                font_size=27,
                line_spacing=1.25,
                color=YELLOW,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        qc.next_to(qb, DOWN, buff=0.8, aligned_edge=LEFT)

        for m in qc:
            self.play(FadeIn(m, shift=UP * 0.2))
            self.next_slide()
