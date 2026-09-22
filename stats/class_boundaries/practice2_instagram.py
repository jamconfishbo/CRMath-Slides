from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.frequency_table import FrequencyTableTemplate, bucket_by_boundaries

INSTA = [
    1.2, 1.5, 2.1, 2.8, 3.0, 3.4, 3.9, 4.1, 4.5, 4.8,
    5.2, 5.6, 6.1, 6.7, 7.3, 8.0, 8.4, 9.1, 9.5, 9.9,
]

HEADERS = ["Class Limits", "Class Boundaries", "Tally", "Frequency (f)"]
COL_X = [0.3, 1.6, 3.6, 5.8, 6.9]

RAW_DATA_TARGET = np.array([-3.0, 0.9, 0])
RAW_DATA_WIDTH = 4.0
TIMER_POSITION = np.array([-6.3, 2.3, 0])

# Table A: k = 2 -- too few bins. Start at a convenient integer <= min (1.2) -> 1.
A_LABELS = ["1 - 5", "6 - 10"]
A_LOWER = ["0.5", "5.5"]
A_UPPER = ["5.5", "10.5"]
A_BOUNDARIES = [(0.5, 5.5), (5.5, 10.5)]
A_TOP_Y, A_ROW_H = 2.5, 0.6
A_ROW_Y = [A_TOP_Y - i * A_ROW_H for i in range(5)]

# Table B: k = 5 -- appropriate number of bins. Same integer start = 1.
B_LABELS = ["1 - 2", "3 - 4", "5 - 6", "7 - 8", "9 - 10"]
B_LOWER = ["0.5", "2.5", "4.5", "6.5", "8.5"]
B_UPPER = ["2.5", "4.5", "6.5", "8.5", "10.5"]
B_BOUNDARIES = [(0.5, 2.5), (2.5, 4.5), (4.5, 6.5), (6.5, 8.5), (8.5, 10.5)]
B_TOP_Y, B_ROW_H = 2.6, 0.6
B_ROW_Y = [B_TOP_Y - i * B_ROW_H for i in range(8)]


