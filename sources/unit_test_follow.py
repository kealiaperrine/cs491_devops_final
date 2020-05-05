import unittest
from follow import Follow

class FollowMethods(unittest.TestCase):

    def test_setGoal_true(self):
        follow = Follow()
        target = [0,0,0]
        self.assertEqual(follow.setGoal(target), [2,0,0])

    def test_setGoal_false(self):
        follow = Follow()
        target = [0,0,0]
        self.assertNotEqual(follow.setGoal(target), [0,0,0])

    def test_setGoal_false2(self):
        follow = Follow()
        target = [0,0,0]
        self.assertNotEqual(follow.setGoal(target), [0,2,0])

    def test_setGoal_false3(self):
        follow = Follow()
        target = [0,0,0]
        self.assertNotEqual(follow.setGoal(target), [0,0,2])

    def test_closeEnough_true_pos(self):
        follow = Follow()
        target = [0,0,0]
        current = [1,1,1]
        self.assertTrue(follow.closeEnough(current, target))

    def test_closeEnough_true_neg(self):
        follow = Follow()
        target = [0,0,0]
        current = [-1,-1,-1]
        self.assertTrue(follow.closeEnough(current, target))

    def test_closeEnough_false_pos(self):
        follow = Follow()
        target = [0,0,0]
        current = [20,20,20]
        self.assertFalse(follow.closeEnough(current, target))

    def test_closeEnough_false_neg(self):
        follow = Follow()
        target = [0,0,0]
        current = [-20,-20,-20]
        self.assertFalse(follow.closeEnough(current, target))

if __name__ == '__main__':
    unittest.main()
