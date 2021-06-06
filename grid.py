from pixel import Pixel
from ansi import Ansi
import logging
import config

color_to_ansi = {
    (1, 1, 1): Ansi.WhiteBackground,
    (0, 1, 1): Ansi.CyanBackground,
    (1, 0, 1): Ansi.MagentaBackground,
    (0, 0, 1): Ansi.BlueBackground,
    (1, 1, 0): Ansi.YellowBackground,
    (0, 1, 0): Ansi.GreenBackground,
    (1, 0, 0): Ansi.RedBackground,
    (0, 0, 0): Ansi.BlackBackground
}

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
        if config.OUTPUT_TO_TERMINAL:
            self.offsetx = (80 - (2 * self.width)) // 2
            Ansi.Init()
            print(Ansi.Clear, end = "", flush = True)

    def clear(self):
        for line in self.grid:
            for p in line:
                p.r = p.g = p.b = 0

    def set_pixel(self, x: int, y: int, r: int, g: int, b: int):
        if x < 0 or x >= self.width:
            return;
        if y < 0 or y >= self.height:
            return;

        self.grid[y][x].r = r
        self.grid[y][x].g = g
        self.grid[y][x].b = b

    def set_pixel_to_letter(self, x: int, y: int, l: str):
        if x < 0 or x >= self.width:
            return;
        if y < 0 or y >= self.height:
            return;

        self.grid[y][x].r = letter_to_rgb[l][0]
        self.grid[y][x].g = letter_to_rgb[l][1]
        self.grid[y][x].b = letter_to_rgb[l][2]

    def refresh(self):
        if config.OUTPUT_TO_TERMINAL == False:
            return
        print(Ansi.HideCursor, flush = False, end = "")
        for y, line in enumerate(self.grid):
            preva = ""
            print(Ansi.MoveCursor(self.offsetx, 1 + y) + "|", end = "", flush = False)
            for p in line:
                a = self.pixel_to_ansi(p)
                if a != preva:
                    preva = a
                    print(a, end = "", flush = False)
                print("  " , end = "", flush = False)
            print(Ansi.Reset + "|", end = "", flush = False)
        print(Ansi.ShowCursor, end = "", flush = False)
        print(Ansi.MoveCursor(1, 20), end = "", flush = True)

    def pixel_to_ansi(self, pixel) -> str:
        h = 256 // 2
        r = pixel.r
        g = pixel.g
        b = pixel.b

        r = 0 if r < h else 1
        g = 0 if g < h else 1
        b = 0 if b < h else 1

        a = color_to_ansi[(r,g,b)]
        return a
