from pluginbase import PluginBase

class Dot(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)
        self.x = 0
        self.y = 0

    @property
    def name(self) -> str: 
        return "Dot"

    @property
    def options(self): 
        return {
            "order": 5,
            "need_arrows": False,
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
        self.grid.clear()
        self.grid.set_pixel(self.x, self.y, 255, 0, 0)        
        self.grid.refresh()
        self.x += 1
        if self.x >= self.grid.width:
            self.y += 1
            self.x = 0
            if self.y >= self.grid.height:
                self.y = 0

        super().step()

    def arrow_pressed(self, arrow):
        print(self.options["display_name"], arrow)

    def menu_pattern(self):
        return [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "R", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
         ]
