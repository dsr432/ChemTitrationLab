from manim import *
import math 

class Full(Scene):
    def construct(self):
        SquareToCircle.construct(self)
        SpreadSheet.construct(self)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(Create(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(FadeOut(circle))

class SpreadSheet(Scene):
    def construct (self):
        text = TextMobject("lol")

        self.add(text)
#C://Dev/python/chemlab> manim -p start.py SquareToCircle