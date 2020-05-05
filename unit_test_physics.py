import unittest
from physics import Physics

class PhysicsMethods(unittest.TestCase):

    def test_update_speed_true(self):
        physics = Physics()
        self.assertEqual(physics.update_speed(5,6,1), 6)

    def test_update_speed_false(self):
        physics = Physics()
        self.assertNotEqual(physics.update_speed(5,6,1), 5)

    def test_update_velocity_x(self):
        physics = Physics()
        velocity = [0,0,0]
        self.assertEqual(physics.update_velocity(velocity, 5, 0), [5,0,0])

    def test_update_velocity_y(self):
        physics = Physics()
        velocity = [0,0,0]
        self.assertEqual(physics.update_velocity(velocity, 5, 1), [0,5,0])

    def test_update_velocity_z(self):
        physics = Physics()
        velocity = [0,0,0]
        self.assertEqual(physics.update_velocity(velocity, 5, 2), [0,0,5])

    def test_update_position_true(self):
        physics = Physics()
        velocity = [1,1,1]
        position = [0,0,0]
        time = 1
        self.assertEqual(physics.update_position(velocity, position, time), [1,1,1])

    def test_update_position_false(self):
        physics = Physics()
        velocity = [2,2,4]
        position = [0,0,0]
        time = 1
        self.assertNotEqual(physics.update_position(velocity, position, time), [1,1,1])


if __name__ == '__main__':
    unittest.main()