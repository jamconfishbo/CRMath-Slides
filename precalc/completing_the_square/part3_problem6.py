from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.distribution import DistributionTemplate
from templates.frequency_table import FrequencyTableTemplate

VAR_COLOR = X_COLOR
SQUARE_COLOR = RED


class Part3Problem6(Slide, DistributionTemplate, FrequencyTableTemplate):
    """Part 3, Problem 6 (YOU DO): 4x^2 - x + 4 = 5x + 9 -> x = 0.75 +/- sqrt(1.8125)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.show_practice()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.show_solution()

    def _original(self):
        original = MathTex(r"{{4x^2}}{{-x}}{{+4}}={{5x}}+{{9}}")
        original.get_part_by_tex("4x^2", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("-x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("5x", substring=False).set_color(VAR_COLOR)
        return original

    def show_practice(self):
        self.show_label("Part 3, Problem 6 (YOU DO)")
        original = self._original()
        original.scale(1.3).move_to(UP * 1.5)
        self.play(Write(original))
        self.next_slide()

        self.show_timer(300, position=np.array([0, -1.5, 0]))

    def show_solution(self):
        self.show_label("Part 3, Problem 6 (Solution)")

        original = self._original()
        self.start_stack(original)

        t_4x2 = original.get_part_by_tex("4x^2", substring=False)
        t_negx = original.get_part_by_tex("-x", substring=False)
        t_4 = original.get_part_by_tex("+4", substring=False)
        t_5x = original.get_part_by_tex("5x", substring=False)
        t_9 = original.get_part_by_tex("9", substring=False)

        # --- move the x-term: add -5x to both sides ---
        inv1_lhs, inv1_rhs = self.write_inverse([t_negx, t_5x], r"-5x", color=VAR_COLOR)
        strike1 = self.strike_pair(t_5x, inv1_rhs)
        self.extend_current_line(inv1_lhs, inv1_rhs, strike1)

        # --- move the constant: add -4 to both sides ---
        inv2_lhs, inv2_rhs = self.write_inverse([t_4, t_9], r"-4", color=WHITE)
        strike2 = self.strike_pair(t_4, inv2_lhs)
        self.extend_current_line(inv2_lhs, inv2_rhs, strike2)

        m1 = self.reveal_term(r"4x^2", after=None, source=t_4x2, indicate=False, color=VAR_COLOR)
        m2 = self.reveal_term(r"-6x", after=m1, source=[t_negx, inv1_lhs], color=VAR_COLOR)
        m_eq = self.reveal_term(r"=", after=m2, indicate=False)
        m3 = self.reveal_term(r"5", after=m_eq, source=[t_9, inv2_rhs])
        self.finish_line([m1, m2, m_eq, m3])

        # --- divide both sides by a = 4 ---
        d1 = self.reveal_term(r"x^2", after=None, source=m1, indicate=False, color=VAR_COLOR)
        d2 = self.reveal_term(r"-1.5x", after=d1, source=m2, color=VAR_COLOR)
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"1.25", after=d_eq, source=m3)
        self.finish_line([d1, d2, d_eq, d3])

        # --- complete the square: add (b/2)^2 = 0.5625 to both sides ---
        sq_lhs, sq_rhs = self.write_inverse(
            [d2, d3], r"+0.5625", color=SQUARE_COLOR, shifts=[LEFT * 0.5, RIGHT * 0.5]
        )
        self.extend_current_line(sq_lhs, sq_rhs)

        f1 = self.reveal_term(r"(x-0.75)^2", after=None, source=[d1, d2, sq_lhs], color=SQUARE_COLOR)
        f_eq = self.reveal_term(r"=", after=f1, indicate=False)
        f2 = self.reveal_term(r"1.8125", after=f_eq, source=[d3, sq_rhs])
        self.finish_line([f1, f_eq, f2])

        # --- square root both sides ---
        sq1 = self.reveal_term(r"\sqrt{(x-0.75)^2}", after=None, source=f1, color=SQUARE_COLOR)
        sq_eq = self.reveal_term(r"=", after=sq1, indicate=False)
        sq2 = self.reveal_term(r"\pm\sqrt{1.8125}", after=sq_eq, source=f2)
        self.finish_line([sq1, sq_eq, sq2])

        # --- evaluate the square root ---
        ev1 = self.reveal_term(r"x-0.75", after=None, source=sq1, indicate=False)
        ev_eq = self.reveal_term(r"=", after=ev1, indicate=False)
        ev2 = self.reveal_term(r"\pm 1.346", after=ev_eq, source=sq2)
        self.finish_line([ev1, ev_eq, ev2])

        # --- isolate x ---
        iso_line = self.reveal_term(r"x = 0.75 \pm 1.346", after=None, source=None, indicate=False)
        self.finish_line([iso_line])

        # --- decimal answer ---
        final_line = self.reveal_term(
            r"x \approx 2.096 \text{ or } x \approx -0.596",
            after=None, source=None, indicate=False, color=ANSWER_COLOR,
        )
        self.finish_line([final_line])
        self.box_final(final_line)
