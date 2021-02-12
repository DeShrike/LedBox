from pluginbase import PluginBase

class Snake(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)

    @property
    def name(self) -> str: 
        return "Snake"

    @property
    def options(self): 
        return {
            "order": 1,
            "need_arrows": True,
            "show_button": True,
            "display_name": "Snake",
            "button_text": "Snake",
            "button_type": "ms-default"
        }

    def start(self):
        super().start()
        print("Start", self.options["display_name"])

    def stop(self):
        print("Stop", self.options["display_name"])
        super().stop()

    def step(self):
        print("Step", self.options["display_name"])
        super().step()

    def arrow_pressed(self, arrow):
        print(self.options["display_name"], arrow)

    def menu_pattern(self):
        return [
            ["W", "W", "W", "W", "W"],
            ["W", " ", " ", " ", "W"],
            ["Y", " ", " ", " ", "W"],
            [" ", " ", "W", " ", "W"],
            ["R", " ", "W", "W", "W"]
         ]
