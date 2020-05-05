class Follow:

    def setGoal(self, target):
        target[0] += 2
        return target

    def closeEnough(self, current, target):
        diff = map(abs, target - current)

        if diff > [1,1,1]:
            return False
        else:
            return True

    def whichWay(self, current, target):
        return target - current
