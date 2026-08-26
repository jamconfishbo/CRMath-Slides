from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, INDICATE_COLOR, ANSWER_COLOR
from templates.distribution import DistributionTemplate


class Problem100Brackets(Slide, DistributionTemplate):
    """Problem 100: 6 - [5t^2 - (3/4)(12 - 8t^2) + 5] + 11t^2"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("100)")

        original = MathTex(
            r"{{6}}-[{{5t^2}}-{{\frac{3}{4} }}({{12}}{{-8t^2}}){{+5}}]+{{11t^2}}"
        )
        self.start_stack(original)

        t_6 = original.get_part_by_tex("6", substring=False)
        t_5tsq = original.get_part_by_tex("5t^2", substring=False)
        t_frac = original.get_part_by_tex(r"\frac{3}{4}")
        t_12 = original.get_part_by_tex("12", substring=False)
        t_neg8tsq = original.get_part_by_tex("-8t^2", substring=False)
        t_pos5 = original.get_part_by_tex("+5", substring=False)
        t_11tsq = original.get_part_by_tex("11t^2", substring=False)

        # --- distribute 3/4 into (12 - 8t^2), one term at a time ---
        r1 = self.reveal_term(r"6", source=t_6, indicate=False)
        r2 = self.reveal_term(r"-[5t^2", after=r1, source=t_5tsq, indicate=False)
        r3 = self.reveal_term(r"-9", after=r2, source=[t_frac, t_12])
        r4 = self.reveal_term(r"+6t^2", after=r3, source=[t_frac, t_neg8tsq])
        r5 = self.reveal_term(r"+5", after=r4, source=t_pos5, indicate=False)
        r6 = self.reveal_term(r"]+11t^2", after=r5, source=t_11tsq, indicate=False)

        self.finish_line([r1, r2, r3, r4, r5, r6])

        # --- combine like terms inside the brackets (5t^2+6t^2=11t^2, -9+5=-4) ---
        s1 = self.reveal_term(r"6", source=r1, indicate=False)
        s2 = self.reveal_term(r"-[", after=s1, indicate=False)
        s3 = self.reveal_term(r"11t^2", after=s2, source=[r2, r4])
        s4 = self.reveal_term(r"-4", after=s3, source=[r3, r5])
        s5 = self.reveal_term(r"]+11t^2", after=s4, source=r6, indicate=False)

        self.finish_line([s1, s2, s3, s4, s5])

        # --- draw the imaginary "1" after the minus sign in front of the bracket ---
        u1 = self.reveal_term(r"6", source=s1, indicate=False)
        u2 = self.reveal_term(r"-1[", after=u1, source=s2)
        u3 = self.reveal_term(r"11t^2", after=u2, source=s3, indicate=False)
        u4 = self.reveal_term(r"-4", after=u3, source=s4, indicate=False)
        u5 = self.reveal_term(r"]+11t^2", after=u4, source=s5, indicate=False)

        self.finish_line([u1, u2, u3, u4, u5])

        # --- distribute the -1 across everything in the brackets ---
        v1 = self.reveal_term(r"6", source=u1, indicate=False)
        v2 = self.reveal_term(r"-11t^2", after=v1, source=[u2, u3])
        v3 = self.reveal_term(r"+4", after=v2, source=[u2, u4])
        v4 = self.reveal_term(r"+11t^2", after=v3, source=u5, indicate=False)

        v_line = self.finish_line([v1, v2, v3, v4])

        # --- final combine: constants (6+4=10), then the t^2 terms (which cancel) ---
        w1 = self.reveal_term(r"10", source=[v1, v3])

        self.play(Indicate(VGroup(v2, v4), color=INDICATE_COLOR, scale_factor=1.2))
        self.play(FadeOut(VGroup(v2, v4)))
        v_line.remove(v2, v4)
        self.remove(v2, v4)
        self.next_slide()

        self.finish_line([w1])
        self.box_final(w1)
