import unittest
from monster import Monster

class MonsterMethods(unittest.TestCase):

    def test_damage_true(self):
        monster = Monster()
        monster.damage()
        self.assertEqual(monster.health, 0)

    def test_damage_false(self):
        monster = Monster()
        monster.damage()
        self.assertNotEqual(monster.health, 1)

    def test_check_alive_true(self):
        monster = Monster()
        self.assertTrue(monster.checkAlive())

    def test_check_alive_false(self):
        monster = Monster()
        monster.health = 0
        self.assertFalse(monster.checkAlive())


if __name__ == '__main__':
    unittest.main()