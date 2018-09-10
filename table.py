
class Table:
    def __init__(self):
        self.board = []
        self.x = 5
        self.y = 5

    def get_max_y(self):
        return (self.y-1)

    def get_max_x(self):
        return (self.x-1)

    def get_min_y(self):
        return 0

    def get_min_x(self):
        return 0
