from pluginbase import PluginBase
import constants

class Pong(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)
        self.x = 0
        self.y = self.grid.height // 2
        self.changed = True
        self.paddle_height = 4
        self.paddle_pos = (self.grid.height - self.paddle_height) // 2

    @property
    def name(self) -> str: 
        return "Pong"

    @property
    def options(self): 
        return {
            "order": 6,
            "in_random": False,
            "need_arrows": True,
            "show_button": True,
            "display_name": "Pong",
            "button_text": "Pong",
            "button_type": "ms-default"
        }

    def start(self):
        super().start()
        # print("Start", self.options["display_name"])
        self.changed = True
        
    def stop(self):
        # print("Stop", self.options["display_name"])
        super().stop()

    def step(self):
        # print("Step", self.options["display_name"])
        if self.changed:
            self.grid.clear()
            self.draw()
            self.grid.refresh()
            self.changed = False
        super().step()

    def arrow_pressed(self, arrow):
        if arrow == constants.UP:
            if self.paddle_pos > 0:
                self.paddle_pos -= 1
        if arrow == constants.DOWN:
            if self.paddle_pos < self.grid.height - self.paddle_height:
                self.paddle_pos += 1
        self.changed = True

    def draw(self):
        self.grid.clear()
        for y in range(self.paddle_height):
            self.grid.set_pixel_to_letter(self.grid.width - 1, y + self.paddle_pos, "W")

        self.grid.set_pixel_to_letter(self.x, self.y, "M")

    def menu_pattern(self):
        return [
            [" ", " ", " ", " ", "W"],
            [" ", " ", " ", " ", "W"],
            ["M", " ", " ", " ", "W"],
            [" ", " ", " ", " ", "W"],
            [" ", " ", " ", " ", "W"]
         ]
