from MultiColorComponent import MultiColorComponent
from MyModelFinger import MyModelFinger
from Point import Point
from Shapes import Cube, Sphere
import ColorType as Ct

# defined macros for dimension
uAxis = 0
vAxis = 1
wAxis = 2


class MyModelHand(MultiColorComponent):
    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale: float = 1.0, left_handed: bool = True):
        super().__init__(position, display_obj)
        self.contextParent = parent

        color_medium_gray = Ct.ColorType(80 / 255, 62 / 255, 89 / 255)
        color_dark_gray = Ct.ColorType(0.2, 0.2, 0.2)

        wrist_radius = 0.12 * scale
        wrist_length = wrist_radius * 2
        wrist_part = Sphere(Point((0, 0, 0)), shaderProg, [0.1, 0.1, 0.1], color_medium_gray)
        self.addChild(wrist_part)
        self.componentList.append(wrist_part)
        self.componentDict['wrist'] = wrist_part
        self.wrist = wrist_part

        palm_length = 1 * scale
        palm_width = 1 * scale
        palm_thickness = 2.2 * wrist_radius
        palm_part = Cube(Point((
            0, 0, wrist_length)), shaderProg, [
            palm_length, palm_thickness, palm_width], color_dark_gray)
        wrist_part.addChild(palm_part)
        self.componentList.append(palm_part)
        self.componentDict['palm'] = palm_part
        self.palm = palm_part

        finger_radius = palm_thickness / 2
        finger_length = 1.5 * palm_thickness

        if not left_handed:
            wrist_part.setRotateExtent(wrist_part.uAxis, -45, 15)
            wrist_part.setRotateExtent(wrist_part.vAxis, -5, 15)
            wrist_part.setRotateExtent(wrist_part.wAxis, -90, 45)

            palm_part.setRotateExtent(wrist_part.uAxis, -45, 15)
            palm_part.setRotateExtent(wrist_part.vAxis, -5, 15)
            palm_part.setRotateExtent(wrist_part.wAxis, 0, 0)

            thumb_finger = MyModelFinger(self, Point((-palm_length / 2, 0, palm_length / 4)), shaderProg,
                                         finger_radius=finger_radius, finger_height=finger_length, finger_nums=2)
            thumb_finger.setDefaultAngle(-45, thumb_finger.vAxis)
            palm_part.addChild(thumb_finger)
            self.componentList += thumb_finger.components
            for k, v in thumb_finger.componentDict.items():
                self.componentDict[f'thumb_{k}'] = v

            Index_finger = MyModelFinger(self, Point((-palm_length / 2 + finger_radius, 0, palm_length)), shaderProg,
                                         finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(Index_finger)
            self.componentList += Index_finger.components
            for k, v in Index_finger.componentDict.items():
                self.componentDict[f'index_{k}'] = v

            middle_finger = MyModelFinger(self, Point((finger_radius / 3 - palm_length / 6, 0, palm_length)), shaderProg,
                                          finger_radius=finger_radius, finger_height=finger_length, finger_nums=3)
            palm_part.addChild(middle_finger)
            self.componentList += middle_finger.components
            for k, v in middle_finger.componentDict.items():
                self.componentDict[f'middle_{k}'] = v

            ring_finger = MyModelFinger(self, Point((palm_length / 6 - finger_radius / 3, 0, palm_length)), shaderProg,
                                        finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(ring_finger)
            self.componentList += ring_finger.components
            for k, v in ring_finger.componentDict.items():
                self.componentDict[f'ring_{k}'] = v

            little_finger = MyModelFinger(self, Point((palm_length / 2 - finger_radius, 0, palm_length)), shaderProg,
                                          finger_radius=finger_radius, finger_height=0.8 * finger_length, finger_nums=3)
            palm_part.addChild(little_finger)
            self.componentList += little_finger.components
            for k, v in little_finger.componentDict.items():
                self.componentDict[f'little_{k}'] = v

            # thumb finger rotation limit
            thumb_finger.setPartRotateExtent(0, 0, -90, 0)
            thumb_finger.setPartRotateExtent(0, vAxis, -30, 30)
            thumb_finger.setPartRotateExtent(0, wAxis, 0, 0)

            thumb_finger.setPartRotateExtent(1, 0, 0, 0)
            thumb_finger.setPartRotateExtent(1, vAxis, 0, 90)
            thumb_finger.setPartRotateExtent(1, wAxis, 0, 0)

        # left handed
        else:
            wrist_part.setRotateExtent(wrist_part.uAxis, -45, 15)
            wrist_part.setRotateExtent(wrist_part.vAxis, -15, 5)
            wrist_part.setRotateExtent(wrist_part.wAxis, -45, 90)

            palm_part.setRotateExtent(wrist_part.uAxis, -45, 15)
            palm_part.setRotateExtent(wrist_part.vAxis, -15, 5)
            palm_part.setRotateExtent(wrist_part.wAxis, 0, 0)

            thumb_finger = MyModelFinger(self, Point((palm_length / 2, 0, palm_length / 4)), shaderProg,
                                         finger_radius=finger_radius, finger_height=finger_length, finger_nums=2)
            thumb_finger.setDefaultAngle(45, thumb_finger.vAxis)
            palm_part.addChild(thumb_finger)
            self.componentList += thumb_finger.components
            for k, v in thumb_finger.componentDict.items():
                self.componentDict[f'thumb_{k}'] = v

            Index_finger = MyModelFinger(self, Point((palm_length / 2 - finger_radius, 0, palm_length)), shaderProg,
                                         finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(Index_finger)
            self.componentList += Index_finger.components
            for k, v in Index_finger.componentDict.items():
                self.componentDict[f'index_{k}'] = v

            middle_finger = MyModelFinger(self, Point((palm_length / 6 - finger_radius / 3, 0, palm_length)), shaderProg,
                                          finger_radius=finger_radius, finger_height=finger_length, finger_nums=3)
            palm_part.addChild(middle_finger)
            self.componentList += middle_finger.components
            for k, v in middle_finger.componentDict.items():
                self.componentDict[f'middle_{k}'] = v

            ring_finger = MyModelFinger(self, Point((finger_radius / 3 - palm_length / 6, 0, palm_length)), shaderProg,
                                        finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(ring_finger)
            self.componentList += ring_finger.components
            for k, v in ring_finger.componentDict.items():
                self.componentDict[f'ring_{k}'] = v

            little_finger = MyModelFinger(self, Point((-palm_length / 2 + finger_radius, 0, palm_length)), shaderProg,
                                          finger_radius=finger_radius, finger_height=0.8 * finger_length, finger_nums=3)
            palm_part.addChild(little_finger)
            self.componentList += little_finger.components
            for k, v in little_finger.componentDict.items():
                self.componentDict[f'little_{k}'] = v

            # thumb finger rotation limit
            thumb_finger.setPartRotateExtent(0, uAxis, -90, 0)
            thumb_finger.setPartRotateExtent(0, vAxis, -30, 30)
            thumb_finger.setPartRotateExtent(0, wAxis, 0, 0)

            thumb_finger.setPartRotateExtent(1, uAxis, 0, 0)
            thumb_finger.setPartRotateExtent(1, vAxis, -90, 0)
            thumb_finger.setPartRotateExtent(1, wAxis, 0, 0)

        self.thumb_finger = thumb_finger
        self.Index_finger = Index_finger
        self.middle_finger = middle_finger
        self.ring_finger = ring_finger
        self.little_finger = little_finger

        # index finger rotation limit
        Index_finger.setPartRotateExtent(0, uAxis, -90, 0)
        Index_finger.setPartRotateExtent(0, vAxis, -5, 5)
        Index_finger.setPartRotateExtent(0, wAxis, 0, 0)

        Index_finger.setPartRotateExtent(1, uAxis, -90, 0)
        Index_finger.setPartRotateExtent(1, vAxis, 0, 0)
        Index_finger.setPartRotateExtent(1, wAxis, 0, 0)

        Index_finger.setPartRotateExtent(2, uAxis, -90, 0)
        Index_finger.setPartRotateExtent(2, vAxis, 0, 0)
        Index_finger.setPartRotateExtent(2, wAxis, 0, 0)

        # middle finger rotation limit
        middle_finger.setPartRotateExtent(0, uAxis, -90, 0)
        middle_finger.setPartRotateExtent(0, vAxis, -5, 5)
        middle_finger.setPartRotateExtent(0, wAxis, 0, 0)

        middle_finger.setPartRotateExtent(1, uAxis, -90, 0)
        middle_finger.setPartRotateExtent(1, vAxis, 0, 0)
        middle_finger.setPartRotateExtent(1, wAxis, 0, 0)

        middle_finger.setPartRotateExtent(2, uAxis, -90, 0)
        middle_finger.setPartRotateExtent(2, vAxis, 0, 0)
        middle_finger.setPartRotateExtent(2, wAxis, 0, 0)

        # ring finger rotation limit
        ring_finger.setPartRotateExtent(0, uAxis, -90, 0)
        ring_finger.setPartRotateExtent(0, vAxis, -5, 5)
        ring_finger.setPartRotateExtent(0, wAxis, 0, 0)

        ring_finger.setPartRotateExtent(1, uAxis, -90, 0)
        ring_finger.setPartRotateExtent(1, vAxis, 0, 0)
        ring_finger.setPartRotateExtent(1, wAxis, 0, 0)

        ring_finger.setPartRotateExtent(2, uAxis, -90, 0)
        ring_finger.setPartRotateExtent(2, vAxis, 0, 0)
        ring_finger.setPartRotateExtent(2, wAxis, 0, 0)

        # little finger rotation limit
        little_finger.setPartRotateExtent(0, uAxis, -90, 0)
        little_finger.setPartRotateExtent(0, vAxis, -5, 5)
        little_finger.setPartRotateExtent(0, wAxis, 0, 0)

        little_finger.setPartRotateExtent(1, uAxis, -90, 0)
        little_finger.setPartRotateExtent(1, vAxis, 0, 0)
        little_finger.setPartRotateExtent(1, wAxis, 0, 0)

        little_finger.setPartRotateExtent(2, uAxis, -90, 0)
        little_finger.setPartRotateExtent(2, vAxis, 0, 0)
        little_finger.setPartRotateExtent(2, wAxis, 0, 0)
