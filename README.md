# Math Presentations

Manim + [manim-slides](https://github.com/jeertmans/manim-slides) presentations for math classes, built one slide-file at a time and stitched into full lesson decks.

## Layout

```
components/    Shared low-level constants (colors, background) - components/theme.py
templates/     Reusable Scene mixins (TitleSlideTemplate, WorkedExampleTemplate, ...)
precalc/       One folder per unit (e.g. order_of_operations/), each holding small
ap-precalc/    Scene files for that unit. Keep each file to a handful of related
               slides so it's easy to workshop in isolation.
presentations/ Combined lesson decks produced by build_course.py
published/     Finished decks ready to hand out / present
assets/        Shared images, logos, etc.
```

A "slide file" is a normal manim-slides `Slide` subclass. Mix in the templates from
`templates/` for anything that should look consistent across the whole course
(titles, worked examples). Import shared colors from `components.theme` rather than
hardcoding manim color constants, per `AGENTS.md` / `STYLE_GUIDE.md`.

## Workflow

1. **Write one slide file** under `precalc/<unit>/`, using `Slide` plus whichever
   template mixin fits (see `templates/worked_example.py` for the worked-example
   pattern used in `precalc/order_of_operations/practice_69_70.py`).
2. **Render and workshop it on its own:**
   ```
   python build_slide.py precalc/order_of_operations/practice_69_70.py Practice69And70 --present
   ```
   `--present` opens manim-slides' interactive click-through presenter so you can
   check the step-by-step pacing before wiring it into a full lesson.
3. **Combine finished scenes into one lesson deck:**
   ```
   python build_course.py precalc/order_of_operations \
       ClearingParenthesesTitle Practice69And70 NestedAbsoluteValuePractice \
       --out order_of_operations_lesson2.html
   ```
   This runs `manim-slides convert` over the already-rendered scenes (render them
   with `build_slide.py` first) and writes the combined deck to `presentations/`.

Both scripts inject the repo root onto `PYTHONPATH`, so any slide file can do
`from components.theme import ...` / `from templates.worked_example import ...`
regardless of which unit folder it lives in. If you ever invoke `manim` /
`manim-slides` directly instead of through these scripts, run it with
`PYTHONPATH=$(pwd)` from the repo root first.

## Known issue

`precalc/order_of_operations/order_of_operations_intro.py` is a known-broken
slide file — leave it as-is for now rather than debugging it.
