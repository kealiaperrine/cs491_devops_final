class Follow:

    def setGoal(self, target):
        target[0] += 2
        return target

    def closeEnough(self, current, target):
        diff = target - current
        if diff[0] < 0:
            diff[0] *= -1
        if diff[1] < 0:
            diff[1] *= -1
        if diff[2] < 0:
            diff[2] *= -1
        if diff > [1,1,1]:
            return False
        else:
            return True

    def whichWay(self, current, target):
        return
