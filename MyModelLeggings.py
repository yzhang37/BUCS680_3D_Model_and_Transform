from MultiColorComponent import MultiColorComponent
from MyModelFoot import MyModelFoot
from Point import Point
from Shapes import Cube, Sphere, Cylinder
import ColorType as Ct


class MyModelWaist(MultiColorComponent):
    """
    Waist Part
    - [x] Waist Base
    - [x] Waist Rib Framework for Legs
    - [x] Connect to the Leg
    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.contextParent = parent

        begin_point = Cube(
            Point((0, 0, 0)), shaderProg, [scale * 0.01] * 3, Ct.GRAY)
        self.addChild(begin_point)

        waist_base_length = scale * 0.3
        waist_base_thickness = scale * 0.7
        waist_base_height = scale * 0.4
        waist_base = Cube(Point((0, 0, -waist_base_height / 2)), shaderProg, [
            waist_base_length, waist_base_thickness, waist_base_height], Ct.WHITE)
        begin_point.addChild(waist_base)
        waist_base.setRotateExtent(waist_base.uAxis, 0, 0)
        waist_base.setRotateExtent(waist_base.vAxis, 0, 0)
        waist_base.setRotateExtent(waist_base.wAxis, -180, 180)

        self.componentList.append(waist_base)
        self.componentDict['waist'] = waist_base

        # rib of the waist
        rib_length = waist_base_length * 2
        rib_thickness = waist_base_thickness * 0.1
        rib_height = waist_base_height * 0.1
        rib_part = Cube(Point((0, 0, 0)), shaderProg,
                        [rib_length, rib_thickness, rib_height], Ct.GRAY)
        waist_base.addChild(rib_part)

        rib_joint_radius = scale * 0.15
        leg_joint1 = Sphere(
            Point((rib_length / 2, 0, 0)), shaderProg,
            [rib_joint_radius, rib_joint_radius, rib_joint_radius], Ct.GRAY, limb=False)
        rib_part.addChild(leg_joint1)
        leg_joint2 = Sphere(
            Point((-rib_length / 2, 0, 0)), shaderProg,
            [rib_joint_radius, rib_joint_radius, rib_joint_radius], Ct.GRAY, limb=False)
        rib_part.addChild(leg_joint2)

        leg_right = MyModelLeg(parent, Point((0, 0, 0)), shaderProg, scale=scale, left_handed=False)
        leg_joint2.addChild(leg_right)
        leg_left = MyModelLeg(parent, Point((0, 0, 0)), shaderProg, scale=scale)
        leg_joint1.addChild(leg_left)

        self.componentList.extend(leg_right.componentList)
        self.componentList.extend(leg_left.componentList)
        for k, v in leg_right.componentDict.items():
            self.componentDict[f'right{k}'] = v
        for k, v in leg_left.componentDict.items():
            self.componentDict[f'left{k}'] = v


class MyModelLeg(MultiColorComponent):
    """
    Leg Part
    - [x] Upper Leg
    - [x] Joints between the upper and lower
    - [x] Lower Leg
    - [x] Joints between the lower and foot
    - [x] Connect to the Foot
    """
    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0, left_handed: bool = True):
        super().__init__(position, display_obj)
        self.contextParent = parent

        slight_degree = 2.5

        # upper_leg
        leg_thickness1 = scale * 0.4
        leg_thickness2 = scale * 0.4
        leg_height = scale * 1
        upper_leg = Cube(Point((0, 0, -leg_height / 2)), shaderProg,
                         [leg_thickness1, leg_thickness2, leg_height],
                         Ct.ColorType(0.85, 0.85, 0.85))
        self.addChild(upper_leg)
        self.componentList.append(upper_leg)
        self.componentDict['leg_upper'] = upper_leg
        upper_leg.setRotateExtent(upper_leg.uAxis, -110, 89)
        if not left_handed:
            upper_leg.setRotateExtent(upper_leg.vAxis, 0, 89)
            upper_leg.setDefaultAngle(slight_degree, upper_leg.vAxis)
            upper_leg.setRotateExtent(upper_leg.wAxis, -90, 0)
        else:
            upper_leg.setRotateExtent(upper_leg.vAxis, -89, 0)
            upper_leg.setDefaultAngle(-slight_degree, upper_leg.vAxis)
            upper_leg.setRotateExtent(upper_leg.wAxis, 0, 90)

        # arm joint
        cylinder_radius = scale * 0.2
        leg_joint_helper = Sphere(Point((0, 0, -leg_height / 2 - cylinder_radius / 2)), shaderProg,
                                  [cylinder_radius * 0.01] * 3,
                                  Ct.ColorType(0.7, 0.7, 0.7))
        upper_leg.addChild(leg_joint_helper)

        leg_joint_part = Cylinder(Point((0, 0, 0)), shaderProg,
                                  [cylinder_radius, cylinder_radius, leg_thickness2 / 2],
                                  Ct.ColorType(0.7, 0.7, 0.7))
        leg_joint_part.setDefaultAngle(90, leg_joint_part.vAxis)
        leg_joint_helper.addChild(leg_joint_part)

        # lower_leg
        lower_leg = Cube(Point((0, 0, -leg_height / 2 - cylinder_radius / 2)), shaderProg,
                         [leg_thickness1, leg_thickness2, leg_height],
                         Ct.ColorType(0.85, 0.85, 0.85))
        leg_joint_helper.addChild(lower_leg)
        self.componentList.append(lower_leg)
        self.componentDict['leg_lower'] = lower_leg
        lower_leg.setRotateExtent(lower_leg.uAxis, -5, 140)
        lower_leg.setRotateExtent(lower_leg.vAxis, 0, 0)
        lower_leg.setRotateExtent(lower_leg.wAxis, 0, 0)

        # leg joint part1 - part3
        joint_radius = scale * 0.15
        foot_joint1 = Sphere(Point((0, 0, -leg_height * 0.5)), shaderProg,
                             [joint_radius, joint_radius, joint_radius],
                             Ct.ColorType(69 / 255, 58 / 255, 74 / 255))
        lower_leg.addChild(foot_joint1)

        joint2_height = leg_height * 0.3
        foot_joint2 = Cube(Point((
            0, 0, -joint_radius / 2)), shaderProg,
            [leg_thickness1 * 0.2, leg_thickness2 * 0.2, joint2_height],
            Ct.ColorType(69 / 255, 58 / 255, 74 / 255))
        foot_joint1.addChild(foot_joint2)

        foot_joint3 = Sphere(Point((0, 0, -joint2_height + joint_radius / 2)), shaderProg,
                             [joint_radius, joint_radius, joint_radius],
                             Ct.ColorType(69 / 255, 58 / 255, 74 / 255))
        foot_joint2.addChild(foot_joint3)

        # add the foot
        foot_part = MyModelFoot(parent, Point((0, 0, 0)), shaderProg, scale=scale * 0.5)
        foot_joint3.addChild(foot_part)
        if not left_handed:
            foot_part.setDefaultAngle(-slight_degree, upper_leg.vAxis)
        else:
            foot_part.setDefaultAngle(slight_degree, upper_leg.vAxis)
        self.componentList.append(foot_part)
        self.componentDict['foot'] = foot_part
        foot_part.setRotateExtent(foot_part.uAxis, -45, 45)
        foot_part.setRotateExtent(foot_part.vAxis, -45, 45)
        foot_part.setRotateExtent(foot_part.wAxis, -90, 90)
