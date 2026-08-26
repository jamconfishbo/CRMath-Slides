# templates/worked_example.py

from manim import *

from components.theme import BACKGROUND_COLOR, INDICATE_COLOR, ANSWER_COLOR


class WorkedExampleTemplate:
    """Mixin providing a reusable "indicate, then simplify" worked-example flow.

    Build each line of the solution as a MathTex string, isolating the piece
    that is about to be worked on with double braces, e.g.:

        MathTex(r"20 - 12(36 \\div {{3^2}} \\div 2)")

    Then hand the sequence of lines to step_through() along with the tex of
    the piece to Indicate before transforming into the next line. Each new
    line is written in below the previous ones (which stay on screen as a
    running record of the derivation); the whole stack then scrolls up (and
    shrinks if needed to keep everything on screen) so the newest line lands
    at a fixed anchor point.

    Usage:
        class MyProblem(Slide, WorkedExampleTemplate):
            def construct(self):
                self.camera.background_color = BACKGROUND_COLOR
                self.show_label("69)")
                lines = [MathTex(...), MathTex(...), MathTex(...)]
                targets = ["3^2", "36 \\div 9", None]
                self.step_through(lines, targets)
    """

    def show_label(self, label, font_size=40):
        heading = Text(label, font_size=font_size, weight=BOLD)
        heading.to_corner(UL)
        self.play(FadeIn(heading))
        return heading

    def step_through(
        self,
        lines,
        indicate_targets,
        box_final=True,
        scale=1.1,
        anchor=DOWN * 0.5,
        line_buff=0.45,
        min_scale=0.55,
        top_margin=1.2,
        bottom_margin=0.4,
    ):
        """
        lines: list of MathTex, one per simplification step (first = the
               original problem, last = the fully simplified answer).
        indicate_targets: list the same length as `lines`. Entry i is the
               exact tex fragment to Indicate on lines[i] right before it
               transforms into lines[i + 1]. The last entry is ignored.
        anchor: point where the newest line should always come to rest.
        top_margin / bottom_margin: space to leave clear at the top (for a
               label) and bottom of the frame when deciding how much the
               growing stack needs to shrink to keep every line visible.
        """
        anchor_y = anchor[1]
        ceiling_y = config.frame_height / 2 - top_margin
        floor_y = -config.frame_height / 2 + bottom_margin

        history = VGroup()
        current = lines[0].scale(scale).move_to(anchor)
        history.add(current)
        self.play(Write(current))
        self.next_slide()

        for i in range(len(lines) - 1):
            target_tex = indicate_targets[i]
            if target_tex is not None:
                part = current.get_part_by_tex(target_tex)
                self.play(Indicate(part, color=INDICATE_COLOR, scale_factor=1.3))

            next_line = lines[i + 1].scale(scale)
            next_line.next_to(current, DOWN, buff=line_buff)
            history.add(next_line)

            self.play(TransformMatchingTex(current.copy(), next_line))

            about_point = next_line.get_center()
            top_offset = history.get_top()[1] - about_point[1]
            bottom_offset = about_point[1] - history.get_bottom()[1]

            fit_scale = 1.0
            if top_offset > 0:
                fit_scale = min(fit_scale, (ceiling_y - anchor_y) / top_offset)
            if bottom_offset > 0:
                fit_scale = min(fit_scale, (anchor_y - floor_y) / bottom_offset)
            fit_scale = max(min_scale, fit_scale)

            self.play(
                history.animate.scale(fit_scale, about_point=about_point).shift(
                    anchor - about_point
                )
            )

            current = next_line
            self.next_slide()

        if box_final:
            self.play(Circumscribe(current, color=ANSWER_COLOR))
            self.next_slide()

        return current
