from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.graph import GraphTemplate

SHIFT_HEADER = r"Translations shift the \emph{entire} function up/down or left/right"


class HorizontalTranslations(Slide, GraphTemplate):
    """Parabola: f(x+3) left 3, f(x-2) right 2."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_graph_header(SHIFT_HEADER, "Horizontal Translations")
        plane = self.show_plane((-6, 5), (-1, 7))
        parent = self.show_parent(plane, lambda x: x ** 2, [(0, 0)])

        self.transform_example(plane, parent, lambda x: (x + 3) ** 2, [(-3, 0)],
                               r"f(x+3)", r"shifts \textbf{left 3} units",
                               r"vertex $(0,0)\to(-3,0)$", color_index=0)
        self.transform_example(plane, parent, lambda x: (x - 2) ** 2, [(2, 0)],
                               r"f(x-2)", r"shifts \textbf{right 2} units",
                               r"vertex $(0,0)\to(2,0)$", color_index=1)


class VerticalTranslations(Slide, GraphTemplate):
    """Parabola: f(x)+2 up 2, f(x)-4 down 4."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_graph_header(SHIFT_HEADER, "Vertical Translations")
        plane = self.show_plane((-4, 4), (-5, 7))
        parent = self.show_parent(plane, lambda x: x ** 2, [(0, 0)])

        self.transform_example(plane, parent, lambda x: x ** 2 + 2, [(0, 2)],
                               r"f(x)+2", r"shifts \textbf{up 2} units",
                               r"vertex $(0,0)\to(0,2)$", color_index=0)
        self.transform_example(plane, parent, lambda x: x ** 2 - 4, [(0, -4)],
                               r"f(x)-4", r"shifts \textbf{down 4} units",
                               r"vertex $(0,0)\to(0,-4)$", color_index=1)
