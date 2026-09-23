from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.frequency_table import FrequencyTableTemplate

VAR_COLOR = X_COLOR

PROBLEMS = [
    (r"9)\ {{3x^2}}{{-10x}}+4={{2x}}+9", "x \\approx 4.381 \\text{ or } x \\approx -0.381"),
    (r"10)\ {{4x^2}}{{+5x}}-3={{x}}", "x = 0.5 \\text{ or } x = -1.5"),
    (r"11)\ {{2x^2}}{{+3x}}-10={{-2x}}+2", "x = 1.5 \\text{ or } x = -4"),
    (r"12)\ {{5x^2}}{{-6x}}+7={{4x}}+1", "x \\approx 1 \\pm 0.447i"),
    (r"13)\ {{2x^2}}{{+3x}}+1={{-4x}}+6", "x \\approx 0.608 \\text{ or } x \\approx -4.108"),
    (r"14)\ {{4x^2}}{{+10x}}+1={{3x}}+6", "x \\approx 0.545 \\text{ or } x \\approx -2.295"),
]


class Part5Practice(Slide, FrequencyTableTemplate):
    """Part 5: Mixed Practice -- all six problems, timed independent work,
    then just the answer key (no step-by-step -- students already learned
    the method in Parts 1-4)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        heading = self.show_heading("Part 5: Mixed Practice -- Multi-Term Equations", font_size=30)

        eqs = []
        for tex, _ in PROBLEMS:
            m = MathTex(tex, font_size=30)
            for part_tex in ["3x^2", "4x^2", "2x^2", "5x^2", "-10x", "+5x", "+3x", "-6x", "+10x", "2x", "x", "-2x", "-4x", "3x"]:
                for part in m.get_parts_by_tex(part_tex, substring=False):
                    part.set_color(VAR_COLOR)
            eqs.append(m)

        grid = VGroup(*eqs).arrange_in_grid(rows=3, cols=2, buff=(1.0, 1.1))
        grid.next_to(heading, DOWN, buff=0.6)
        self.play(LaggedStart(*[FadeIn(e) for e in eqs], lag_ratio=0.15))
        self.next_slide()

        self.show_timer(480, position=np.array([6.3, 0, 0]), font_size=32, bar_height=4.5)

        answers = []
        for eq, (_, ans_tex) in zip(eqs, PROBLEMS):
            a = MathTex(ans_tex, font_size=26, color=ANSWER_COLOR)
            a.next_to(eq, DOWN, buff=0.25)
            answers.append(a)

        for a in answers:
            self.play(FadeIn(a, shift=UP * 0.15))
            self.next_slide()
