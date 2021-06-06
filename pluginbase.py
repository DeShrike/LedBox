import abc
from abc import ABC, abstractmethod 

class PluginBase(ABC):

    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"

    def __init__(self, ledbox, grid):
        self.grid = grid
        self.ledbox = ledbox

    @abc.abstractproperty 
    def name(self) -> str: 
        return None

    @abc.abstractproperty 
    def options(self): 
        return {
            "order": 1000,
            "in_random": False,
            "need_arrows": False,
            "show_button": False,
            "display_name": None,
            "button_text": None,
            "button_type": "ms-default" # ms-default or ms-success or ms-info or ms-warning or ms-danger
        }

    def arrow_pressed(self, arrow):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def step(self):
        pass

    def menu_pattern(self):
        return [
            ["R", "G", "B", "C", "W"],
            ["R", "G", "B", "M", "Y"],
            ["R", "G", "B", "C", "W"],
            ["R", "G", "B", "M", "Y"],
            ["R", "G", "B", "C", "W"]
        ]
