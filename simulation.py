import os

from robot import Robot
from table import Table
from command_parser import CommandParser

if __name__ == '__main__':
    table = Table()
    robot = Robot(table)
    input_command = 'init'
    
    os.system('cls')
    print("Toy Robot Simulation\n")
    input_choice = str(input('CHOOSE 1 AUTOMATE TESTING (with ready files) or 2 FOR MANUAL TESTING (input via console) '))
    if input_choice == '1':
        with open('example_files/commands1.txt') as fp:
            lines = fp.read().split("\n")
        for input_command in lines:
            print("Input: " + input_command)
            command_parser = CommandParser(input_command).get_validated_command()
            robot.robot_movemant(command_parser)
            print("\n")
    elif input_choice == '2':
        while input_command:
            input_command= str(input('Input: '))
            command_parser = CommandParser(input_command).get_validated_command()
            robot.robot_movemant(command_parser)


    
    
    