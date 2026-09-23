from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = X_COLOR
SQUARE_COLOR = RED


class Part3Problem5(Slide, DistributionTemplate):
    """Part 3, Problem 5 (I DO): 2x^2 + 9x - 1 = 4x + 2 -> x = 0.5 or x = -3 (exact)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Part 3, Problem 5 (I DO)")

        original = MathTex(r"{{2x^2}}{{+9x}}{{-1}}={{4x}}+{{2}}")
        original.get_part_by_tex("2x^2", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("+9x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("4x", substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t_2x2 = original.get_part_by_tex("2x^2", substring=False)
        t_9x = original.get_part_by_tex("+9x", substring=False)
        t_neg1 = original.get_part_by_tex("-1", substring=False)
        t_4x = original.get_part_by_tex("4x", substring=False)
        t_2 = original.get_part_by_tex("2", substring=False)

        # --- move the x-term: add -4x to both sides ---
        inv1_lhs, inv1_rhs = self.write_inverse([t_9x, t_4x], r"-4x", color=VAR_COLOR)
        strike1 = self.strike_pair(t_4x, inv1_rhs)
        self.extend_current_line(inv1_lhs, inv1_rhs, strike1)

        # --- move the constant: add +1 to both sides ---
        inv2_lhs, inv2_rhs = self.write_inverse([t_neg1, t_2], r"+1", color=WHITE)
        strike2 = self.strike_pair(t_neg1, inv2_lhs)
        self.extend_current_line(inv2_lhs, inv2_rhs, strike2)

        m1 = self.reveal_term(r"2x^2", after=None, source=t_2x2, indicate=False, color=VAR_COLOR)
        m2 = self.reveal_term(r"+5x", after=m1, source=[t_9x, inv1_lhs], color=VAR_COLOR)
        m_eq = self.reveal_term(r"=", after=m2, indicate=False)
        m3 = self.reveal_term(r"3", after=m_eq, source=[t_2, inv2_rhs])
        self.finish_line([m1, m2, m_eq, m3])

        # --- divide both sides by a = 2 ---
        d1 = self.reveal_term(r"x^2", after=None, source=m1, indicate=False, color=VAR_COLOR)
        d2 = self.reveal_term(r"+2.5x", after=d1, source=m2, color=VAR_COLOR)
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"1.5", after=d_eq, source=m3)
        self.finish_line([d1, d2, d_eq, d3])

        # --- complete the square: add (b/2)^2 = 1.5625 to both sides ---
        sq_lhs, sq_rhs = self.write_inverse([d2, d3], r"+1.5625", color=SQUARE_COLOR)
        self.extend_current_line(sq_lhs, sq_rhs)

        f1 = self.reveal_term(r"(x+1.25)^2", after=None, source=[d1, d2, sq_lhs], color=SQUARE_COLOR)
        f_eq = self.reveal_term(r"=", after=f1, indicate=False)
        f2 = self.reveal_term(r"3.0625", after=f_eq, source=[d3, sq_rhs])
        self.finish_line([f1, f_eq, f2])

        # --- square root both sides ---
        sqrt_line = self.reveal_term(r"x = -1.25 \pm \sqrt{3.0625}", after=None, source=None, indicate=False)
        self.finish_line([sqrt_line])

        # --- this sqrt happens to be exact ---
        eval_line = self.reveal_term(r"x = -1.25 \pm 1.75", after=None, source=None, indicate=False)
        self.finish_line([eval_line])

        # --- final answer ---
        final_line = self.reveal_term(
            r"x = 0.5 \text{ or } x = -3",
            after=None, source=None, indicate=False, color=ANSWER_COLOR,
        )
        self.finish_line([final_line])
        self.box_final(final_line)
