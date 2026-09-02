from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR
from templates.worked_example import WorkedExampleTemplate
from templates.distribution import DistributionTemplate

VAR_COLOR = GREEN
INVERSE_COLOR = RED


class Problem16LinearEquation(Slide, WorkedExampleTemplate, DistributionTemplate):
    """Problem 16: 4(y-3) = 3[y+2(y-2)]  ->  one solution, y = 0."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.clear_brackets()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_equation()

    def clear_brackets(self):
        self.show_label("16)")

        l0 = MathTex(r"4({{y}}-3)=3[{{y}}+{{2}}({{y}}-2)]")
        for part in l0.get_parts_by_tex("y", substring=False):
            part.set_color(VAR_COLOR)

        l1 = MathTex(r"4({{y}}-3)=3[{{y}}+{{2y}}-4]")
        for part in l1.get_parts_by_tex("y", substring=False):
            part.set_color(VAR_COLOR)
        l1.get_part_by_tex("2y", substring=False).set_color(VAR_COLOR)

        l2 = MathTex(r"4({{y}}-3)=3[{{3y}}-4]")
        l2.get_part_by_tex("y", substring=False).set_color(VAR_COLOR)
        l2.get_part_by_tex("3y", substring=False).set_color(VAR_COLOR)

        l3 = MathTex(r"{{4y}}{{-12}}={{9y}}{{-12}}")
        l3.get_part_by_tex("4y", substring=False).set_color(VAR_COLOR)
        l3.get_part_by_tex("9y", substring=False).set_color(VAR_COLOR)

        lines = [l0, l1, l2, l3]
        targets = ["2", "2y", "3y", None]

        self.step_through(lines, targets, box_final=False)

    def solve_equation(self):
        self.show_label("16) (continued)")

        original = MathTex(r"{{4y}}{{-12}}={{9y}}{{-12}}")
        original.get_part_by_tex("4y", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("9y", substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t4y = original.get_part_by_tex("4y", substring=False)
        t9y = original.get_part_by_tex("9y", substring=False)
        neg12_parts = original.get_parts_by_tex("-12", substring=False)

        # --- get variables on one side: add the additive inverse of 4y to both sides ---
        inv_lhs, inv_rhs = self.write_inverse([t4y, t9y], r"-4y", color=INVERSE_COLOR)
        self.strike_pair(t4y, inv_lhs)
        self.extend_current_line(inv_rhs)

        m1 = self.reveal_term(r"-12", after=None, source=neg12_parts[0], indicate=False)
        m_eq = self.reveal_term(r"=", after=m1, indicate=False)
        m2 = self.reveal_term(r"5y", after=m_eq, source=[t9y, inv_rhs], color=VAR_COLOR)
        m3 = self.reveal_term(r"-12", after=m2, source=neg12_parts[1], indicate=False)

        self.finish_line([m1, m_eq, m2, m3])

        # --- get constants on one side: add the additive inverse of -12 to both sides ---
        inv2_lhs, inv2_rhs = self.write_inverse([m1, m3], r"+12", color=INVERSE_COLOR)
        self.strike_pair(m3, inv2_rhs)
        self.extend_current_line(inv2_lhs)

        q1 = self.reveal_term(r"0", after=None, source=[m1, inv2_lhs])
        q_eq = self.reveal_term(r"=", after=q1, indicate=False)
        q2 = self.reveal_term(r"5y", after=q_eq, source=m2, indicate=False, color=VAR_COLOR)

        self.finish_line([q1, q_eq, q2])

        # --- apply the multiplicative inverse: divide both sides by 5 ---
        r1 = self.reveal_term(r"y", after=None, source=q2, indicate=False, color=VAR_COLOR)
        r_eq = self.reveal_term(r"=", after=r1, indicate=False)
        r2 = self.reveal_term(r"0", after=r_eq, source=[q1, q2])

        self.finish_line([r1, r_eq, r2])
        self.box_final(VGroup(r1, r_eq, r2))

        result = Text("One Solution", font_size=36, weight=BOLD, color=ANSWER_COLOR)
        result.next_to(VGroup(r1, r_eq, r2), DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.next_slide()
