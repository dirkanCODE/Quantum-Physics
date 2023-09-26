from manimgl import *

    class Example(Scene):
        def construct(self):
            sq=Square(color=BLUE,stroke_width=20)
            sq.set(height=config.frame_height-3)
            sq.rotate(30*DEGREES)
            self.add(sq)

    SCENE_TO_RENDER=Example