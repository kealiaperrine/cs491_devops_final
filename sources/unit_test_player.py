import unittest
from player import Player

class PlayerMethods(unittest.TestCase):

    def test_increase_x_vel_true(self):
        player1 = Player()
        player1.increase_x_velocity()
        self.assertEqual(player1.velocity, [5,0,0])

    def test_increase_x_vel_false(self):
        player1 = Player()
        player1.increase_x_velocity()
        self.assertNotEqual(player1.velocity, [0,0,0])

    def test_increase_y_vel_true(self):
        player1 = Player()
        player1.increase_y_velocity()
        self.assertEqual(player1.velocity, [0,5,0])

    def test_increase_y_vel_false(self):
        player1 = Player()
        player1.increase_y_velocity()
        self.assertNotEqual(player1.velocity, [0,0,0])

    def test_increase_z_vel_true(self):
        player1 = Player()
        player1.increase_z_velocity()
        self.assertEqual(player1.velocity, [0,0,5])

    def test_increase_z_vel_false(self):
        player1 = Player()
        player1.increase_z_velocity()
        self.assertNotEqual(player1.velocity, [0,0,0])

    def test_change_x_pos_true(self):
        player1 = Player()
        player1.change_x_pos()
        self.assertEqual(player1.position, [2,0,0])

    def test_change_x_pos_false(self):
        player1 = Player()
        player1.change_x_pos()
        self.assertNotEqual(player1.position, [0, 0, 0])

    def test_change_y_pos_true(self):
        player1 = Player()
        player1.change_y_pos()
        self.assertEqual(player1.position, [0,2,0])

    def test_change_y_pos_false(self):
        player1 = Player()
        player1.change_y_pos()
        self.assertNotEqual(player1.position, [0, 0, 0])

    def test_change_z_pos_true(self):
        player1 = Player()
        player1.change_z_pos()
        self.assertEqual(player1.position, [0,0,2])

    def test_change_z_pos_false(self):
        player1 = Player()
        player1.change_z_pos()
        self.assertNotEqual(player1.position, [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
