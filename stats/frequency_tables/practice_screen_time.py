from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate

SCREEN_TIME = [
    112, 145, 210, 188, 95,
    240, 165, 178, 130, 205,
    222, 150, 185, 118, 255,
    190, 172, 160, 230, 140,
    198, 175, 162, 208, 182,
]

CLASSES = [(90, 129), (130, 169), (170, 209), (210, 249), (250, 289)]
CLASS_LABELS = [f"{lo}-{hi}" for lo, hi in CLASSES]

COL_X = [0.3, 1.9, 4.3, 5.4, 6.8]
TOP_Y = 2.6
ROW_H = 0.6
ROW_Y = [TOP_Y - i * ROW_H for i in range(8)]

RAW_DATA_CENTER = DOWN * 0.5
RAW_DATA_TARGET = np.array([-3.2, 0.25, 0])
RAW_DATA_WIDTH = 3.2


def bucket(value):
    for i, (lo, hi) in enumerate(CLASSES):
        if lo <= value <= hi:
            return i
    raise ValueError(value)


class PracticeScreenTime(Slide, FrequencyTableTemplate):
    """Student Practice 1: Daily Screen Time Analysis (quantitative)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def show_practice(self):
        self.show_heading("Student Practice 1: Daily Screen Time Analysis (minutes)")

        data_mobs = self.show_raw_data(SCREEN_TIME, per_row=5, font_size=30, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        self.build_table_skeleton(
            CLASS_LABELS,
            ["Screen Time", "Tally", "Freq. (f)", "Percent"],
            COL_X,
            ROW_Y,
            font_size=22,
            label_font_size=20,
        )

        self.show_timer(300, position=np.array([-6.0, 2.2, 0]))

    def show_solution(self):
        self.show_heading("Student Practice 1: Solution")

        data_mobs = self.show_raw_data(SCREEN_TIME, per_row=5, font_size=30, center=RAW_DATA_CENTER)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        table = self.build_table_skeleton(
            CLASS_LABELS,
            ["Screen Time", "Tally", "Freq. (f)", "Percent"],
            COL_X,
            ROW_Y,
            font_size=22,
            label_font_size=20,
        )

        row_indices = [bucket(v) for v in SCREEN_TIME]
        counts = self.run_tally_phase(data_mobs, row_indices, table["tally_anchors"])

        total = sum(counts)
        rows = []
        for i, c in enumerate(counts):
            pct = round(c / total * 100)
            rows.append((table["freq_slots"][i], str(c), table["percent_slots"][i], f"{pct}%"))
        self.reveal_row_counts(rows, font_size=22)

        self.reveal_total(
            table["freq_total_slot"], str(total),
            table["percent_total_slot"], "100%",
            font_size=22,
        )

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_analysis_questions()

    def show_analysis_questions(self):
        self.show_heading("Student Practice 1: Analysis")

        qa = VGroup(
            Text(
                "a) What percentage of students spent 170 minutes or more on their phones?",
                font_size=28,
            ),
            Text(
                "170-209 (10) + 210-249 (4) + 250-289 (1) = 15 out of 25 students",
                font_size=26,
                color=BLUE,
            ),
            Text("15 / 25 = 60%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        qa.move_to(UP * 1.1)

        for m in qa:
            self.play(FadeIn(m, shift=UP * 0.2))
            self.next_slide()

        qb = VGroup(
            Text(
                "b) What interval represents the modal class (most frequent range)?",
                font_size=28,
            ),
            Text("170-209 has the highest frequency (f = 10)", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        qb.next_to(qa, DOWN, buff=0.7, aligned_edge=LEFT)

        for m in qb:
            self.play(FadeIn(m, shift=UP * 0.2))
            self.next_slide()
