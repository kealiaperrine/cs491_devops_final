import unittest
from follow import Follow
from monster import Monster
from physics import Physics
from player import Player

class GameMethods(unittest.TestCase):

    def test_integration1_true_close(self):
        player = Player()
        monster = Monster()
        follow = Follow()
        self.assertTrue(follow.closeEnough(monster.position, player.position))

    def test_integration1_false_close(self):
        player = Player()
        monster = Monster()
        monster.position = [20,20,20]
        follow = Follow()
        self.assertFalse(follow.closeEnough(monster.position, player.position))

    def test_integration1_player_physics_pos_true(self):
        player = Player()
        physics = Physics()
        player.position = physics.update_position([2,2,2], player.position, 1)
        self.assertEqual(player.position, [2,2,2])

    def test_integration1_player_physics_pos_false(self):
        player = Player()
        physics = Physics()
        player.position = physics.update_position([2,2,2], player.position, 1)
        self.assertNotEqual(player.position, [0,0,0])

    def test_integration1_player_physics_vel_speed_true(self):
        player = Player()
        physics = Physics()
        speed = physics.update_speed(0, 10, 5)
        player.velocity = physics.update_velocity(player.velocity, speed, 0)
        self.assertEqual(player.velocity, [5,0,0])

    def test_integration1_player_physics_vel_speed_false(self):
        player = Player()
        physics = Physics()
        speed = physics.update_speed(0, 10, 5)
        player.velocity = physics.update_velocity(player.velocity, speed, 0)
        self.assertNotEqual(player.velocity, [0,0,0])

    def test_integration1_monster_physics_pos_true(self):
        monster = Monster()
        physics = Physics()
        monster.position = physics.update_position([2,2,2], monster.position, 1)
        self.assertEqual(monster.position, [2,2,2])

    def test_integration1_monster_physics_pos_false(self):
        monster = Monster()
        physics = Physics()
        monster.position = physics.update_position([2,2,2], monster.position, 1)
        self.assertNotEqual(monster.position, [0,0,0])

    def test_integration1_monster_physics_vel_speed_true(self):
        monster = Monster()
        physics = Physics()
        speed = physics.update_speed(0, 10, 5)
        monster.velocity = physics.update_velocity(monster.velocity, speed, 0)
        self.assertEqual(monster.velocity, [5,0,0])

    def test_integration1_monster_physics_vel_speed_false(self):
        monster = Monster()
        physics = Physics()
        speed = physics.update_speed(0, 10, 5)
        monster.velocity = physics.update_velocity(monster.velocity, speed, 0)
        self.assertNotEqual(monster.velocity, [0,0,0])

if __name__ == '__main__':
    unittest.main()
