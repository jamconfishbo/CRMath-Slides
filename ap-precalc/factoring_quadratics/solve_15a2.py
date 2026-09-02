from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = GREEN
FILL_COLOR = BLUE
WRONG_COLOR = RED
RIGHT_COLOR = GREEN


class Solve15ASquared(Slide, DistributionTemplate):
    """Solve 15a^2 - 3a = 3 - 7a by factoring (guess and check)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Solve by Factoring:")

        original = MathTex(r"15{{a}}^2 - 3{{a}} = 3 - 7{{a}}", font_size=56)
        for part in original.get_parts_by_tex("a", substring=False):
            part.set_color(VAR_COLOR)
        original.move_to(UP * 2.5)
        self.play(Write(original))
        self.next_slide()

        standard = MathTex(r"15{{a}}^2 + 4{{a}} - 3 = 0", font_size=56)
        for part in standard.get_parts_by_tex("a", substring=False):
            part.set_color(VAR_COLOR)
        standard.move_to(original)
        self.play(TransformMatchingTex(original, standard))
        self.next_slide()

        breakdown = MathTex(r"15 = 5 \times 3 \qquad\qquad 3 = 1 \times 3", font_size=36)
        breakdown.next_to(standard, DOWN, buff=0.6)
        self.play(Write(breakdown))
        self.next_slide()

        template = MathTex(r"(5{{a}}+\rule{0.35cm}{0.5pt})(3{{a}}+\rule{0.35cm}{0.5pt})", font_size=48)
        for part in template.get_parts_by_tex("a", substring=False):
            part.set_color(VAR_COLOR)
        template.next_to(breakdown, DOWN, buff=0.5)
        self.play(Write(template))
        self.next_slide()

        guess_label = Text("Guess and check the placement:", font_size=28)
        guess_label.next_to(template, DOWN, buff=0.5)
        self.play(FadeIn(guess_label))
        self.next_slide()

        wrong = MathTex(
            r"(5a-1)(3a+3): \;\; 5a(3)+3a(-1) = 12a",
            font_size=32,
        )
        wrong.next_to(guess_label, DOWN, buff=0.4)
        self.play(Write(wrong))
        self.next_slide()

        wrong_strike = Line(
            wrong.get_corner(UL) + UP * 0.06 + LEFT * 0.06,
            wrong.get_corner(DR) + DOWN * 0.06 + RIGHT * 0.06,
            color=WRONG_COLOR,
            stroke_width=5,
        )
        self.play(Create(wrong_strike))
        self.next_slide()

        right = MathTex(
            r"(5a+3)(3a-1): \;\; 5a(-1)+3a(3) = 4a \; \checkmark",
            font_size=32,
            color=RIGHT_COLOR,
        )
        right.next_to(wrong, DOWN, buff=0.4)
        self.play(Write(right))
        self.next_slide()

        self.play(FadeOut(guess_label, wrong, wrong_strike, right))

        factored = MathTex(r"(5{{a}}{{+3}})(3{{a}}{{-1}}) = 0", font_size=52)
        for part in factored.get_parts_by_tex("a", substring=False):
            part.set_color(VAR_COLOR)
        factored.get_part_by_tex("+3", substring=False).set_color(FILL_COLOR)
        factored.get_part_by_tex("-1", substring=False).set_color(FILL_COLOR)
        factored.next_to(template, DOWN, buff=1.0)
        self.play(Write(factored))
        self.next_slide()

        solutions = MathTex(
            r"5a+3=0 \;\Rightarrow\; a=-\frac{3}{5} \qquad\qquad 3a-1=0 \;\Rightarrow\; a=\frac{1}{3}",
            font_size=36,
        )
        solutions.next_to(factored, DOWN, buff=0.6)
        self.play(Write(solutions))
        self.next_slide()

        self.box_final(solutions)
