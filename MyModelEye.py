from Component import Component
from Point import Point
import ColorType as Ct
from Shapes import Sphere


class MyModelEye(Component):
    """
    Define the eye and eyeball.
    """

    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # Define eye and eyeball
        eye_radius = 0.2 * scale
        eye_thickness = 0.75 * eye_radius

        eye = Sphere(position, shaderProg, [eye_radius, eye_thickness, eye_radius],
                     Ct.ColorType(217 / 255, 166 / 255, 82 / 255))

        eyeball_radius = 0.5 * eye_radius
        eyeball_thickness = eye_thickness / 3
        eyeball = Sphere(Point((0, -0.8 * eye_thickness, 0)), shaderProg,
                         [eyeball_radius, eyeball_thickness, eyeball_radius], Ct.BLACK)
        eyeball.setRotateExtent(eyeball.uAxis, -35, 35)
        eyeball.setRotateExtent(eyeball.vAxis, 0, 0)
        eyeball.setRotateExtent(eyeball.wAxis, -35, 35)

        self.addChild(eye)
        eye.addChild(eyeball)
        eye.setDefaultAngle(-90, eye.uAxis)

        self.componentList.append(eyeball)
        self.componentDict['eyeball'] = eyeball
