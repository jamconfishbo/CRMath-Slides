from manim import *
from manim_slides import Slide

from components.theme import BACKGROUND_COLOR
from templates.relations_functions import RelationsFunctionsTemplate
from templates.frequency_table import FrequencyTableTemplate


class GroupWork(Slide, RelationsFunctionsTemplate, FrequencyTableTemplate):
    """Final slide: group-work problem list, page 42."""

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        problems = [9, 10, 12, 15, 16, 18, 21, 22, 23, 24, 27, 28, 29, 31, 32]
        heading, page, grid = self.group_work_slide(page_number=42, problems=problems, cols=5)

        self.show_timer(600, position=np.array([0, -2.4, 0]), bar_height=1.6)
