from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR, ANSWER_COLOR, X_COLOR
from templates.distribution import DistributionTemplate

VAR_COLOR = X_COLOR
SQUARE_COLOR = RED

PICTURE_CENTER = RIGHT * 4.1
STACK_LEFT_X = -5.6


class Problem4Projectile(Slide, DistributionTemplate):
    """Problem 4 (juggler's toss): 10 = -16t^2 + 24t + 5 -> t ~= 1.25 s (accept) or 0.25 s (reject)."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.show_label("Problem 4 — Juggler's Toss")

        self.show_picture()

        # --- set up the equation from the picture: h(t) = 10 ---
        original = MathTex(r"{{10}}{{=}}{{-16t^2}}+{{24t}}+{{5}}")
        original[2].set_color(VAR_COLOR)
        original[4].set_color(VAR_COLOR)

        self.start_stack(original, bottom_margin=1.7, left_x=STACK_LEFT_X)

        t_10, t_eq0, t_quad, t_plus1, t_lin, t_plus2, t_5 = original

        # --- subtract 5 from both sides ---
        inv_lhs, inv_rhs = self.write_inverse([t_10, t_5], r"-5", color=WHITE)
        strike = self.strike_pair(t_5, inv_rhs)
        self.extend_current_line(inv_lhs, inv_rhs, strike)

        s1 = self.reveal_term(r"5", after=None, source=[t_10, inv_lhs], indicate=False)
        s_eq = self.reveal_term(r"=", after=s1, indicate=False)
        s2 = self.reveal_term(
            r"{{-16}}{{t^2}}", after=s_eq, source=t_quad, indicate=False, color=VAR_COLOR, buff=0.9
        )
        s3 = self.reveal_term(r"+24t", after=s2, source=t_lin, indicate=False, color=VAR_COLOR, buff=0.9)
        self.finish_line([s1, s_eq, s2, s3])

        # --- divide every term by -16, in white; the -16 coefficient cancels, so strike it ---
        div_s1 = self.write_inverse([s1], r"\div(-16)", color=WHITE)[0]
        div_s2 = self.write_inverse([s2[0]], r"\div(-16)", color=WHITE)[0]
        strike_div = self.strike_pair(s2[0], div_s2)
        div_s3 = self.write_inverse([s3], r"\div(-16)", color=WHITE, shifts=[RIGHT * 0.3])[0]
        self.extend_current_line(div_s1, div_s2, div_s3, strike_div)

        # --- the result, reaching var^2 +/- var = # form ---
        d1 = self.reveal_term(r"t^2", after=None, source=s2[1], indicate=False, color=VAR_COLOR)
        d2 = self.reveal_term(r"-1.5t", after=d1, source=[s3, div_s3], color=VAR_COLOR)
        d_eq = self.reveal_term(r"=", after=d2, indicate=False)
        d3 = self.reveal_term(r"-0.3125", after=d_eq, source=[s1, div_s1])
        self.finish_line([d1, d2, d_eq, d3])

        # --- complete the square: add (b/2)^2 = 0.5625 to both sides, in red ---
        sq_lhs, sq_rhs = self.write_inverse(
            [d2, d3], r"+0.5625", color=SQUARE_COLOR, shifts=[LEFT * 0.4, RIGHT * 0.4]
        )
        self.extend_current_line(sq_lhs, sq_rhs)

        f1 = self.reveal_term(r"(t-0.75)^2", after=None, source=[d1, d2, sq_lhs], color=SQUARE_COLOR)
        f_eq = self.reveal_term(r"=", after=f1, indicate=False)
        f2 = self.reveal_term(r"0.25", after=f_eq, source=[d3, sq_rhs])
        self.finish_line([f1, f_eq, f2])

        # --- square root both sides, in red, with +/- ---
        sq1 = self.reveal_term(r"\sqrt{(t-0.75)^2}", after=None, source=f1, color=SQUARE_COLOR)
        sq_eq = self.reveal_term(r"=", after=sq1, indicate=False)
        sq2 = self.reveal_term(r"\pm\sqrt{0.25}", after=sq_eq, source=f2, color=SQUARE_COLOR)
        self.finish_line([sq1, sq_eq, sq2])

        ev1 = self.reveal_term(r"t-0.75", after=None, source=sq1, indicate=False)
        ev_eq = self.reveal_term(r"=", after=ev1, indicate=False)
        ev2 = self.reveal_term(r"\pm 0.5", after=ev_eq, source=sq2)
        self.finish_line([ev1, ev_eq, ev2])

        # --- isolate t: two candidate times ---
        iso_line = self.reveal_term(
            r"t = 0.75 \pm 0.5 \Rightarrow t = 0.25 \text{ or } t = 1.25",
            after=None, source=None, indicate=False,
        )
        self.finish_line([iso_line])

        # --- final answer ---
        final_line = self.reveal_term(
            r"t \approx 1.3 \text{ s}",
            after=None, source=None, indicate=False, color=ANSWER_COLOR,
        )
        self.finish_line([final_line])
        self.box_final(final_line)

        explanation = Text(
            "The ball passes h = 10 ft twice: rising at t ≈ 0.25 s, falling at t ≈ 1.25 s.\n"
            "Caught after the peak, so keep the larger time: t ≈ 1.3 s.",
            font_size=24, color=GRAY_A, line_spacing=1.2,
        )
        explanation.scale_to_fit_width(6.0)
        explanation.next_to(self._stack, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(explanation))
        self.next_slide()

    def show_picture(self):
        axes = Axes(
            x_range=[0, 1.6, 0.5],
            y_range=[0, 15, 5],
            x_length=6.2,
            y_length=4,
            axis_config={"color": WHITE, "include_tip": True},
        )
        x_label = axes.get_x_axis_label(Tex("t (sec)", font_size=28))
        y_label = axes.get_y_axis_label(Tex("h (ft)", font_size=28)).shift(LEFT * 0.3)

        curve = axes.plot(lambda t: -16 * t**2 + 24 * t + 5, x_range=[0, 1.564], color=VAR_COLOR)

        start_dot = Dot(axes.c2p(0, 5), color=WHITE)
        start_label = Text("toss: 5 ft", font_size=20, color=WHITE)
        start_label.next_to(start_dot, UR, buff=0.12)

        catch_line = DashedLine(axes.c2p(0, 10), axes.c2p(1.6, 10), color=ANSWER_COLOR, stroke_width=2)
        catch_dot = Dot(axes.c2p(1.25, 10), color=ANSWER_COLOR)
        catch_label = Text("caught: 10 ft", font_size=20, color=ANSWER_COLOR)
        catch_label.next_to(catch_dot, UR, buff=0.12)

        picture = VGroup(
            axes, x_label, y_label, curve,
            start_dot, start_label, catch_line, catch_dot, catch_label,
        )
        picture.scale(0.72).move_to(PICTURE_CENTER)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(curve))
        self.play(FadeIn(start_dot), Write(start_label))
        self.play(Create(catch_line), FadeIn(catch_dot), Write(catch_label))
        self.next_slide()
