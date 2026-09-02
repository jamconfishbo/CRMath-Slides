from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR


class PracticeListLinearEquations(Slide):
    """Slide displaying practice problems a, b, c with a 3-minute countdown."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Practice Problems", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        label_a = MathTex(r"\textbf{a)}", font_size=44)
        prob_a = MathTex(r"4x+1-x=6x-2", font_size=44)
        group_a = VGroup(label_a, prob_a).arrange(RIGHT, buff=0.5)

        label_b = MathTex(r"\textbf{b)}", font_size=44)
        prob_b = MathTex(r"2(-5x-1)=2x-12x+6", font_size=44)
        group_b = VGroup(label_b, prob_b).arrange(RIGHT, buff=0.5)

        label_c = MathTex(r"\textbf{c)}", font_size=44)
        prob_c = MathTex(r"2(3x-1)=6(x+1)-8", font_size=44)
        group_c = VGroup(label_c, prob_c).arrange(RIGHT, buff=0.5)

        problems_group = VGroup(group_a, group_b, group_c)
        problems_group.arrange(DOWN, buff=1.0, aligned_edge=LEFT)
        problems_group.move_to(ORIGIN).shift(LEFT * 2)

        self.play(FadeIn(title, shift=UP), FadeIn(problems_group))
        self.next_slide()

        time_total = 180
        time_tracker = ValueTracker(time_total)

        def get_time_string(seconds):
            mins, secs = divmod(int(seconds), 60)
            return f"{mins:02d}:{secs:02d}"

        timer_text = always_redraw(
            lambda: Text(
                get_time_string(time_tracker.get_value()),
                font="monospace",
                font_size=48,
            ).to_edge(RIGHT, buff=1).shift(UP * 2)
        )

        timer_bar_bg = Rectangle(height=6, width=0.5, color=GRAY, fill_opacity=0.3).next_to(timer_text, DOWN, buff=0.5)
        timer_bar = always_redraw(
            lambda: Rectangle(
                height=6 * (time_tracker.get_value() / time_total),
                width=0.5,
                color=BLUE,
                fill_opacity=0.8,
            ).move_to(timer_bar_bg, aligned_edge=DOWN)
        )

        self.play(FadeIn(timer_text), FadeIn(timer_bar_bg), FadeIn(timer_bar))
        self.next_slide()

        self.play(
            time_tracker.animate.set_value(0),
            run_time=time_total,
            rate_func=linear,
        )

        time_up_text = Text("Time's Up!", font_size=48, color=RED).move_to(timer_text)
        self.play(Transform(timer_text, time_up_text), FadeOut(timer_bar))
