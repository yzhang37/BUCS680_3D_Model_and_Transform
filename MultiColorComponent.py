import typing

from Component import Component
import ColorType as Ct


class MultiColorComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.componentList = []
        self.componentDict = {}
        self.my_componentDict = {}
        self.setDefaultColor(Ct.BLACK)
        self.default_color_list = {}

    def setCurrentColor(self, color):
        if color == Ct.BLACK:
            for comp_name, color in self.default_color_list.items():
                comp = self.my_componentDict[comp_name]
                comp.setCurrentColor(comp.default_color)
        else:
            for comp in self.my_componentDict.values():
                comp.setCurrentColor(color)

    def register_color(self, comp: Component, name: str, color: typing.Optional[Ct.ColorType] = None) -> None:
        if isinstance(comp, MultiColorComponent):
            return
        if color is None:
            color = Ct.BLACK
        self.my_componentDict[name] = comp
        self.default_color_list[name] = color
        comp.setDefaultColor(color)
