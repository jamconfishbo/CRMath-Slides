from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = GREEN
INVERSE_COLOR = RED
NO_SOLUTION_COLOR = RED
INFINITE_COLOR = BLUE


class PracticeSolutionsLinearEquations(Slide, DistributionTemplate):
    """Worked solutions for practice problems a) one solution, b) no solution,
    c) infinitely many solutions."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.solve_a()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_b()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

        self.solve_c()

    def solve_a(self):
        """4x + 1 - x = 6x - 2  ->  one solution, x = 1."""
        self.show_label("a)")

        original = MathTex(r"{{4x}}+{{1}}-{{x}}={{6x}}{{-2}}")
        for tex in ("4x", "x", "6x"):
            original.get_part_by_tex(tex, substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t4x = original.get_part_by_tex("4x", substring=False)
        t1 = original.get_part_by_tex("1", substring=False)
        tx = original.get_part_by_tex("x", substring=False)
        t6x = original.get_part_by_tex("6x", substring=False)
        t_neg2 = original.get_part_by_tex("-2", substring=False)

        # --- combine like terms (no parentheses to distribute here) ---
        c1 = self.reveal_term(r"3x", after=None, source=[t4x, tx], color=VAR_COLOR)
        c2 = self.reveal_term(r"+1", after=c1, source=t1, indicate=False)
        c_eq = self.reveal_term(r"=", after=c2, indicate=False)
        c3 = self.reveal_term(r"6x", after=c_eq, source=t6x, indicate=False, color=VAR_COLOR)
        c4 = self.reveal_term(r"-2", after=c3, source=t_neg2, indicate=False)

        self.finish_line([c1, c2, c_eq, c3, c4])

        # --- get variables on one side: add the additive inverse of 3x to both sides ---
        inv_lhs, inv_rhs = self.write_inverse([c1, c3], r"-3x", color=INVERSE_COLOR)
        self.strike_pair(c1, inv_lhs)
        self.extend_current_line(inv_rhs)

        n1 = self.reveal_term(r"1", after=None, source=c2, indicate=False)
        n_eq = self.reveal_term(r"=", after=n1, indicate=False)
        n2 = self.reveal_term(r"3x", after=n_eq, source=[c3, inv_rhs], color=VAR_COLOR)
        n3 = self.reveal_term(r"-2", after=n2, source=c4, indicate=False)

        self.finish_line([n1, n_eq, n2, n3])

        # --- get constants on one side: add the additive inverse of -2 to both sides ---
        inv2_lhs, inv2_rhs = self.write_inverse([n1, n3], r"+2", color=INVERSE_COLOR)
        self.strike_pair(n3, inv2_rhs)
        self.extend_current_line(inv2_lhs)

        q1 = self.reveal_term(r"3", after=None, source=[n1, inv2_lhs])
        q_eq = self.reveal_term(r"=", after=q1, indicate=False)
        q2 = self.reveal_term(r"3x", after=q_eq, source=n2, indicate=False, color=VAR_COLOR)

        self.finish_line([q1, q_eq, q2])

        # --- apply the multiplicative inverse: divide both sides by 3 ---
        r1 = self.reveal_term(r"x", after=None, source=q2, indicate=False, color=VAR_COLOR)
        r_eq = self.reveal_term(r"=", after=r1, indicate=False)
        r2 = self.reveal_term(r"1", after=r_eq, source=[q1, q2], color=VAR_COLOR)

        self.finish_line([r1, r_eq, r2])
        self.box_final(VGroup(r1, r_eq, r2))

        result = Text("One Solution", font_size=36, weight=BOLD, color=ANSWER_COLOR)
        result.next_to(VGroup(r1, r_eq, r2), DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.next_slide()

    def solve_b(self):
        """2(-5x-1) = 2x - 12x + 6  ->  no solution."""
        self.show_label("b)")

        original = MathTex(r"{{2}}({{-5x}}{{-1}})={{2x}}{{-12x}}+{{6}}")
        for tex in ("-5x", "2x", "-12x"):
            original.get_part_by_tex(tex, substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t2 = original.get_part_by_tex("2", substring=False)
        t_neg5x = original.get_part_by_tex("-5x", substring=False)
        t_neg1 = original.get_part_by_tex("-1", substring=False)
        t2x = original.get_part_by_tex("2x", substring=False)
        t_neg12x = original.get_part_by_tex("-12x", substring=False)
        t6 = original.get_part_by_tex("6", substring=False)

        # --- distribute on the left, carry the right down unchanged ---
        d1 = self.reveal_term(r"-10x", after=None, source=[t2, t_neg5x], color=VAR_COLOR)
        d2 = self.reveal_term(r"-2", after=d1, source=[t2, t_neg1])
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"2x", after=d_eq, source=t2x, indicate=False, color=VAR_COLOR)
        d4 = self.reveal_term(r"-12x", after=d3, source=t_neg12x, indicate=False, color=VAR_COLOR)
        d5 = self.reveal_term(r"+6", after=d4, source=t6, indicate=False)

        self.finish_line([d1, d2, d_eq, d3, d4, d5])

        # --- combine like terms on the right ---
        c1 = self.reveal_term(r"-10x", after=None, source=d1, indicate=False, color=VAR_COLOR)
        c2 = self.reveal_term(r"-2", after=c1, source=d2, indicate=False)
        c_eq = self.reveal_term(r"=", after=c2, indicate=False)
        c3 = self.reveal_term(r"-10x", after=c_eq, source=[d3, d4], color=VAR_COLOR)
        c4 = self.reveal_term(r"+6", after=c3, source=d5, indicate=False)

        self.finish_line([c1, c2, c_eq, c3, c4])

        # --- get variables on one side: add the additive inverse of -10x to both sides ---
        inv_lhs, inv_rhs = self.write_inverse([c1, c3], r"+10x", color=INVERSE_COLOR)
        self.strike_pair(c1, inv_lhs)
        self.strike_pair(c3, inv_rhs)

        n1 = self.reveal_term(r"-2", after=None, source=c2, indicate=False)
        n_eq = self.reveal_term(r"=", after=n1, indicate=False)
        n2 = self.reveal_term(r"6", after=n_eq, source=c4, indicate=False)

        self.finish_line([n1, n_eq, n2])

        final = VGroup(n1, n_eq, n2)
        self.play(Circumscribe(final, color=NO_SOLUTION_COLOR))

        result = Text("No Solution (Contradiction)", font_size=36, weight=BOLD, color=NO_SOLUTION_COLOR)
        result.next_to(final, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.next_slide()

    def solve_c(self):
        """2(3x-1) = 6(x+1) - 8  ->  infinitely many solutions."""
        self.show_label("c)")

        original = MathTex(r"{{2}}({{3x}}{{-1}})={{6}}({{x}}+{{1}}){{-8}}")
        original.get_part_by_tex("3x", substring=False).set_color(VAR_COLOR)
        original.get_part_by_tex("x", substring=False).set_color(VAR_COLOR)

        self.start_stack(original)

        t2 = original.get_part_by_tex("2", substring=False)
        t3x = original.get_part_by_tex("3x", substring=False)
        t_neg1 = original.get_part_by_tex("-1", substring=False)
        t6 = original.get_part_by_tex("6", substring=False)
        tx = original.get_part_by_tex("x", substring=False)
        t1 = original.get_part_by_tex("1", substring=False)
        t_neg8 = original.get_part_by_tex("-8", substring=False)

        # --- distribute on both sides, term by term ---
        d1 = self.reveal_term(r"6x", after=None, source=[t2, t3x], color=VAR_COLOR)
        d2 = self.reveal_term(r"-2", after=d1, source=[t2, t_neg1])
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"6x", after=d_eq, source=[t6, tx], color=VAR_COLOR)
        d4 = self.reveal_term(r"+6", after=d3, source=[t6, t1])
        d5 = self.reveal_term(r"-8", after=d4, source=t_neg8, indicate=False)

        self.finish_line([d1, d2, d_eq, d3, d4, d5])

        # --- combine like terms on the right ---
        c1 = self.reveal_term(r"6x", after=None, source=d1, indicate=False, color=VAR_COLOR)
        c2 = self.reveal_term(r"-2", after=c1, source=d2, indicate=False)
        c_eq = self.reveal_term(r"=", after=c2, indicate=False)
        c3 = self.reveal_term(r"6x", after=c_eq, source=d3, indicate=False, color=VAR_COLOR)
        c4 = self.reveal_term(r"-2", after=c3, source=[d4, d5])

        self.finish_line([c1, c2, c_eq, c3, c4])

        # --- get variables on one side: add the additive inverse of 6x to both sides ---
        inv_lhs, inv_rhs = self.write_inverse([c1, c3], r"-6x", color=INVERSE_COLOR)
        self.strike_pair(c1, inv_lhs)
        self.strike_pair(c3, inv_rhs)

        n1 = self.reveal_term(r"-2", after=None, source=c2, indicate=False)
        n_eq = self.reveal_term(r"=", after=n1, indicate=False)
        n2 = self.reveal_term(r"-2", after=n_eq, source=c4, indicate=False)

        self.finish_line([n1, n_eq, n2])

        final = VGroup(n1, n_eq, n2)
        self.play(Circumscribe(final, color=INFINITE_COLOR))

        result = Text("Infinitely Many Solutions (Identity)", font_size=36, weight=BOLD, color=INFINITE_COLOR)
        result.next_to(final, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(result, shift=UP * 0.2))
        self.next_slide()
