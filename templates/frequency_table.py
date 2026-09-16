# templates/frequency_table.py

from manim import *

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR

STRIKE_COLOR = GRAY
TALLY_COLOR = WHITE
GRID_COLOR = GRAY

MARK_W = 0.11      # spacing between consecutive strokes within a group of 5
MARK_H = 0.3        # height of one tally stroke
GROUP_GAP = 0.18    # extra gap between groups of 5


class FrequencyTableTemplate:
    """Mixin for "raw data -> tally -> frequency/percent" one-way frequency
    table builds.

    Flow for one table:
        1. show_heading() -- short title pinned at the top.
        2. show_raw_data() -- the full raw data set, centered, large.
        3. shrink_raw_data() -- shrink + move it to a side column.
        4. build_table_skeleton() -- draw the grid + headers + class labels
           on the other side.
        5. run_tally_phase() -- walk the raw data in order; for each datum,
           strike it out in place and add one tally stroke to its class's
           row, as one continuous animated sequence (no slide-break between
           marks -- the class discusses while it plays, then advances).
        6. reveal_row_counts() -- afterwards, reveal frequency + percent for
           each row, one row per click.
        7. reveal_total() -- reveal + circumscribe the total row.
    """

    def show_heading(self, text, font_size=28):
        heading = Text(text, font_size=font_size, weight=BOLD)
        heading.to_edge(UP, buff=0.3)
        self.play(FadeIn(heading))
        self.next_slide()
        return heading

    def show_raw_data(self, values, per_row, font_size=28, h_buff=0.5, v_buff=0.4, center=ORIGIN):
        mobs = [Text(str(v), font_size=font_size) for v in values]
        grid = VGroup(*mobs).arrange_in_grid(cols=per_row, buff=(h_buff, v_buff))
        grid.move_to(center)
        self.play(FadeIn(grid))
        self.next_slide()
        return mobs

    def shrink_raw_data(self, mobs, target_point, width, run_time=1.0):
        grid = VGroup(*mobs)
        self.play(grid.animate.set(width=width).move_to(target_point), run_time=run_time)
        self.next_slide()
        return grid

    def build_table_skeleton(self, class_labels, header_labels, col_x, row_y, font_size=24, label_font_size=24):
        """
        col_x: [x0, x1, x2, x3, x4] -- 4 column boundaries (class, tally, freq, percent).
        row_y: [y0, y1, ..., y_{n+2}] -- boundaries for header row + one row
               per class + a total row (n classes -> n+2 boundaries beyond y0).
        Returns (grid_lines, tally_anchors, freq_slots, percent_slots, total_y)
        where tally_anchors[i] is the left-center point to start row i's tally
        marks, freq_slots[i] / percent_slots[i] are center points to place
        that row's frequency / percent text, and total_y is the row-center y
        for the total row.
        """
        lines = VGroup()
        for x in col_x:
            lines.add(Line([x, row_y[0], 0], [x, row_y[-1], 0], color=GRID_COLOR, stroke_width=2))
        for y in row_y:
            lines.add(Line([col_x[0], y, 0], [col_x[-1], y, 0], color=GRID_COLOR, stroke_width=2))

        header_y = (row_y[0] + row_y[1]) / 2
        headers = VGroup()
        col_centers = [(col_x[i] + col_x[i + 1]) / 2 for i in range(4)]
        col_widths = [col_x[i + 1] - col_x[i] for i in range(4)]
        for label, cx, cw in zip(header_labels, col_centers, col_widths):
            h = Text(label, font_size=label_font_size, weight=BOLD)
            if h.width > cw - 0.1:
                h.scale_to_fit_width(cw - 0.1)
            h.move_to([cx, header_y, 0])
            headers.add(h)

        class_texts = VGroup()
        tally_anchors = []
        freq_slots = []
        percent_slots = []
        for i, label in enumerate(class_labels):
            y_top, y_bot = row_y[i + 1], row_y[i + 2]
            y_c = (y_top + y_bot) / 2
            lbl = Text(label, font_size=font_size)
            if lbl.width > (col_x[1] - col_x[0]) - 0.15:
                lbl.scale_to_fit_width((col_x[1] - col_x[0]) - 0.15)
            lbl.move_to([col_centers[0], y_c, 0])
            class_texts.add(lbl)
            tally_anchors.append(np.array([col_x[1] + 0.15, y_c, 0]))
            freq_slots.append(np.array([col_centers[2], y_c, 0]))
            percent_slots.append(np.array([col_centers[3], y_c, 0]))

        total_y = (row_y[-2] + row_y[-1]) / 2
        total_label = Text("Total", font_size=font_size, weight=BOLD)
        total_label.move_to([col_centers[0], total_y, 0])

        self.play(Create(lines), FadeIn(headers), FadeIn(class_texts), FadeIn(total_label))
        self.next_slide()

        return {
            "lines": lines,
            "headers": headers,
            "class_texts": class_texts,
            "total_label": total_label,
            "tally_anchors": tally_anchors,
            "freq_slots": freq_slots,
            "percent_slots": percent_slots,
            "freq_total_slot": np.array([col_centers[2], total_y, 0]),
            "percent_total_slot": np.array([col_centers[3], total_y, 0]),
        }

    def tally_stroke(self, cell_left, count):
        """The mobject for the (count)-th (0-indexed) tally mark in a cell
        whose tally marks start at `cell_left` (left-center anchor)."""
        group_idx = count // 5
        pos_in_group = count % 5
        x0 = cell_left[0] + group_idx * (4 * MARK_W + GROUP_GAP)
        y = cell_left[1]

        if pos_in_group < 4:
            x = x0 + pos_in_group * MARK_W
            return Line([x, y - MARK_H / 2, 0], [x, y + MARK_H / 2, 0], color=TALLY_COLOR, stroke_width=3)
        else:
            return Line(
                [x0, y - MARK_H / 2, 0],
                [x0 + 3 * MARK_W, y + MARK_H / 2, 0],
                color=TALLY_COLOR,
                stroke_width=3,
            )

    def cross_out_datum(self, mob, color=STRIKE_COLOR, pad=0.06, stroke_width=4):
        return Line(
            mob.get_corner(UL) + UP * pad + LEFT * pad,
            mob.get_corner(DR) + DOWN * pad + RIGHT * pad,
            color=color,
            stroke_width=stroke_width,
        )

    def run_tally_phase(self, data_mobs, row_indices, tally_anchors, run_time=0.15):
        """
        data_mobs: the raw-data mobjects, in original order.
        row_indices: parallel list -- the class-row index each datum belongs to.
        tally_anchors: tally_anchors[i] from build_table_skeleton().
        Plays one continuous sequence (no slide-breaks between marks) so the
        teacher can pause/resume the video while narrating, then a single
        next_slide() once every datum has been used.
        """
        counts = [0] * len(tally_anchors)
        for mob, row in zip(data_mobs, row_indices):
            mark = self.tally_stroke(tally_anchors[row], counts[row])
            strike = self.cross_out_datum(mob)
            self.play(Create(mark), Create(strike), run_time=run_time)
            counts[row] += 1
        self.next_slide()
        return counts

    def reveal_row_counts(self, slots_and_values, font_size=24, color=ANSWER_COLOR):
        """slots_and_values: list of (freq_point, freq_str, percent_point, percent_str).
        Reveals one row (frequency + percent together) per click."""
        mobs = []
        for freq_pt, freq_str, pct_pt, pct_str in slots_and_values:
            f = Text(freq_str, font_size=font_size, color=color).move_to(freq_pt)
            p = Text(pct_str, font_size=font_size, color=color).move_to(pct_pt)
            self.play(FadeIn(f, shift=UP * 0.1), FadeIn(p, shift=UP * 0.1))
            self.next_slide()
            mobs.append((f, p))
        return mobs

    def reveal_total(self, freq_point, freq_str, percent_point, percent_str, font_size=24, color=ANSWER_COLOR):
        f = Text(freq_str, font_size=font_size, weight=BOLD, color=color).move_to(freq_point)
        p = Text(percent_str, font_size=font_size, weight=BOLD, color=color).move_to(percent_point)
        self.play(FadeIn(f, shift=UP * 0.1), FadeIn(p, shift=UP * 0.1))
        self.play(Circumscribe(VGroup(f, p), color=color))
        self.next_slide()
        return f, p

    def show_timer(self, seconds, position=None):
        """A countdown timer + draining bar, for independent-practice slides.
        Mirrors the pattern used in precalc/solving_linear_equations/practice_list.py."""
        time_tracker = ValueTracker(seconds)

        def get_time_string(s):
            mins, secs = divmod(int(s), 60)
            return f"{mins:02d}:{secs:02d}"

        anchor = position if position is not None else np.array([6.0, 3.0, 0])

        timer_text = always_redraw(
            lambda: Text(get_time_string(time_tracker.get_value()), font="monospace", font_size=40).move_to(anchor)
        )
        bar_bg = Rectangle(height=3.5, width=0.4, color=GRAY, fill_opacity=0.3).next_to(timer_text, DOWN, buff=0.35)
        bar = always_redraw(
            lambda: Rectangle(
                height=3.5 * (time_tracker.get_value() / seconds),
                width=0.4,
                color=BLUE,
                fill_opacity=0.8,
            ).move_to(bar_bg, aligned_edge=DOWN)
        )

        self.play(FadeIn(timer_text), FadeIn(bar_bg), FadeIn(bar))
        self.next_slide()

        self.play(time_tracker.animate.set_value(0), run_time=seconds, rate_func=linear)

        time_up = Text("Time's Up!", font_size=36, color=RED).move_to(timer_text)
        self.play(Transform(timer_text, time_up), FadeOut(bar))
        self.next_slide()
