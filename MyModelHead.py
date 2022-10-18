from Component import Component
from MyModelEye import MyModelEye
from Point import Point
import ColorType as Ct
from Shapes import Sphere, Cube, Cylinder, Cone


class MyModelHead(Component):
    """
    Define the head part.
    - [x] Faces
    - [x] Eyes
    - [x] Chin
    - [x] horns
    """

    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # define neck
        neck_radius = 0.2 * scale
        neck_length = 0.35 * scale
        neck_part = Cylinder(position, shaderProg, [neck_radius, neck_radius, neck_length], Ct.GRAY)
        neck_part.setRotateExtent(neck_part.uAxis, 0, 0)
        neck_part.setRotateExtent(neck_part.vAxis, 0, 0)
        neck_part.setRotateExtent(neck_part.wAxis, -80, 80)
        self.addChild(neck_part)
        self.componentList.append(neck_part)
        self.componentDict['head_neck'] = neck_part

        # define the square head
        head_length = scale * 0.8
        head_thickness = scale * 0.7
        head_height = scale * 0.9
        head_part = Cube(Point((0, 0, neck_length)), shaderProg,
                         [head_length, head_thickness, head_height],
                         Ct.ColorType(0.88, 0.88, 0.88))
        neck_part.addChild(head_part)

        # define the horn
        hb_length = scale * 0.2
        hb_thickness = scale * 0.12
        hb_height = scale * 0.2
        horn_base_part = Cube(Point((0,
                                     -head_thickness / 2 - hb_thickness * 0.25,
                                     head_height / 2 - hb_height * 0.25)), shaderProg,
                              [hb_length, hb_thickness, hb_height], Ct.RED)
        head_part.addChild(horn_base_part)

        horn_diameter = hb_thickness * 0.5
        horn_length = scale * 0.3
        horn_1 = Cone(Point((0, 0, horn_length)),
                      shaderProg, [horn_diameter, horn_diameter, horn_length],
                      Ct.ColorType(0.92, 0.92, 0.92), True)
        horn_1.setDefaultAngle(-55, horn_1.vAxis)
        horn_base_part.addChild(horn_1)
        horn_2 = Cone(Point((0, 0, horn_length)),
                      shaderProg, [horn_diameter, horn_diameter, horn_length],
                      Ct.ColorType(0.92, 0.92, 0.92), True)
        horn_2.setDefaultAngle(55, horn_2.vAxis)
        horn_base_part.addChild(horn_2)

        # Chin part
        chin_length = scale * 0.2
        chin_thickness = scale * 0.15
        chin_height = scale * 0.3
        chin_part = Cube(Point((0,
                                -head_thickness / 2,
                                -head_height / 2 + chin_height * 0.15)),
                         shaderProg,
                         [chin_length, chin_thickness, chin_height], Ct.RED)
        head_part.addChild(chin_part)

        # eyes
        eye_scale = head_length * 0.15
        eye1 = MyModelEye(self, Point((head_length * 0.12,
                                       -head_thickness * 0.29 + eye_scale * 0.3,
                                       head_height * 0.08)),
                          shaderProg, scale=eye_scale,
                          eye_color=Ct.BLACK,
                          eyeball_color=Ct.ColorType(217 / 255, 166 / 255, 82 / 255))
        head_part.addChild(eye1)
        eye2 = MyModelEye(self, Point((-head_length * 0.12,
                                       -head_thickness * 0.29 + eye_scale * 0.3,
                                       head_height * 0.08)),
                          shaderProg, scale=eye_scale,
                          eye_color=Ct.BLACK,
                          eyeball_color=Ct.ColorType(217 / 255, 166 / 255, 82 / 255))
        head_part.addChild(eye2)

        self.componentList.extend(eye2.componentList)
        for key, value in eye2.componentDict.items():
            self.componentDict[f'right_{key}'] = value
        self.componentList.extend(eye1.componentList)
        for key, value in eye1.componentDict.items():
            self.componentDict[f'left_{key}'] = value
