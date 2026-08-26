# templates/title_slide.py

from manim import *

from components.theme import BACKGROUND_COLOR, THEOREM_COLOR


class TitleSlideTemplate:
    """Mixin providing a consistent title-slide layout.

    Usage:
        class MyTitle(Slide, TitleSlideTemplate):
            def construct(self):
                self.show_title("Main Title", "Optional Subtitle")
                self.next_slide()
    """

    def show_title(self, title, subtitle=None, title_font_size=60, subtitle_font_size=36):
        self.camera.background_color = BACKGROUND_COLOR

        title_text = Text(title, font_size=title_font_size, weight=BOLD)
        group = VGroup(title_text)

        subtitle_text = None
        if subtitle:
            subtitle_text = Text(subtitle, font_size=subtitle_font_size, color=THEOREM_COLOR)
            subtitle_text.next_to(title_text, DOWN, buff=0.5)
            group.add(subtitle_text)

        group.move_to(ORIGIN)

        self.play(Write(title_text))
        if subtitle_text is not None:
            self.play(FadeIn(subtitle_text, shift=UP * 0.3))

        return group
