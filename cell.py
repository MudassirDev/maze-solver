from window import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.__win.draw_line(line)

        if self.has_right_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.__win.draw_line(line)

        if self.has_top_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.__win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(self.x2, self.y2), Point(self.x1, self.y2))
            self.__win.draw_line(line)

    def draw_move(self, cell, undo=False):
        center_point = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        other_center_point = Point((cell.x1 + cell.x2) / 2, (cell.y1 + cell.y2) / 2)
        line_to_draw = Line(center_point, other_center_point)
        if undo:
            self.__win.draw_line(line_to_draw, "gray")
        else:
            self.__win.draw_line(line_to_draw, "red")
