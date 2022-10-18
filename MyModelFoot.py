import ColorType as Ct
from MultiColorComponent import MultiColorComponent
from Point import Point
from Shapes import Cube


class MyModelFoot(MultiColorComponent):
    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.setDefaultColor(Ct.BLACK)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # add red bottom
        foot_bottom_length = scale * 1
        foot_bottom_thickness = scale * 2
        foot_bottom_height = scale * 0.3
        foot_bottom = Cube(Point((
            0, -foot_bottom_thickness / 4, -foot_bottom_height / 2)), shaderProg, [
            foot_bottom_length, foot_bottom_thickness, foot_bottom_height], Ct.RED)
        self.addChild(foot_bottom)

        # add inner bottom
        inner_bottom_length = scale * 0.8
        inner_bottom_thickness = scale * 1.5
        inner_bottom_height = scale * 0.2
        inner_bottom = Cube(Point((
            0, -inner_bottom_thickness / 4, inner_bottom_height / 2)), shaderProg, [
            inner_bottom_length, inner_bottom_thickness, inner_bottom_height],
            Ct.ColorType(0.85, 0.85, 0.85))
        self.addChild(inner_bottom)


class MyModelShoeCover(MultiColorComponent):
    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0, left_handed: bool = True):
        super().__init__(position, display_obj)
        self.setDefaultColor(Ct.BLACK)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent
