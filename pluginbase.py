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
    def order(self) -> int: 
        return 1000

    @abc.abstractproperty 
    def need_arrows(self) -> bool: 
        return False

    @abc.abstractproperty 
    def show_button(self) -> bool: 
        return False

    @abc.abstractproperty 
    def name(self) -> str: 
        return None

    @abc.abstractproperty 
    def display_name(self) -> str: 
        return None

    @abc.abstractproperty 
    def button_text(self) -> str: 
        return None

    @abc.abstractproperty 
    def button_type(self) -> str:
        """ ms-default or ms-success or ms-info or ms-warning or ms-danger""" 
        return "ms-default"

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
            ["R", "G", "B"],
            ["R", "G", "B"],
            ["R", "G", "B"]
        ]
