from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate


class ApplySkills4(Slide, RelationsFunctionsTemplate):
    """YOU DO: #4a, 4b, 4c together -- all three problems shown first, then all three answers."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Apply the Skills #4 (YOU DO)")

        label_a = Text("a)", font_size=28, weight=BOLD).move_to(LEFT * 4.3 + UP * 2.6)
        label_b = Text("b)", font_size=28, weight=BOLD).move_to(RIGHT * 3.0 + UP * 3.3)
        label_c = Text("c)", font_size=28, weight=BOLD).move_to(RIGHT * 3.0 + UP * 0.5)
        self.play(FadeIn(label_a), FadeIn(label_b), FadeIn(label_c))

        # --- show all three problems first ---
        diagram_a, _ = self.mapping_diagram(
            domain_vals=[2, 3, 8],
            range_vals=[4],
            arrows=[(2, 4), (3, 4), (8, 4)],
            repeated_source=None,
            font_size=26, oval_width=1.4, gap=2.8, center=LEFT * 4.3 + DOWN * 0.2,
            reveal_verdict=False,
        )

        eq_b = MathTex(r"|y+1| = x", font_size=28)
        eq_b.move_to(RIGHT * 3.0 + UP * 2.9)
        eq_c = MathTex(r"x^2+y^2=25", font_size=28)
        eq_c.move_to(RIGHT * 3.0 + UP * 0.1)
        self.play(Write(eq_b), Write(eq_c))
        self.next_slide()

        # --- now reveal all three answers ---
        self.reveal_mapping_verdict(diagram_a, is_function=True)

        lines_b = self.solve_for_y([
            r"y + 1 = {{\pm}} x",
            r"y = -1 {{\pm}} x",
        ], font_size=28, start_after=eq_b, line_buff=0.25)
        self.flag_plus_minus(lines_b[-1], note_font_size=22, note_buff=0.3)

        lines_c = self.solve_for_y([
            r"y^2 = 25-x^2",
            r"y = {{\pm}}\sqrt{25-x^2}",
        ], font_size=28, start_after=eq_c, line_buff=0.25)
        self.flag_plus_minus(lines_c[-1], note_font_size=22, note_buff=0.3)
