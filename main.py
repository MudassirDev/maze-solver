from cell import Cell
from maze import Maze
from window import *


def main():
    win = Window(800, 800)

    cell1 = Cell(100, 100, 150, 150, win)
    cell2 = Cell(150, 100, 200, 150, win)
    cell3 = Cell(100, 150, 150, 200, win)  # Cell below

    # Draw all cells
    cell1.draw()
    cell2.draw()
    cell3.draw()

    # Test different moves
    cell1.draw_move(cell2)
    cell1.draw_move(cell3)

    win.wait_for_close()


main()
