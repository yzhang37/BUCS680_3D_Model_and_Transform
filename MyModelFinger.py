from MultiColorComponent import MultiColorComponent
from Point import Point
import ColorType as Ct
from Shapes import Cylinder, Cube, Sphere


class MyModelFinger(MultiColorComponent):
    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0, finger_radius=0.05, finger_height=0.15, finger_nums=3):
        super().__init__(position, display_obj)
        self.components = []
        self.contextParent = parent

        radius = finger_radius * scale
        length = finger_height * scale

        color_medium_gray = Ct.ColorType(0.2, 0.2, 0.2)
        joint_helper = Cube(Point((0, 0, 0)), shaderProg, [scale * 0.01] * 3, color_medium_gray)
        self.addChild(joint_helper)

        first_finger = Cylinder(Point((0, 0, length / 2)), shaderProg, [radius, radius, length])
        first_finger.setDefaultColor(color_medium_gray)
        joint_helper.addChild(first_finger)
        self.components.append(first_finger)

        if finger_nums > 1:
            parent_finger = first_finger
            for i in range(finger_nums - 1):
                joint_helper = Sphere(Point((0, 0, length)), shaderProg, [radius * 1.2] * 3, color_medium_gray, limb=False)
                parent_finger.addChild(joint_helper)
                curr_finger = Cylinder(Point((0, 0, length / 2 + radius * 0.5)), shaderProg, [radius, radius, length])
                curr_finger.setDefaultColor(color_medium_gray)
                joint_helper.addChild(curr_finger)
                self.components.append(curr_finger)
                parent_finger = curr_finger

    def setPartRotateExtent(self, index, axis, min_deg: float = None, max_deg: float = None):
        curr_comp = self.components[index]
        if axis == 0:
            curr_comp.setRotateExtent(curr_comp.uAxis, min_deg, max_deg)
        elif axis == 1:
            curr_comp.setRotateExtent(curr_comp.vAxis, min_deg, max_deg)
        elif axis == 2:
            curr_comp.setRotateExtent(curr_comp.wAxis, min_deg, max_deg)
