from MultiColorComponent import MultiColorComponent
from Point import Point
import ColorType as Ct
from Shapes import Sphere


class MyModelEye(MultiColorComponent):
    """
    Define the eye and eyeball.
    """

    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0, eye_color=Ct.WHITE, eyeball_color=Ct.BLACK):
        super().__init__(position, display_obj)
        self.setDefaultColor(Ct.BLACK)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # Define eye and eyeball
        eye_radius = scale
        eye_thickness = 0.75 * eye_radius

        eye = Sphere(position, shaderProg, [eye_radius, eye_thickness, eye_radius], eye_color)

        eyeball_radius = 0.5 * eye_radius
        eyeball_thickness = eye_thickness / 3
        eyeball = Sphere(Point((0, -0.8 * eye_thickness, 0)), shaderProg,
                         [eyeball_radius, eyeball_thickness, eyeball_radius], eyeball_color)
        eyeball.setRotateExtent(eyeball.uAxis, -35, 35)
        eyeball.setRotateExtent(eyeball.vAxis, 0, 0)
        eyeball.setRotateExtent(eyeball.wAxis, -35, 35)

        self.addChild(eye)
        eye.addChild(eyeball)

        self.componentList.append(eyeball)
        self.componentDict['eyeball'] = eyeball
