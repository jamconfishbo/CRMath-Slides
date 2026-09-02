from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = GREEN
INVERSE_COLOR = RED
NO_SOLUTION_COLOR = RED
INFINITE_COLOR = BLUE


class Example2LinearEquations(Slide, DistributionTemplate):
    """Example 2: a) no solution, b) infinitely many solutions."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.solve_a()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_b()

    def solve_a(self):
        """3(2x-1) = 2(3x-2)  ->  no solution."""
        self.show_label("Example 2a)")

        original = MathTex(r"{{3}}({{2x}}{{-1}})={{2}}({{3x}}{{-2}})")
        original.get_part_by_tex("2x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("3x", substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t3 = original.get_part_by_tex("3", substring=False)
        t2x = original.get_part_by_tex("2x", substring=False)
        t_neg1 = original.get_part_by_tex("-1", substring=False)
        t2 = original.get_part_by_tex("2", substring=False)
        t3x = original.get_part_by_tex("3x", substring=False)
        t_neg2 = original.get_part_by_tex("-2", substring=False)

        # --- distribute, term by term ---
        d1 = self.reveal_term(r"6x", after=None, source=[t3, t2x], color=VAR_COLOR)
        d2 = self.reveal_term(r"-3", after=d1, source=[t3, t_neg1])
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"6x", after=d_eq, source=[t2, t3x], color=VAR_COLOR)
        d4 = self.reveal_term(r"-4", after=d3, source=[t2, t_neg2])

        self.finish_line([d1, d2, d_eq, d3, d4])

        # --- get variables on one side: add the additive inverse of 6x to both sides ---
        inv_lhs, inv_rhs = self.write_inverse([d1, d3], r"-6x", color=INVERSE_COLOR)
        strike_lhs = self.strike_pair(d1, inv_lhs)
        strike_rhs = self.strike_pair(d3, inv_rhs)
        self.extend_current_line(inv_lhs, inv_rhs, strike_lhs, strike_rhs)

        n1 = self.reveal_term(r"-3", after=None, source=d2, indicate=False)
        n_eq = self.reveal_term(r"=", after=n1, indicate=False)
        n2 = self.reveal_term(r"-4", after=n_eq, source=d4, indicate=False)

        self.finish_line([n1, n_eq, n2])

        final = VGroup(n1, n_eq, n2)
        self.play(Circumscribe(final, color=NO_SOLUTION_COLOR))

        result = Text("No Solution (Contradiction)", font_size=36, weight=BOLD, color=NO_SOLUTION_COLOR)
        result.next_to(final, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.finish_line([result])
        self.next_slide()

    def solve_b(self):
        """3(2x-1) = 2(3x-2) + 1  ->  infinitely many solutions."""
        self.show_label("Example 2b)")

        original = MathTex(r"{{3}}({{2x}}{{-1}})={{2}}({{3x}}{{-2}})+{{1}}")
        original.get_part_by_tex("2x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("3x", substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t3 = original.get_part_by_tex("3", substring=False)
        t2x = original.get_part_by_tex("2x", substring=False)
        t_neg1 = original.get_part_by_tex("-1", substring=False)
        t2 = original.get_part_by_tex("2", substring=False)
        t3x = original.get_part_by_tex("3x", substring=False)
        t_neg2 = original.get_part_by_tex("-2", substring=False)
        t_1 = original.get_part_by_tex("1", substring=False)

        # --- distribute, term by term ---
        d1 = self.reveal_term(r"6x", after=None, source=[t3, t2x], color=VAR_COLOR)
        d2 = self.reveal_term(r"-3", after=d1, source=[t3, t_neg1])
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"6x", after=d_eq, source=[t2, t3x], color=VAR_COLOR)
        d4 = self.reveal_term(r"-4", after=d3, source=[t2, t_neg2])
        d5 = self.reveal_term(r"+1", after=d4, source=t_1, indicate=False)

        self.finish_line([d1, d2, d_eq, d3, d4, d5])

        # --- combine like terms on the right ---
        c1 = self.reveal_term(r"6x", after=None, source=d1, indicate=False, color=VAR_COLOR)
        c2 = self.reveal_term(r"-3", after=c1, source=d2, indicate=False)
        c_eq = self.reveal_term(r"=", after=c2, indicate=False)
        c3 = self.reveal_term(r"6x", after=c_eq, source=d3, indicate=False, color=VAR_COLOR)
        c4 = self.reveal_term(r"-3", after=c3, source=[d4, d5])

        self.finish_line([c1, c2, c_eq, c3, c4])

        # --- get variables on one side: add the additive inverse of 6x to both sides ---
        inv_lhs, inv_rhs = self.write_inverse([c1, c3], r"-6x", color=INVERSE_COLOR)
        strike_lhs = self.strike_pair(c1, inv_lhs)
        strike_rhs = self.strike_pair(c3, inv_rhs)
        self.extend_current_line(inv_lhs, inv_rhs, strike_lhs, strike_rhs)

        n1 = self.reveal_term(r"-3", after=None, source=c2, indicate=False)
        n_eq = self.reveal_term(r"=", after=n1, indicate=False)
        n2 = self.reveal_term(r"-3", after=n_eq, source=c4, indicate=False)

        self.finish_line([n1, n_eq, n2])

        final = VGroup(n1, n_eq, n2)
        self.play(Circumscribe(final, color=INFINITE_COLOR))

        result = Text("Infinitely Many Solutions (Identity)", font_size=36, weight=BOLD, color=INFINITE_COLOR)
        result.next_to(final, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.finish_line([result])
        self.next_slide()