class Practice2Instagram(Slide, FrequencyTableTemplate):
    """Practice 2 (YOU DO), Part 3: same 20-value data set binned two ways --
    Table A (k=2, too few bins) then Table B (k=5, appropriate)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.table_a_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.table_a_solution()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.table_b_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.table_b_solution()

    # ---- Table A ----

    def table_a_practice(self):
        self.show_heading("Practice 2 (YOU DO): Instagram Followers -- Table A (k = 2)")

        data_mobs = self.show_raw_data(INSTA, per_row=10, font_size=26, center=DOWN * 1.3)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        self.build_table_grid(["", ""], HEADERS, COL_X, A_ROW_Y, font_size=22, label_font_size=20)

        self.show_timer(300, position=TIMER_POSITION, font_size=32, bar_height=3.0)

    def table_a_solution(self):
        heading = self.show_heading("Table A Solution (k = 2, too few bins)")

        data_mobs = self.show_raw_data(INSTA, per_row=10, font_size=26, center=DOWN * 1.3)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        range_line = MathTex(r"\text{Range} = 9.9 - 1.2 = 8.7", font_size=28)
        range_line.move_to(np.array([-3.0, 2.9, 0]))
        self.play(Write(range_line))
        self.next_slide()

        width_line = MathTex(
            r"\text{Width} = \frac{8.7}{2} = 4.35 \rightarrow \text{round UP to } 5",
            font_size=28,
        )
        width_line.move_to(np.array([-3.0, 2.45, 0]))
        self.play(Write(width_line))
        self.next_slide()

        start_line = MathTex(
            r"\text{Start at a convenient integer} \leq \text{min (1.2)} \rightarrow \text{Start} = 1",
            font_size=26,
        )
        start_line.move_to(np.array([-3.0, 2.0, 0]))
        self.play(Write(start_line))
        self.next_slide()

        table = self.build_table_grid(["", ""], HEADERS, COL_X, A_ROW_Y, font_size=22, label_font_size=20)

        self.reveal_column(table["col_center"][0], A_LABELS, font_size=22, color=WHITE)
        self.reveal_boundaries(table["col_left"][1], A_LOWER, A_UPPER, font_size=22)

        row_indices = bucket_by_boundaries(INSTA, A_BOUNDARIES)
        counts = self.run_tally_phase(data_mobs, row_indices, table["col_left"][2])

        total = sum(counts)
        freq_points = table["col_center"][3] + [table["total_center"][3]]
        freq_strs = [str(c) for c in counts] + [str(total)]
        self.reveal_column(freq_points, freq_strs, font_size=22, last_bold=True)

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.critical_thinking()

    def critical_thinking(self):
        self.show_heading("Critical Thinking")

        q = Text(
            "How easy is it to determine how many students have between\n"
            "4.0 and 6.0 thousand followers using Table A?",
            font_size=28,
            line_spacing=1.2,
        )
        a = Text(
            "Not easy at all -- 4.0 to 6.0 is split across both classes\n"
            "(1-5, boundary up to 5.5, and 6-10). With only 2 broad bins\n"
            "you can only see that 11 students fall somewhere below 5.5\n"
            "and 9 fall above -- there is no way to isolate the 4.0-6.0\n"
            "range from the table alone. Too few bins hides the very\n"
            "detail you're trying to find.",
            font_size=26,
            line_spacing=1.25,
            color=YELLOW,
        )
        block = VGroup(q, a).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        block.move_to(ORIGIN)

        self.play(FadeIn(q, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeIn(a, shift=UP * 0.2))
        self.next_slide()

    # ---- Table B ----

    def table_b_practice(self):
        self.show_heading("Practice 2 (YOU DO): Instagram Followers -- Table B (k = 5)")

        data_mobs = self.show_raw_data(INSTA, per_row=10, font_size=26, center=DOWN * 1.3)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        self.build_table_grid(
            ["", "", "", "", ""], HEADERS, COL_X, B_ROW_Y, font_size=20, label_font_size=18,
        )

        self.show_timer(360, position=TIMER_POSITION, font_size=32, bar_height=3.0)

    def table_b_solution(self):
        self.show_heading("Table B Solution (k = 5, appropriate bins)")

        data_mobs = self.show_raw_data(INSTA, per_row=10, font_size=26, center=DOWN * 1.3)
        self.shrink_raw_data(data_mobs, target_point=RAW_DATA_TARGET, width=RAW_DATA_WIDTH)

        width_line = MathTex(
            r"\text{Width} = \frac{8.7}{5} = 1.74 \rightarrow \text{round UP to } 2",
            font_size=26,
        )
        width_line.move_to(np.array([-3.0, 2.9, 0]))
        self.play(Write(width_line))
        self.next_slide()

        start_line = MathTex(
            r"\text{Start at a convenient integer} \leq \text{min (1.2)} \rightarrow \text{Start} = 1",
            font_size=24,
        )
        start_line.move_to(np.array([-3.0, 2.5, 0]))
        self.play(Write(start_line))
        self.next_slide()

        table = self.build_table_grid(
            ["", "", "", "", ""], HEADERS, COL_X, B_ROW_Y, font_size=20, label_font_size=18,
        )

        self.reveal_column(table["col_center"][0], B_LABELS, font_size=20, color=WHITE)
        self.reveal_boundaries(table["col_left"][1], B_LOWER, B_UPPER, font_size=20)

        row_indices = bucket_by_boundaries(INSTA, B_BOUNDARIES)
        counts = self.run_tally_phase(data_mobs, row_indices, table["col_left"][2])

        total = sum(counts)
        freq_points = table["col_center"][3] + [table["total_center"][3]]
        freq_strs = [str(c) for c in counts] + [str(total)]
        self.reveal_column(freq_points, freq_strs, font_size=20, last_bold=True)

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_analysis()

    def show_analysis(self):
        self.show_heading("Table B: Analysis")

        qa = VGroup(
            Text("a) What is the modal class in Table B?", font_size=28),
            Text(
                "Tie: 3 - 4 and 5 - 6 both have the highest frequency (f = 5)",
                font_size=26, weight=BOLD, color=YELLOW,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        qb = VGroup(
            Text("b) What percent have less than 4.75 thousand followers?", font_size=28),
            Text("9 out of 20 students", font_size=26, color=BLUE),
            Text("9 / 20 = 45%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        qc = VGroup(
            Text("c) What percent have more than 8.35 thousand followers?", font_size=28),
            Text("4 out of 20 students", font_size=26, color=BLUE),
            Text("4 / 20 = 20%", font_size=30, weight=BOLD, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        qd = VGroup(
            Text("d) Why is Table B more useful for finding detailed ranges?", font_size=28),
            Text(
                "With 5 narrower bins, each class covers a smaller span, so you\n"
                "can pinpoint where values fall (like 4.0-6.0) far more precisely\n"
                "than Table A's two broad, uninformative bins.",
                font_size=25,
                line_spacing=1.2,
                color=YELLOW,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        block = VGroup(qa, qb, qc, qd).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        if block.width > 12.5:
            block.scale_to_fit_width(12.5)
        if block.height > 6.3:
            block.scale_to_fit_height(6.3)
        block.move_to(np.array([0, 2.7, 0]), aligned_edge=UP)

        for q in block:
            for m in q:
                self.play(FadeIn(m, shift=UP * 0.2))
                self.next_slide()
