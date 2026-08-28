from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.distribution import DistributionTemplate


class Problem123Fractions(Slide, DistributionTemplate):
    """Problem 123: (1/8)(24n - 16m) - (2/5)(3m - 18n - 2) + 3/2

    NOTE: source text had "...-18n-2}+..." (an unmatched closing brace where
    a closing parenthesis was expected). Reconstructed with the parenthetical
    closing right after "-2". Flag if a different grouping was intended.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("123)")

        original = MathTex(
            r"{{\frac{1}{8} }}({{24n}}{{-16m}})-{{\frac{2}{5} }}"
            r"({{3m}}{{-18n}}{{-2}})+{{\frac{3}{2} }}"
        )
        self.start_stack(original)

        t_frac18 = original.get_part_by_tex(r"\frac{1}{8}")
        t_24n = original.get_part_by_tex("24n", substring=False)
        t_neg16m = original.get_part_by_tex("-16m", substring=False)
        t_frac25 = original.get_part_by_tex(r"\frac{2}{5}")
        t_3m = original.get_part_by_tex("3m", substring=False)
        t_neg18n = original.get_part_by_tex("-18n", substring=False)
        t_neg2 = original.get_part_by_tex("-2", substring=False)
        t_frac32 = original.get_part_by_tex(r"\frac{3}{2}")

        # --- distribute both fractions, one term at a time ---
        r1 = self.reveal_term(r"3n", source=[t_frac18, t_24n])
        r2 = self.reveal_term(r"-2m", after=r1, source=[t_frac18, t_neg16m])
        r3 = self.reveal_term(r"-\frac{6m}{5}", after=r2, source=[t_frac25, t_3m])
        r4 = self.reveal_term(r"+\frac{36n}{5}", after=r3, source=[t_frac25, t_neg18n])
        r5 = self.reveal_term(r"+\frac{4}{5}", after=r4, source=[t_frac25, t_neg2])
        r6 = self.reveal_term(r"+\frac{3}{2}", after=r5, source=t_frac32, indicate=False)

        self.finish_line([r1, r2, r3, r4, r5, r6])

        # --- combine like terms: n's, then m's, then constants ---
        s1 = self.reveal_term(r"\frac{51n}{5}", source=[r1, r4])
        s2 = self.reveal_term(r"-\frac{16m}{5}", after=s1, source=[r2, r3])
        s3 = self.reveal_term(r"+\frac{23}{10}", after=s2, source=[r5, r6])

        self.finish_line([s1, s2, s3])
        self.box_final(VGroup(s1, s2, s3))
