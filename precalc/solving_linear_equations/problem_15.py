from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR
from templates.worked_example import WorkedExampleTemplate
from templates.distribution import DistributionTemplate

VAR_COLOR = GREEN
INVERSE_COLOR = RED


class Problem15LinearEquation(Slide, WorkedExampleTemplate, DistributionTemplate):
    """Problem 15: 2(5x-6) = 4[x-3(x-10)]  ->  one solution, x = 22/3."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.clear_brackets()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_equation()

    def clear_brackets(self):
        self.show_label("15)")

        l0 = MathTex(r"2({{5x}}-6)=4[{{x}}-{{3}}({{x}}-10)]")
        l0.get_part_by_tex("5x", substring=False).set_color(VAR_COLOR)
        for part in l0.get_parts_by_tex("x", substring=False):
            part.set_color(VAR_COLOR)

        l1 = MathTex(r"2({{5x}}-6)=4[{{x}}-{{3x}}+30]")
        l1.get_part_by_tex("5x", substring=False).set_color(VAR_COLOR)
        for part in l1.get_parts_by_tex("x", substring=False):
            part.set_color(VAR_COLOR)
        l1.get_part_by_tex("3x", substring=False).set_color(VAR_COLOR)

        l2 = MathTex(r"2({{5x}}-6)=4[{{-2x}}+30]")
        l2.get_part_by_tex("5x", substring=False).set_color(VAR_COLOR)
        l2.get_part_by_tex("-2x", substring=False).set_color(VAR_COLOR)

        l3 = MathTex(r"{{10x}}{{-12}}={{-8x}}+{{120}}")
        l3.get_part_by_tex("10x", substring=False).set_color(VAR_COLOR)
        l3.get_part_by_tex("-8x", substring=False).set_color(VAR_COLOR)

        lines = [l0, l1, l2, l3]
        targets = ["3", "3x", "4", None]

        self.step_through(lines, targets, box_final=False)

    def solve_equation(self):
        self.show_label("15) (continued)")

        original = MathTex(r"{{10x}}{{-12}}={{-8x}}+{{120}}")
        original.get_part_by_tex("10x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("-8x", substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t10x = original.get_part_by_tex("10x", substring=False)
        t_neg12 = original.get_part_by_tex("-12", substring=False)
        t_neg8x = original.get_part_by_tex("-8x", substring=False)
        t120 = original.get_part_by_tex("120", substring=False)

        # --- get variables on one side: add the additive inverse of -8x to both sides ---
        inv_lhs, inv_rhs = self.write_inverse([t10x, t_neg8x], r"+8x", color=INVERSE_COLOR)
        self.strike_pair(t_neg8x, inv_rhs)
        self.extend_current_line(inv_lhs)

        m1 = self.reveal_term(r"18x", after=None, source=[t10x, inv_lhs], color=VAR_COLOR)
        m2 = self.reveal_term(r"-12", after=m1, source=t_neg12, indicate=False)
        m_eq = self.reveal_term(r"=", after=m2, indicate=False)
        m3 = self.reveal_term(r"120", after=m_eq, source=t120, indicate=False)

        self.finish_line([m1, m2, m_eq, m3])

        # --- get constants on one side: add the additive inverse of -12 to both sides ---
        inv2_lhs, inv2_rhs = self.write_inverse([m2, m3], r"+12", color=INVERSE_COLOR)
        self.strike_pair(m2, inv2_lhs)
        self.extend_current_line(inv2_rhs)

        q1 = self.reveal_term(r"18x", after=None, source=m1, indicate=False, color=VAR_COLOR)
        q_eq = self.reveal_term(r"=", after=q1, indicate=False)
        q2 = self.reveal_term(r"132", after=q_eq, source=[m3, inv2_rhs])

        self.finish_line([q1, q_eq, q2])

        # --- apply the multiplicative inverse: divide both sides by 18 ---
        r1 = self.reveal_term(r"x", after=None, source=q1, indicate=False, color=VAR_COLOR)
        r_eq = self.reveal_term(r"=", after=r1, indicate=False)
        r2 = self.reveal_term(r"\frac{22}{3}", after=r_eq, source=[q1, q2], color=VAR_COLOR)

        self.finish_line([r1, r_eq, r2])
        self.box_final(VGroup(r1, r_eq, r2))

        result = Text("One Solution", font_size=36, weight=BOLD, color=ANSWER_COLOR)
        result.next_to(VGroup(r1, r_eq, r2), DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.next_slide()
