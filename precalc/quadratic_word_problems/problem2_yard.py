from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = X_COLOR
SQUARE_COLOR = RED

PICTURE_CENTER = RIGHT * 3.6


class Problem2Yard(Slide, DistributionTemplate):
    """Problem 2 (dog park yard): park = grass + concrete -> L^2 - 6L = 800 -> L ~= 31.4 ft."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Problem 2 — Dog Park Yard")

        self.show_picture()

        # --- set up the equation in words, from the picture ---
        word_eq = MathTex(r"{{\text{park} }}{{=}}{{\text{grass} }}+{{\text{concrete} }}")
        self.start_stack(word_eq, bottom_margin=1.7)
        t_park, t_eq0, t_grass, t_plus0, t_concrete = word_eq

        # --- substitute the known expressions for each area ---
        b1 = self.reveal_term(r"L^2", after=None, source=t_park, color=VAR_COLOR)
        b_eq = self.reveal_term(r"=", after=b1, indicate=False)
        b2 = self.reveal_term(r"800", after=b_eq, source=t_grass)
        b3 = self.reveal_term(r"+6L", after=b2, source=t_concrete, color=VAR_COLOR)
        self.finish_line([b1, b_eq, b2, b3])

        # --- subtract 6L from both sides to reach var^2 +/- var = # form ---
        inv_lhs, inv_rhs = self.write_inverse(
            [b1, b3], r"-6L", color=VAR_COLOR, shifts=[LEFT * 0.3, RIGHT * 0.3]
        )
        strike = self.strike_pair(b3, inv_rhs)
        self.extend_current_line(inv_lhs, inv_rhs, strike)

        c1 = self.reveal_term(r"L^2", after=None, source=b1, indicate=False, color=VAR_COLOR)
        c2 = self.reveal_term(r"-6L", after=c1, source=inv_lhs, color=VAR_COLOR)
        c_eq = self.reveal_term(r"=", after=c2, indicate=False)
        c3 = self.reveal_term(r"800", after=c_eq, source=b2)
        self.finish_line([c1, c2, c_eq, c3])

        # --- complete the square: add (b/2)^2 = 9 to both sides, in red ---
        sq_lhs, sq_rhs = self.write_inverse(
            [c2, c3], r"+9", color=SQUARE_COLOR, shifts=[LEFT * 0.3, RIGHT * 0.3]
        )
        self.extend_current_line(sq_lhs, sq_rhs)

        f1 = self.reveal_term(r"(L-3)^2", after=None, source=[c1, c2, sq_lhs], color=SQUARE_COLOR)
        f_eq = self.reveal_term(r"=", after=f1, indicate=False)
        f2 = self.reveal_term(r"809", after=f_eq, source=[c3, sq_rhs])
        self.finish_line([f1, f_eq, f2])

        # --- square root both sides, in red, with +/- ---
        sq1 = self.reveal_term(r"\sqrt{(L-3)^2}", after=None, source=f1, color=SQUARE_COLOR)
        sq_eq = self.reveal_term(r"=", after=sq1, indicate=False)
        sq2 = self.reveal_term(r"\pm\sqrt{809}", after=sq_eq, source=f2, color=SQUARE_COLOR)
        self.finish_line([sq1, sq_eq, sq2])

        ev1 = self.reveal_term(r"L-3", after=None, source=sq1, indicate=False)
        ev_eq = self.reveal_term(r"=", after=ev1, indicate=False)
        ev2 = self.reveal_term(r"\pm 28.443", after=ev_eq, source=sq2)
        self.finish_line([ev1, ev_eq, ev2])

        # --- isolate L ---
        iso_line = self.reveal_term(r"L = 3 \pm 28.443", after=None, source=None, indicate=False)
        self.finish_line([iso_line])

        # --- final answer ---
        final_line = self.reveal_term(
            r"L \approx 31.4 \text{ ft}",
            after=None, source=None, indicate=False, color=ANSWER_COLOR,
        )
        self.finish_line([final_line])
        self.box_final(final_line)

        explanation = Text(
            "Reject L ≈ -25.4 — a side length can't be negative.\n"
            "The yard is a square, so each of its 4 edges is about 31.4 ft.",
            font_size=24, color=GRAY_A, line_spacing=1.2,
        )
        explanation.scale_to_fit_width(6.0)
        explanation.next_to(self._stack, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(explanation))
        self.next_slide()

    def show_picture(self):
        side = 3.0
        strip_h = 0.6

        square = Square(side_length=side, color=WHITE, stroke_width=3)
        strip = Rectangle(width=side, height=strip_h, fill_color=GRAY, fill_opacity=0.5, stroke_width=0)
        strip.move_to(square.get_bottom() + UP * strip_h / 2)
        grass = Rectangle(
            width=side, height=side - strip_h, fill_color=GREEN, fill_opacity=0.25, stroke_width=0
        )
        grass.move_to(square.get_top() + DOWN * (side - strip_h) / 2)
        divider = Line(
            square.get_corner(DL) + UP * strip_h,
            square.get_corner(DR) + UP * strip_h,
            color=WHITE,
        )

        # rotate the whole park 90 degrees, so the strip runs along a side instead of the bottom
        diagram = VGroup(grass, strip, square, divider)
        diagram.rotate(PI / 2)

        brace = Brace(square, DOWN)
        brace_label = brace.get_tex("L")
        brace_label.set_color(VAR_COLOR)

        strip_label = Text("6 ft", font_size=22, color=WHITE)
        strip_label.move_to(strip.get_center())

        grass_label = Text("grass =\n800 ft²", font_size=22, color=GREEN, line_spacing=1.1)
        grass_label.move_to(grass.get_center())

        picture = VGroup(diagram, brace, brace_label, strip_label, grass_label)
        picture.scale(0.85).move_to(PICTURE_CENTER)

        self.play(Create(diagram), FadeIn(brace), Write(brace_label))
        self.play(FadeIn(strip_label), FadeIn(grass_label))
        self.next_slide()
