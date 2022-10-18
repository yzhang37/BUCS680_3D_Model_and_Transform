from Component import Component
import ColorType as Ct


class MultiColorComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.componentList = []
        self.componentDict = {}
        self.setDefaultColor(Ct.BLACK)
        self.default_color_list = {}

    def setCurrentColor(self, color):
        super().setCurrentColor(color)
        if self.current_color == Ct.BLACK:
            for comp_name, color in self.default_color_list.items():
                self.componentDict[comp_name].setDefaultColor(color)
