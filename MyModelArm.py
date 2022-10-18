from Component import Component
from MyModelHead import MyModelHead
from MyModelSaber import MyModelSaber
from Point import Point
from Shapes import Cube, Sphere
import ColorType as Ct


class MyModelArm(Component):
    """
    - [x] Shoulder
    - [x] Shoulder Joint
    - [ ] Upper Arm
    - [ ] Arm Joint
    - [ ] Lower Arm
    - [ ] Hand Joint
    - [ ] Hand
    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0, left_handed: bool = True):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        joint_radius = scale * 0.3
        shoulder_joint = Sphere(Point((0, 0, 0)), shaderProg,
                                [joint_radius, joint_radius, joint_radius],
                                Ct.ColorType(69 / 255, 58 / 255, 74 / 255))
        self.addChild(shoulder_joint)
        self.componentList.append(shoulder_joint)
        self.componentDict['shoulder_joint'] = shoulder_joint

        shoulder_panel = MyModelShoulderPanel(self, Point((0, 0, 0)), shaderProg, scale=scale)
        shoulder_joint.addChild(shoulder_panel)
        if not left_handed:
            shoulder_panel.setDefaultAngle(-180, shoulder_panel.wAxis)


class MyModelShoulderPanel(Component):
    """
    - [x] Shoulder
    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # Add masking panels
        p2_clr = Ct.ColorType(0.8, 0.8, 0.8)

        thickness = scale * 0.15
        length1 = scale * 0.95
        length2 = scale * 0.85
        self.addChild(Cube(
            Point((-scale / 2 + thickness / 2 + thickness / 4, 0, 0)), shaderProg, [thickness, length2, length2], p2_clr))
        self.addChild(Cube(
            Point((thickness / 4, -length2 / 2 + thickness / 2, length2 - length1)), shaderProg, [length2, thickness, length1], p2_clr))
        self.addChild(Cube(
            Point((thickness / 4, length2 / 2 - thickness / 2, length2 - length1)), shaderProg, [length2, thickness, length1], p2_clr))
        self.addChild(Cube(
            Point((thickness / 4, 0, length2 / 2 - thickness / 2)), shaderProg, [length2, length2, thickness], p2_clr))

