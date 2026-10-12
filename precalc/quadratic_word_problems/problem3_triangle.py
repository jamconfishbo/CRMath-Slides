from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = X_COLOR
SQUARE_COLOR = RED

PICTURE_CENTER = RIGHT * 3.6


class Problem3Triangle(Slide, DistributionTemplate):
    """Problem 3 (stained-glass triangle): x^2 + (3x)^2 = 10^2 -> x ~= 3.162 in."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Problem 3 — Stained-Glass Triangle")

        self.show_picture()

        # --- set up the equation from the picture: Pythagorean theorem ---
        original = MathTex(r"{{x^2}}+{{(3x)^2}}{{=}}{{10^2}}")
        original[0].set_color(VAR_COLOR)
        original[2].set_color(VAR_COLOR)

        self.start_stack(original, bottom_margin=1.7)

        t_x2, t_plus, t_3x2, t_eq0, t_10sq = original

        # --- square the 3 (and the 10) ---
        sq_a1 = self.reveal_term(r"x^2", after=None, source=t_x2, indicate=False, color=VAR_COLOR)
        sq_a2 = self.reveal_term(r"+9x^2", after=sq_a1, source=t_3x2, color=VAR_COLOR)
        sq_a_eq = self.reveal_term(r"=", after=sq_a2, indicate=False)
        sq_a3 = self.reveal_term(r"100", after=sq_a_eq, source=t_10sq)
        self.finish_line([sq_a1, sq_a2, sq_a_eq, sq_a3])

        # --- combine like terms on the left ---
        s1 = self.reveal_term(r"10x^2", after=None, source=[sq_a1, sq_a2], color=VAR_COLOR)
        s_eq = self.reveal_term(r"=", after=s1, indicate=False)
        s2 = self.reveal_term(r"100", after=s_eq, source=sq_a3)
        self.finish_line([s1, s_eq, s2])

        # --- divide both sides by 10 to reach var^2 = # form ---
        d1 = self.reveal_term(r"x^2", after=None, source=s1, indicate=False, color=VAR_COLOR)
        d_eq = self.reveal_term(r"=", after=d1, indicate=False)
        d2 = self.reveal_term(r"10", after=d_eq, source=s2)
        self.finish_line([d1, d_eq, d2])

        note = Text(
            "No linear (x) term, so b = 0 — this is already a perfect square.",
            font_size=24, color=GRAY_A,
        )
        note.next_to(self._current_line, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(note))
        self.next_slide()
        self.extend_current_line(note)

        # --- square root both sides, in red, with +/- ---
        sq1 = self.reveal_term(r"\sqrt{x^2}", after=None, source=d1, color=SQUARE_COLOR)
        sq_eq = self.reveal_term(r"=", after=sq1, indicate=False)
        sq2 = self.reveal_term(r"\pm\sqrt{10}", after=sq_eq, source=d2, color=SQUARE_COLOR)
        self.finish_line([sq1, sq_eq, sq2])

        ev_line = self.reveal_term(r"x = \pm 3.162", after=None, source=sq2, indicate=False)
        self.finish_line([ev_line])

        # --- final answer ---
        final_line = self.reveal_term(
            r"x \approx 3.162 \text{ in}",
            after=None, source=None, indicate=False, color=ANSWER_COLOR,
        )
        self.finish_line([final_line])
        self.box_final(final_line)

        explanation = Text(
            "Reject x ≈ -3.162 — a leg length can't be negative.\n"
            "The shorter leg is about 3.2 inches.",
            font_size=24, color=GRAY_A, line_spacing=1.2,
        )
        explanation.scale_to_fit_width(6.0)
        explanation.next_to(self._stack, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(explanation))
        self.next_slide()

    def show_picture(self):
        a = LEFT * 2.2 + DOWN * 1.2
        b = RIGHT * 2.2 + DOWN * 1.2
        c = LEFT * 2.2 + UP * 1.2

        triangle = Polygon(a, b, c, color=WHITE, stroke_width=3)
        right_angle = Square(side_length=0.22, color=WHITE, stroke_width=2, fill_opacity=0)
        right_angle.move_to(a + RIGHT * 0.11 + UP * 0.11)

        short_leg_label = MathTex("x", color=VAR_COLOR)
        short_leg_label.next_to(Line(a, c), LEFT, buff=0.25)

        long_leg_label = MathTex("3x", color=VAR_COLOR)
        long_leg_label.next_to(Line(a, b), DOWN, buff=0.25)

        hyp_label = MathTex(r"10\text{ in}")
        hyp_label.move_to(Line(b, c).point_from_proportion(0.5))
        hyp_label.shift(UR * 0.4)

        picture = VGroup(triangle, right_angle, short_leg_label, long_leg_label, hyp_label)
        picture.scale(0.85).move_to(PICTURE_CENTER)

        self.play(Create(triangle), FadeIn(right_angle))
        self.play(Write(short_leg_label), Write(long_leg_label), Write(hyp_label))
        self.next_slide()
