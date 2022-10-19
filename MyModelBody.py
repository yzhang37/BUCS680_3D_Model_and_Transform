from MultiColorComponent import MultiColorComponent
from MyModelArm import MyModelArm
from MyModelHead import MyModelHead
from MyModelSaber import MyModelSaber
from MyModelLeggings import MyModelWaist
from Point import Point
from Shapes import Cube, Sphere, Cone
import ColorType as Ct


class MyModelBody(MultiColorComponent):
    """
    Body Part
    - [x] Main Body
    - [x] Connect the head
    - [x] Jetpack
    - [x] Saber Slot
    - [x] Sabers
    - [x] Shoulder Part

    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.contextParent = parent

        # define body
        body1_length = scale * 0.8
        body1_thickness = scale * 0.6
        body1_height = scale * 0.9
        body_part_1 = Cube(Point((0, 0, 0)), shaderProg,
                           [body1_length, body1_thickness, body1_height], Ct.RED)
        self.addChild(body_part_1)

        body2_length = body1_length * 1.2
        body2_thickness = body1_thickness * 1.2
        body2_height = body1_height * 0.6
        body_part_2 = Cube(Point((0, 0, body1_height / 2 - body2_height / 3)), shaderProg,
                           [body2_length, body2_thickness, body2_height], Ct.BLUE)
        self.addChild(body_part_2)

        # define neck_platform and chest
        neck_platform_length = body2_length * 0.4
        neck_platform_thickness = body2_thickness * 1.1
        neck_platform_height = body2_length * 0.1

        body_3_helper = Cube(Point((0, -body1_thickness * 0.4, body1_height * 0.08)), shaderProg, [neck_platform_length * 0.001] * 3, Ct.BLUE)
        self.addChild(body_3_helper)

        body3_height = body2_height * 1.41
        body_part_3 = Cube(Point((
            0, 0, 0)), shaderProg, [neck_platform_length * 0.8, neck_platform_thickness * 0.7, body3_height],
            Ct.BLUE)
        body_part_3.setDefaultAngle(35, body_part_3.uAxis)
        body_3_helper.addChild(body_part_3)
        body4_height = body2_thickness * 0.5
        body4_thickness = body2_height * 0.7
        body_part_4 = Cube(Point((0, 0, body3_height / 2 - body4_height / 2)),
                           shaderProg, [body2_length, body4_thickness, body4_height],
                           Ct.BLUE)
        body_part_3.addChild(body_part_4)
        # two outlets control
        outlet1 = MyModelOutlet(self, Point(
            (-body2_length / 2 + 0.18 * scale,
             -body4_thickness * 0.48, 0)), shaderProg, scale=0.28 * scale)
        body_part_4.addChild(outlet1)
        outlet2 = MyModelOutlet(self, Point(
            (body2_length / 2 - 0.18 * scale,
             -body4_thickness * 0.48, 0)), shaderProg, scale=0.28 * scale)
        body_part_4.addChild(outlet2)

        color_gundam_yellow = Ct.ColorType(217 / 255, 166 / 255, 82 / 255)

        neck_platform = Cube(Point((0, 0, body2_height / 2 - neck_platform_height * 0.48)), shaderProg,
                             [neck_platform_length, neck_platform_thickness, neck_platform_height],
                             color_gundam_yellow)
        body_part_2.addChild(neck_platform)

        # Connect the neck
        head_neck_part = MyModelHead(self,
                                     Point((0, 0, neck_platform_height * 0.95)),
                                     shaderProg, scale=scale * 0.5)
        neck_platform.addChild(head_neck_part)
        self.componentList.extend(head_neck_part.componentList)
        for key, value in head_neck_part.componentDict.items():
            self.componentDict[f'head_{key}'] = value

        # Jetpack
        color_medium_gray = Ct.ColorType(80 / 255, 62 / 255, 89 / 255)
        color_deep_gray = Ct.ColorType(69 / 255, 58 / 255, 74 / 255)
        jetpack_length = body1_length * 0.9
        jetpack_thickness = body2_thickness * 0.4
        jetpack_height = body1_height * 0.8
        jetpack = Cube(Point((0, body1_thickness / 2 + jetpack_thickness / 2,
                              body1_height / 2 - jetpack_height * 0.48)), shaderProg,
                       [jetpack_length, jetpack_thickness, jetpack_height],
                       color_medium_gray)
        body_part_1.addChild(jetpack)

        # add two connection points of jet
        jet_joint_left = Sphere(Point((
            jetpack_length / 4, jetpack_thickness / 2, -jetpack_height / 2)),
            shaderProg, [jetpack_length * 0.08] * 3, color_deep_gray)
        jetpack.addChild(jet_joint_left)
        jet_joint_right = Sphere(Point((
            -jetpack_length / 4, jetpack_thickness / 2, -jetpack_height / 2)),
            shaderProg, [jetpack_length * 0.08] * 3, color_deep_gray)
        jetpack.addChild(jet_joint_right)
        jet_left = MyModelJet(self, Point((0, 0, 0)), shaderProg, scale=scale * 0.2)
        jet_joint_left.addChild(jet_left)
        jet_right = MyModelJet(self, Point((0, 0, 0)), shaderProg, scale=scale * 0.2)
        jet_joint_right.addChild(jet_right)
        for j, p in zip((jet_left, jet_right), ("left", "right")):
            j.setDefaultAngle(45, j.uAxis)
            self.componentList.append(j)
            self.componentDict[f'{p}_jet'] = j
            j.setRotateExtent(j.uAxis, 0, 89)
            j.setRotateExtent(j.vAxis, -45, 45)
            j.setRotateExtent(j.wAxis, 0, 0)

    # Saber Slot
        saber_slot_size = scale * 0.1
        slot1 = Sphere(
            Point((
                -jetpack_length / 2 + saber_slot_size * 0.8,
                jetpack_thickness / 4 - saber_slot_size / 2,
                jetpack_height / 2)),
            shaderProg,
            [saber_slot_size, saber_slot_size, saber_slot_size],
            color_deep_gray)
        jetpack.addChild(slot1)
        slot2 = Sphere(
            Point((
                jetpack_length / 2 - saber_slot_size * 0.8,
                jetpack_thickness / 4 - saber_slot_size / 2,
                jetpack_height / 2)),
            shaderProg,
            [saber_slot_size, saber_slot_size, saber_slot_size],
            color_deep_gray)
        jetpack.addChild(slot2)

        right_saber = MyModelSaber(self, Point((0, 0, 0)), shaderProg, scale=saber_slot_size)
        slot1.addChild(right_saber)
        left_saber = MyModelSaber(self, Point((0, 0, 0)), shaderProg, scale=saber_slot_size)
        slot2.addChild(left_saber)
        self.componentList.extend(right_saber.componentList)
        self.componentList.extend(left_saber.componentList)
        for key, value in right_saber.componentDict.items():
            self.componentDict[f'right_saber_{key}'] = value
        for key, value in left_saber.componentDict.items():
            self.componentDict[f'left_saber_{key}'] = value

        right_saber_joint = self.componentDict[f'right_saber_saber']
        left_saber_joint = self.componentDict[f'left_saber_saber']

        right_saber_joint.setDefaultAngle(-20, right_saber_joint.vAxis)
        right_saber_joint.setRotateExtent(right_saber_joint.uAxis, -50, 20)
        right_saber_joint.setRotateExtent(right_saber_joint.vAxis, -80, 20)
        right_saber_joint.setRotateExtent(right_saber_joint.wAxis, 0, 0)

        left_saber_joint.setDefaultAngle(20, left_saber_joint.vAxis)
        left_saber_joint.setRotateExtent(left_saber_joint.uAxis, -50, 20)
        left_saber_joint.setRotateExtent(left_saber_joint.vAxis, -20, 80)
        left_saber_joint.setRotateExtent(right_saber_joint.wAxis, 0, 0)

        # rib framework
        rib_length = body2_length * 1.5
        rib_thickness = body1_thickness * 0.1
        rib_height = body1_height * 0.1
        rib_part = Cube(Point((0, 0, 0)), shaderProg,
                        [rib_length, rib_thickness, rib_height], Ct.GRAY)
        body_part_2.addChild(rib_part)

        shoulder_slot1 = Sphere(
            Point((rib_length / 2, 0, 0)), shaderProg,
            [saber_slot_size, saber_slot_size, saber_slot_size], Ct.GRAY)
        rib_part.addChild(shoulder_slot1)
        shoulder_slot2 = Sphere(
            Point((-rib_length / 2, 0, 0)), shaderProg,
            [saber_slot_size, saber_slot_size, saber_slot_size], Ct.GRAY)
        rib_part.addChild(shoulder_slot2)

        # shoulder connection
        left_arm = MyModelArm(self, Point((0, 0, 0)), shaderProg, scale=scale * 0.5, left_handed=True)
        shoulder_slot1.addChild(left_arm)
        right_arm = MyModelArm(self, Point((0, 0, 0)), shaderProg, scale=scale * 0.5, left_handed=False)
        shoulder_slot2.addChild(right_arm)
        self.componentList.extend(right_arm.componentList)
        self.componentList.extend(left_arm.componentList)
        for key, value in right_arm.componentDict.items():
            self.componentDict[f'right_arm_{key}'] = value
        for key, value in left_arm.componentDict.items():
            self.componentDict[f'left_arm_{key}'] = value

        # waist connection
        waist_joint = Sphere(
            Point((0, 0, -body1_height / 2)), shaderProg,
            [saber_slot_size, saber_slot_size, saber_slot_size], Ct.GRAY)
        body_part_1.addChild(waist_joint)

        waist_part = MyModelWaist(self, Point((0, 0, 0)), shaderProg, scale=scale)
        waist_joint.addChild(waist_part)
        self.componentList.extend(waist_part.componentList)
        self.componentDict.update(waist_part.componentDict)


class MyModelOutlet(MultiColorComponent):
    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.contextParent = parent

        num = 4
        r_bgn, g_bgn, b_bgn = [180 / 255, 146 / 255, 90 / 255]
        r_end, g_end, b_end = [217 / 255, 166 / 255, 82 / 255]
        for i in range(num):
            height = - scale * 2 / num + scale / num * i
            t = i / (num - 1)
            self.addChild(
                Cube(Point((0, 0, height)), shaderProg, [scale, scale / 2, scale * 0.05],
                     Ct.ColorType((1 - t) * r_bgn + t * r_end,
                                  (1 - t) * g_bgn + t * g_end,
                                  (1 - t) * b_bgn + t * b_end)))


class MyModelJet(MultiColorComponent):
    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.contextParent = parent

        num = 4
        color_deep_gray = Ct.ColorType(69 / 255, 58 / 255, 74 / 255)
        cone_height = 0.5 * scale

        # the cone of the jet
        base_cone = Cone(
            Point((0, 0, -cone_height * 0.45)), shaderProg, [cone_height] * 3,
            color_deep_gray)
        self.register_color(base_cone, 'base_cone', color_deep_gray)
        self.addChild(base_cone)

        # add fire
        fire_length = cone_height * 6
        fire = Sphere(
            Point((
                0, 0, -fire_length)), shaderProg, [
                cone_height, cone_height, fire_length],
            Ct.ColorType(57 / 255, 209 / 255, 209 / 255))
        base_cone.addChild(fire)
