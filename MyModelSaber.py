from Component import Component
from MyModelHead import MyModelHead
from Point import Point
from Shapes import Cylinder, Sphere
import ColorType as Ct


class MyModelSaber(Component):
    """
    - [x] Saber Slot (Sphere)
    - [x] Saber (Cylinder)
    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # define saber
        saber_radius = scale * 0.4
        saber_length = scale * 3.5
        saber = Cylinder(Point((0, 0, saber_length)), shaderProg,
                         [saber_radius, saber_radius, saber_length],
                         Ct.ColorType(0.8, 0.8, 0.8))
        self.addChild(saber)
        self.componentList.append(saber)
        self.componentDict['saber'] = saber
