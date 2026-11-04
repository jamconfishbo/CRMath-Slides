# templates/box_plot.py

from manim import *

from components.theme import ANSWER_COLOR, BACKGROUND_COLOR, GRID_COLOR, INDICATE_COLOR, PARENT_GRAPH_COLOR
from templates.cumulative_frequency import CumulativeFrequencyTemplate
from templates.graph import GraphTemplate
from templates.mean_median import MeanMedianTemplate

# Color code for the whole lesson -- a statistic keeps its color in the ordered
# list, the answer box, the table and the work lines.
MEDIAN_COLOR = ANSWER_COLOR
Q1_COLOR = TEAL
Q3_COLOR = PINK
PLAYER_COLORS = [PARENT_GRAPH_COLOR, INDICATE_COLOR]   # first / second box plot

CROSSED_OPACITY = 0.3

HEADING_FONT_SIZE = 30
BODY_FONT_SIZE = 28
NUMBER_FONT_SIZE = 38
BOX_FONT_SIZE = 34
TAG_FONT_SIZE = 26

SLOT_X0 = -4.5          # x of the first ordered-list slot
SLOT_W = 0.78           # spacing between slots
SORT_ROW_Y = [-1.0, -2.4]
TOP_ROW_Y = [2.75, 1.6]

BLOCK_LEFT = -6.6       # left edge of the Step 2 work
BLANK_X = (-3.1, 1.2)  # the "lower half" / "upper half" blanks
ANSWER_X = 1.5          # left edge of the Q1 / Q3 answers

TABLE_COL_X = [-6.0, -3.6, -2.25, -0.9, 0.45, 1.8, 3.15, 4.5, 5.85]
TABLE_TOP_Y = 0.35
TABLE_TOP_Y_WITH_GRAPH = 2.85
TABLE_WORK_Y = -2.6
TABLE_TOP_Y_UNDER_GRAPH = -0.75
TABLE_WORK_Y_UNDER_GRAPH = -3.25
HEADERS = ["", "Min", "Q1", "Median", "Q3", "Max", "IQR", "Range"]

PLOT_Y = [2.2, 0.9]     # plane y of the first / second box plot
BOX_HALF_H = 0.28
GRAPH_SCALE_TOP = 0.75
GRAPH_CENTER_TOP = np.array([0.75, 1.6, 0])
QUESTION_TOP_Y = -0.5


def fmt(v):
    return f"{v:g}"


def ordinal(n):
    return f"{n}{ {1: 'st', 2: 'nd', 3: 'rd'}.get(n if n < 20 else n % 10, 'th') }"


