# templates/summary.py

import re

from manim import *

from components.theme import ANSWER_COLOR, AXIS_COLOR, PARAM_COLORS

COLOR_TEX_TEMPLATE = TexTemplate()
COLOR_TEX_TEMPLATE.add_to_preamble(r"\usepackage{xcolor}")


class SummaryTemplate:
    """Mixin for wrap-up / key-idea slides: a boxed definition, and a
    two-column summary table revealed one row per click.

    In show_key_lines / summary_table strings, wrap a letter as <<a>> to
    draw it in its PARAM_COLORS color (works inside or outside $...$).

    Usage:
        class MySummary(Slide, SummaryTemplate):
            def construct(self):
                self.camera.background_color = BACKGROUND_COLOR
                head = self.show_key_lines([r"Given $f(x)$:"])
                self.summary_table(["Left", "Right"], [[r"a", r"b"], [r"c", r"d"]], below=head)
    """

    def show_definition(self, title, tex_lines, title_font_size=56, font_size=42, box_color=ANSWER_COLOR):
        """Title, then the definition (Tex lines, one per row) boxed below it."""
        heading = Text(title, font_size=title_font_size, weight=BOLD, color=box_color)
        body = Tex(*[l + r"\\" for l in tex_lines[:-1]], tex_lines[-1], font_size=font_size)
        box = SurroundingRectangle(body, color=box_color, buff=0.35)
        VGroup(heading, VGroup(body, box)).arrange(DOWN, buff=0.8)

        self.play(Write(heading))
        self.next_slide()
        self.play(FadeIn(body, shift=UP * 0.3))
        self.play(Create(box))
        self.next_slide()
        return heading, body, box

    def colored_tex(self, s, font_size, color=None):
        """Tex with every <<letter>> marker drawn in PARAM_COLORS[letter]."""
        def swap(m):
            hex_code = ManimColor(PARAM_COLORS[m.group(1)]).to_hex()[1:]
            return rf"\textcolor[HTML]{{{hex_code}}}{{{m.group(1)}}}"
        kwargs = {"color": color} if color is not None else {}
        return Tex(re.sub(r"<<(\w)>>", swap, s), font_size=font_size,
                   tex_template=COLOR_TEX_TEMPLATE, **kwargs)

    def show_key_lines(self, tex_lines, font_size=38, buff=0.3, row_buff=1.2):
        """tex_lines: a list whose items are a Tex string (own row) or a list
        of Tex strings (shown side by side on one row). Each row fades in."""
        rows = VGroup()
        for item in tex_lines:
            parts = item if isinstance(item, list) else [item]
            rows.add(VGroup(*[self.colored_tex(p, font_size) for p in parts]).arrange(RIGHT, buff=row_buff))
        rows.arrange(DOWN, buff=buff).to_edge(UP, buff=0.3)
        for row in rows:
            for part in row:
                self.play(FadeIn(part, shift=UP * 0.2))
        self.next_slide()
        return rows

    def summary_table(self, headers, rows, below=None, font_size=30, header_color=None,
                      max_width=12.5, bottom_y=-3.9):
        """headers: column header Tex strings. rows: list of rows, each a list
        of Tex strings. Grid + headers draw first, then one row per click."""
        table = MobjectTable(
            [[self.colored_tex(s, font_size) for s in r] for r in rows],
            col_labels=[self.colored_tex(h, font_size, header_color) for h in headers],
            include_outer_lines=True, h_buff=0.6, v_buff=0.35,
            line_config={"stroke_width": 2, "color": AXIS_COLOR},
        )
        table.scale_to_fit_width(max_width)
        if below is not None:
            table.next_to(below, DOWN, buff=0.4)
        if table.get_bottom()[1] < bottom_y:
            table.scale(1 - (bottom_y - table.get_bottom()[1]) / table.height, about_edge=UP)

        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()),
                  Write(table.get_col_labels()))
        for row in table.get_rows()[1:]:
            self.next_slide()
            self.play(Write(row))
        self.next_slide()
        return table
