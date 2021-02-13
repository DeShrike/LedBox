from pluginbase import PluginBase

class Menu(PluginBase):

    menuitem_width = 5
    menuitem_height = 5

    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)
        self.menuitems = []
        self.selected = 0
        self.offsety = 0
        self.desired_offsety = 0
        self.frame = 0
        self.changed = False

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
            mp = p.menu_pattern()
            if mp is not None:
                self.menuitems.append([p.name, mp])

    def stop(self):
        print("Stop", self.options["display_name"])
        super().stop()

    def step(self):
        # print("Step", self.options["display_name"])
        super().step()

        if self.desired_offsety > self.offsety:
            self.offsety += 1
            self.changed = True
            self.draw_menu()
        elif self.desired_offsety < self.offsety:
            self.offsety -= 1
            self.changed = True
            self.draw_menu()

        if self.changed:
            self.grid.refresh()
            self.changed = False

    def arrow_pressed(self, arrow):
        # print(self.options["display_name"], arrow)
        if arrow == "up":
            if self.selected > 0:
                self.selected -= 1
                self.changed = True
                self.draw_menu()
        elif arrow == "down":
            if self.selected < len(self.menuitems) - 1:
                self.selected += 1
                self.changed = True
                self.draw_menu()

    def menu_pattern(self):
        return None

    def draw_menu(self):
        bordery = 2
        guttery = 1

        y = self.offsety + bordery
        for ix, mi in self.menuitems:
            self.draw_menuitem(y, mi, True if ix == self.selected else False)

            # make sure selected item is in view
            if ix == self.selected:
                if y < bordery:
                    pass 
                elif y + self.menuitem_height - 1 > self.grid.height - bordery:
                    pass
            
            y += guttery
            y += self.menuitem_height

    def draw_menuitem(self, row: int, menuitem, as_selected: bool):
        borderx = (self.grid.width - self.menuitem_width) // 2

        for y in range(self.menuitem_height):
            gridy = row + y
            if as_selected:
                self.grid.set_pixel_to_letter(0, gridy, "R")
                self.grid.set_pixel_to_letter(self.grid.width - 1, gridy, "R")
            for x in range(self.menuitem_width):
                gridx = borderx + x
                self.grid.set_pixel_to_letter(gridx, gridy, menuitem[y][x])
