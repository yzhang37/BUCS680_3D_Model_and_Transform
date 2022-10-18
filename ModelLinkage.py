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
