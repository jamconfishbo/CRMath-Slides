from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.distribution import DistributionTemplate

C_COLOR = BLUE
D_COLOR = RED


class Example7Distribution(Slide, DistributionTemplate):
    """Example 7: 5 - 2(4c - 8d) + 3(1 - d) + c"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Example 7)")

        original = MathTex(r"{{5}}{{-2}}({{4c}}{{-8d}})+{{3}}({{1}}{{-d}})+{{c}}")
        original.set_color_by_tex("c", C_COLOR)
        original.set_color_by_tex("d", D_COLOR)

        self.start_stack(original)

        t5 = original.get_part_by_tex("5", substring=False)
        t_neg2 = original.get_part_by_tex("-2", substring=False)
        t_4c = original.get_part_by_tex("4c", substring=False)
        t_neg8d = original.get_part_by_tex("-8d", substring=False)
        t_3 = original.get_part_by_tex("3", substring=False)
        t_1 = original.get_part_by_tex("1", substring=False)
        t_negd = original.get_part_by_tex("-d", substring=False)
        t_c = original.get_part_by_tex("c", substring=False)

        # --- distribute, one term at a time ---
        d5 = self.reveal_term("5", source=t5, indicate=False)
        d_neg8c = self.reveal_term(r"-8c", after=d5, source=[t_neg2, t_4c], color=C_COLOR)
        d_16d = self.reveal_term(r"+16d", after=d_neg8c, source=[t_neg2, t_neg8d], color=D_COLOR)
        d_3 = self.reveal_term(r"+3", after=d_16d, source=[t_3, t_1])
        d_neg3d = self.reveal_term(r"-3d", after=d_3, source=[t_3, t_negd], color=D_COLOR)
        d_c = self.reveal_term(r"+c", after=d_neg3d, source=t_c, indicate=False, color=C_COLOR)

        self.finish_line([d5, d_neg8c, d_16d, d_3, d_neg3d, d_c])

        # --- combine like terms: constants, then c's, then d's ---
        e8 = self.reveal_term("8", source=[d5, d_3])
        e_neg7c = self.reveal_term(r"-7c", after=e8, source=[d_neg8c, d_c], color=C_COLOR)
        e_13d = self.reveal_term(r"+13d", after=e_neg7c, source=[d_16d, d_neg3d], color=D_COLOR)

        self.finish_line([e8, e_neg7c, e_13d])

        self.box_final(VGroup(e8, e_neg7c, e_13d))
