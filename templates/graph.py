# templates/graph.py

import numpy as np
from manim import *

from components.theme import (
    BACKGROUND_COLOR, ANSWER_COLOR, PARENT_GRAPH_COLOR, TRANSFORM_COLORS, GRID_COLOR, AXIS_COLOR,
)


class GraphTemplate:
    """Mixin for graphing a parent function and morphing transformed copies
    out of it with TransformFromCopy (so the parent stays on screen).

    The graph sits on the left; the parent's label and each example's
    label + notebook description stack down the right side.

    Usage:
        class MyShift(Slide, GraphTemplate):
            def construct(self):
                self.camera.background_color = BACKGROUND_COLOR
                self.show_graph_header("Translations", "Horizontal")
                plane = self.show_plane((-6, 5), (-1, 7))
                parent = self.show_parent(plane, lambda x: x**2, [(0, 0)])
                self.transform_example(plane, parent, lambda x: (x + 3)**2, [(-3, 0)],
                                       r"f(x+3)", r"shifts \\textbf{left 3} units",
                                       r"vertex $(0,0)\\to(-3,0)$", color_index=0)
    """

    def show_graph_header(self, title, subtitle=None, title_font_size=38, subtitle_font_size=32):
        heading = Tex(title, font_size=title_font_size).to_edge(UP, buff=0.25)
        group = VGroup(heading)
        self.play(Write(heading))
        if subtitle:
            sub = Tex(subtitle, font_size=subtitle_font_size, color=ANSWER_COLOR)
            sub.next_to(heading, DOWN, buff=0.15)
            group.add(sub)
            self.play(FadeIn(sub))
        return group

    def show_plane(self, x_range, y_range, x_length=6.4, y_length=5.6, label_font_size=20):
        plane = NumberPlane(
            x_range=[*x_range, 1], y_range=[*y_range, 1],
            x_length=x_length, y_length=y_length,
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1, "stroke_opacity": 0.5},
            axis_config={"color": AXIS_COLOR, "include_numbers": True, "font_size": label_font_size},
        ).to_edge(LEFT, buff=0.4).to_edge(DOWN, buff=0.3)
        labels = plane.get_axis_labels(MathTex("x", font_size=28), MathTex("y", font_size=28))
        self.play(Create(plane), FadeIn(labels))
        return plane

    def show_data_plane(self, x_range, y_range, x_numbers, y_numbers, x_label, y_label,
                        x_length=7.4, y_length=5.4, center=ORIGIN, y_suffix="", y_number_colors=None,
                        label_font_size=24):
        """NumberPlane for real-world data: x_range / y_range are [min, max,
        grid step], x_numbers / y_numbers are the values to label (y_suffix,
        e.g. "\\%", is appended to each y label; y_number_colors optionally
        maps a y value to its label color). Axis titles sit outside the tick
        labels -- the y title rotated along the axis."""
        plane = NumberPlane(
            x_range=x_range, y_range=y_range, x_length=x_length, y_length=y_length,
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1, "stroke_opacity": 0.5},
            axis_config={"color": AXIS_COLOR, "include_numbers": False, "include_tip": False},
        ).move_to(center)
        y_number_colors = y_number_colors or {}
        x_nums = VGroup(*[
            MathTex(f"{x:g}", font_size=label_font_size).next_to(plane.c2p(x, y_range[0]), DOWN, buff=0.15)
            for x in x_numbers
        ])
        y_nums = VGroup(*[
            MathTex(f"{y:g}{y_suffix}", font_size=label_font_size, color=y_number_colors.get(y, WHITE))
            .next_to(plane.c2p(x_range[0], y), LEFT, buff=0.15)
            for y in y_numbers
        ])
        x_title = Text(x_label, font_size=label_font_size).next_to(x_nums, DOWN, buff=0.15)
        y_title = Text(y_label, font_size=label_font_size).rotate(PI / 2).next_to(y_nums, LEFT, buff=0.2)
        self.play(Create(plane), FadeIn(x_nums), FadeIn(y_nums), FadeIn(x_title), FadeIn(y_title))
        return plane, VGroup(x_nums, y_nums, x_title, y_title)

    def plot_clipped(self, plane, f, color, stroke_width=5):
        """Plot f only where it stays inside the visible y-range."""
        x0, x1 = plane.x_range[:2]
        y0, y1 = plane.y_range[:2]
        ok = [x for x in np.linspace(x0, x1, 4001) if y0 <= f(x) <= y1]
        return plane.plot(f, x_range=[ok[0], ok[-1], 0.01], color=color, stroke_width=stroke_width)

    def key_points(self, plane, pts, color, radius=0.09):
        return VGroup(*[Dot(plane.c2p(x, y), color=color, radius=radius) for x, y in pts])

    def show_parent(self, plane, f, pts, label=r"f(x)", note=r"(parent)", font_size=40,
                    anchor=RIGHT * 0.9 + UP * 1.9):
        """Draws the blue parent curve + key points and its label. Returns a
        dict the examples morph from and stack under."""
        text = VGroup(
            MathTex(label, font_size=font_size, color=PARENT_GRAPH_COLOR),
            Tex(note, font_size=font_size - 6, color=PARENT_GRAPH_COLOR),
        ).arrange(RIGHT, buff=0.3)
        text.move_to(anchor, aligned_edge=LEFT)
        curve = self.plot_clipped(plane, f, PARENT_GRAPH_COLOR)
        dots = self.key_points(plane, pts, PARENT_GRAPH_COLOR)

        self.play(Write(text))
        self.play(Create(curve), FadeIn(dots))
        self.next_slide()
        return {"curve": curve, "dots": dots, "anchor": text}

    def transform_example(self, plane, parent, f, pts, label, description, points_note=None,
                          color_index=0, font_size=40, desc_font_size=34, note_font_size=28, run_time=2):
        """Writes the example's label, morphs a copy of the parent into the
        transformed curve, then immediately writes the description (and the
        optional key-point note) beside the label for students to copy."""
        color = TRANSFORM_COLORS[color_index]
        lbl = MathTex(label, font_size=font_size, color=color)
        desc = Tex(description, font_size=desc_font_size, color=color)
        block = VGroup(VGroup(lbl, desc).arrange(RIGHT, buff=0.35))
        if points_note:
            block.add(Tex(points_note, font_size=note_font_size, color=color))
        block.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        block.next_to(parent["anchor"], DOWN, buff=0.55, aligned_edge=LEFT)

        curve = self.plot_clipped(plane, f, color)
        dots = self.key_points(plane, pts, color)

        self.play(Write(lbl))
        self.play(TransformFromCopy(parent["curve"], curve), TransformFromCopy(parent["dots"], dots),
                  run_time=run_time)
        self.play(Write(desc), *[Write(m) for m in block[1:]])
        self.next_slide()
        parent["anchor"] = block
        return curve, dots, block
