from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.summary import SummaryTemplate


class TransformationsSummary(Slide, SummaryTemplate):
    """f(x+h)+k and a*f(bx), then the outside (same) / inside (opposite) table.
    h, k, a, b (and x/y in the axis names) carry their PARAM_COLORS everywhere."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        head = self.show_key_lines([
            r"Given parent function $f(x)$:",
            [r"$f(x+<<h>>)+<<k>>$ is a transformation", r"$<<a>>\cdot f(<<b>>x)$ is a transformation"],
        ])
        self.summary_table(
            [r"\textbf{Outside} $f(x)$ \ (same)", r"\textbf{Inside} $f(x)$ \ (opposite)"],
            [
                [r"vertical translation \textbf{up} $<<k>>$",
                 r"horizontal translation \textbf{left} $<<h>>$"],
                [r"$|<<a>>|>1$: vertical \textbf{stretch} by $<<a>>$",
                 r"$|<<b>>|>1$: horizontal \textbf{shrink} by $\tfrac{1}{<<b>>}$"],
                [r"$|<<a>>|<1$: vertical \textbf{shrink} by $<<a>>$",
                 r"$|<<b>>|<1$: horizontal \textbf{stretch} by $\tfrac{1}{<<b>>}$"],
                [r"$<<a>><0$: \textbf{reflect} over $<<x>>$-axis",
                 r"$<<b>><0$: \textbf{reflect} over $<<y>>$-axis"],
            ],
            below=head,
        )
