from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.distribution import DistributionTemplate


class Problem97Brackets(Slide, DistributionTemplate):
    """Problem 97: 12 - 4[(8 - 2v) + 5(-3w - 4v)] - w"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("97)")

        original = MathTex(
            r"{{12}}{{-4}}[({{8}}{{-2v}})+{{5}}({{-3w}}{{-4v}})]{{-w}}"
        )
        self.start_stack(original)

        t_12 = original.get_part_by_tex("12", substring=False)
        t_neg4 = original.get_part_by_tex("-4", substring=False)
        t_8 = original.get_part_by_tex("8", substring=False)
        t_neg2v = original.get_part_by_tex("-2v", substring=False)
        t_5 = original.get_part_by_tex("5", substring=False)
        t_neg3w = original.get_part_by_tex("-3w", substring=False)
        t_neg4v = original.get_part_by_tex("-4v", substring=False)
        t_negw = original.get_part_by_tex("-w", substring=False)

        # --- bring everything down, drop the redundant (8-2v) parens, distribute the 5 ---
        r1 = self.reveal_term("12", source=t_12, indicate=False)
        r2 = self.reveal_term(r"-4[8", after=r1, source=[t_neg4, t_8], indicate=False)
        r3 = self.reveal_term(r"-2v", after=r2, source=t_neg2v, indicate=False)
        r4 = self.reveal_term(r"-15w", after=r3, source=[t_5, t_neg3w])
        r5 = self.reveal_term(r"-20v", after=r4, source=[t_5, t_neg4v])
        r6 = self.reveal_term(r"]-w", after=r5, source=t_negw, indicate=False)

        self.finish_line([r1, r2, r3, r4, r5, r6])

        # --- combine like terms inside the brackets (-2v - 20v = -22v) ---
        s1 = self.reveal_term("12", source=r1, indicate=False)
        s2 = self.reveal_term(r"-4[8", after=s1, source=r2, indicate=False)
        s3 = self.reveal_term(r"-22v", after=s2, source=[r3, r5])
        s4 = self.reveal_term(r"-15w", after=s3, source=r4, indicate=False)
        s5 = self.reveal_term(r"]-w", after=s4, source=r6, indicate=False)

        self.finish_line([s1, s2, s3, s4, s5])

        # --- distribute the -4 across everything in the brackets ---
        u1 = self.reveal_term("12", source=s1, indicate=False)
        u2 = self.reveal_term(r"-32", after=u1, source=s2)
        u3 = self.reveal_term(r"+88v", after=u2, source=[s2, s3])
        u4 = self.reveal_term(r"+60w", after=u3, source=[s2, s4])
        u5 = self.reveal_term(r"-w", after=u4, source=s5, indicate=False)

        self.finish_line([u1, u2, u3, u4, u5])

        # --- final combine: constants, then the w's (v has nothing to combine with) ---
        v1 = self.reveal_term("-20", source=[u1, u2])
        v2 = self.reveal_term(r"+88v", after=v1, source=u3, indicate=False)
        v3 = self.reveal_term(r"+59w", after=v2, source=[u4, u5])

        self.finish_line([v1, v2, v3])
        self.box_final(VGroup(v1, v2, v3))
