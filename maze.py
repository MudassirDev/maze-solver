from time import sleep

from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()

    def _create_cells(self):
        self.__cells = []
        x1 = self.x1
        x2 = x1 + self.cell_size_x
        for _ in range(self.num_cols):
            y1 = self.y1
            y2 = y1 + self.cell_size_y
            col = []
            for _ in range(self.num_rows):
                cell = Cell(x1, y1, x2, y2, self.__win)
                self._draw_cell(cell)
                y1 = y2
                y2 += self.cell_size_y
                col.append(cell)
            x1 = x2
            x2 += self.cell_size_x
            self.__cells.append(col)

    def _draw_cell(self, cell):
        cell.draw()

    def _animate(self):
        self.__win.redraw()
        sleep(0.05)
