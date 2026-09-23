from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = X_COLOR      # every x / x^2 term
SQUARE_COLOR = RED       # the (b/2)^2 completing-the-square terms


class Part1Problem1(Slide, DistributionTemplate):
    """Part 1, Problem 1 (I DO): 2x^2 - 5x + 3 = 3x + 8 -> x = 2 +/- sqrt(6.5)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Part 1, Problem 1 (I DO)")

        original = MathTex(r"{{2x^2}}{{-5x}}+{{3}}={{3x}}+{{8}}")
        original.get_part_by_tex("2x^2", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("-5x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("3x", substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t_2x2 = original.get_part_by_tex("2x^2", substring=False)
        t_neg5x = original.get_part_by_tex("-5x", substring=False)
        t_3 = original.get_part_by_tex("3", substring=False)
        t_3x = original.get_part_by_tex("3x", substring=False)
        t_8 = original.get_part_by_tex("8", substring=False)

        # --- move the x-term: add -3x to both sides ---
        inv1_lhs, inv1_rhs = self.write_inverse([t_neg5x, t_3x], r"-3x", color=VAR_COLOR)
        strike1 = self.strike_pair(t_3x, inv1_rhs)
        self.extend_current_line(inv1_lhs, inv1_rhs, strike1)

        # --- move the constant: add -3 to both sides ---
        inv2_lhs, inv2_rhs = self.write_inverse([t_3, t_8], r"-3", color=WHITE)
        strike2 = self.strike_pair(t_3, inv2_lhs)
        self.extend_current_line(inv2_lhs, inv2_rhs, strike2)

        m1 = self.reveal_term(r"2x^2", after=None, source=t_2x2, indicate=False, color=VAR_COLOR)
        m2 = self.reveal_term(r"-8x", after=m1, source=[t_neg5x, inv1_lhs], color=VAR_COLOR)
        m_eq = self.reveal_term(r"=", after=m2, indicate=False)
        m3 = self.reveal_term(r"5", after=m_eq, source=[t_8, inv2_rhs])
        self.finish_line([m1, m2, m_eq, m3])

        # --- divide both sides by a = 2 ---
        d1 = self.reveal_term(r"x^2", after=None, source=m1, indicate=False, color=VAR_COLOR)
        d2 = self.reveal_term(r"-4x", after=d1, source=m2, color=VAR_COLOR)
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"2.5", after=d_eq, source=m3)
        self.finish_line([d1, d2, d_eq, d3])

        # --- complete the square: add (b/2)^2 = 4 to both sides ---
        sq_lhs, sq_rhs = self.write_inverse([d2, d3], r"+4", color=SQUARE_COLOR)
        self.extend_current_line(sq_lhs, sq_rhs)

        f1 = self.reveal_term(r"(x-2)^2", after=None, source=[d1, d2, sq_lhs], color=SQUARE_COLOR)
        f_eq = self.reveal_term(r"=", after=f1, indicate=False)
        f2 = self.reveal_term(r"6.5", after=f_eq, source=[d3, sq_rhs])
        self.finish_line([f1, f_eq, f2])

        # --- square root both sides ---
        sqrt_line = self.reveal_term(r"x = 2 \pm \sqrt{6.5}", after=None, source=None, indicate=False)
        self.finish_line([sqrt_line])

        # --- decimal answer ---
        final_line = self.reveal_term(
            r"x \approx 4.550 \text{ or } x \approx -0.550",
            after=None, source=None, indicate=False, color=ANSWER_COLOR,
        )
        self.finish_line([final_line])
        self.box_final(final_line)
