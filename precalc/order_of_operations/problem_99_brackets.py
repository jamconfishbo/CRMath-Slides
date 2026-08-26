from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, INDICATE_COLOR, ANSWER_COLOR
from templates.distribution import DistributionTemplate


class Problem99Brackets(Slide, DistributionTemplate):
    """Problem 99: 2y^2 - [13 - (2/3)(6y^2 - 9) - 10] + 9

    NOTE: the source text was missing a closing parenthesis after "6y^2-9"
    (it read "...6y^2-9-10]..."). Reconstructed with "-10" as its own term
    inside the brackets, after the (2/3)(...) group -- this gives a clean
    final answer of 6y^2. Flag if a different grouping was intended.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("99)")

        original = MathTex(
            r"{{2y^2}}-[{{13}}-{{\frac{2}{3} }}({{6y^2}}{{-9}}){{-10}}]+{{9}}"
        )
        self.start_stack(original)

        t_2ysq = original.get_part_by_tex("2y^2", substring=False)
        t_13 = original.get_part_by_tex("13", substring=False)
        t_frac = original.get_part_by_tex(r"\frac{2}{3}")
        t_6ysq = original.get_part_by_tex("6y^2", substring=False)
        t_neg9 = original.get_part_by_tex("-9", substring=False)
        t_neg10 = original.get_part_by_tex("-10", substring=False)
        t_9outer = original.get_part_by_tex("9", substring=False)

        # --- distribute 2/3 into (6y^2 - 9), one term at a time ---
        r1 = self.reveal_term(r"2y^2", source=t_2ysq, indicate=False)
        r2 = self.reveal_term(r"-[13", after=r1, source=t_13, indicate=False)
        r3 = self.reveal_term(r"-4y^2", after=r2, source=[t_frac, t_6ysq])
        r4 = self.reveal_term(r"+6", after=r3, source=[t_frac, t_neg9])
        r5 = self.reveal_term(r"-10", after=r4, source=t_neg10, indicate=False)
        r6 = self.reveal_term(r"]+9", after=r5, source=t_9outer, indicate=False)

        self.finish_line([r1, r2, r3, r4, r5, r6])

        # --- combine like terms inside the brackets (13 + 6 - 10 = 9) ---
        s1 = self.reveal_term(r"2y^2", source=r1, indicate=False)
        s2 = self.reveal_term(r"-[", after=s1, indicate=False)
        s3 = self.reveal_term(r"-4y^2", after=s2, source=r3, indicate=False)
        s4 = self.reveal_term(r"+9", after=s3, source=[r2, r4, r5])
        s5 = self.reveal_term(r"]+9", after=s4, source=r6, indicate=False)

        self.finish_line([s1, s2, s3, s4, s5])

        # --- draw the imaginary "1" after the minus sign in front of the bracket ---
        u1 = self.reveal_term(r"2y^2", source=s1, indicate=False)
        u2 = self.reveal_term(r"-1[", after=u1, source=s2)
        u3 = self.reveal_term(r"-4y^2", after=u2, source=s3, indicate=False)
        u4 = self.reveal_term(r"+9", after=u3, source=s4, indicate=False)
        u5 = self.reveal_term(r"]+9", after=u4, source=s5, indicate=False)

        self.finish_line([u1, u2, u3, u4, u5])

        # --- distribute the -1 across everything in the brackets ---
        v1 = self.reveal_term(r"2y^2", source=u1, indicate=False)
        v2 = self.reveal_term(r"+4y^2", after=v1, source=[u2, u3])
        v3 = self.reveal_term(r"-9", after=v2, source=[u2, u4])
        v4 = self.reveal_term(r"+9", after=v3, source=u5, indicate=False)

        v_line = self.finish_line([v1, v2, v3, v4])

        # --- final combine: y^2 terms, then the constants (which cancel) ---
        w1 = self.reveal_term(r"6y^2", source=[v1, v2])

        self.play(Indicate(VGroup(v3, v4), color=INDICATE_COLOR, scale_factor=1.2))
        self.play(FadeOut(VGroup(v3, v4)))
        v_line.remove(v3, v4)
        self.remove(v3, v4)
        self.next_slide()

        self.finish_line([w1])
        self.box_final(w1)
