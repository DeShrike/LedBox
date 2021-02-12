from pixel import Pixel
from ansi import Ansi

class Grid():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Pixel() for _ in range(self.width)] for _ in range(self.height)]
        self.offsetx = (80 - (2 * self.width)) // 2
        Ansi.Init()

    def clear(self):
        for line in self.grid:
            for p in line:
                p.r = p.g = p.g = 0

    def set_pixel(self, x: int, y: int, r: int, g: int, b: int):
        self.grid[y][x].r = r
        self.grid[y][x].g = g
        self.grid[y][x].b = b

    def refresh(self):
        print(Ansi.HideCursor, flush = False)
        for y, line in enumerate(self.grid):
            print(Ansi.MoveCursor(self.offsetx, 1 + y) + "|", end = "", flush = False)
            for p in line:
                a = self.pixel_to_ansi(p)
                print(a + "  " + Ansi.Reset, end = "", flush = False)
            print("|", end = "", flush = False)
        print(Ansi.ShowCursor, flush = True)

    def pixel_to_ansi(self, pixel) -> str:
        h = 256 // 2
        r = pixel.r
        g = pixel.g
        b = pixel.b

        colors = { 
            (1,1,1): Ansi.WhiteBackground,
            (0,1,1): Ansi.CyanBackground,
            (1,0,1): Ansi.MagentaBackground,
            (0,0,1): Ansi.BlueBackground,
            (1,1,0): Ansi.YellowBackground,
            (0,1,0): Ansi.GreenBackground,
            (1,0,0): Ansi.RedBackground,
            (0,0,0): Ansi.BlackBackground,
        }

        r = 0 if r < h else 1
        g = 0 if g < h else 1
        b = 0 if b < h else 1

        a = colors[(r,g,b)]
        return a
