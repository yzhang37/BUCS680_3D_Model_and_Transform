from Component import Component
from Point import Point
from Shapes import Cube, Sphere
import ColorType as Ct


class MyModelWaist(Component):
    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
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
