from pluginbase import PluginBase
import constants
import random

class Snake(PluginBase):
    def __init__(self, ledbox, grid):
        PluginBase.__init__(self, ledbox, grid)
        self.changed = False
        self.snake = []
        self.food = None
        self.vx = 1
        self.vy = 0
        self.dead = False
        self.speed = 1

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
        self.changed = True
        self.snake = [(self.grid.width // 2, self.grid.height // 2)]
        self.food = None
        self.add_food()
        self.vx = 1
        self.vy = 0
        self.dead = False
        self.speed = 1

    def stop(self):
        print("Stop", self.options["display_name"])
        super().stop()

    def step(self):
        # print("Step", self.options["display_name"])
        if self.dead == False:
            x = self.snake[0][0]
            y = self.snake[0][1]

            if x == self.food[0] and y == self.food[1]:
                self.add_food()
                self.speed = max(0.1, self.speed - 0.05)
            else:
                self.snake.pop()

            x = (x + self.vx) % self.grid.width
            y = (y + self.vy) % self.grid.height

            if (x, y) in self.snake:
                self.dead = True
                self.changed = True
            else:
                self.snake.insert(0, (x, y))
                self.changed = True
            self.draw()

        if self.changed:
            self.grid.refresh()
            self.changed = False
        
        super().step()
        return self.speed

    def arrow_pressed(self, arrow):
        # print(self.options["display_name"], arrow)
        if arrow == constants.LEFT:
            self.vx = -1
            self.vy = 0
        if arrow == constants.RIGHT:
            self.vx = 1
            self.vy = 0
        if arrow == constants.UP:
            self.vx = 0
            self.vy = -1
        if arrow == constants.DOWN:
            self.vx = 0
            self.vy = 1

    def menu_pattern(self):
        return [
            ["W", "W", "W", "W", "W"],
            ["W", " ", " ", " ", "W"],
            ["Y", " ", " ", " ", "W"],
            [" ", " ", "W", " ", "W"],
            ["G", " ", "W", "W", "W"]
         ]

    def add_food(self):
        x = 0
        y = 0
        while True:
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            if (x, y) not in self.snake:
                break
        self.food = (x, y)
        self.changed = True

    def draw(self):
        self.grid.clear()
        self.grid.set_pixel_to_letter(self.food[0], self.food[1], "G")
        for ix, s in enumerate(self.snake):
            self.grid.set_pixel_to_letter(s[0], s[1], ("R" if self.dead else "Y") if ix == 0 else "W")
