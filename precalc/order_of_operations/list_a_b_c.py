
from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR


class PracticeProblemsList(Slide):
    """Slide displaying all three practice problems with a 5-minute countdown."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # Title
        title = Text("Practice Problems", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # Problem A
        label_a = MathTex(r"\textbf{a)}", font_size=44)
        prob_a = MathTex(r"30 - 24 \div (4^2 \div 2^2 \cdot 3)", font_size=44)
        group_a = VGroup(label_a, prob_a).arrange(RIGHT, buff=0.5)
        
        # Problem B
        label_b = MathTex(r"\textbf{b)}", font_size=44)
        prob_b = MathTex(r"15 - \left[ -4 + 2 \left[ (2 - 5)^2 - 4 \right] \right]", font_size=44)
        group_b = VGroup(label_b, prob_b).arrange(RIGHT, buff=0.5)
        
        # Problem C
        label_c = MathTex(r"\textbf{c)}", font_size=44)
        prob_c = MathTex(r"12 - \left[ 3(2y+5) - 4(y-3) \right] - 5", font_size=44)
        group_c = VGroup(label_c, prob_c).arrange(RIGHT, buff=0.5)

        # Arrange all problems vertically
        problems_group = VGroup(group_a, group_b, group_c)
        problems_group.arrange(DOWN, buff=1.0, aligned_edge=LEFT)
        # Shift slightly left to make room for the timer on the right
        problems_group.move_to(ORIGIN).shift(LEFT * 2)

        # Show title and all problems at once
        self.play(
            FadeIn(title, shift=UP),
            FadeIn(problems_group)
        )
        self.next_slide()

        # Timer setup (5 minutes = 300 seconds)
        time_total = 300
        time_tracker = ValueTracker(time_total)

        def get_time_string(seconds):
            mins, secs = divmod(int(seconds), 60)
            return f"{mins:02d}:{secs:02d}"

        # Timer Text
        timer_text = always_redraw(
            lambda: Text(
                get_time_string(time_tracker.get_value()), 
                font="monospace", 
                font_size=48
            ).to_edge(RIGHT, buff=1).shift(UP * 2)
        )

        # Timer Bar (visual indicator)
        timer_bar_bg = Rectangle(height=6, width=0.5, color=GRAY, fill_opacity=0.3).next_to(timer_text, DOWN, buff=0.5)
        timer_bar = always_redraw(
            lambda: Rectangle(
                height=6 * (time_tracker.get_value() / time_total), 
                width=0.5, 
                color=BLUE, 
                fill_opacity=0.8
            ).move_to(timer_bar_bg, aligned_edge=DOWN)
        )

        # Show the timer
        self.play(FadeIn(timer_text), FadeIn(timer_bar_bg), FadeIn(timer_bar))
        self.next_slide() # Wait for you to press 'next' to start the timer

        # Run the countdown
        # Note: In a real presentation, a 5-minute animation might make the video file huge.
        # run_time=300 plays it in real-time. If you want to compress the video generation time, 
        # but keep it 5 minutes in presentation mode, you might need external tools, but this is 
        # how you do it natively in Manim.
        self.play(
            time_tracker.animate.set_value(0),
            run_time=time_total,
            rate_func=linear
        )
        
        # Optional: visual cue that time is up
        time_up_text = Text("Time's Up!", font_size=48, color=RED).move_to(timer_text)
        self.play(Transform(timer_text, time_up_text), FadeOut(timer_bar))