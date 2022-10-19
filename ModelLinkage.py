"""
Model our creature and wrap it in one class
First version at 09/28/2021

:author: micou(Zezhou Sun)
:version: 2021.2.1

----------------------------------

This class implements the bird model by
    - creating all components for the body
    - setting default rotation behavior for each component as well as rotation limits
    - linking components together in a hierarchy
Modified by Daniel Scrivener 07/2022
"""

from Component import Component
from MyModelBody import MyModelBody
from Point import Point
import ColorType as Ct
import numpy as np


class ModelLinkage(Component):
    """
    Define our linkage model
    """
    # Build the class(es) of objects that could utilize your built geometric object/combination classes. E.g., you could define
    # three instances of the cyclinder trunk class and link them together to be the "limb" class of your creature. 

    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        # Requirements:
        #   1. Set a reasonable rotation range for each joint,
        #      so that creature won't intersect itself or bend in unnatural way
        #   2. Orientation of joint rotations for the left and right parts should mirror each other.
        body = MyModelBody(self, Point((0, 0, 1)), shaderProg, scale=1)
        self.addChild(body)
        self.setDefaultAngle(-90, self.uAxis)
        self.componentList = body.componentList
        self.componentDict = body.componentDict

    def reset_component(self):
        for c in self.componentList:
            c.reset()

    def test_case_1(self):
        self.reset_component()
        self.componentDict['head_neck'].rotate(45, self.wAxis)
        self.componentDict['right_arm_shoulder_panel'].rotate(-10, self.uAxis)
        self.componentDict['right_arm_upper'].rotate(10, self.uAxis)
        self.componentDict['right_arm_lower'].rotate(-50, self.uAxis)
        self.componentDict['left_arm_upper'].rotate(-15, self.uAxis)
        self.componentDict['left_arm_upper'].rotate(90, self.wAxis)
        self.componentDict['waist'].rotate(20, self.wAxis)
        self.componentDict['right_leg_upper'].rotate(10, self.uAxis)
        self.componentDict['right_foot'].rotate(-10, self.uAxis)
        self.componentDict['left_leg_upper'].rotate(-10, self.uAxis)
        self.componentDict['left_leg_upper'].rotate(-10, self.vAxis)
        self.componentDict['left_leg_upper'].rotate(20, self.wAxis)
        self.componentDict['left_leg_lower'].rotate(20, self.uAxis)
        self.componentDict['left_foot'].rotate(-20, self.wAxis)

    def test_case_2(self):
        self.reset_component()
        pass

    def test_case_3(self):
        self.reset_component()
        pass

    def test_case_4(self):
        self.reset_component()
        pass

    def test_case_5(self):
        self.reset_component()
        pass
