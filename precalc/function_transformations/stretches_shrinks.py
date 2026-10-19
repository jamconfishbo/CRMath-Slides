from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.graph import GraphTemplate

# (-1, 1) isn't on y = x^3, so the third key point is (-1, -1).
CUBE_PTS = [(0, 0), (1, 1), (-1, -1)]


class VerticalStretchShrink(Slide, GraphTemplate):
    """Cubic: 2f(x) vertical stretch by 2, 1/4 f(x) vertical shrink by 1/4."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_graph_header(r"Vertical Stretches \& Shrinks", r"Multiply the \emph{outputs} ($y$-values)")
        plane = self.show_plane((-4, 4), (-4, 4))
        parent = self.show_parent(plane, lambda x: x ** 3, CUBE_PTS)

        self.transform_example(plane, parent, lambda x: 2 * x ** 3, [(0, 0), (1, 2), (-1, -2)],
                               r"2f(x)", r"\textbf{vertical stretch} by 2",
                               r"$(1,1)\to(1,2)$, \ $(-1,-1)\to(-1,-2)$", color_index=0)
        self.transform_example(plane, parent, lambda x: x ** 3 / 4, [(0, 0), (1, 0.25), (-1, -0.25)],
                               r"\tfrac14 f(x)", r"\textbf{vertical shrink} by $\tfrac14$",
                               r"$(1,1)\to(1,\tfrac14)$, \ $(-1,-1)\to(-1,-\tfrac14)$", color_index=1)


class HorizontalStretchShrink(Slide, GraphTemplate):
    """Cubic: f(2x) horizontal shrink by 1/2, f(x/2) horizontal stretch by 2."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_graph_header(r"Horizontal Stretches \& Shrinks",
                               r"Multiply the \emph{inputs} ($x$-values) -- works opposite!")
        plane = self.show_plane((-4, 4), (-4, 4))
        parent = self.show_parent(plane, lambda x: x ** 3, CUBE_PTS)

        self.transform_example(plane, parent, lambda x: (2 * x) ** 3, [(0, 0), (0.5, 1), (-0.5, -1)],
                               r"f(2x)", r"\textbf{horizontal shrink} by $\tfrac12$",
                               r"$(1,1)\to(\tfrac12,1)$, \ $(-1,-1)\to(-\tfrac12,-1)$", color_index=0)
        self.transform_example(plane, parent, lambda x: (x / 2) ** 3, [(0, 0), (2, 1), (-2, -1)],
                               r"f(\tfrac12 x)", r"\textbf{horizontal stretch} by 2",
                               r"$(1,1)\to(2,1)$, \ $(-1,-1)\to(-2,-1)$", color_index=1)
