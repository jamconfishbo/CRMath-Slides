from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, X_COLOR, Y_COLOR
from templates.distribution import DistributionTemplate


class Problem7Distribution(Slide, DistributionTemplate):
    """Problem 7: 12 - 3(5x - 2y) + 5(3 - x) - y"""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("7)")

        original = MathTex(r"{{12}}{{-3}}({{5x}}{{-2y}})+{{5}}({{3}}{{-x}}){{-y}}")
        original.set_color_by_tex("x", X_COLOR)
        original.set_color_by_tex("y", Y_COLOR)

        self.start_stack(original)

        t12 = original.get_part_by_tex("12", substring=False)
        t_neg3 = original.get_part_by_tex("-3", substring=False)
        t_5x = original.get_part_by_tex("5x", substring=False)
        t_neg2y = original.get_part_by_tex("-2y", substring=False)
        t_5 = original.get_part_by_tex("5", substring=False)
        t_3 = original.get_part_by_tex("3", substring=False)
        t_negx = original.get_part_by_tex("-x", substring=False)
        t_negy = original.get_part_by_tex("-y", substring=False)

        # --- distribute, one term at a time ---
        d12 = self.reveal_term("12", source=t12, indicate=False)
        d_neg15x = self.reveal_term(r"-15x", after=d12, source=[t_neg3, t_5x], color=X_COLOR)
        d_6y = self.reveal_term(r"+6y", after=d_neg15x, source=[t_neg3, t_neg2y], color=Y_COLOR)
        d_15 = self.reveal_term(r"+15", after=d_6y, source=[t_5, t_3])
        d_neg5x = self.reveal_term(r"-5x", after=d_15, source=[t_5, t_negx], color=X_COLOR)
        d_negy = self.reveal_term(r"-y", after=d_neg5x, source=t_negy, indicate=False, color=Y_COLOR)

        self.finish_line([d12, d_neg15x, d_6y, d_15, d_neg5x, d_negy])

        # --- combine like terms: constants, then x's, then y's ---
        e27 = self.reveal_term("27", source=[d12, d_15])
        e_neg20x = self.reveal_term(r"-20x", after=e27, source=[d_neg15x, d_neg5x], color=X_COLOR)
        e_5y = self.reveal_term(r"+5y", after=e_neg20x, source=[d_6y, d_negy], color=Y_COLOR)

        self.finish_line([e27, e_neg20x, e_5y])

        self.box_final(VGroup(e27, e_neg20x, e_5y))
