import unittest
from table import Table
from robot import Robot
from command_parser import CommandParser

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.table = Table()
        self.robot = Robot(self.table)
        
    def test_creating_board(self):
        self.assertIsInstance(self.table, Table)

    def test_creating_robot(self):
        self.assertIsInstance(self.robot, Robot)

    def test_robot_movement(self):
        command = CommandParser('PLACE 0,0,NORTH MOVE REPORT').get_validated_command()
        self.robot.robot_movemant(command)
        self.assertEqual('Output: 0,1,NORTH', self.robot.get_report_state())

        command = CommandParser('PLACE 0,0,NORTH LEFT REPORT').get_validated_command()
        self.robot.robot_movemant(command)
        self.assertEqual('Output: 0,0,WEST', self.robot.get_report_state())

        command = CommandParser('PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT').get_validated_command()
        self.robot.robot_movemant(command)
        self.assertEqual('Output: 3,3,NORTH', self.robot.get_report_state())

        command = CommandParser('PLACE 0,0,EAST MOVE MOVE LEFT MOVE REPORT').get_validated_command()
        self.robot.robot_movemant(command)
        self.assertEqual('Output: 2,1,NORTH', self.robot.get_report_state())

        command = CommandParser('PLACE 0,0,EAST MOVE MOVE LEFT MOVE PLACE 3,3,SOUTH MOVE REPORT').get_validated_command()
        self.robot.robot_movemant(command)
        self.assertEqual('Output: 3,2,SOUTH', self.robot.get_report_state())
        
if __name__ == '__main__':
    unittest.main()
