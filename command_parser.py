import re
from table import Table

class CommandParser:
    
    FACING = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self, input_command):
        self.table = Table()
        self.input_command = input_command
        self.parsed_command = []
        self.validated_command = []
        self.error_messages = []
        self.placed_index = 0
        self.commands =  {
            'PLACE': self.place_validate,
            'MOVE': self.move_validate,
            'RIGHT': self.rotate_right_validate,
            'LEFT': self.rotate_left_validate,
            'REPORT': self.report_validate,
        }
        
    def get_validated_command(self):
        self.validate_command()
        if self.error_messages:
            self.print_errors()    
            self.validated_command = []
        return self.validated_command

    def validate_command(self):
        self.parse_input() 
        for index, command in enumerate(self.parsed_command):
            if index < self.placed_index:
                continue
            self.commands.get(command, self.command_resolver)(index)
                
    def pattern_match(self):
        pattern = re.compile(r'[^a-zA-Z0-9,\s]')
        string = pattern.search(self.input_command)
        return not bool(string)

    def parse_input(self):
        if self.pattern_match():
            self.input_command = self.input_command.upper()
            self.parsed_command = self.input_command.replace(",", " ")
            self.parsed_command = self.parsed_command.split()
        else:
            self.error_messages.append("Input is not valid")
    
    def place_validate(self, index):
        x = self.parsed_command[index+1]
        y = self.parsed_command[index+2]
        f = self.parsed_command[index+3]
        place_valid = self.__validate_place_command(x, y, f)

        if place_valid:
            self.validated_command.append(['PLACE', x, y, f])
            self.placed_index = index+4

    def __validate_place_command(self, x, y, f):
        valid = False

        if not x.isnumeric() or int(x) < self.table.get_min_x() or int(x) > self.table.get_max_x():
            self.error_messages.append('Position X must be numeric, min:{0}, max:{1}'.format(self.table.get_min_x(), self.table.get_max_x()))
        if not y.isnumeric() or int(y) < self.table.get_min_y() or int(y) > self.table.get_max_y():
            self.error_messages.append('Position Y must be numeric, min:{0}, max:{1}'.format(self.table.get_min_y(), self.table.get_max_y()))
        if not isinstance(f, str) or f not in self.FACING:
            self.error_messages.append('Orientation must be string with value: NORTH, EAST, SOUTH or WEST')
        if not self.error_messages:
            valid = True
        return valid

    def move_validate(self, index):
        self.validated_command.append(['MOVE'])

    def report_validate(self, index):
        self.validated_command.append(['REPORT'])

    def rotate_left_validate(self, index):
        self.validated_command.append(['LEFT'])

    def rotate_right_validate(self, index):
        self.validated_command.append(['RIGHT'])

    def command_resolver(self, index):
        self.error_messages.append("Command {0} is not valid".format(self.parsed_command[index]))
        
    def print_errors(self):
        for message in self.error_messages:
            print(message)
        self.error_messages = []
