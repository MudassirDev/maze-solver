from cell import Cell
from window import *


def main():
    win = Window(800, 800)
    cell = Cell(20, 20, 40, 40, win)
    cell.draw()
    win.wait_for_close()


main()
