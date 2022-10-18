from Component import Component
from MyModelHead import MyModelHead
from Point import Point
from Shapes import Cylinder, Sphere
import ColorType as Ct


class MyModelSaber(Component):
    """
    - [x] Saber Slot (Sphere)
    - [ ] Saber (Cylinder)
    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # define saber slot
        saber_slot_radius = scale
        saber_slot = Sphere(Point((0, 0, 0)), shaderProg,
                            [saber_slot_radius, saber_slot_radius, saber_slot_radius], Ct.GRAY, limb=False)
        self.addChild(saber_slot)
        self.componentList.append(saber_slot)
        self.componentDict['joint'] = saber_slot

        # define saber
        saber_radius = saber_slot_radius * 0.4
        saber_length = saber_slot_radius * 3.5
        saber = Cylinder(Point((0, 0, saber_length)), shaderProg,
                         [saber_radius, saber_radius, saber_length],
                         Ct.ColorType(0.8, 0.8, 0.8))
        saber_slot.addChild(saber)
