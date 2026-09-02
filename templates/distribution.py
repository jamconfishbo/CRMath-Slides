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

    def rewrite_line(self, new_line):
        """Transform the current line in place into new_line, at the same
        stack slot (no new row added) -- e.g. rewriting "-(x+1)" as
        "-1(x+1)" to expose the "invisible" coefficient before distributing."""
        new_line.scale(self._current_scale)
        new_line.move_to(self._current_line, aligned_edge=LEFT)

        self.play(TransformMatchingTex(self._current_line, new_line))

        self._stack.remove(self._current_line)
        self._stack.add(new_line)
        self._current_line = new_line
        self._top_left = new_line.get_corner(UL)

        self.next_slide()
        return new_line

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

    def write_inverse(self, targets, inverse_text, color=RED, buff=0.3):
        """Write inverse_text (e.g. the additive inverse of a term) directly
        below each mobject in `targets`, in one simultaneous move -- this is
        "add/subtract the same thing on both sides." Returns the new
        mobjects, in the same order as `targets`."""
        inverses = []
        for target in targets:
            inv = MathTex(inverse_text, color=color)
            inv.scale(self._current_scale)
            inv.next_to(target, DOWN, buff=buff)
            inverses.append(inv)

        self.play(*[Write(inv) for inv in inverses])
        self.next_slide()
        return inverses

    def strike_pair(self, top, bottom):
        """Draw a strikethrough line through `top` and the additive-inverse
        term written below it (they cancel to zero), then fade both away."""
        group = VGroup(top, bottom)
        line = Line(
            group.get_corner(UL) + UP * 0.08 + LEFT * 0.08,
            group.get_corner(DR) + DOWN * 0.08 + RIGHT * 0.08,
            color=GRAY,
            stroke_width=6,
        )
        self.play(Create(line))
        self.next_slide()
        self.play(FadeOut(group), FadeOut(line))
        # FadeOut only animates opacity -- since these mobjects stay nested
        # inside the permanent stack (for later rescales), pin opacity to 0
        # for good, or they'd pop back to full opacity on the next rescale.
        group.set_opacity(0)
        line.set_opacity(0)
        self.next_slide()

    def extend_current_line(self, *extra):
        """Fold extra mobjects (a surviving additive-inverse annotation left
        under the current line) into the stack -- so a later rescale moves
        them too -- and into the current-line reference, so the next
        stacked row is placed below them instead of overlapping them."""
        for mob in extra:
            self._stack.add(mob)
        self._current_line = VGroup(self._current_line, *extra)

    def box_final(self, mobject):
        self.play(Circumscribe(mobject, color=ANSWER_COLOR))
        self.next_slide()
