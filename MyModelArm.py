from Component import Component
from MyModelHead import MyModelHead
from MyModelSaber import MyModelSaber
from Point import Point
from Shapes import Cube, Sphere, Cylinder
import ColorType as Ct


class MyModelArm(Component):
    """
    - [x] Shoulder
    - [x] Shoulder Joint
    - [x] Upper Arm
    - [x] Arm Joint
    - [x] Lower Arm
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
        # self.componentList.append(shoulder_joint)
        # self.componentDict['shoulder_joint'] = shoulder_joint
        # if not left_handed:
        #
        # else:
        # shoulder_joint.setRotateExtent(shoulder_joint.wAxis, 0, 0)

        shoulder_panel = MyModelShoulderPanel(self, Point((0, 0, 0)), shaderProg, scale=scale)
        self.addChild(shoulder_panel)
        self.componentList.append(shoulder_panel)
        self.componentDict['shoulder_panel'] = shoulder_panel
        shoulder_panel.setRotateExtent(shoulder_panel.uAxis, -180, 180)
        shoulder_panel.setRotateExtent(shoulder_panel.vAxis, 0, 0)
        if not left_handed:
            shoulder_panel.setDefaultAngle(-180, shoulder_panel.wAxis)
            shoulder_panel.setRotateExtent(shoulder_panel.wAxis, -180, -180)
        else:
            shoulder_panel.setRotateExtent(shoulder_panel.wAxis, 0, 0)

        # upper arm that can rotate w-axis
        arm_thickness1 = scale * 0.55
        arm_thickness2 = scale * 0.4
        upper_arm_height = scale * 0.9
        upper_arm = Cube(Point((0, 0, -upper_arm_height / 2)), shaderProg,
                         [arm_thickness1, arm_thickness2, upper_arm_height],
                         Ct.ColorType(0.85, 0.85, 0.85))
        shoulder_joint.addChild(upper_arm)
        self.componentList.append(upper_arm)
        self.componentDict['upper_arm'] = upper_arm
        upper_arm.setRotateExtent(upper_arm.uAxis, -180, 180)
        if not left_handed:
            upper_arm.setRotateExtent(upper_arm.vAxis, -10, 95)
        else:
            upper_arm.setRotateExtent(upper_arm.vAxis, -95, 10)

        # arm joint
        hidden_joint_radius = joint_radius * 1.2
        arm_joint_helper = Sphere(Point((0, 0, -upper_arm_height / 2 - hidden_joint_radius / 2)), shaderProg,
                                [joint_radius * 0.01, joint_radius * 0.01, joint_radius * 0.01],
                                Ct.ColorType(0.7, 0.7, 0.7))
        upper_arm.addChild(arm_joint_helper)

        arm_joint_part = Cylinder(Point((0, 0, 0)), shaderProg,
                                  [joint_radius, joint_radius, arm_thickness1 / 2],
                                  Ct.ColorType(0.7, 0.7, 0.7))
        arm_joint_part.setDefaultAngle(90, arm_joint_part.vAxis)
        arm_joint_helper.addChild(arm_joint_part)

        lower_arm = Cube(Point((0, 0, -upper_arm_height / 2 - hidden_joint_radius / 2)), shaderProg,
                         [arm_thickness1, arm_thickness2, upper_arm_height],
                         Ct.ColorType(0.85, 0.85, 0.85))
        arm_joint_helper.addChild(lower_arm)
        self.componentList.append(lower_arm)
        self.componentDict['lower_arm'] = lower_arm
        lower_arm.setRotateExtent(lower_arm.uAxis, -180, 90)
        lower_arm.setRotateExtent(lower_arm.vAxis, 0, 0)
        lower_arm.setRotateExtent(lower_arm.wAxis, 0, 0)


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
            Point((-scale / 2 + thickness / 2 + thickness / 4, 0, 0)), shaderProg, [thickness, length2, length2],
            p2_clr))
        self.addChild(Cube(
            Point((thickness / 4, -length2 / 2 + thickness / 2, length2 - length1)), shaderProg,
            [length2, thickness, length1], p2_clr))
        self.addChild(Cube(
            Point((thickness / 4, length2 / 2 - thickness / 2, length2 - length1)), shaderProg,
            [length2, thickness, length1], p2_clr))
        self.addChild(Cube(
            Point((thickness / 4, 0, length2 / 2 - thickness / 2)), shaderProg, [length2, length2, thickness], p2_clr))
