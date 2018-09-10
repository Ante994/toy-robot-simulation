
class Robot:
    
    ORIENTATION_DICT = {'NORTH': 0, 'EAST': 1, 'SOUTH': 2, 'WEST': 3}
    ORIENTATION_LIST = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self, table):
        self.table = table
        self.on_board = False
        self.facing = None
        self.x = None
        self.y = None
        self.error_messages = []
        self.commands =  {
            'PLACE': self.place_robot,
            'MOVE': self.move_robot,
            'RIGHT': self.rotate_robot,
            'LEFT': self.rotate_robot,
            'REPORT': self.report_state,
        }
        self.orientation = {
            'NORTH': self.move_robot_north,
            'EAST': self.move_robot_east,
            'SOUTH': self.move_robot_south,
            'WEST': self.move_robot_west,
        }
        self.rotations = {
            'LEFT': self.rotate_robot_left,
            'RIGHT': self.rotate_robot_right,
        }

    def robot_movemant(self, command_line):
        for command in command_line:
            self.commands.get(command[0], self.command_resolver)(command)
            if self.get_errors():
                self.print_errors()
                return
        
    def get_errors(self):
        if self.error_messages:
            return True
        return False

    def is_robot_on_board(self):
        return self.on_board

    def print_errors(self):
        for error in self.error_messages:
            print("Error Robot Message: " + error)
        self.error_messages = []

    def place_robot(self, command):
        self.x, self.y, self.facing = int(command[1]), int(command[2]), str(command[3])
        self.on_board = True

    def move_robot(self, command):
        if self.is_robot_on_board():
            if not self.change_position_by_facing(self.facing):
                self.error_messages.append("Robot cannot move in {0} direction".format(self.facing))
        else:
            self.error_messages.append("Robot must be placed on board to be moved")

    def rotate_robot(self, command):
        if self.is_robot_on_board():
            self.make_robot_rotate(command[0])
        else:
            self.error_messages.append("Robot must be placed on board to be rotated")
        
    def change_position_by_facing(self, facing):
        return self.orientation.get(facing)()
    
    def make_robot_rotate(self, rotation):
        return self.rotations.get(rotation)()

    def report_state(self, command=None):
        print("Output: " + str(self.x) + "," + str(self.y) + "," + str(self.facing))
    
    def get_report_state(self):
        return ("Output: " + str(self.x) + "," + str(self.y) + "," + str(self.facing))

    def move_robot_north(self):
        if self.y+1 < self.table.get_max_y():
            self.y += 1
            return True
        return False

    def move_robot_east(self):
        if self.x+1 < self.table.get_max_x():
            self.x += 1
            return True
        return False

    def move_robot_south(self):
        if self.y-1 > self.table.get_min_y(): 
            self.y -= 1
            return True
        return False

    def move_robot_west(self):
        if self.x-1 > self.table.get_min_x():
            self.x -= 1
            return True
        return False

    def rotate_robot_left(self):
        value_facing = (self.ORIENTATION_DICT[self.facing] - 1) % 4
        self.facing = self.ORIENTATION_LIST[value_facing]
        
    def rotate_robot_right(self):
        value_facing = (self.ORIENTATION_DICT[self.facing] + 1) % 4
        self.facing = self.ORIENTATION_LIST[value_facing]
        
    def command_resolver(self, command):
        self.error_messages.append('UNPARSED {0} - No One Expected Me :('.format(command))
