class Tetris:
    height, width = 0, 0
    field = []
    score = 0
    state = "start"

    def __init__(self, _width, _height):
        self.height = _height
        self.width = _width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)
        self.field[1][1] = 3