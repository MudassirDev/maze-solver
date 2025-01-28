from window import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.__point_a = Point(x1, y1)
        self.__point_c = Point(x2, y2)
        self.__point_b = Point(x2, y1)
        self.__point_d = Point(x1, y2)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win

    def draw(self):
        if self.has_left_wall:
            line = Line(self.__point_a, self.__point_d)
            self.__win.draw_line(line)

        if self.has_right_wall:
            line = Line(self.__point_b, self.__point_c)
            self.__win.draw_line(line)

        if self.has_top_wall:
            line = Line(self.__point_a, self.__point_b)
            self.__win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(self.__point_c, self.__point_d)
            self.__win.draw_line(line)
