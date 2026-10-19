# components/theme.py

from manim import *

X_COLOR = GREEN
Y_COLOR = RED
Z_COLOR = "#FF00FF"  # MAGENTA -- not a built-in manim color constant

ANSWER_COLOR = YELLOW
THEOREM_COLOR = BLUE
INDICATE_COLOR = ORANGE

BACKGROUND_COLOR = ManimColor("#111111")

# Graphs: the parent function is always blue; transformed copies of it on
# the same slide use these, in order.
PARENT_GRAPH_COLOR = BLUE
TRANSFORM_COLORS = [RED, GREEN]
GRID_COLOR = GREY_D
AXIS_COLOR = GREY_B

# Transformation parameters in f(x+h)+k and a*f(bx), used wherever the
# letter shows up so students can match each letter to its effect.
PARAM_COLORS = {"h": ORANGE, "k": BLUE, "a": YELLOW, "b": PURPLE, "x": X_COLOR, "y": Y_COLOR}


# then every slide will run from components.theme import *