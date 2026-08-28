from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.distribution import DistributionTemplate


class Problem98Brackets(Slide, DistributionTemplate):
    """Problem 98: 6 - 2[(9z + 6y) - 8(y - z)] - 11"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("98)")

        original = MathTex(
            r"{{6}}{{-2}}[({{9z}}{{+6y}}){{-8}}({{y}}{{-z}})]{{-11}}"
        )
        self.start_stack(original)

        t_6 = original.get_part_by_tex("6", substring=False)
        t_neg2 = original.get_part_by_tex("-2", substring=False)
        t_9z = original.get_part_by_tex("9z", substring=False)
        t_pos6y = original.get_part_by_tex("+6y", substring=False)
        t_neg8 = original.get_part_by_tex("-8", substring=False)
        t_y = original.get_part_by_tex("y", substring=False)
        t_negz = original.get_part_by_tex("-z", substring=False)
        t_neg11 = original.get_part_by_tex("-11", substring=False)

        # --- bring everything down, drop the redundant (9z+6y) parens, distribute the -8 ---
        r1 = self.reveal_term("6", source=t_6, indicate=False)
        r2 = self.reveal_term(r"-2[9z", after=r1, source=[t_neg2, t_9z], indicate=False)
        r3 = self.reveal_term(r"+6y", after=r2, source=t_pos6y, indicate=False)
        r4 = self.reveal_term(r"-8y", after=r3, source=[t_neg8, t_y])
        r5 = self.reveal_term(r"+8z", after=r4, source=[t_neg8, t_negz])
        r6 = self.reveal_term(r"]-11", after=r5, source=t_neg11, indicate=False)

        self.finish_line([r1, r2, r3, r4, r5, r6])

        # --- combine like terms inside the brackets (9z+8z=17z, 6y-8y=-2y) ---
        s1 = self.reveal_term("6", source=r1, indicate=False)
        s2 = self.reveal_term(r"-2[", after=s1, indicate=False)
        s3 = self.reveal_term(r"17z", after=s2, source=[r2, r5])
        s4 = self.reveal_term(r"-2y", after=s3, source=[r3, r4])
        s5 = self.reveal_term(r"]-11", after=s4, source=r6, indicate=False)

        self.finish_line([s1, s2, s3, s4, s5])

        # --- distribute the -2 across everything in the brackets ---
        u1 = self.reveal_term("6", source=s1, indicate=False)
        u2 = self.reveal_term(r"-34z", after=u1, source=[s2, s3])
        u3 = self.reveal_term(r"+4y", after=u2, source=[s2, s4])
        u4 = self.reveal_term(r"-11", after=u3, source=s5, indicate=False)

        self.finish_line([u1, u2, u3, u4])

        # --- final combine: constants, then z's, then y's ---
        v1 = self.reveal_term("-5", source=[u1, u4])
        v2 = self.reveal_term(r"-34z", after=v1, source=u2, indicate=False)
        v3 = self.reveal_term(r"+4y", after=v2, source=u3, indicate=False)

        self.finish_line([v1, v2, v3])
        self.box_final(VGroup(v1, v2, v3))
