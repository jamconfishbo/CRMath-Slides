from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = GREEN     # every instance of w
INVERSE_COLOR = RED   # additive inverses written below a term


class Example1LinearEquation(Slide, DistributionTemplate):
    """Example 1: -3(w-4) + 5 = 10 - (w+1)  ->  one solution, w = 4."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Example 1)")

        original = MathTex(r"{{-3}}({{w}}{{-4}})+{{5}}={{10}}-({{w}}+{{1}})")
        for part in original.get_parts_by_tex("w", substring=False):
            part.set_color(VAR_COLOR)

        self.start_stack(original)

        # --- rewrite "-(w+1)" as "-1(w+1)" to expose the invisible coefficient, same line ---
        new_line = MathTex(r"{{-3}}({{w}}{{-4}})+{{5}}={{10}}{{-1}}({{w}}+{{1}})")
        for part in new_line.get_parts_by_tex("w", substring=False):
            part.set_color(VAR_COLOR)
        current = self.rewrite_line(new_line)

        t_neg3 = current.get_part_by_tex("-3", substring=False)
        t_neg4 = current.get_part_by_tex("-4", substring=False)
        t_5 = current.get_part_by_tex("5", substring=False)
        t_10 = current.get_part_by_tex("10", substring=False)
        t_neg1 = current.get_part_by_tex("-1", substring=False)
        t_1 = current.get_part_by_tex("1", substring=False)
        w_parts = current.get_parts_by_tex("w", substring=False)

        # --- distribute, term by term ---
        d1 = self.reveal_term(r"-3w", after=None, source=[t_neg3, w_parts[0]], color=VAR_COLOR)
        d2 = self.reveal_term(r"+12", after=d1, source=[t_neg3, t_neg4])
        d3 = self.reveal_term(r"+5", after=d2, source=t_5, indicate=False)
        d_eq1 = self.reveal_term(r"=", after=d3, indicate=False)
        d4 = self.reveal_term(r"10", after=d_eq1, source=t_10, indicate=False)
        d5 = self.reveal_term(r"-w", after=d4, source=[t_neg1, w_parts[1]], color=VAR_COLOR)
        d6 = self.reveal_term(r"-1", after=d5, source=[t_neg1, t_1])

        self.finish_line([d1, d2, d3, d_eq1, d4, d5, d6])

        # --- combine like terms ---
        c1 = self.reveal_term(r"-3w", after=None, source=d1, indicate=False, color=VAR_COLOR)
        c2 = self.reveal_term(r"+17", after=c1, source=[d2, d3])
        c_eq = self.reveal_term(r"=", after=c2, indicate=False)
        c3 = self.reveal_term(r"9", after=c_eq, source=[d4, d6])
        c4 = self.reveal_term(r"-w", after=c3, source=d5, indicate=False, color=VAR_COLOR)

        self.finish_line([c1, c2, c_eq, c3, c4])

        # --- get variables on one side: add the additive inverse of the right side's w ---
        inv_lhs, inv_rhs = self.write_inverse([c1, c4], r"+1w", color=INVERSE_COLOR)
        strike1 = self.strike_pair(c4, inv_rhs)
        self.extend_current_line(inv_lhs, inv_rhs, strike1)

        v1 = self.reveal_term(r"-2w", after=None, source=[c1, inv_lhs], color=VAR_COLOR)
        v2 = self.reveal_term(r"+17", after=v1, source=c2, indicate=False)
        v_eq = self.reveal_term(r"=", after=v2, indicate=False)
        v3 = self.reveal_term(r"9", after=v_eq, source=c3, indicate=False)

        self.finish_line([v1, v2, v_eq, v3])

        # --- get constants on one side: add the additive inverse of the left side's 17 ---
        inv2_lhs, inv2_rhs = self.write_inverse([v2, v3], r"-17", color=INVERSE_COLOR)
        strike2 = self.strike_pair(v2, inv2_lhs)
        self.extend_current_line(inv2_lhs, inv2_rhs, strike2)

        k1 = self.reveal_term(r"-2w", after=None, source=v1, indicate=False, color=VAR_COLOR)
        k_eq = self.reveal_term(r"=", after=k1, indicate=False)
        k2 = self.reveal_term(r"-8", after=k_eq, source=[v3, inv2_rhs])

        self.finish_line([k1, k_eq, k2])

        # --- apply the multiplicative inverse: divide both sides by -2 ---
        f1 = self.reveal_term(r"w", after=None, source=k1, indicate=False, color=VAR_COLOR)
        f_eq = self.reveal_term(r"=", after=f1, indicate=False)
        f2 = self.reveal_term(r"4", after=f_eq, source=[k1, k2], color=VAR_COLOR)

        self.finish_line([f1, f_eq, f2])
        self.box_final(VGroup(f1, f_eq, f2))

        result = Text("One Solution", font_size=36, weight=BOLD, color=ANSWER_COLOR)
        result.next_to(VGroup(f1, f_eq, f2), DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.finish_line([result])
        self.next_slide()
