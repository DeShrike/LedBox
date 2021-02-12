from pluginbase import PluginBase

class Menu(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)
        self.menuoptions = []
        self.active = 0
        self.offset = 0
        
    @property
    def name(self) -> str: 
        return "Menu"

    @property
    def options(self): 
        return {
            "order": 0,
            "need_arrows": True,
            "show_button": True,
            "display_name": "Menu",
            "button_text": "Menu",
            "button_type": "ms-info",
        }

    def start(self):
        super().start()
        print("Start", self.options["display_name"])
        for p in self.ledbox.plugins:
            self.menuoptions.append([p.name, p.menu_pattern()])

    def stop(self):
        print("Stop", self.options["display_name"])
        super().stop()

    def step(self):
        # print("Step", self.options["display_name"])
        super().step()
        self.grid.refresh()

    def arrow_pressed(self, arrow):
        print(self.options["display_name"], arrow)

    def menu_pattern(self):
        return None
