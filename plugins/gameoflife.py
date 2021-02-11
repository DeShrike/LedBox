from pluginbase import PluginBase

class GameOfLife(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)

    @property
    def order(self) -> int: 
        return 3

    @property
    def need_arrows(self) -> bool:
        return False

    @property
    def show_button(self) -> bool: 
        return True

    @property
    def name(self) -> str: 
        return "GoL"

    @property
    def display_name(self) -> str: 
        return "Game Of Life"

    @property
    def button_text(self) -> str: 
        return "Life"

    @property
    def button_type(self) -> str:
        return "ms-default"

    def start(self):
        super().start()
        print("Start", self.display_name)

    def stop(self):
        print("Stop", self.display_name)
        super().stop()

    def step(self):
        print("Step", self.display_name)
        super().step()
        self.grid.refresh()

    def menu_pattern(self):
        return [
            [" ", " ", "W", "W", " "],
            [" ", " ", "W", " ", "W"],
            [" ", "W", "W", " ", "W"],
            [" ", " ", " ", "W", " "],
            [" ", "W", " ", " ", "W"]
         ]
