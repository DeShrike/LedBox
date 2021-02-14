from pluginbase import PluginBase
import constants

class Dot(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)
        self.x = self.grid.width // 2
        self.y = self.grid.height // 2
        self.changed = True

    @property
    def name(self) -> str: 
        return "Dot"

    @property
    def options(self): 
        return {
            "order": 5,
            "need_arrows": True,
            "show_button": True,
            "display_name": "Dot",
            "button_text": "Dot",
            "button_type": "ms-default"
        }

    def start(self):
        super().start()
        print("Start", self.options["display_name"])

    def stop(self):
        print("Stop", self.options["display_name"])
        super().stop()

    def step(self):
        # print("Step", self.options["display_name"])
        if self.changed:
            self.grid.clear()
            self.grid.set_pixel(self.x, self.y, 255, 0, 0)        
            self.grid.refresh()
            self.changed = False
        super().step()

    def arrow_pressed(self, arrow):
        # print(self.options["display_name"], arrow)
        if arrow == constants.LEFT:
            self.x = (self.x - 1) % self.grid.width
        if arrow == constants.RIGHT:
            self.x = (self.x + 1) % self.grid.width
        if arrow == constants.UP:
            self.y = (self.y - 1) % self.grid.height
        if arrow == constants.DOWN:
            self.y = (self.y + 1) % self.grid.height
        self.changed = True

    def menu_pattern(self):
        return [
            ["W", "W", "W", "W", "W"],
            ["W", " ", " ", " ", "W"],
            ["W", " ", "R", " ", "W"],
            ["W", " ", " ", " ", "W"],
            ["W", "W", "W", "W", "W"]
         ]
