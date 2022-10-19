from MultiColorComponent import MultiColorComponent
from Point import Point
import ColorType as Ct
from Shapes import Cylinder


class MyModelFinger(MultiColorComponent):
    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0, finger_radius=0.05, finger_height=0.15, finger_nums=3):
        super().__init__(position, display_obj)
        self.components = []
        self.contextParent = parent

        color_medium_gray = Ct.ColorType(80 / 255, 62 / 255, 89 / 255)
        finger0 = Cylinder(Point((0, 0, 0)), shaderProg, [
            finger_radius * scale, finger_radius * scale, finger_height * scale])
        finger0.setDefaultColor(color_medium_gray)
        self.addChild(finger0)
        self.components.append(finger0)

        if finger_nums > 1:
            parent_finger = finger0
            for i in range(finger_nums - 1):
                curr_finger = Cylinder(Point((
                    0, 0, finger_height * scale)), shaderProg, [
                    finger_radius* scale, finger_radius * scale, finger_height * scale])
                curr_finger.setDefaultColor(color_medium_gray)
                parent_finger.addChild(curr_finger)
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
