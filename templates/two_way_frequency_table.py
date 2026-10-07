# templates/two_way_frequency_table.py

from manim import *

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR

GRID_COLOR = GRAY
TALLY_COLOR = WHITE
STRIKE_COLOR = GRAY
TAG_COLOR = GRAY
NUMERATOR_COLOR = BLUE
DENOMINATOR_COLOR = RED

MARK_W = 0.11
MARK_H = 0.3
GROUP_GAP = 0.18


class TwoWayFrequencyTableTemplate:
    """Mixin for 2-row x 2-column two-way frequency tables.

    Column/row "slots" throughout this file are indices into a 5-entry
    boundary list [x0..x4] / [y0..y4]: slot 0 is the row-label column /
    header row, slots 1-2 are the two data categories (C1/C2 or R1/R2),
    slot 3 is the Total column / row.

    Flow for one table:
        1. show_heading() / show_legend()
        2. show_ordered_pairs() -> shrink_ordered_pairs()
        3. build_tally_grid() -- 3x3 grid (no totals), then reveal_tags()
        4. run_tally_phase_stepped() -- one tally mark per click
        5. build_frequency_grid() -- 4x4 grid (adds Total row/col + tags)
        6. reveal_cell_frequencies() -- copy tally counts into cells
        7. reveal_row_total() / reveal_col_total() / reveal_grand_total()
           -- each shows the addition, then the sum
        8. answer_question() -- one relative-frequency word problem: red
           denominator region, blue numerator region, labeled fraction,
           numeric fraction, boxed percent answer
    """

    # ---- headings / raw data -------------------------------------------------

    def show_heading(self, text, font_size=28):
        heading = Text(text, font_size=font_size, weight=BOLD)
        heading.to_edge(UP, buff=0.3)
        self.play(FadeIn(heading))
        self.next_slide()
        return heading

    def show_legend(self, row_var_text, col_var_text, font_size=22, below=None):
        legend = VGroup(
            Text(row_var_text, font_size=font_size, color=DENOMINATOR_COLOR),
            Text(col_var_text, font_size=font_size, color=NUMERATOR_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        if below is not None:
            legend.next_to(below, DOWN, buff=0.25)
        else:
            legend.to_edge(UP, buff=1.0)
        self.play(FadeIn(legend))
        self.next_slide()
        return legend

    def show_ordered_pairs(self, pairs, per_row=4, font_size=26, center=ORIGIN):
        mobs = [Text(f"({a}, {b})", font_size=font_size) for a, b in pairs]
        grid = VGroup(*mobs).arrange_in_grid(cols=per_row, buff=(0.7, 0.35))
        grid.move_to(center)
        self.play(FadeIn(grid))
        self.next_slide()
        return mobs

    def shrink_ordered_pairs(self, mobs, target_point, width, run_time=1.0):
        grid = VGroup(*mobs)
        self.play(grid.animate.set(width=width).move_to(target_point), run_time=run_time)
        self.next_slide()
        return grid

    # ---- tally table (no totals yet) -----------------------------------------

    def build_tally_grid(self, row_labels, col_labels, col_x, row_y, font_size=24, label_font_size=22):
        """col_x: [x0,x1,x2,x3] (row-label | C1 | C2). row_y: [y0,y1,y2,y3] (header | R1 | R2)."""
        lines = VGroup()
        for x in col_x:
            lines.add(Line([x, row_y[0], 0], [x, row_y[-1], 0], color=GRID_COLOR, stroke_width=2))
        for y in row_y:
            lines.add(Line([col_x[0], y, 0], [col_x[-1], y, 0], color=GRID_COLOR, stroke_width=2))

        col_centers = [(col_x[i] + col_x[i + 1]) / 2 for i in range(3)]
        row_centers = [(row_y[i] + row_y[i + 1]) / 2 for i in range(3)]

        headers = VGroup()
        for j, label in enumerate(col_labels):
            h = Text(label, font_size=label_font_size, weight=BOLD)
            cw = col_x[j + 2] - col_x[j + 1]
            if h.width > cw - 0.1:
                h.scale_to_fit_width(cw - 0.1)
            h.move_to([col_centers[j + 1], row_centers[0], 0])
            headers.add(h)

        row_texts = VGroup()
        for i, label in enumerate(row_labels):
            lbl = Text(label, font_size=font_size)
            cw0 = col_x[1] - col_x[0]
            if lbl.width > cw0 - 0.15:
                lbl.scale_to_fit_width(cw0 - 0.15)
            lbl.move_to([col_centers[0], row_centers[i + 1], 0])
            row_texts.add(lbl)

        tally_anchors = [
            [np.array([col_x[1] + 0.15, row_centers[1], 0]), np.array([col_x[2] + 0.15, row_centers[1], 0])],
            [np.array([col_x[1] + 0.15, row_centers[2], 0]), np.array([col_x[2] + 0.15, row_centers[2], 0])],
        ]

        self.play(Create(lines), FadeIn(headers), FadeIn(row_texts))
        self.next_slide()

        return {
            "lines": lines, "headers": headers, "row_texts": row_texts,
            "col_x": col_x, "row_y": row_y,
            "col_centers": col_centers, "row_centers": row_centers,
            "tally_anchors": tally_anchors,
        }

    def reveal_tags(self, headers, row_texts, col_tags=("C1", "C2"), row_tags=("R1", "R2"), font_size=18):
        col_tag_mobs = VGroup()
        for tag, header in zip(col_tags, headers):
            t = Text(tag, font_size=font_size, color=TAG_COLOR, weight=BOLD)
            t.next_to(header, UP, buff=0.1)
            col_tag_mobs.add(t)

        row_tag_mobs = VGroup()
        for tag, row_text in zip(row_tags, row_texts):
            t = Text(tag, font_size=font_size, color=TAG_COLOR, weight=BOLD)
            t.next_to(row_text, LEFT, buff=0.12)
            row_tag_mobs.add(t)

        self.play(FadeIn(col_tag_mobs), FadeIn(row_tag_mobs))
        self.next_slide()
        return col_tag_mobs, row_tag_mobs

    def tally_stroke(self, cell_left, count):
        group_idx = count // 5
        pos_in_group = count % 5
        x0 = cell_left[0] + group_idx * (4 * MARK_W + GROUP_GAP)
        y = cell_left[1]

        if pos_in_group < 4:
            x = x0 + pos_in_group * MARK_W
            return Line([x, y - MARK_H / 2, 0], [x, y + MARK_H / 2, 0], color=TALLY_COLOR, stroke_width=3)
        else:
            return Line(
                [x0, y - MARK_H / 2, 0], [x0 + 3 * MARK_W, y + MARK_H / 2, 0],
                color=TALLY_COLOR, stroke_width=3,
            )

    def cross_out_datum(self, mob, color=STRIKE_COLOR, pad=0.06, stroke_width=4):
        return Line(
            mob.get_corner(UL) + UP * pad + LEFT * pad,
            mob.get_corner(DR) + DOWN * pad + RIGHT * pad,
            color=color, stroke_width=stroke_width,
        )

    def run_tally_phase_stepped(self, data_mobs, cell_indices, tally_anchors, indicate_color=ANSWER_COLOR):
        """One tally mark per click -- next_slide() after every single datum."""
        counts = [[0, 0], [0, 0]]
        for mob, (r, c) in zip(data_mobs, cell_indices):
            self.play(Indicate(mob, color=indicate_color, scale_factor=1.3), run_time=0.4)
            mark = self.tally_stroke(tally_anchors[r][c], counts[r][c])
            strike = self.cross_out_datum(mob)
            self.play(Create(mark), Create(strike), run_time=0.3)
            counts[r][c] += 1
            self.next_slide()
        return counts

    # ---- frequency table (with Total row/col) --------------------------------

    def build_frequency_grid(self, row_labels, col_labels, col_x, row_y, font_size=24, label_font_size=22):
        """col_x: [x0,x1,x2,x3,x4] (row-label | C1 | C2 | Total).
        row_y: [y0,y1,y2,y3,y4] (header | R1 | R2 | Total)."""
        lines = VGroup()
        for x in col_x:
            lines.add(Line([x, row_y[0], 0], [x, row_y[-1], 0], color=GRID_COLOR, stroke_width=2))
        for y in row_y:
            lines.add(Line([col_x[0], y, 0], [col_x[-1], y, 0], color=GRID_COLOR, stroke_width=2))

        col_centers = [(col_x[i] + col_x[i + 1]) / 2 for i in range(4)]
        row_centers = [(row_y[i] + row_y[i + 1]) / 2 for i in range(4)]

        headers = VGroup()
        for j, label in enumerate(col_labels):
            h = Text(label, font_size=label_font_size, weight=BOLD)
            cw = col_x[j + 2] - col_x[j + 1]
            if h.width > cw - 0.1:
                h.scale_to_fit_width(cw - 0.1)
            h.move_to([col_centers[j + 1], row_centers[0], 0])
            headers.add(h)
        total_col_header = Text("Total", font_size=label_font_size, weight=BOLD)
        total_col_header.move_to([col_centers[3], row_centers[0], 0])
        headers.add(total_col_header)

        row_texts = VGroup()
        for i, label in enumerate(row_labels):
            lbl = Text(label, font_size=font_size)
            cw0 = col_x[1] - col_x[0]
            if lbl.width > cw0 - 0.15:
                lbl.scale_to_fit_width(cw0 - 0.15)
            lbl.move_to([col_centers[0], row_centers[i + 1], 0])
            row_texts.add(lbl)
        total_row_label = Text("Total", font_size=font_size, weight=BOLD)
        total_row_label.move_to([col_centers[0], row_centers[3], 0])
        row_texts.add(total_row_label)

        cell_points = [
            [np.array([col_centers[1], row_centers[1], 0]), np.array([col_centers[2], row_centers[1], 0])],
            [np.array([col_centers[1], row_centers[2], 0]), np.array([col_centers[2], row_centers[2], 0])],
        ]
        row_total_points = [
            np.array([col_centers[3], row_centers[1], 0]),
            np.array([col_centers[3], row_centers[2], 0]),
        ]
        col_total_points = [
            np.array([col_centers[1], row_centers[3], 0]),
            np.array([col_centers[2], row_centers[3], 0]),
        ]
        grand_total_point = np.array([col_centers[3], row_centers[3], 0])

        self.play(Create(lines), FadeIn(headers), FadeIn(row_texts))
        self.next_slide()

        return {
            "lines": lines, "headers": headers, "row_texts": row_texts,
            "col_x": col_x, "row_y": row_y,
            "col_centers": col_centers, "row_centers": row_centers,
            "cell_points": cell_points,
            "row_total_points": row_total_points,
            "col_total_points": col_total_points,
            "grand_total_point": grand_total_point,
        }

    def reveal_cell_frequencies(self, cell_points, counts, font_size=24, color=ANSWER_COLOR):
        mobs = [[None, None], [None, None]]
        for i in range(2):
            for j in range(2):
                m = Text(str(counts[i][j]), font_size=font_size, color=color).move_to(cell_points[i][j])
                self.play(FadeIn(m, shift=UP * 0.1))
                self.next_slide()
                mobs[i][j] = m
        return mobs

    def reveal_total_with_addition(self, point, addends, font_size=22, color=ANSWER_COLOR):
        """Shows "a + b" in place, then transforms it into the sum (bold,
        circumscribed). Returns (final_mobject, total)."""
        total = sum(addends)
        expr_text = " + ".join(str(a) for a in addends)
        expr_mob = Text(expr_text, font_size=font_size).move_to(point)
        self.play(FadeIn(expr_mob))
        self.next_slide()

        total_mob = Text(str(total), font_size=font_size, weight=BOLD, color=color).move_to(point)
        self.play(Transform(expr_mob, total_mob))
        self.play(Circumscribe(expr_mob, color=color))
        self.next_slide()
        return expr_mob, total

    # ---- highlighted relative-frequency word problems ------------------------

    def region_rect(self, col_x, row_y, col_slots, row_slots, color, opacity=0.22):
        x0, x1 = col_x[col_slots[0]], col_x[col_slots[1]]
        y0, y1 = row_y[row_slots[0]], row_y[row_slots[1]]
        rect = Rectangle(
            width=x1 - x0, height=y0 - y1,
            fill_color=color, fill_opacity=opacity,
            stroke_color=color, stroke_width=3,
        )
        rect.move_to([(x0 + x1) / 2, (y0 + y1) / 2, 0])
        return rect

    def whole_table_region(self, col_x, row_y, color=DENOMINATOR_COLOR):
        return self.region_rect(col_x, row_y, (0, 4), (0, 4), color)

    def row_region(self, col_x, row_y, row_idx, color):
        """row_idx: 0 for R1, 1 for R2 (the full row band, label through Total cell)."""
        return self.region_rect(col_x, row_y, (0, 4), (row_idx + 1, row_idx + 2), color)

    def col_region(self, col_x, row_y, col_idx, color):
        """col_idx: 0 for C1, 1 for C2 (the full column band, header through Total cell)."""
        return self.region_rect(col_x, row_y, (col_idx + 1, col_idx + 2), (0, 4), color)

    def cell_region(self, col_x, row_y, row_idx, col_idx, color):
        return self.region_rect(col_x, row_y, (col_idx + 1, col_idx + 2), (row_idx + 1, row_idx + 2), color)

    def make_fraction(self, num_text, den_text, font_size=30, num_color=NUMERATOR_COLOR, den_color=DENOMINATOR_COLOR):
        num = Text(num_text, font_size=font_size, color=num_color)
        den = Text(den_text, font_size=font_size, color=den_color)
        bar_width = max(num.width, den.width) + 0.3
        bar = Line(LEFT * bar_width / 2, RIGHT * bar_width / 2, color=WHITE, stroke_width=3)
        return VGroup(num, bar, den).arrange(DOWN, buff=0.12)

    def answer_question(
        self, prompt_text, denom_rect, numer_rect, numer_label, denom_label,
        numer_value, denom_value, anchor, prompt_font_size=26, work_font_size=30,
    ):
        """Denominator highlighted red first, then numerator highlighted blue
        (on top, since numerator region is always a subset of the
        denominator region for these problems); then the labeled fraction,
        which stays on screen as "= " the numeric fraction appears below it,
        and that in turn stays as "= " the boxed percent answer appears
        below that -- a running equation, not a disappearing swap. Cleans
        itself up before returning."""
        prompt = Text(prompt_text, font_size=prompt_font_size)
        max_width = 5.3
        if prompt.width > max_width:
            prompt.scale_to_fit_width(max_width)
        left_x = anchor[0] - 2.6
        prompt.move_to([left_x, anchor[1] + 1.8, 0], aligned_edge=LEFT)
        self.play(FadeIn(prompt))
        self.next_slide()

        self.play(FadeIn(denom_rect))
        self.next_slide()
        self.play(FadeIn(numer_rect))
        self.next_slide()

        label_frac = self.make_fraction(numer_label, denom_label, font_size=work_font_size)
        label_frac.move_to(anchor + UP * 0.9)
        self.play(FadeIn(label_frac, shift=UP * 0.2))
        self.next_slide()

        value_frac = self.make_fraction(str(numer_value), str(denom_value), font_size=work_font_size)
        eq1 = Text("=", font_size=work_font_size)
        line2 = VGroup(eq1, value_frac).arrange(RIGHT, buff=0.25)
        line2.next_to(label_frac, DOWN, buff=0.45)
        self.play(FadeIn(line2, shift=UP * 0.2))
        self.next_slide()

        pct = round(numer_value / denom_value * 100, 1)
        pct_str = f"{pct:g}%"
        answer = Text(pct_str, font_size=40, weight=BOLD, color=ANSWER_COLOR)
        box = SurroundingRectangle(answer, color=ANSWER_COLOR, buff=0.18)
        answer_group = VGroup(answer, box)
        eq2 = Text("=", font_size=work_font_size)
        line3 = VGroup(eq2, answer_group).arrange(RIGHT, buff=0.25)
        line3.next_to(line2, DOWN, buff=0.45)
        self.play(FadeIn(line3, shift=UP * 0.2))
        self.next_slide()

        self.play(
            FadeOut(prompt), FadeOut(denom_rect), FadeOut(numer_rect),
            FadeOut(label_frac), FadeOut(line2), FadeOut(line3),
        )
        self.next_slide()
        return pct

    # ---- independent-practice timer -------------------------------------------

    def show_timer(self, seconds, position=None, font_size=40, bar_height=3.5):
        time_tracker = ValueTracker(seconds)

        def get_time_string(s):
            mins, secs = divmod(int(s), 60)
            return f"{mins:02d}:{secs:02d}"

        anchor = position if position is not None else np.array([6.0, 3.0, 0])

        timer_text = always_redraw(
            lambda: Text(
                get_time_string(time_tracker.get_value()), font="monospace", font_size=font_size
            ).move_to(anchor)
        )
        bar_bg = Rectangle(height=bar_height, width=0.4, color=GRAY, fill_opacity=0.3).next_to(
            timer_text, DOWN, buff=0.35
        )
        bar = always_redraw(
            lambda: Rectangle(
                height=bar_height * (time_tracker.get_value() / seconds),
                width=0.4, color=BLUE, fill_opacity=0.8,
            ).move_to(bar_bg, aligned_edge=DOWN)
        )

        self.play(FadeIn(timer_text), FadeIn(bar_bg), FadeIn(bar))
        self.next_slide()

        self.play(time_tracker.animate.set_value(0), run_time=seconds, rate_func=linear)

        time_up = Text("Time's Up!", font_size=36, color=RED).move_to(timer_text)
        self.play(Transform(timer_text, time_up), FadeOut(bar))
        self.next_slide()
