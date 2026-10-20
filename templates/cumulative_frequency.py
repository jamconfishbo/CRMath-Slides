# templates/cumulative_frequency.py

from manim import *

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, INDICATE_COLOR, AXIS_COLOR
from templates.frequency_table import FrequencyTableTemplate

# Color code for the whole lesson -- every number in a work line is drawn in
# the same color as the table cell it was copied out of.
TOTAL_COLOR = BLUE              # the table's Total (and every division by it)
ROW_COLOR = INDICATE_COLOR      # the row currently being worked
RUNNING_COLOR = PURPLE_B        # the previous cumulative value being added onto
HEADER_FILL = GREY_E
GRID_COLOR = GRAY

# Ogive percentile reference lines (Q1 / median / Q3).
PERCENTILE_COLORS = {25: PINK, 50: ORANGE, 75: PURPLE_B}

WORK_Y = -2.35          # center line for row-by-row work below the tables
PROMPT_Y = -1.6         # interpretation-question prompt
LINE_BUFF = 0.3


class GridTable:
    """Geometry + mobjects for one drawn table. Rows 0..n-1 are data rows;
    row n is the Total row (when the table has one). Column 0 is the label
    column."""

    def __init__(self, col_x, row_y, n_rows, has_total):
        self.col_x = col_x
        self.row_y = row_y
        self.n_rows = n_rows
        self.has_total = has_total
        self.values = {}

    @property
    def total_row(self):
        return self.n_rows

    def center(self, r, c):
        x = (self.col_x[c] + self.col_x[c + 1]) / 2
        y = (self.row_y[r + 1] + self.row_y[r + 2]) / 2
        return np.array([x, y, 0])

    def rect(self, r0, r1, c0, c1, color, opacity=0.25, stroke_width=3):
        """Rows r0..r1 and columns c0..c1, inclusive."""
        x0, x1 = self.col_x[c0], self.col_x[c1 + 1]
        y0, y1 = self.row_y[r0 + 1], self.row_y[r1 + 2]
        return Rectangle(
            width=x1 - x0, height=y0 - y1,
            fill_color=color, fill_opacity=opacity,
            stroke_color=color, stroke_width=stroke_width,
        ).move_to([(x0 + x1) / 2, (y0 + y1) / 2, 0])

    def cell_rect(self, r, c, color, opacity=0.25):
        return self.rect(r, r, c, c, color, opacity)

    def row_rect(self, r, color, opacity=0.25):
        return self.rect(r, r, 0, len(self.col_x) - 2, color, opacity)


