from pixel import Pixel
import logging
import config

letter_to_rgb = {
    "R": (255,   0,   0),
    "G": (  0, 255,   0),
    "B": (  0,   0, 255),
    "W": (255, 255, 255),
    "C": (  0, 255, 255),
    "M": (255,   0, 255),
    "Y": (255, 255,   0),
    " ": (  0,   0,   0)
}

logger = logging.getLogger(__name__)

class Grid():

    def __init__(self, width, height):
        logger.info(f"Grid {width}x{height}")
        self.width = width
        self.height = height
        self.grid = [[Pixel() for _ in range(self.width)] for _ in range(self.height)]

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
        print("Grid Refresh")
