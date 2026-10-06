# templates/relations_functions.py

import numpy as np
from manim import *

from components.theme import BACKGROUND_COLOR, X_COLOR, Y_COLOR, ANSWER_COLOR, THEOREM_COLOR, INDICATE_COLOR

IS_FUNCTION_COLOR = GREEN
NOT_FUNCTION_COLOR = RED


class RelationsFunctionsTemplate:
    """Mixin for the Relations & Functions lesson: ordered-pair tables,
    domain/range sets, function-definition checks, mapping diagrams, rough
    vertical-line-test sketches, and solve-for-y verdicts.

    Shared conventions: x-values/domain are X_COLOR (green), y-values/range
    are Y_COLOR (red); a verdict of "IS a function" is drawn in
    IS_FUNCTION_COLOR (green), "NOT a function" in NOT_FUNCTION_COLOR (red).
    """

    # ---- shared chrome ----

    def show_label(self, label, font_size=40):
        heading = Text(label, font_size=font_size, weight=BOLD)
        heading.to_corner(UL)
        self.play(FadeIn(heading))
        return heading

    def mixed_line(self, parts, font_size=28, buff=0.15):
        """parts: list of (text, color_or_None), each text WITHOUT leading or
        trailing spaces (Text() trims those when sizing, so use `buff` for
        the gaps between chunks, not embedded spaces). Builds one row mixing
        colored and plain words -- use for short notes lines where specific
        whole words (domain, range, ...) need to carry the theme color."""
        chunks = [
            Text(t, font_size=font_size, color=c, weight=BOLD if c else NORMAL)
            for t, c in parts
        ]
        return VGroup(*chunks).arrange(RIGHT, buff=buff, aligned_edge=DOWN)

    def show_notes(self, title, lines, title_font_size=38, line_font_size=28, title_color=THEOREM_COLOR):
        """lines: list of strings (plain Text) or pre-built Mobjects (e.g.
        from mixed_line). Revealed one at a time so students can copy."""
        heading = Text(title, font_size=title_font_size, weight=BOLD, color=title_color)
        heading.to_edge(UP, buff=0.6)
        self.play(Write(heading))
        self.next_slide()

        bullets = VGroup(*[
            l if isinstance(l, Mobject) else Text(l, font_size=line_font_size) for l in lines
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        bullets.next_to(heading, DOWN, buff=0.7)
        if bullets.width > 11:
            bullets.scale_to_fit_width(11)

        for b in bullets:
            self.play(FadeIn(b, shift=UP * 0.15))
            self.next_slide()
        return heading, bullets

    def write_soundbite(self, text, font_size=34, box_color=ANSWER_COLOR):
        """A short boxed takeaway sentence students write down verbatim."""
        prompt = Text("Write this down:", font_size=26, color=GRAY)
        prompt.to_edge(UP, buff=1.0)
        quote = Text(text, font_size=font_size, weight=BOLD, color=box_color)
        quote.next_to(prompt, DOWN, buff=0.6)
        if quote.width > 10:
            quote.scale_to_fit_width(10)
        box = SurroundingRectangle(quote, color=box_color, buff=0.35)

        self.play(FadeIn(prompt))
        self.next_slide()
        self.play(Write(quote))
        self.play(Create(box))
        self.next_slide()
        return quote, box

    def verdict_text(self, is_function, font_size=36):
        if is_function:
            return Text("This IS a function.", font_size=font_size, color=IS_FUNCTION_COLOR, weight=BOLD)
        return Text("This is NOT a function.", font_size=font_size, color=NOT_FUNCTION_COLOR, weight=BOLD)

    # ---- ordered-pair tables ----

    def two_column_table(self, header_a, header_b, values_a, values_b, color_a=X_COLOR, color_b=Y_COLOR,
                          font_size=32, col_width=2.4, row_height=0.75, center=ORIGIN):
        """Vertical table: header row, then one row per (a, b) pair, stacked down."""
        n = len(values_a)
        col_x = [-col_width, 0, col_width]
        row_y = [row_height] + [-i * row_height for i in range(n + 1)]
        lines = VGroup()
        for x in col_x:
            lines.add(Line([x, row_y[0], 0], [x, row_y[-1], 0], color=GRAY, stroke_width=2))
        for y in row_y:
            lines.add(Line([col_x[0], y, 0], [col_x[-1], y, 0], color=GRAY, stroke_width=2))

        header_y = (row_y[0] + row_y[1]) / 2
        h_a = Text(header_a, font_size=font_size, weight=BOLD, color=color_a)
        h_a.move_to([(col_x[0] + col_x[1]) / 2, header_y, 0])
        h_b = Text(header_b, font_size=font_size, weight=BOLD, color=color_b)
        h_b.move_to([(col_x[1] + col_x[2]) / 2, header_y, 0])

        cells_a, cells_b = [], []
        for i in range(n):
            y_c = (row_y[i + 1] + row_y[i + 2]) / 2
            ca = Text(str(values_a[i]), font_size=font_size, color=color_a)
            ca.move_to([(col_x[0] + col_x[1]) / 2, y_c, 0])
            cb = Text(str(values_b[i]), font_size=font_size, color=color_b)
            cb.move_to([(col_x[1] + col_x[2]) / 2, y_c, 0])
            cells_a.append(ca)
            cells_b.append(cb)

        table = VGroup(lines, h_a, h_b, *cells_a, *cells_b)
        table.move_to(center)
        self.play(Create(lines), FadeIn(h_a), FadeIn(h_b))
        self.play(LaggedStart(*[FadeIn(m) for m in cells_a + cells_b], lag_ratio=0.1))
        self.next_slide()
        return cells_a, cells_b, table

    def two_row_table(self, row_a_label, row_b_label, values_a, values_b, color_a=X_COLOR, color_b=Y_COLOR,
                       font_size=32, label_col_width=1.0, data_col_width=1.3, row_height=0.9, center=ORIGIN):
        """Sideways table: a label column (row_a_label/row_b_label) then one
        data column per (a, b) pair, stacked right."""
        n = len(values_a)
        col_x = [0, label_col_width] + [label_col_width + (i + 1) * data_col_width for i in range(n)]
        row_y = [row_height, 0, -row_height]
        lines = VGroup()
        for x in col_x:
            lines.add(Line([x, row_y[0], 0], [x, row_y[-1], 0], color=GRAY, stroke_width=2))
        for y in row_y:
            lines.add(Line([col_x[0], y, 0], [col_x[-1], y, 0], color=GRAY, stroke_width=2))

        label_a = Text(row_a_label, font_size=font_size, weight=BOLD, color=color_a)
        label_a.move_to([(col_x[0] + col_x[1]) / 2, (row_y[0] + row_y[1]) / 2, 0])
        label_b = Text(row_b_label, font_size=font_size, weight=BOLD, color=color_b)
        label_b.move_to([(col_x[0] + col_x[1]) / 2, (row_y[1] + row_y[2]) / 2, 0])

        cells_a, cells_b = [], []
        for i in range(n):
            x_c = (col_x[i + 1] + col_x[i + 2]) / 2
            ca = Text(str(values_a[i]), font_size=font_size, color=color_a)
            ca.move_to([x_c, (row_y[0] + row_y[1]) / 2, 0])
            cb = Text(str(values_b[i]), font_size=font_size, color=color_b)
            cb.move_to([x_c, (row_y[1] + row_y[2]) / 2, 0])
            cells_a.append(ca)
            cells_b.append(cb)

        table = VGroup(lines, label_a, label_b, *cells_a, *cells_b)
        table.move_to(center)
        self.play(Create(lines), FadeIn(label_a), FadeIn(label_b))
        self.play(LaggedStart(*[FadeIn(m) for m in cells_a + cells_b], lag_ratio=0.1))
        self.next_slide()
        return cells_a, cells_b, table

    def build_ordered_pairs(self, cells_a, cells_b, color_a=X_COLOR, color_b=Y_COLOR,
                             font_size=30, anchor=None, max_width=11):
        """Builds the {(a, b), (a, b), ...} relation set under the table,
        by fading it in while the source cells are indicated."""
        anchor = anchor if anchor is not None else DOWN * 2.6
        pairs = []
        for ca, cb in zip(cells_a, cells_b):
            lp = Text("(", font_size=font_size)
            a_copy = Text(ca.text, font_size=font_size, color=color_a)
            comma = Text(",", font_size=font_size)
            b_copy = Text(cb.text, font_size=font_size, color=color_b)
            rp = Text(")", font_size=font_size)
            pairs.append(VGroup(lp, a_copy, comma, b_copy, rp).arrange(RIGHT, buff=0.06, aligned_edge=DOWN))

        relation_set = self._bracket_row(pairs, font_size)
        if relation_set.width > max_width:
            relation_set.scale_to_fit_width(max_width)
        relation_set.move_to(anchor)

        self.play(Indicate(VGroup(*cells_a, *cells_b), color=INDICATE_COLOR))
        self.play(FadeIn(relation_set, shift=UP * 0.2))
        self.next_slide()
        return relation_set

    def build_set(self, values, label, color, anchor, dedupe=True, font_size=34, label_font_size=30):
        """A labeled {v1, v2, ...} set (used for domain/range), deduping
        repeats by default since set elements aren't listed twice."""
        if dedupe:
            seen = []
            for v in values:
                if v not in seen:
                    seen.append(v)
            values = seen

        label_mob = Text(f"{label}:", font_size=label_font_size, weight=BOLD, color=color)
        items = [Text(str(v), font_size=font_size, color=color) for v in values]
        set_mob = self._bracket_row(items, font_size)
        group = VGroup(label_mob, set_mob).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        group.move_to(anchor)
        self.play(FadeIn(group, shift=UP * 0.2))
        self.next_slide()
        return group

    def _bracket_row(self, items, font_size):
        lb = Text("{", font_size=font_size + 8)
        rb = Text("}", font_size=font_size + 8)
        commas = [Text(",", font_size=font_size) for _ in range(len(items) - 1)]
        row = [lb]
        for i, it in enumerate(items):
            row.append(it)
            if i < len(items) - 1:
                row.append(commas[i])
        row.append(rb)
        return VGroup(*row).arrange(RIGHT, buff=0.15, aligned_edge=DOWN)

    # ---- function checks from a list of ordered pairs ----

    def write_relation_pairs(self, pairs, font_size=36, anchor=UP * 1.0, max_width=11, pause=True):
        """Writes just the {(x, y), ...} relation (the "problem"), with no
        verdict yet. Returns (relation, pair_mobs) -- pass both into
        reveal_function_verdict() once students have had time to work it."""
        pair_mobs = []
        for x, y in pairs:
            lp = Text("(", font_size=font_size)
            xm = Text(str(x), font_size=font_size, color=X_COLOR)
            comma = Text(",", font_size=font_size)
            ym = Text(str(y), font_size=font_size, color=Y_COLOR)
            rp = Text(")", font_size=font_size)
            pair_mobs.append(VGroup(lp, xm, comma, ym, rp).arrange(RIGHT, buff=0.06, aligned_edge=DOWN))

        relation = self._bracket_row(pair_mobs, font_size)
        if relation.width > max_width:
            relation.scale_to_fit_width(max_width)
        relation.move_to(anchor)
        self.play(Write(relation))
        if pause:
            self.next_slide()
        return relation, pair_mobs

    def reveal_function_verdict(self, relation, pair_mobs, repeat_indices=None):
        """Circles the repeated x's, underlines the differing y's, and
        writes the verdict below a relation already written by
        write_relation_pairs(). None -> verdict is IS a function."""
        if repeat_indices is not None:
            i, j = repeat_indices
            x_i, x_j = pair_mobs[i][1], pair_mobs[j][1]
            y_i, y_j = pair_mobs[i][3], pair_mobs[j][3]

            circ_i = Circle(radius=0.3, color=NOT_FUNCTION_COLOR).move_to(x_i)
            circ_j = Circle(radius=0.3, color=NOT_FUNCTION_COLOR).move_to(x_j)
            self.play(Create(circ_i), Create(circ_j))
            self.next_slide()

            under_i = Underline(y_i, color=INDICATE_COLOR)
            under_j = Underline(y_j, color=INDICATE_COLOR)
            note = Text("same x, different y", font_size=26, color=NOT_FUNCTION_COLOR)
            note.next_to(relation, DOWN, buff=0.6)
            self.play(Create(under_i), Create(under_j), FadeIn(note, shift=UP * 0.2))
            self.next_slide()

        verdict = self.verdict_text(repeat_indices is None)
        verdict.next_to(relation, DOWN, buff=1.5 if repeat_indices else 0.9)
        self.play(Write(verdict))
        self.next_slide()
        return verdict

    def function_check_pairs(self, pairs, repeat_indices=None, font_size=36, anchor=UP * 1.0, max_width=11):
        """pairs: list of (x, y). repeat_indices: (i, j) indices sharing the
        same x -> circles both x's, underlines the differing y's, and the
        verdict is NOT a function. None -> verdict is IS a function."""
        relation, pair_mobs = self.write_relation_pairs(pairs, font_size, anchor, max_width)
        verdict = self.reveal_function_verdict(relation, pair_mobs, repeat_indices)
        return relation, verdict

    # ---- mapping diagrams ----

    def mapping_diagram(self, domain_vals, range_vals, arrows, repeated_source=None, font_size=32,
                         oval_width=2.0, gap=5.0, center=ORIGIN, row_buff=0.9, reveal_verdict=True):
        """arrows: list of (domain_val, range_val). repeated_source: a
        domain value with more than one outgoing arrow -> highlighted red,
        verdict NOT a function. None -> verdict IS a function. center: point
        midway between the two ovals, so multiple diagrams can share a slide.
        reveal_verdict=False stops after drawing the arrows (the "problem")
        and skips the verdict -- pair with reveal_mapping_verdict() later."""
        left_h = max(len(domain_vals) * row_buff + 0.6, 2.0)
        right_h = max(len(range_vals) * row_buff + 0.6, 2.0)
        left_oval = Ellipse(width=oval_width, height=left_h, color=X_COLOR)
        left_oval.move_to(center + LEFT * gap / 2)
        right_oval = Ellipse(width=oval_width, height=right_h, color=Y_COLOR)
        right_oval.move_to(center + RIGHT * gap / 2)
        self.play(Create(left_oval), Create(right_oval))

        label_buff = max(row_buff - 0.3, 0.2)
        left_pts = VGroup(*[Text(str(v), font_size=font_size) for v in domain_vals]).arrange(DOWN, buff=label_buff)
        left_pts.move_to(left_oval.get_center())
        right_pts = VGroup(*[Text(str(v), font_size=font_size) for v in range_vals]).arrange(DOWN, buff=label_buff)
        right_pts.move_to(right_oval.get_center())
        left_labels = dict(zip(domain_vals, left_pts))
        right_labels = dict(zip(range_vals, right_pts))

        self.play(FadeIn(left_pts), FadeIn(right_pts))
        self.next_slide()

        arrow_mobs = []
        for a, b in arrows:
            start = left_labels[a].get_right()
            end = right_labels[b].get_left()
            color = NOT_FUNCTION_COLOR if a == repeated_source else WHITE
            arr = Arrow(start, end, buff=0.15, color=color, stroke_width=3, max_tip_length_to_length_ratio=0.12)
            arrow_mobs.append(arr)
            self.play(Create(arr), run_time=0.5)
        self.next_slide()

        diagram = VGroup(left_oval, right_oval, left_pts, right_pts, *arrow_mobs)

        if not reveal_verdict:
            return diagram, None

        verdict = self.reveal_mapping_verdict(diagram, repeated_source is None)
        return diagram, verdict

    def reveal_mapping_verdict(self, diagram, is_function, buff=0.8):
        """Writes the verdict below a diagram built by mapping_diagram()
        (with reveal_verdict=False), once students have had time to work it."""
        verdict = self.verdict_text(is_function)
        verdict.next_to(diagram, DOWN, buff=buff)
        self.play(Write(verdict))
        self.next_slide()
        return verdict

    # ---- rough sketches + vertical line test ----

    def show_axes(self, x_range=(-5, 5, 1), y_range=(-5, 5, 1), length=5.5, center=ORIGIN):
        axes = Axes(
            x_range=list(x_range), y_range=list(y_range), x_length=length, y_length=length,
            axis_config={"color": GRAY, "include_tip": True, "font_size": 20},
        )
        axes.move_to(center)
        self.play(Create(axes))
        return axes

    def rough_curve(self, axes, points_axes_coords, color=BLUE, stroke_width=4):
        """points_axes_coords: list of (x, y) in axes units -- a hand-drawn-
        style curve threaded smoothly through them (one continuous piece)."""
        pts = [axes.c2p(x, y) for x, y in points_axes_coords]
        curve = VMobject(color=color, stroke_width=stroke_width)
        curve.set_points_smoothly(pts)
        return curve

    def endpoint_dot(self, axes, point_axes_coords, closed=True, color=BLUE, radius=0.09):
        pt = axes.c2p(*point_axes_coords)
        if closed:
            return Dot(pt, radius=radius, color=color)
        return Circle(radius=radius, color=color).move_to(pt).set_fill(BACKGROUND_COLOR, opacity=1)

    def vertical_line_test(self, axes, curve, test_lines, passes, y_bottom=-5, y_top=5):
        """curve: a Mobject (or VGroup of several pieces) to Create first.
        test_lines: list of (x, color) -- each drawn as a dashed vertical
        line at that x. passes: overall verdict to draw at the end."""
        self.play(Create(curve))
        self.next_slide()

        vlines = []
        for x, color in test_lines:
            vline = DashedLine(axes.c2p(x, y_bottom), axes.c2p(x, y_top), color=color, stroke_width=3)
            vlines.append(vline)
            self.play(Create(vline), run_time=0.6)
            self.next_slide()

        verdict = self.verdict_text(passes)
        verdict.next_to(axes, DOWN, buff=0.4)
        self.play(Write(verdict))
        self.next_slide()
        return vlines, verdict

    # ---- solving for y ----

    def solve_for_y(self, equation_lines, font_size=36, anchor=UP * 1.5, line_buff=0.5, start_after=None):
        """equation_lines: MathTex strings, one per step, each staying
        visible below the last (running record). Isolate the final +/- with
        double braces (e.g. r"y = -1 {{\\pm}} \\sqrt{...}") so flag_plus_minus
        can circle it afterward. start_after: an existing mobject (e.g. the
        given equation, written separately) to stack the first new line
        below, instead of placing it at `anchor`."""
        mobs = []
        prev = start_after
        for s in equation_lines:
            m = MathTex(s, font_size=font_size)
            if prev is None:
                m.move_to(anchor)
            else:
                m.next_to(prev, DOWN, buff=line_buff, aligned_edge=LEFT)
            self.play(Write(m))
            self.next_slide()
            mobs.append(m)
            prev = m
        return mobs

    def flag_plus_minus(self, mob, tex_fragment=r"\pm", color=NOT_FUNCTION_COLOR,
                         note="Plus or minus means NOT a function.", note_font_size=30, note_buff=0.8):
        part = mob.get_part_by_tex(tex_fragment, substring=False)
        self.play(Circumscribe(part, color=color))
        verdict = Text(note, font_size=note_font_size, color=color, weight=BOLD)
        verdict.next_to(mob, DOWN, buff=note_buff)
        self.play(Write(verdict))
        self.next_slide()
        return verdict

    # ---- wrap-up ----

    def group_work_slide(self, page_number, problems, title="Group Work", font_size=30, cols=3):
        heading = Text(title, font_size=48, weight=BOLD)
        heading.to_edge(UP, buff=0.5)
        page = Text(f"Page {page_number}", font_size=34, color=THEOREM_COLOR)
        page.next_to(heading, DOWN, buff=0.4)
        self.play(Write(heading), FadeIn(page))
        self.next_slide()

        items = [Text(f"#{p}", font_size=font_size) for p in problems]
        grid = VGroup(*items).arrange_in_grid(cols=cols, buff=(0.7, 0.4))
        grid.next_to(page, DOWN, buff=0.6)
        if grid.width > 11:
            grid.scale_to_fit_width(11)
        self.play(FadeIn(grid, shift=UP * 0.2))
        self.next_slide()
        return heading, page, grid
