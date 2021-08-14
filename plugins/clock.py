from pluginbase import PluginBase

class Clock(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)

    @property
    def name(self) -> str: 
        return "Clock"

    @property
    def options(self): 
        return {
            "order": 2,
            "in_random": True,
            "need_arrows": False,
            "show_button": True,
            "display_name": "Clock",
            "button_text": "Clock",
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
        self.grid.refresh()

    def menu_pattern(self):
        return [
            [" ", "C", "C", "C", " "],
            ["C", " ", "W", " ", "C"],
            ["C", " ", "W", " ", "C"],
            ["C", " ", " ", "W", "C"],
            [" ", "C", "C", "C", " "]
         ]
