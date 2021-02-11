from pluginbase import PluginBase

class Menu(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)
        self.menuoptions = []
        self.active = 0
        self.offset = 0
        
    @property
    def order(self) -> int: 
        return 0

    @property
    def need_arrows(self) -> bool: 
        return True

    @property
    def show_button(self) -> bool: 
        return True

    @property
    def name(self) -> str: 
        return "Menu"

    @property
    def display_name(self) -> str: 
        return "Menu"

    @property
    def button_text(self) -> str: 
        return "Menu"

    @property
    def button_type(self) -> str:
        return "ms-info"

    def start(self):
        super().start()
        print("Start", self.display_name)
        for p in self.ledbox.plugins:
            self.menuoptions.append([p.name, p.menu_pattern()])

    def stop(self):
        print("Stop", self.display_name)
        super().stop()

    def step(self):
        print("Step", self.display_name)
        super().step()
        self.grid.refresh()

    def arrow_pressed(self, arrow):
        print(self.display_name, arrow)
        if arrow == self.LEFT:
            print("Yes LEFT")

    def menu_pattern(self):
        return None