class CumulativeFrequencyTemplate(FrequencyTableTemplate):
    """Mixin for cumulative / relative / cumulative-relative frequency tables
    built from an already-completed frequency table, plus interpretation
    questions answered by reading those tables.

    Every row is worked one at a time below the tables (highlight the source
    cells -> running equation -> copy the answer into the table), so the
    class finishes one row before moving to the next.

    Flow for one problem:
        1. show_heading() + show_scenario()
        2. build_table() for each table (prefill the given columns)
        3. fill_cumulative_column() / fill_relative_column() / fill_relative_total()
        4. run_question() for each interpretation question
    """

    # ---- intro ------------------------------------------------------------

    def show_scenario(self, scenario, task, font_size=28, width=12.0):
        body = VGroup(
            Text(scenario, font_size=font_size, line_spacing=0.9),
            Text(task, font_size=font_size, line_spacing=0.9, color=ANSWER_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        if body.width > width:
            body.scale_to_fit_width(width)
        box = SurroundingRectangle(body, color=TOTAL_COLOR, buff=0.4, corner_radius=0.1)
        group = VGroup(box, body).move_to(DOWN * 0.2)
        self.play(Create(box), FadeIn(body, shift=UP * 0.2))
        self.next_slide()
        self.play(FadeOut(group))
        return group

    def swap_heading(self, heading, text, font_size=28):
        new = Text(text, font_size=font_size, weight=BOLD).to_edge(UP, buff=0.3)
        self.play(Transform(heading, new))
        return heading

    # ---- tables -----------------------------------------------------------

    def build_table(self, title, headers, row_labels, col_x, top_y=2.7, header_h=0.8, row_h=0.5,
                    total_label=None, font_size=22, header_font_size=20, columns=None,
                    total_values=None, animate=True):
        """headers: one string per column ("\\n" for two-line headers).
        columns: {col_index: [str per data row]} values already given.
        total_values: {col_index: str} values already given in the Total row
        (drawn in TOTAL_COLOR)."""
        n = len(row_labels)
        n_lines = n + (1 if total_label else 0)
        row_y = [top_y, top_y - header_h] + [top_y - header_h - (i + 1) * row_h for i in range(n_lines)]
        table = GridTable(col_x, row_y, n, total_label is not None)

        header_band = Rectangle(
            width=col_x[-1] - col_x[0], height=header_h,
            fill_color=HEADER_FILL, fill_opacity=1, stroke_width=0,
        ).move_to([(col_x[0] + col_x[-1]) / 2, top_y - header_h / 2, 0])

        lines = VGroup()
        for x in col_x:
            lines.add(Line([x, row_y[0], 0], [x, row_y[-1], 0], color=GRID_COLOR, stroke_width=2))
        for y in row_y:
            lines.add(Line([col_x[0], y, 0], [col_x[-1], y, 0], color=GRID_COLOR, stroke_width=2))

        header_mobs = VGroup()
        for c, label in enumerate(headers):
            h = Text(label, font_size=header_font_size, weight=BOLD, line_spacing=0.8)
            cw = col_x[c + 1] - col_x[c]
            if h.width > cw - 0.12:
                h.scale_to_fit_width(cw - 0.12)
            h.move_to([(col_x[c] + col_x[c + 1]) / 2, top_y - header_h / 2, 0])
            header_mobs.add(h)

        label_mobs = VGroup()
        for r, label in enumerate(row_labels):
            label_mobs.add(self._cell_text(table, r, 0, label, font_size))
        if total_label:
            label_mobs.add(self._cell_text(table, n, 0, total_label, font_size, weight=BOLD))

        value_mobs = VGroup()
        for c, strs in (columns or {}).items():
            for r, s in enumerate(strs):
                m = self._cell_text(table, r, c, s, font_size)
                table.values[(r, c)] = m
                value_mobs.add(m)
        for c, s in (total_values or {}).items():
            m = self._cell_text(table, n, c, s, font_size, weight=BOLD, color=TOTAL_COLOR)
            table.values[(n, c)] = m
            value_mobs.add(m)

        title_mob = Text(title, font_size=22, weight=BOLD, color=GREY_A)
        title_mob.move_to([(col_x[0] + col_x[-1]) / 2, top_y + 0.28, 0])

        table.title = title_mob
        table.font_size = font_size
        table.group = VGroup(title_mob, header_band, lines, header_mobs, label_mobs, value_mobs)
        if animate:
            self.play(
                FadeIn(title_mob), FadeIn(header_band), Create(lines),
                FadeIn(header_mobs), FadeIn(label_mobs), FadeIn(value_mobs),
            )
        return table

    def _cell_text(self, table, r, c, s, font_size, weight=NORMAL, color=WHITE):
        m = Text(s, font_size=font_size, weight=weight, color=color)
        cw = table.col_x[c + 1] - table.col_x[c]
        if m.width > cw - 0.15:
            m.scale_to_fit_width(cw - 0.15)
        return m.move_to(table.center(r, c))

    def place_value(self, table, r, c, s, source=None, color=ANSWER_COLOR, bold=False):
        """Put s in cell (r, c) -- flown in from `source` (a work-line piece)
        when given, otherwise faded in."""
        m = self._cell_text(table, r, c, s, table.font_size, weight=BOLD if bold else NORMAL, color=color)
        if source is not None:
            self.play(TransformFromCopy(source, m))
        else:
            self.play(FadeIn(m, shift=UP * 0.1))
        table.values[(r, c)] = m
        table.group.add(m)
        return m

    # ---- work lines -------------------------------------------------------

    def math_line(self, pieces, font_size=40):
        """pieces: list of (tex, color). Each piece is its own submobject so
        it can be revealed / copied on its own."""
        m = MathTex(*[t for t, _ in pieces], font_size=font_size)
        for sub, (_, color) in zip(m, pieces):
            sub.set_color(color)
        return m

    def work_row(self, label, pieces, y=WORK_Y, font_size=40, label_font_size=28):
        """A row label ("Less than 70:") followed by a math line, centered at y."""
        lbl = Text(label, font_size=label_font_size, color=GREY_A)
        line = self.math_line(pieces, font_size=font_size)
        VGroup(lbl, line).arrange(RIGHT, buff=0.45).move_to([0, y, 0])
        return lbl, line

    def pct(self, v):
        return f"{v:g}\\%"

    # ---- column fills -----------------------------------------------------

    def fill_cumulative_column(self, src, src_col, dst, dst_col, values, labels, percent=False):
        """Running total of src column `src_col` (values = its numbers) into
        dst column `dst_col`, one row at a time:
            click 1: highlight (purple = rows already counted + previous
                     cumulative cell, orange = the new row) + "prev + new"
            click 2: "= result"
            click 3: result copied into the table
        """
        fmt = self.pct if percent else str
        cum = []
        running = 0
        for i, v in enumerate(values):
            running += v
            cum.append(running)

            hl = VGroup(src.row_rect(i, ROW_COLOR), dst.row_rect(i, ROW_COLOR, opacity=0.12))
            if i == 0:
                lbl, line = self.work_row(f"{labels[i]}:", [(fmt(v), ROW_COLOR), ("=", WHITE), (fmt(running), ANSWER_COLOR)])
                note = Text("first row -- nothing to add yet, just copy it", font_size=22, color=GREY_B)
                note.next_to(VGroup(lbl, line), DOWN, buff=0.25)
                self.play(FadeIn(hl), FadeIn(lbl), FadeIn(line[0]), FadeIn(note))
                extra = VGroup(note)
            else:
                hl.add(src.rect(0, i - 1, 0, len(src.col_x) - 2, RUNNING_COLOR, opacity=0.12))
                hl.add(dst.cell_rect(i - 1, dst_col, RUNNING_COLOR, opacity=0.35))
                lbl, line = self.work_row(
                    f"{labels[i]}:",
                    [(fmt(cum[i - 1]), RUNNING_COLOR), ("+", WHITE), (fmt(v), ROW_COLOR),
                     ("=", WHITE), (fmt(running), ANSWER_COLOR)],
                )
                self.play(FadeIn(hl), FadeIn(lbl), FadeIn(line[:3]))
                extra = VGroup()
            self.next_slide()

            self.play(FadeIn(line[-2:]))
            self.next_slide()

            self.place_value(dst, i, dst_col, fmt(running).replace("\\", ""), source=line[-1])
            self.next_slide()
            self.play(FadeOut(hl), FadeOut(lbl), FadeOut(line), FadeOut(extra))
        return cum

    def check_last_equals_total(self, dst, dst_col, last, total_table, total_col, total, percent=False):
        """The last cumulative value always equals the table's total."""
        fmt = self.pct if percent else str
        hl = VGroup(
            dst.cell_rect(dst.n_rows - 1, dst_col, ANSWER_COLOR),
            total_table.cell_rect(total_table.total_row, total_col, TOTAL_COLOR, opacity=0.35),
        )
        lbl, line = self.work_row("Check:", [(fmt(last), ANSWER_COLOR), ("=", WHITE), (fmt(total), TOTAL_COLOR)])
        note = Text("the last cumulative value always equals the total", font_size=22, color=GREY_B)
        note.next_to(VGroup(lbl, line), DOWN, buff=0.25)
        self.play(FadeIn(hl), FadeIn(lbl), FadeIn(line), FadeIn(note))
        self.next_slide()
        self.play(FadeOut(hl), FadeOut(lbl), FadeOut(line), FadeOut(note))

    def highlight_total(self, table, col):
        """Blue box on the Total cell -- stays up while the relative-frequency
        column is calculated, so every division points back to it."""
        box = table.cell_rect(table.total_row, col, TOTAL_COLOR, opacity=0.35)
        self.play(FadeIn(box), Indicate(table.values[(table.total_row, col)], color=TOTAL_COLOR, scale_factor=1.4))
        return box

    def fill_relative_column(self, src, freq_col, dst, rel_col, freqs, total, labels):
        """f / Total for each row, one row at a time:
            click 1: highlight the row (orange) + "f ÷ Total" (Total in blue)
            click 2: "= decimal"
            click 3: "= percent"
            click 4: percent copied into the table
        """
        pcts = []
        for i, f in enumerate(freqs):
            p = round(f / total * 100, 1)
            pcts.append(p)
            hl = VGroup(src.row_rect(i, ROW_COLOR, opacity=0.18), src.cell_rect(i, freq_col, ROW_COLOR, opacity=0.35),
                        dst.cell_rect(i, rel_col, ROW_COLOR, opacity=0.12))
            lbl, line = self.work_row(
                f"{labels[i]}:",
                [(str(f), ROW_COLOR), (r"\div", WHITE), (str(total), TOTAL_COLOR),
                 ("=", WHITE), (f"{f / total:.2f}", WHITE), ("=", WHITE), (self.pct(p), ANSWER_COLOR)],
            )
            self.play(FadeIn(hl), FadeIn(lbl), FadeIn(line[:3]))
            self.next_slide()
            self.play(FadeIn(line[3:5]))
            self.next_slide()
            self.play(FadeIn(line[5:]))
            self.next_slide()
            self.place_value(dst, i, rel_col, f"{p:g}%", source=line[-1])
            self.next_slide()
            self.play(FadeOut(hl), FadeOut(lbl), FadeOut(line))
        return pcts

    def fill_relative_total(self, table, rel_col, pcts, total_box=None):
        """Relative frequencies always add to 100%."""
        hl = table.rect(0, table.n_rows - 1, rel_col, rel_col, ANSWER_COLOR, opacity=0.15)
        pieces = []
        for j, p in enumerate(pcts):
            if j:
                pieces.append(("+", WHITE))
            pieces.append((self.pct(p), ANSWER_COLOR))
        pieces += [("=", WHITE), (self.pct(round(sum(pcts), 1)), TOTAL_COLOR)]
        lbl, line = self.work_row("Total:", pieces, font_size=36)
        self.play(FadeIn(hl), FadeIn(lbl), FadeIn(line[:-2]))
        self.next_slide()
        self.play(FadeIn(line[-2:]))
        self.next_slide()
        fades = [FadeOut(hl), FadeOut(lbl), FadeOut(line)]
        if total_box is not None:
            fades.append(FadeOut(total_box))
        self.place_value(table, table.total_row, rel_col, f"{sum(pcts):g}%", source=line[-1],
                         color=TOTAL_COLOR, bold=True)
        self.next_slide()
        self.play(*fades)

    # ---- interpretation questions ----------------------------------------

    def show_question_list(self, prompts, top_y=PROMPT_Y, font_size=22):
        """All of a problem's questions at once (for YOU DO practice)."""
        lines = VGroup(*[Text(p, font_size=font_size) for p in prompts])
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        if lines.width > 10.3:
            lines.scale_to_fit_width(10.3)
        lines.move_to([-6.6, top_y, 0], aligned_edge=UL)
        self.play(FadeIn(lines))
        return lines

    def run_question(self, prompt, steps, tables, font_size=24, math_size=38):
        """One interpretation question, one click per step. steps entries:
            ("hl", [(table_key, row, col_or_None, color), ...])  highlight cells / whole rows
            ("math", [(tex, color), ...])                         next work line
            ("text", "words", color)                              next work line (plain words)
            ("answer", "18 students")                             boxed yellow answer
        Work lines stack under the prompt; the answer sits beside the last
        line. Everything clears at the end."""
        q = Text(prompt, font_size=font_size, weight=BOLD)
        if q.width > 13.4:
            q.scale_to_fit_width(13.4)
        q.move_to([0, PROMPT_Y, 0])
        self.play(FadeIn(q))
        self.next_slide()

        shown = VGroup(q)
        stack = VGroup()
        for step in steps:
            kind = step[0]
            if kind == "hl":
                rects = VGroup()
                for key, r, c, color in step[1]:
                    t = tables[key]
                    rects.add(t.row_rect(r, color, 0.25) if c is None else t.cell_rect(r, c, color, 0.35))
                self.play(FadeIn(rects))
                shown.add(rects)
            elif kind in ("math", "text"):
                if kind == "math":
                    m = self.math_line(step[1], font_size=math_size)
                else:
                    m = Text(step[1], font_size=font_size, color=step[2] if len(step) > 2 else WHITE)
                anchor = stack[-1] if len(stack) else q
                m.next_to(anchor, DOWN, buff=LINE_BUFF)
                stack.add(m)
                self.play(FadeIn(m, shift=UP * 0.15))
                shown.add(m)
            elif kind == "answer":
                a = Text(step[1], font_size=30, weight=BOLD, color=ANSWER_COLOR)
                box = SurroundingRectangle(a, color=ANSWER_COLOR, buff=0.15)
                ans = VGroup(a, box)
                if len(stack):
                    ans.next_to(stack[-1], RIGHT, buff=0.6)
                else:
                    ans.next_to(q, DOWN, buff=LINE_BUFF)
                self.play(FadeIn(a), Create(box))
                shown.add(ans)
            self.next_slide()

        self.play(FadeOut(shown))

    # ---- ogive ------------------------------------------------------------

    def interpolate_ogive(self, xs, ys, p):
        """x-value where the ogive (straight segments through (xs, ys)) reaches y = p."""
        for (x0, y0), (x1, y1) in zip(zip(xs, ys), zip(xs[1:], ys[1:])):
            if y0 <= p <= y1 and y1 > y0:
                return x0 + (x1 - x0) * (p - y0) / (y1 - y0)
        raise ValueError(p)

    def plot_ogive_points(self, plane, table, value_col, xs, ys, unit=""):
        """One click per table row: highlight it, drop its point with its
        coordinates, then keep the dot and move on."""
        dots = VGroup()
        for i, (x, y) in enumerate(zip(xs, ys)):
            hl = table.row_rect(i, ROW_COLOR, opacity=0.25)
            dot = Dot(plane.c2p(x, y), color=BLUE, radius=0.08)
            coord = MathTex(f"({x}{unit},\\ {y}\\%)", font_size=26, color=ROW_COLOR)
            coord.next_to(dot, UL if i else UR, buff=0.08)
            self.play(FadeIn(hl), FadeIn(dot, scale=1.5), FadeIn(coord))
            self.next_slide()
            self.play(FadeOut(hl), FadeOut(coord))
            dots.add(dot)
        return dots

    def connect_ogive(self, plane, xs, ys):
        curve = VMobject(color=BLUE, stroke_width=4)
        curve.set_points_as_corners([plane.c2p(x, y) for x, y in zip(xs, ys)])
        self.play(Create(curve), run_time=1.5)
        self.next_slide()
        return curve

    def estimate_percentile(self, plane, xs, ys, p, name, unit, result_anchor, x_round=0):
        """Across from p% to the curve, down to the x-axis, then the boxed
        estimate written on the left. Returns the estimate."""
        color = PERCENTILE_COLORS[p]
        x_p = self.interpolate_ogive(xs, ys, p)
        est = round(x_p, x_round) if x_round else round(x_p)
        x_min = plane.x_range[0]

        across = DashedLine(plane.c2p(x_min, p), plane.c2p(x_p, p), color=color, stroke_width=4)
        hit = Dot(plane.c2p(x_p, p), color=color, radius=0.08)
        self.play(Create(across), FadeIn(hit))
        self.next_slide()

        down = DashedLine(plane.c2p(x_p, p), plane.c2p(x_p, 0), color=color, stroke_width=4)
        foot = Dot(plane.c2p(x_p, 0), color=color, radius=0.08)
        tag = MathTex(f"\\approx {est:g}", font_size=28, color=color)
        tag.next_to(foot, UR, buff=0.08)
        self.play(Create(down), FadeIn(foot), FadeIn(tag))
        self.next_slide()

        label = MathTex(name, f"\\ ({p}\\%)", r"\approx", font_size=36)
        label[0].set_color(color)
        label[1].set_color(color)
        value = Text(f"{est:g} {unit}", font_size=30, weight=BOLD, color=ANSWER_COLOR)
        box = SurroundingRectangle(value, color=ANSWER_COLOR, buff=0.12)
        row = VGroup(label, VGroup(value, box)).arrange(RIGHT, buff=0.3).move_to(result_anchor)
        self.play(FadeIn(row, shift=UP * 0.15))
        self.next_slide()
        return est

    # ---- whole-problem runners (shared by I DO and YOU DO scenes) ---------

    TWO_TABLE_COLS = ([-5.6, -3.1, -1.2], [0.6, 3.3, 5.6])
    COMBINED_COLS = ([-6.6, -4.6, -3.0, -1.1], [0.4, 3.1, 5.3])
    OGIVE_COLS = [-6.9, -4.4, -2.7]
    TIMER_POS = np.array([5.5, -1.55, 0])     # lower right, beside the question list

    def run_problem(self, spec):
        """spec["kind"]: "cumulative" (Part 1), "relative" (Part 2) or
        "combined" (Part 3). With spec["practice"], the blank tables and
        questions get a countdown first, then the full solution plays."""
        self.camera.background_color = BACKGROUND_COLOR
        heading = self.show_heading(spec["heading"])
        self.show_scenario(spec["scenario"], spec["task"])
        tables = self._problem_tables(spec)
        self.next_slide()

        if spec.get("practice"):
            self._practice_countdown(
                lambda: self.show_question_list([p for p, _ in spec["questions"]]),
                spec.get("seconds", 300), self.TIMER_POS, bar_height=1.6,
            )
            self.swap_heading(heading, spec["solution_heading"])
            self.next_slide()

        self._fill_problem(spec, tables)
        for prompt, steps in spec["questions"]:
            self.run_question(prompt, steps, tables)

    def _practice_countdown(self, show_extra, seconds, position, bar_height=3.0):
        before = set(self.mobjects)
        show_extra()
        self.show_timer(seconds, position=position, bar_height=bar_height)
        self.play(FadeOut(*[m for m in self.mobjects if m not in before]))

    def _problem_tables(self, spec):
        freqs = spec["freqs"]
        total = sum(freqs)
        freq_strs = [str(f) for f in freqs]
        kind = spec["kind"]
        if kind == "combined":
            left_cols, right_cols = self.COMBINED_COLS
            left = self.build_table(
                "Class Frequency & Relative Freq. Table",
                [spec["var_header"], "Frequency\n(f)", "Relative\nFreq."], spec["classes"], left_cols,
                total_label="Total", columns={1: freq_strs}, total_values={1: str(total)},
            )
            right = self.build_table(
                "Cumulative Relative Freq. Table",
                [spec["cum_header"], "Cum. Rel.\nFreq."], spec["boundaries"], right_cols,
            )
            return {"left": left, "cum": right}

        left_cols, right_cols = self.TWO_TABLE_COLS
        freq = self.build_table(
            "Frequency Table", [spec["var_header"], "Frequency\n(f)"], spec["classes"], left_cols,
            total_label="Total", columns={1: freq_strs}, total_values={1: str(total)},
        )
        if kind == "cumulative":
            cum = self.build_table(
                "Cumulative Frequency Table", [spec["cum_header"], "Cumulative\nFrequency"],
                spec["boundaries"], right_cols,
            )
            return {"freq": freq, "cum": cum}
        rel = self.build_table(
            "Relative Frequency Table", [spec["var_header"], "Relative\nFreq. (%)"],
            spec["classes"], right_cols, total_label="Total",
        )
        return {"freq": freq, "rel": rel}

    def _fill_problem(self, spec, tables):
        freqs = spec["freqs"]
        total = sum(freqs)
        kind = spec["kind"]
        if kind == "cumulative":
            cum = self.fill_cumulative_column(tables["freq"], 1, tables["cum"], 1, freqs, spec["boundaries"])
            self.check_last_equals_total(tables["cum"], 1, cum[-1], tables["freq"], 1, total)
        elif kind == "relative":
            box = self.highlight_total(tables["freq"], 1)
            self.next_slide()
            pcts = self.fill_relative_column(tables["freq"], 1, tables["rel"], 1, freqs, total, spec["work_labels"])
            self.fill_relative_total(tables["rel"], 1, pcts, box)
        else:
            left = tables["left"]
            box = self.highlight_total(left, 1)
            self.next_slide()
            pcts = self.fill_relative_column(left, 1, left, 2, freqs, total, spec["work_labels"])
            self.fill_relative_total(left, 2, pcts, box)
            cum = self.fill_cumulative_column(left, 2, tables["cum"], 1, pcts, spec["boundaries"], percent=True)
            self.check_last_equals_total(tables["cum"], 1, cum[-1], left, 2, 100, percent=True)

    def run_ogive(self, spec):
        """Cumulative relative frequency table on the left, ogive on the
        right -- both stay up the whole time so students can check each
        point against its table row. (Needs GraphTemplate mixed in too.)"""
        self.camera.background_color = BACKGROUND_COLOR
        heading = self.show_heading(spec["heading"])
        self.show_scenario(spec["scenario"], spec["task"])

        xs, ys, unit = spec["xs"], spec["ys"], spec["unit"]
        table = self.build_table(
            spec["table_title"], ["Boundary", "Cum. Rel.\nFreq."],
            spec.get("labels") or [f"Less than {x} {unit}" for x in xs], self.OGIVE_COLS,
            columns={1: [f"{y}%" for y in ys]},
        )
        plane, _ = self.show_data_plane(
            [xs[0], xs[-1], (xs[1] - xs[0]) / 4], [0, 100, 5],
            xs, [0, 25, 50, 75, 100], spec["x_label"], "Cumulative Rel. Freq. (%)",
            x_length=7.0, y_length=5.2, center=np.array([3.2, -0.2, 0]), y_suffix="\\%",
            y_number_colors=PERCENTILE_COLORS,
        )
        self.next_slide()

        if spec.get("practice"):
            self._practice_countdown(lambda: None, spec.get("seconds", 300),
                                     np.array([-4.8, -1.6, 0]), bar_height=1.3)
            self.swap_heading(heading, spec["solution_heading"])
            self.next_slide()

        self.plot_ogive_points(plane, table, 1, xs, ys, unit=f"\\text{{ {unit}}}" if unit == "g" else "")
        self.connect_ogive(plane, xs, ys)
        for (p, name), y in zip([(25, "Q_1"), (50, r"\text{Median}"), (75, "Q_3")], [-1.85, -2.6, -3.35]):
            self.estimate_percentile(plane, xs, ys, p, name, spec["answer_unit"], np.array([-4.8, y, 0]))
