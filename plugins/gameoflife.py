from pluginbase import PluginBase

class GameOfLife(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)

    @property
    def name(self) -> str: 
        return "GoL"

    @property
    def options(self): 
        return {
            "order": 3,
            "in_random": True,
            "need_arrows": False,
            "show_button": True,
            "display_name": "Game Of Life",
            "button_text": "Game Of Life",
            "button_type": "ms-default"
        }

    def start(self):
        super().start()
        # print("Start", self.options["display_name"])

    def stop(self):
        # print("Stop", self.options["display_name"])
        super().stop()

    def step(self):
        # print("Step", self.options["display_name"])
        super().step()
        self.grid.refresh()

    def menu_pattern(self):
        return [
            [" ", " ", " ", " ", " "],
            [" ", " ", "W", " ", " "],
            [" ", " ", " ", "W", " "],
            [" ", "W", "W", "W", " "],
            [" ", " ", " ", " ", " "]
         ]