def middle_indices(lo, hi):
    """Index (odd count) or pair of indices (even count) at the center of lo..hi."""
    n = hi - lo + 1
    return [lo + n // 2] if n % 2 else [lo + n // 2 - 1, lo + n // 2]


class FiveNumbers:
    """A five-number summary, e.g. one read off a given box plot."""

    def __init__(self, name, minimum, q1, median, q3, maximum):
        self.name = name
        self.min = minimum
        self.q1 = q1
        self.median = median
        self.q3 = q3
        self.max = maximum
        self.iqr = q3 - q1
        self.range = maximum - minimum

    @property
    def table_row(self):
        return [self.min, self.q1, self.median, self.q3, self.max, self.iqr, self.range]


class DataSet(FiveNumbers):
    """One data set and everything computed from it. Split rule: an odd count
    leaves the median out of both halves; an even count splits exactly in half."""

    def __init__(self, name, raw):
        self.raw = raw
        self.sorted = sorted(raw)
        self.n = len(raw)
        self.median_idx = middle_indices(0, self.n - 1)
        half = self.n // 2
        self.lower = (0, half - 1)
        self.upper = (self.n - half, self.n - 1)
        self.q1_idx = middle_indices(*self.lower)
        self.q3_idx = middle_indices(*self.upper)
        super().__init__(name, self.sorted[0], self._average(self.q1_idx), self._average(self.median_idx),
                         self._average(self.q3_idx), self.sorted[-1])

    def _average(self, idx):
        return sum(self.sorted[i] for i in idx) / len(idx)

    @property
    def is_even(self):
        return self.n % 2 == 0


class OrderedRow:
    """A data set's "designated spot": one blank per value, numbers written on
    the blanks, and the marks (strikes, highlights, underlines, tags) on top."""

    def __init__(self, data, y):
        self.data = data
        self.y = y
        self.label = Text(data.name, font_size=BODY_FONT_SIZE, weight=BOLD)
        self.label.move_to([SLOT_X0 - 0.55, y + 0.2, 0], aligned_edge=RIGHT)
        self.slots = VGroup(*[
            Line([self.x(i) - SLOT_W * 0.38, y, 0], [self.x(i) + SLOT_W * 0.38, y, 0], color=GREY_B, stroke_width=2)
            for i in range(data.n)
        ])
        self.numbers = [
            MathTex(str(v), font_size=NUMBER_FONT_SIZE).move_to([self.x(i), y + 0.27, 0])
            for i, v in enumerate(data.sorted)
        ]
        self.strikes = VGroup()

    def x(self, i):
        return SLOT_X0 + i * SLOT_W

    def center_x(self, idx):
        return sum(self.x(i) for i in idx) / len(idx)

    def highlight(self, i, color):
        return Rectangle(
            width=SLOT_W - 0.08, height=0.56, fill_color=color, fill_opacity=0.3, stroke_color=color, stroke_width=3,
        ).move_to(self.numbers[i])

    def underline(self, lo, hi, color):
        return Line(
            [self.x(lo) - SLOT_W * 0.38, self.y, 0], [self.x(hi) + SLOT_W * 0.38, self.y, 0],
            color=color, stroke_width=7,
        )

    def divider(self):
        x = self.center_x(self.data.median_idx)
        return Line([x, self.y - 0.05, 0], [x, self.y + 0.58, 0], color=MEDIAN_COLOR, stroke_width=5)

    def tag(self, tex, idx, color=WHITE):
        return MathTex(tex, font_size=TAG_FONT_SIZE, color=color).move_to([self.center_x(idx), self.y - 0.28, 0])

    def median_tag(self):
        return self.tag(rf"\text{{Med}}={fmt(self.data.median)}", self.data.median_idx, MEDIAN_COLOR)

    def q1_tag(self):
        return self.tag(rf"Q_1={fmt(self.data.q1)}", self.data.q1_idx, Q1_COLOR)

    def q3_tag(self):
        return self.tag(rf"Q_3={fmt(self.data.q3)}", self.data.q3_idx, Q3_COLOR)

    def min_tag(self):
        return self.tag(rf"\text{{Min}}={self.data.min}", [0])

    def max_tag(self):
        return self.tag(rf"\text{{Max}}={self.data.max}", [self.data.n - 1])

    def finished_marks(self):
        d = self.data
        marks = VGroup(*[self.highlight(i, MEDIAN_COLOR) for i in d.median_idx])
        marks.add(*[self.highlight(i, Q1_COLOR) for i in d.q1_idx])
        marks.add(*[self.highlight(i, Q3_COLOR) for i in d.q3_idx])
        if d.is_even:
            marks.add(self.divider())
        marks.add(self.q1_tag(), self.median_tag(), self.q3_tag())
        return marks


class BoxPlotTemplate(CumulativeFrequencyTemplate, MeanMedianTemplate, GraphTemplate):
    """Mixin for "compare two data sets with box plots", built by hand the way
    the packet does it: order each set, cross inward to the median, split,
    cross inward to Q1 and Q3, fill in the table, draw the plots, interpret.

    Each run_* method is one scene and redraws what the previous scene left on
    screen, so a scene can be re-rendered on its own. All the statistics are
    computed from spec["data"].

    spec: {"context": str, "data": [(name, raw values, raw-table label), x2],
           "x_range": [min, max, 1], "x_numbers": [...], "x_label": str,
           "questions": [{"prompt", "answer", "show", "follow", "explain"}, ...]}
    A problem that starts from given box plots uses "summaries" in place of
    "data" and run_read_table() in place of the ordering / Step 2 / table scenes;
    see run_percents() for its "percents" questions.
    """

    def data_sets(self, spec):
        """spec["data"] holds raw data to work from; spec["summaries"] holds
        (name, min, Q1, median, Q3, max) read off a given box plot."""
        if "summaries" in spec:
            return [FiveNumbers(*row) for row in spec["summaries"]]
        return [DataSet(name, raw) for name, raw, _ in spec["data"]]

    def use_heading(self, text, animate=True):
        heading = Text(text, font_size=HEADING_FONT_SIZE, weight=BOLD).to_edge(UP, buff=0.22)
        if animate:
            self.play(FadeIn(heading))
        else:
            self.add(heading)
        return heading

    # ---- marks ------------------------------------------------------------

    def strike(self, row, i):
        s = self.cross_out_datum(row.numbers[i], stroke_width=6)
        row.strikes.add(s)
        self.play(Create(s), row.numbers[i].animate.set_opacity(CROSSED_OPACITY), run_time=0.4)
        self.next_slide()

    def cross_inward(self, row, lo, hi):
        """Cross off left, right, left, right -- one click each -- until the
        one or two middle values of lo..hi are left."""
        while hi - lo >= 2:
            self.strike(row, lo)
            self.strike(row, hi)
            lo += 1
            hi -= 1

    def clear_strike_animations(self, row):
        return [FadeOut(row.strikes)] + [n.animate.set_opacity(1) for n in row.numbers]

    def add_rows(self, data_sets, finished):
        """Both ordered lists at the top of the screen, as finished work."""
        rows = []
        for d, y, done in zip(data_sets, TOP_ROW_Y, finished):
            row = OrderedRow(d, y)
            self.add(row.label, row.slots, *row.numbers)
            row.marks = row.finished_marks() if done else VGroup()
            self.add(row.marks)
            rows.append(row)
        return rows

    # ---- Step 1: order the data -------------------------------------------

    def raw_row(self, values, label_text, y):
        label = Text(label_text, font_size=BODY_FONT_SIZE, weight=BOLD)
        label.move_to([-6.7, y, 0], aligned_edge=LEFT)
        row, numbers = self._number_row([str(v) for v in values], 32)
        for m in row:
            m.align_to(numbers[0], DOWN)
        row.arrange(RIGHT, buff=0.14, aligned_edge=DOWN)
        row.move_to([-3.05, y, 0], aligned_edge=LEFT)
        return label, row, numbers

    def run_ordering(self, spec):
        self.camera.background_color = BACKGROUND_COLOR
        data = self.data_sets(spec)
        heading = self.use_heading(spec["heading"])
        context = Text(spec["context"], font_size=BODY_FONT_SIZE).next_to(heading, DOWN, buff=0.22)

        raw_ys = [2.15, 1.45]
        frame = VGroup(
            Rectangle(width=13.7, height=1.4, stroke_color=GREY_B, stroke_width=2).move_to([0, sum(raw_ys) / 2, 0]),
            Line([-6.85, sum(raw_ys) / 2, 0], [6.85, sum(raw_ys) / 2, 0], color=GREY_B, stroke_width=2),
            Line([-3.2, raw_ys[0] + 0.35, 0], [-3.2, raw_ys[1] - 0.35, 0], color=GREY_B, stroke_width=2),
        )
        raw_mobs, raw_numbers = VGroup(), []
        for (_, values, label_text), y in zip(spec["data"], raw_ys):
            label, row, numbers = self.raw_row(values, label_text, y)
            raw_mobs.add(label, row)
            raw_numbers.append(numbers)

        self.play(FadeIn(context), Create(frame), FadeIn(raw_mobs))
        self.next_slide()

        step = Text("Step 1: Put each data set in order from least to greatest.", font_size=BODY_FONT_SIZE, weight=BOLD)
        step.move_to([0, 0.35, 0])
        rows = [OrderedRow(d, y) for d, y in zip(data, SORT_ROW_Y)]
        self.play(FadeIn(step), *[FadeIn(r.label) for r in rows], *[Create(r.slots) for r in rows])
        self.next_slide()

        raw_strikes = VGroup()
        for d, row, numbers in zip(data, rows, raw_numbers):
            order = sorted(range(d.n), key=lambda i: d.raw[i])
            for i, source_i in enumerate(order):
                source = numbers[source_i]
                s = self.cross_out_datum(source, stroke_width=5)
                raw_strikes.add(s)
                self.play(Create(s), source.animate.set_opacity(CROSSED_OPACITY), run_time=0.35)
                self.play(TransformFromCopy(source, row.numbers[i]), run_time=0.6)
                self.next_slide()

        self.play(
            FadeOut(context), FadeOut(frame), FadeOut(raw_mobs), FadeOut(raw_strikes), FadeOut(step), FadeOut(heading),
            *[VGroup(r.label, r.slots, *r.numbers).animate.shift(UP * (top - r.y)) for r, top in zip(rows, TOP_ROW_Y)],
        )

    # ---- Step 2: median and quartiles -------------------------------------

    def answer_box(self, width=1.15):
        return Rectangle(width=width, height=0.58, stroke_color=GREY_B, stroke_width=3)

    def average_block(self, label_tex, color):
        """label = (box + box) / 2 = box, all boxes empty. Returns (group, parts)."""
        label = MathTex(label_tex, "=", font_size=BOX_FONT_SIZE)
        label[0].set_color(color)
        a, b = self.answer_box(0.95), self.answer_box(0.95)
        top = VGroup(a, MathTex("+", font_size=BOX_FONT_SIZE), b).arrange(RIGHT, buff=0.12)
        bar = Line(ORIGIN, RIGHT * top.width, color=WHITE, stroke_width=3)
        two = MathTex("2", font_size=BOX_FONT_SIZE)
        fraction = VGroup(top, bar, two).arrange(DOWN, buff=0.08)
        equals = MathTex("=", font_size=BOX_FONT_SIZE)
        result = self.answer_box()
        group = VGroup(label, fraction, equals, result).arrange(RIGHT, buff=0.16)
        return group, {"a": a, "b": b, "result": result}

    def single_block(self, label_tex, color):
        """label = box, the box empty. Returns (group, parts)."""
        label = MathTex(label_tex, "=", font_size=BOX_FONT_SIZE)
        label[0].set_color(color)
        result = self.answer_box()
        return VGroup(label, result).arrange(RIGHT, buff=0.16), {"result": result}

    def fill(self, box, value, color, source=None):
        """Animations that put value in box -- flown from `source` when given."""
        m = MathTex(value, font_size=BOX_FONT_SIZE, color=color).move_to(box)
        anim = TransformFromCopy(source, m) if source is not None else Write(m)
        return [anim, box.animate.set_stroke(color)], m

    def half_line(self, side, count, y):
        label = Text(f"{side} half ({count} values):", font_size=BODY_FONT_SIZE)
        label.move_to([BLOCK_LEFT, y, 0], aligned_edge=LEFT)
        blank = Line([BLANK_X[0], y - 0.24, 0], [BLANK_X[1], y - 0.24, 0], color=GREY_B, stroke_width=2)
        return label, blank

    def run_step2(self, spec, index):
        self.camera.background_color = BACKGROUND_COLOR
        data = self.data_sets(spec)
        rows = self.add_rows(data, [i < index for i in range(len(data))])
        row, d = rows[index], data[index]
        heading = self.use_heading("Step 2: Find the median, then split each data set in half.", animate=index == 0)
        block = VGroup()

        # ---- median ----
        if d.is_even:
            where = (f"The median is between the {ordinal(d.median_idx[0] + 1)} "
                     f"and {ordinal(d.median_idx[1] + 1)} values.")
            median_block, parts = self.average_block(r"\text{Median}", MEDIAN_COLOR)
            median_y, lower_y, upper_y = -0.55, -2.0, -3.1
        else:
            where = f"The median is the {ordinal(d.median_idx[0] + 1)} value."
            median_block, parts = self.single_block(r"\text{Median}", MEDIAN_COLOR)
            median_y, lower_y, upper_y = -0.2, -1.4, -3.05
        intro = Text(f"{d.name} has {d.n} data points ({'even' if d.is_even else 'odd'}). {where}",
                     font_size=BODY_FONT_SIZE)
        intro.move_to([BLOCK_LEFT, 0.55, 0], aligned_edge=LEFT)
        median_block.move_to([0, median_y, 0])
        block.add(intro, median_block)
        self.play(FadeIn(intro), FadeIn(median_block))
        self.next_slide()

        self.cross_inward(row, 0, d.n - 1)

        highlights = VGroup(*[row.highlight(i, MEDIAN_COLOR) for i in d.median_idx])
        self.play(FadeIn(highlights))
        self.next_slide()

        calc_highlight = SurroundingRectangle(
            median_block, color=MEDIAN_COLOR, fill_color=MEDIAN_COLOR, fill_opacity=0.12, buff=0.12,
        )
        block.add(calc_highlight)
        if d.is_even:
            fill_a, a = self.fill(parts["a"], str(d.sorted[d.median_idx[0]]), MEDIAN_COLOR, row.numbers[d.median_idx[0]])
            fill_b, b = self.fill(parts["b"], str(d.sorted[d.median_idx[1]]), MEDIAN_COLOR, row.numbers[d.median_idx[1]])
            block.add(a, b)
            self.play(FadeIn(calc_highlight), *fill_a, *fill_b)
            self.next_slide()
            fill_r, r = self.fill(parts["result"], fmt(d.median), MEDIAN_COLOR)
        else:
            fill_r, r = self.fill(parts["result"], fmt(d.median), MEDIAN_COLOR, row.numbers[d.median_idx[0]])
            self.play(FadeIn(calc_highlight), *fill_r)
            fill_r = []
        block.add(r)
        if fill_r:
            self.play(*fill_r)
        self.next_slide()

        # ---- split ----
        keep = VGroup(row.median_tag())
        if d.is_even:
            keep.add(row.divider())
        self.play(*self.clear_strike_animations(row), FadeIn(keep))
        row.strikes = VGroup()
        self.next_slide()

        count = d.lower[1] - d.lower[0] + 1
        underlines = VGroup()
        half_specs = [
            ("Lower", d.lower, d.q1_idx, d.q1, Q1_COLOR, r"Q_1", lower_y, row.q1_tag),
            ("Upper", d.upper, d.q3_idx, d.q3, Q3_COLOR, r"Q_3", upper_y, row.q3_tag),
        ]
        answer_blocks = []
        for side, (lo, hi), _, _, color, tex, y, _ in half_specs:
            label, blank = self.half_line(side, count, y)
            line = row.underline(lo, hi, color)
            underlines.add(line)
            listed = MathTex(", ".join(str(v) for v in d.sorted[lo:hi + 1]), font_size=BOX_FONT_SIZE, color=color)
            listed.move_to([sum(BLANK_X) / 2, y, 0])
            if listed.width > BLANK_X[1] - BLANK_X[0]:
                listed.scale_to_fit_width(BLANK_X[1] - BLANK_X[0])
            answer, answer_parts = (self.average_block if count % 2 == 0 else self.single_block)(tex, color)
            answer.move_to([ANSWER_X, y, 0], aligned_edge=LEFT)
            answer_blocks.append(answer_parts)
            block.add(label, blank, listed, answer)
            self.play(Create(line), FadeIn(label), FadeIn(blank), FadeIn(answer))
            self.play(TransformFromCopy(VGroup(*row.numbers[lo:hi + 1]), listed))
            self.next_slide()

        # ---- quartiles ----
        for (_, (lo, hi), idx, value, color, _, _, make_tag), answer_parts in zip(half_specs, answer_blocks):
            self.cross_inward(row, lo, hi)
            marks = VGroup(*[row.highlight(i, color) for i in idx])
            self.play(FadeIn(marks))
            self.next_slide()
            if len(idx) == 2:
                fill_a, a = self.fill(answer_parts["a"], str(d.sorted[idx[0]]), color, row.numbers[idx[0]])
                fill_b, b = self.fill(answer_parts["b"], str(d.sorted[idx[1]]), color, row.numbers[idx[1]])
                block.add(a, b)
                self.play(*fill_a, *fill_b)
                self.next_slide()
                fill_r, r = self.fill(answer_parts["result"], fmt(value), color)
            else:
                fill_r, r = self.fill(answer_parts["result"], fmt(value), color, row.numbers[idx[0]])
            block.add(r)
            self.play(*fill_r, FadeIn(make_tag()))
            self.next_slide()

        # The heading carries over between data sets and leaves after the last one.
        exit_heading = [FadeOut(heading)] if index == len(data) - 1 else []
        self.play(FadeOut(block), FadeOut(underlines), *exit_heading, *self.clear_strike_animations(row))

    # ---- Step 3: the table ------------------------------------------------

    def summary_grid(self, data, top_y, filled):
        columns = None
        if filled:
            columns = {c + 1: [fmt(d.table_row[c]) for d in data] for c in range(len(HEADERS) - 1)}
        table = self.build_table(
            "Five-Number Summary, IQR, and Range", HEADERS, [d.name for d in data], TABLE_COL_X,
            top_y=top_y, header_h=0.55, row_h=0.6, font_size=30, header_font_size=24,
            columns=columns, animate=False,
        )
        if filled:
            for r in range(len(data)):
                table.values[(r, 2)].set_color(Q1_COLOR)
                table.values[(r, 3)].set_color(MEDIAN_COLOR)
                table.values[(r, 4)].set_color(Q3_COLOR)
        return table

    def run_table(self, spec):
        self.camera.background_color = BACKGROUND_COLOR
        data = self.data_sets(spec)
        rows = self.add_rows(data, [True] * len(data))
        heading = self.use_heading("Step 3: Complete the five-number summary, IQR, and range.")
        table = self.summary_grid(data, TABLE_TOP_Y, filled=False)
        self.play(FadeIn(table.group))
        self.next_slide()

        tags = VGroup()
        for r, (row, d) in enumerate(zip(rows, data)):
            min_tag, max_tag = row.min_tag(), row.max_tag()
            tags.add(min_tag, max_tag)
            self.play(FadeIn(min_tag))
            self.place_value(table, r, 1, fmt(d.min), source=min_tag, color=WHITE)
            self.next_slide()
            for c, make_tag, value, color in [
                (2, row.q1_tag, d.q1, Q1_COLOR),
                (3, row.median_tag, d.median, MEDIAN_COLOR),
                (4, row.q3_tag, d.q3, Q3_COLOR),
            ]:
                self.place_value(table, r, c, fmt(value), source=make_tag(), color=color)
                self.next_slide()
            self.play(FadeIn(max_tag))
            self.place_value(table, r, 5, fmt(d.max), source=max_tag, color=WHITE)
            self.next_slide()

            self.fill_iqr_and_range(table, r, d, TABLE_WORK_Y)

        self.play(
            FadeOut(heading), FadeOut(tags),
            *[FadeOut(m) for row in rows for m in [row.label, row.slots, *row.numbers]],
            *[FadeOut(row.marks) for row in rows],
            table.group.animate.shift(UP * (TABLE_TOP_Y_WITH_GRAPH - TABLE_TOP_Y)),
        )

    def fill_iqr_and_range(self, table, r, d, y):
        self.table_subtraction(table, r, d, 6, "IQR = Q3 - Q1:", (d.q3, Q3_COLOR, 4), (d.q1, Q1_COLOR, 2), d.iqr, y)
        self.table_subtraction(table, r, d, 7, "Range = Max - Min:", (d.max, WHITE, 5), (d.min, WHITE, 1), d.range, y)

    def table_subtraction(self, table, r, d, col, label, big, small, result, y):
        """click 1: highlight the two source cells + "big - small"
        click 2: "= result" (boxed)    click 3: result copied into the table"""
        hl = VGroup(table.cell_rect(r, big[2], big[1], opacity=0.3), table.cell_rect(r, small[2], small[1], opacity=0.3))
        lbl, line = self.work_row(
            f"{d.name}   {label}",
            [(fmt(big[0]), big[1]), ("-", WHITE), (fmt(small[0]), small[1]), ("=", WHITE), (fmt(result), WHITE)],
            y=y,
        )
        self.play(FadeIn(hl), FadeIn(lbl), FadeIn(line[:3]))
        self.next_slide()
        box = SurroundingRectangle(line[-1], color=ANSWER_COLOR, buff=0.1)
        self.play(FadeIn(line[3:]), Create(box))
        self.next_slide()
        self.place_value(table, r, col, fmt(result), source=line[-1], color=WHITE)
        self.next_slide()
        self.play(FadeOut(hl), FadeOut(lbl), FadeOut(line), FadeOut(box))

    # ---- Step 4: the box plots --------------------------------------------

    def graph_base(self, spec, data, animate):
        x_range = spec["x_range"]
        plane, axis_labels = self.show_data_plane(
            x_range, [0, 3, 3], spec["x_numbers"], [], spec["x_label"], None,
            x_length=11.0, y_length=3.9, center=[0.75, -1.2, 0], label_font_size=26, animate=False,
        )
        majors = VGroup(*[
            Line(plane.c2p(x, 0), plane.c2p(x, 3), color=GRID_COLOR, stroke_width=2)
            for x in spec["x_numbers"]
        ])
        names = VGroup(*[
            Text(d.name, font_size=BODY_FONT_SIZE, weight=BOLD, color=color)
            .next_to(plane.c2p(x_range[0], y), LEFT, buff=0.2)
            for d, y, color in zip(data, PLOT_Y, PLAYER_COLORS)
        ])
        if animate:
            self.play(Create(plane), FadeIn(majors), FadeIn(axis_labels), FadeIn(names))
        return plane, VGroup(plane, majors, axis_labels, names)

    def plot_parts(self, plane, d, y, color):
        def at(x, offset=0):
            return plane.c2p(x, y + offset)

        def tick(x, tick_color=color, width=5):
            return Line(at(x, -BOX_HALF_H), at(x, BOX_HALF_H), color=tick_color, stroke_width=width)

        def value(x, tick_color=WHITE):
            return MathTex(fmt(x), font_size=30, color=tick_color).next_to(at(x, BOX_HALF_H), UP, buff=0.07)

        corners = [at(d.q1, -BOX_HALF_H), at(d.q3, -BOX_HALF_H), at(d.q3, BOX_HALF_H), at(d.q1, BOX_HALF_H)]
        return {
            "ticks": [tick(d.min), tick(d.q1), tick(d.median, MEDIAN_COLOR, 6), tick(d.q3), tick(d.max)],
            "values": [value(d.min), value(d.q1, Q1_COLOR), value(d.median, MEDIAN_COLOR),
                       value(d.q3, Q3_COLOR), value(d.max)],
            "box": Polygon(*corners, color=color, fill_color=color, fill_opacity=0.4, stroke_width=5),
            "whiskers": VGroup(Line(at(d.min), at(d.q1), color=color, stroke_width=5),
                               Line(at(d.q3), at(d.max), color=color, stroke_width=5)),
        }

    def run_box_plots(self, spec):
        self.camera.background_color = BACKGROUND_COLOR
        data = self.data_sets(spec)
        heading = self.use_heading("Step 4: Draw both box plots above the number line.", animate=False)
        table = self.summary_grid(data, TABLE_TOP_Y_WITH_GRAPH, filled=True)
        self.add(table.group)

        plane, graph = self.graph_base(spec, data, animate=True)
        self.next_slide()

        plots = VGroup()
        for r, (d, y, color) in enumerate(zip(data, PLOT_Y, PLAYER_COLORS)):
            parts = self.plot_parts(plane, d, y, color)
            for k, (tick, value) in enumerate(zip(parts["ticks"], parts["values"])):
                cell = table.cell_rect(r, k + 1, color, opacity=0.3)
                self.play(FadeIn(cell), Create(tick), FadeIn(value), run_time=0.6)
                self.next_slide()
                self.play(FadeOut(cell), run_time=0.2)
            self.play(Create(parts["box"]))
            self.bring_to_front(parts["ticks"][2])
            self.next_slide()
            self.play(Create(parts["whiskers"]))
            self.next_slide()
            plots.add(parts["box"], parts["whiskers"], *parts["ticks"], *parts["values"])

        self.play(
            FadeOut(table.group), FadeOut(heading),
            VGroup(graph, plots).animate.scale(GRAPH_SCALE_TOP).move_to(GRAPH_CENTER_TOP),
        )

    # ---- Step 5: interpret ------------------------------------------------

    def graph_top(self, spec, data, show_values=True):
        """The finished graph at its spot above the questions. Returns (plane,
        all parts by data set). show_values=False leaves the value labels off
        screen, still in position, for students to read off the plot first."""
        plane, graph = self.graph_base(spec, data, animate=False)
        all_parts = [self.plot_parts(plane, d, y, c) for d, y, c in zip(data, PLOT_Y, PLAYER_COLORS)]
        drawn, values = VGroup(graph), VGroup()
        for parts in all_parts:
            drawn.add(parts["box"], parts["whiskers"], *parts["ticks"])
            values.add(*parts["values"])
        VGroup(drawn, values).scale(GRAPH_SCALE_TOP).move_to(GRAPH_CENTER_TOP)
        self.add(drawn)
        if show_values:
            self.add(values)
        return plane, all_parts

    def span_note(self, plane, x0, x1, y, text):
        """Double arrow under a box plot from x0 to x1, labeled in yellow."""
        arrow = DoubleArrow(
            plane.c2p(x0, y - BOX_HALF_H - 0.12), plane.c2p(x1, y - BOX_HALF_H - 0.12),
            color=ANSWER_COLOR, buff=0, stroke_width=4, tip_length=0.14,
        )
        label = Text(text, font_size=22, color=ANSWER_COLOR).next_to(arrow, DOWN, buff=0.04)
        return VGroup(arrow, label)

    def graph_callout(self, plane, data, all_parts, show):
        if show == "median":
            return VGroup(*[
                SurroundingRectangle(VGroup(p["ticks"][2], p["values"][2]), color=ANSWER_COLOR, buff=0.05)
                for p in all_parts
            ])
        if show == "iqr":
            return VGroup(*[
                self.span_note(plane, d.q1, d.q3, y, f"IQR = {fmt(d.iqr)}") for d, y in zip(data, PLOT_Y)
            ])
        if show == "range":
            return VGroup(*[
                self.span_note(plane, d.min, d.max, y, f"Range = {fmt(d.range)}") for d, y in zip(data, PLOT_Y)
            ])
        return VGroup()

    def run_interpretation(self, spec):
        self.camera.background_color = BACKGROUND_COLOR
        data = self.data_sets(spec)
        plane, all_parts = self.graph_top(spec, data)
        heading = self.use_heading(spec.get("compare_heading", "Step 5: Compare the data sets."))
        self.next_slide()

        for number, q in enumerate(spec["questions"]):
            prompt = Text(q["prompt"], font_size=30, line_spacing=0.9)
            prompt.move_to([BLOCK_LEFT, -0.55, 0], aligned_edge=UL + LEFT)
            self.play(FadeIn(prompt))
            self.next_slide()

            callout = self.graph_callout(plane, data, all_parts, q.get("show"))
            shown = VGroup(prompt, callout)
            below = prompt
            if q.get("answer"):
                answer = Text(q["answer"], font_size=30, weight=BOLD, color=ANSWER_COLOR)
                if "\n" in q["prompt"]:
                    answer.next_to(prompt, DOWN, buff=0.3).align_to(prompt, LEFT).shift(RIGHT * 0.12)
                else:
                    answer.next_to(prompt, RIGHT, buff=0.45, aligned_edge=DOWN)
                box = SurroundingRectangle(answer, color=ANSWER_COLOR, buff=0.12)
                self.play(FadeIn(answer), Create(box), FadeIn(callout))
                shown.add(answer, box)
                if "\n" in q["prompt"]:
                    below = box
            else:
                self.play(FadeIn(callout))
            self.next_slide()

            if q.get("follow"):
                follow = Text(q["follow"], font_size=30)
                follow.next_to(prompt, DOWN, buff=0.4).align_to(prompt, LEFT)
                self.play(FadeIn(follow))
                self.next_slide()
                shown.add(follow)
                below = follow

            explain = Text(q["explain"], font_size=30, line_spacing=0.9, color=ANSWER_COLOR)
            explain.next_to(below, DOWN, buff=0.3).align_to(prompt, LEFT)
            self.play(FadeIn(explain, shift=UP * 0.15))
            self.next_slide()
            shown.add(explain)
            if number < len(spec["questions"]) - 1:
                self.play(FadeOut(shown))

    # ---- reading given box plots ------------------------------------------

    def run_read_table(self, spec):
        """Given plots with no value labels: read each value down to the number
        line and into the table, then work out IQR and range."""
        self.camera.background_color = BACKGROUND_COLOR
        data = self.data_sets(spec)
        heading = self.use_heading(spec["heading"])
        plane, all_parts = self.graph_top(spec, data, show_values=False)
        context = Text(spec["context"], font_size=BODY_FONT_SIZE, line_spacing=0.9)
        context.move_to([0, -1.6, 0])
        self.play(FadeIn(context))
        self.next_slide()

        table = self.summary_grid(data, TABLE_TOP_Y_UNDER_GRAPH, filled=False)
        new_heading = Text("Fill in the table using the box plots.", font_size=HEADING_FONT_SIZE, weight=BOLD)
        new_heading.move_to(heading)
        self.play(FadeOut(context), FadeIn(table.group), Transform(heading, new_heading))
        self.next_slide()

        colors = [WHITE, Q1_COLOR, MEDIAN_COLOR, Q3_COLOR, WHITE]
        for r, (d, y, parts) in enumerate(zip(data, PLOT_Y, all_parts)):
            for k, (x, color) in enumerate(zip(d.table_row[:5], colors)):
                drop = DashedLine(plane.c2p(x, y - BOX_HALF_H), plane.c2p(x, 0), color=color, stroke_width=4)
                self.play(Create(drop), FadeIn(parts["values"][k]), run_time=0.6)
                self.place_value(table, r, k + 1, fmt(x), source=parts["values"][k], color=color)
                self.next_slide()
                self.play(FadeOut(drop), run_time=0.2)
            self.fill_iqr_and_range(table, r, d, TABLE_WORK_Y_UNDER_GRAPH)

        self.play(FadeOut(table.group), FadeOut(heading))

    # ---- percents ---------------------------------------------------------

    def graph_mark(self, plane, callout):
        """("span", row, x0, x1, label): arrow under a plot.
        ("mark", row, x, label or None): yellow line at x on a plot."""
        if callout[0] == "span":
            _, row, x0, x1, label = callout
            return self.span_note(plane, x0, x1, PLOT_Y[row], label)
        _, row, x, label = callout
        y = PLOT_Y[row]
        mark = VGroup(Line(plane.c2p(x, y - BOX_HALF_H - 0.1), plane.c2p(x, y + BOX_HALF_H + 0.1),
                           color=ANSWER_COLOR, stroke_width=6))
        if label:
            mark.add(Text(label, font_size=22, color=ANSWER_COLOR).next_to(mark[0], UP, buff=0.04))
        return mark

    def question_rows(self, rows):
        """rows: one list per line, each entry a string or a blank
        {"tex", "callouts"}. Returns (group, [(box, blank), ...] in order)."""
        lines, blanks = VGroup(), []
        for row in rows:
            line = VGroup()
            for entry in row:
                if isinstance(entry, str):
                    line.add(Text(entry, font_size=30))
                else:
                    width = MathTex(entry["tex"], font_size=BOX_FONT_SIZE).width + 0.35
                    box = self.answer_box(max(width, 1.15))
                    line.add(box)
                    blanks.append((box, entry))
            lines.add(line.arrange(RIGHT, buff=0.18))
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        lines.move_to([BLOCK_LEFT, QUESTION_TOP_Y, 0], aligned_edge=UL)
        return lines, blanks

    def run_percents(self, spec):
        """Plots stay up top. Each question appears with empty answer boxes;
        one click per box fills it and marks the matching part of the plot."""
        self.camera.background_color = BACKGROUND_COLOR
        data = self.data_sets(spec)
        plane, _ = self.graph_top(spec, data)
        self.use_heading(spec["percents_heading"])
        reminder = Text(spec["percents_reminder"], font_size=30, line_spacing=0.9)
        reminder.move_to([0, -1.6, 0])
        self.play(FadeIn(reminder))
        self.next_slide()
        self.play(FadeOut(reminder))

        for number, q in enumerate(spec["percents"]):
            lines, blanks = self.question_rows(q["rows"])
            self.play(FadeIn(lines))
            self.next_slide()

            shown = VGroup(lines)
            for box, entry in blanks:
                fill, value = self.fill(box, entry["tex"], ANSWER_COLOR)
                marks = VGroup(*[self.graph_mark(plane, c) for c in entry.get("callouts", [])])
                self.play(*fill, FadeIn(marks))
                self.next_slide()
                shown.add(value, marks)

            if q.get("explain"):
                explain = Text(q["explain"], font_size=30, line_spacing=0.9, color=ANSWER_COLOR)
                explain.next_to(lines, DOWN, buff=0.28).align_to(lines, LEFT)
                self.play(FadeIn(explain, shift=UP * 0.15))
                self.next_slide()
                shown.add(explain)
            if number < len(spec["percents"]) - 1:
                self.play(FadeOut(shown))
