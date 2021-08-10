from pixel import Pixel
import logging
import config
import neopixel

letter_to_rgb = {
    "R": (255,   0,   0),
    "G": (  0, 255,   0),
    "B": (  0,   0, 255),

    "W": (255, 255, 255),
    "A": (  0,   0,   0),

    "C": (  0, 255, 255),
    "M": (255,   0, 255),
    "Y": (255, 255,   0),

    " ": (  0,   0,   0)
}

logger = logging.getLogger(__name__)

class DummyStrip():
    def __init__(self):
        pass
    def show(self):
        pass
    def __getitem__(self, key):
        pass
    def __setitem__(self, key, value):
        pass

class Grid():

    def __init__(self, width, height):
        logger.info(f"Grid {width}x{height}")
        self.width = width
        self.height = height
        self.grid = [[Pixel() for _ in range(self.width)] for _ in range(self.height)]

        self.grid_to_strip_index = {}
        # strip starts bottom right and zigzags first horizontally and then up
        stripindex = 0
        y = self.height - 1
        while y >= 0:
            x = self.width - 1
            while x >= 0:
                self.grid_to_strip_index[(x, y)] = stripindex
                stripindex += 1
                x -= 1
            y -= 1
        
        #self.strip = neopixel.NeoPixel(pixel_pin, self.width * self.height, brightness = 0.1, auto_write = False, pixel_order = ORDER)
        self.strip = DummyStrip()

    def clear(self):
        for line in self.grid:
            for p in line:
                p.r = p.g = p.b = 0

    def set_pixel(self, x: int, y: int, r: int, g: int, b: int):
        if x < 0 or x >= self.width:
            return
        if y < 0 or y >= self.height:
            return

        self.grid[y][x].r = r
        self.grid[y][x].g = g
        self.grid[y][x].b = b

    def set_pixel_to_letter(self, x: int, y: int, l: str):
        if x < 0 or x >= self.width:
            return
        if y < 0 or y >= self.height:
            return

        self.grid[y][x].r = letter_to_rgb[l][0]
        self.grid[y][x].g = letter_to_rgb[l][1]
        self.grid[y][x].b = letter_to_rgb[l][2]

    def refresh(self):
        for x in range(self.width):
            for y in range(self.height):
                self.strip[self.grid_to_strip_index[(x, y)]] = self.grid[y][x].to_color()
        self.strip.show()
