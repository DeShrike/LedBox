from pluginbase import PluginBase

class Snake(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)

    @property
    def order(self) -> int: 
        return 1

    @property
    def need_arrows(self) -> bool: 
        return True

    @property
    def show_button(self) -> bool: 
        return True

    @property
    def name(self) -> str: 
        return "Snake"

    @property
    def display_name(self) -> str: 
        return "Snake"

    @property
    def button_text(self) -> str: 
        return "Snake"

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

    def arrow_pressed(self, arrow):
        print(self.display_name, arrow)

    def menu_pattern(self):
        return [
            ["W", "W", "W", "W", "W"],
            ["W", " ", " ", " ", "W"],
            ["Y", " ", " ", " ", "W"],
            [" ", " ", "W", " ", "W"],
            ["R", " ", "W", "W", "W"]
         ]
