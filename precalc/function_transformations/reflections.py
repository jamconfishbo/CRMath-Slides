from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.graph import GraphTemplate


def shifted_cube(x):
    # Plain x^3 looks identical reflected over either axis, so shift it.
    return (x - 1) ** 3 + 2


class Reflections(Slide, GraphTemplate):
    """Cubic: -f(x) over the x-axis, f(-x) over the y-axis."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_graph_header("Reflections", r"Parent: $f(x)=(x-1)^3+2$")
        plane = self.show_plane((-4, 4), (-5, 5))
        parent = self.show_parent(plane, shifted_cube, [(1, 2), (2, 3), (0, 1)])

        self.transform_example(plane, parent, lambda x: -shifted_cube(x), [(1, -2), (2, -3), (0, -1)],
                               r"-f(x)", r"reflects over the \textbf{$x$-axis}",
                               r"$(x,y)\to(x,-y)$: \ $(1,2)\to(1,-2)$", color_index=0)
        self.transform_example(plane, parent, lambda x: shifted_cube(-x), [(-1, 2), (-2, 3), (0, 1)],
                               r"f(-x)", r"reflects over the \textbf{$y$-axis}",
                               r"$(x,y)\to(-x,y)$: \ $(1,2)\to(-1,2)$", color_index=1)
