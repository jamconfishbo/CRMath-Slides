from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.distribution import DistributionTemplate
from templates.frequency_table import FrequencyTableTemplate

VAR_COLOR = X_COLOR
SQUARE_COLOR = RED


class Part1Problem2(Slide, DistributionTemplate, FrequencyTableTemplate):
    """Part 1, Problem 2 (YOU DO): 4x^2 + 10x - 2 = -6x + 5 -> x = -2 +/- sqrt(5.75)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def _original(self):
        original = MathTex(r"{{4x^2}}{{+10x}}{{-2}}={{-6x}}+{{5}}")
        original.get_part_by_tex("4x^2", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("+10x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("-6x", substring=False).set_color(VAR_COLOR)
        return original

    def show_practice(self):
        self.show_label("Part 1, Problem 2 (YOU DO)")
        original = self._original()
        original.scale(1.3).move_to(UP * 1.5)
        self.play(Write(original))
        self.next_slide()

        self.show_timer(300, position=np.array([0, -1.5, 0]))

    def show_solution(self):
        self.show_label("Part 1, Problem 2 (Solution)")

        original = self._original()
        self.start_stack(original)

        t_4x2 = original.get_part_by_tex("4x^2", substring=False)
        t_10x = original.get_part_by_tex("+10x", substring=False)
        t_neg2 = original.get_part_by_tex("-2", substring=False)
        t_neg6x = original.get_part_by_tex("-6x", substring=False)
        t_5 = original.get_part_by_tex("5", substring=False)

        # --- move the x-term: add +6x to both sides ---
        inv1_lhs, inv1_rhs = self.write_inverse([t_10x, t_neg6x], r"+6x", color=VAR_COLOR)
        strike1 = self.strike_pair(t_neg6x, inv1_rhs)
        self.extend_current_line(inv1_lhs, inv1_rhs, strike1)

        # --- move the constant: add +2 to both sides ---
        inv2_lhs, inv2_rhs = self.write_inverse([t_neg2, t_5], r"+2", color=WHITE)
        strike2 = self.strike_pair(t_neg2, inv2_lhs)
        self.extend_current_line(inv2_lhs, inv2_rhs, strike2)

        m1 = self.reveal_term(r"4x^2", after=None, source=t_4x2, indicate=False, color=VAR_COLOR)
        m2 = self.reveal_term(r"+16x", after=m1, source=[t_10x, inv1_lhs], color=VAR_COLOR)
        m_eq = self.reveal_term(r"=", after=m2, indicate=False)
        m3 = self.reveal_term(r"7", after=m_eq, source=[t_5, inv2_rhs])
        self.finish_line([m1, m2, m_eq, m3])

        # --- divide both sides by a = 4 ---
        d1 = self.reveal_term(r"x^2", after=None, source=m1, indicate=False, color=VAR_COLOR)
        d2 = self.reveal_term(r"+4x", after=d1, source=m2, color=VAR_COLOR)
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"1.75", after=d_eq, source=m3)
        self.finish_line([d1, d2, d_eq, d3])

        # --- complete the square: add (b/2)^2 = 4 to both sides ---
        sq_lhs, sq_rhs = self.write_inverse([d2, d3], r"+4", color=SQUARE_COLOR)
        self.extend_current_line(sq_lhs, sq_rhs)

        f1 = self.reveal_term(r"(x+2)^2", after=None, source=[d1, d2, sq_lhs], color=SQUARE_COLOR)
        f_eq = self.reveal_term(r"=", after=f1, indicate=False)
        f2 = self.reveal_term(r"5.75", after=f_eq, source=[d3, sq_rhs])
        self.finish_line([f1, f_eq, f2])

        # --- square root both sides ---
        sqrt_line = self.reveal_term(r"x = -2 \pm \sqrt{5.75}", after=None, source=None, indicate=False)
        self.finish_line([sqrt_line])

        # --- decimal answer ---
        final_line = self.reveal_term(
            r"x \approx 0.398 \text{ or } x \approx -4.398",
            after=None, source=None, indicate=False, color=ANSWER_COLOR,
        )
        self.finish_line([final_line])
        self.box_final(final_line)
