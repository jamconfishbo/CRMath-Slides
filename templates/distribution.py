# templates/distribution.py

from manim import *

from components.theme import BACKGROUND_COLOR, INDICATE_COLOR, ANSWER_COLOR

LEFT_MARGIN = -6.2
FIRST_LINE_Y = 2.6


class DistributionTemplate:
    """Mixin for "distribute, then combine like terms" worked examples.

    Unlike WorkedExampleTemplate (which morphs one centered expression into
    the next), this builds each line left-to-right, term by term, and keeps
    every finished line on screen, left-aligned, stacked below the last.

    Usage:
        class MyProblem(Slide, DistributionTemplate):
            def construct(self):
                self.camera.background_color = BACKGROUND_COLOR
                self.show_label("Example 7)")

                original = MathTex(r"{{5}}{{-2}}({{4c}}{{-8d}})...")
                self.start_stack(original)

                t5 = original.get_part_by_tex("5", substring=False)
                ...
                d5 = self.reveal_term("5", source=t5, indicate=False)
                d_neg8c = self.reveal_term(r"-8c", after=d5, source=[t_neg2, t_4c])
                ...
                self.finish_line([d5, d_neg8c, ...])
    """

    def show_label(self, label, font_size=40):
        heading = Text(label, font_size=font_size, weight=BOLD)
        heading.to_corner(UL)
        self.play(FadeIn(heading))
        return heading

    def start_stack(
        self,
        first_line,
        scale=1.1,
        line_buff=0.55,
        min_scale=0.5,
        bottom_margin=0.5,
        left_x=LEFT_MARGIN,
        top_y=FIRST_LINE_Y,
    ):
        self._stack = VGroup()
        self._left_x = left_x
        self._line_buff = line_buff
        self._min_scale = min_scale
        self._floor = -config.frame_height / 2 + bottom_margin
        self._current_scale = scale

        first_line.scale(scale)
        first_line.move_to(np.array([left_x, top_y, 0]), aligned_edge=LEFT)
        self._top_left = first_line.get_corner(UL)

        self._stack.add(first_line)
        self.play(Write(first_line))
        self.next_slide()
        self._current_line = first_line
        return first_line

    def reveal_term(self, term_text, *, after=None, source=None, indicate=True, color=None, buff=0.18):
        """
        Add one term to the line currently being built.

        after: the term (already on screen) this one should sit to the right
               of. Leave as None for the first term of a new line -- it will
               be placed below self._current_line, at the stack's left margin.
        source: a mobject, or list of mobjects, this term is derived from.
               If given, they're Indicated (unless indicate=False) and then
               copied down into the new term via TransformFromCopy.
        """
        term = MathTex(term_text, color=color if color else WHITE)
        term.scale(self._current_scale)

        if after is None:
            term.next_to(self._current_line, DOWN, buff=self._line_buff, aligned_edge=LEFT)
        else:
            term.next_to(after, RIGHT, buff=buff)

        src = VGroup(*source) if isinstance(source, (list, tuple)) else source

        if src is not None and indicate:
            self.play(Indicate(src, color=INDICATE_COLOR, scale_factor=1.2))

        if src is not None:
            self.play(TransformFromCopy(src, term))
        else:
            self.play(Write(term))

        self.next_slide()
        return term

    def finish_line(self, terms):
        """Group the completed line's terms, add it to the stack, and shrink
        the whole stack (about its fixed top-left corner) if it would
        otherwise overflow the bottom of the frame."""
        line = VGroup(*terms)
        self._stack.add(line)

        available = self._top_left[1] - self._floor
        needed = self._top_left[1] - self._stack.get_bottom()[1]

        if needed > available:
            fit_scale = max(self._min_scale, available / needed)
            self.play(self._stack.animate.scale(fit_scale, about_point=self._top_left))
            self._current_scale *= fit_scale

        self._current_line = line
        return line

    def box_final(self, mobject):
        self.play(Circumscribe(mobject, color=ANSWER_COLOR))
        self.next_slide()
