from manim import *
from manim_slides import Slide


class OrderOfOperations(Slide):
    def construct(self):

# -----------------------
# Slide 1
# -----------------------

        title = Text(
            "Order of Operations",
            font_size=48
        ).to_edge(UP)

        steps = VGroup(
            Text("1. Simplify expressions inside grouping symbols"),
            Text("2. Evaluate exponents"),
            Text("3. Multiply and divide from left to right"),
            Text("4. Add and subtract from left to right"),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        )

        self.play(Write(title))
        self.play(LaggedStart(*[Write(step) for step in steps], lag_ratio=0.2))

        self.next_slide()

        # -----------------------
        # Slide 2
        # -----------------------

        self.play(
            FadeOut(title),
            FadeOut(steps)
        )

        step_title = Text(
            "Step 1: Grouping Symbols",
            font_size=48
        ).to_edge(UP)

        explanation = Text(
            "Simplify expressions within grouping symbols first.",
            font_size=32
        )

        example = MathTex(
            "3\\,(2 + 4)^2"
        ).scale(1.5)

        example.set_color_by_tex("2", GREEN)
        example.set_color_by_tex("4", RED)

        work = MathTex(
            "3\\,(6)^2"
        ).scale(1.5)

        work.next_to(example, DOWN, buff=1)

        arrow = Arrow(
            example.get_bottom(),
            work.get_top(),
            buff=0.2
        )

        self.play(Write(step_title))
        self.play(FadeIn(explanation))
        self.play(Write(example))
        self.play(GrowArrow(arrow))
        self.play(TransformFromCopy(example, work))

        self.wait()

        self.next_slide()
