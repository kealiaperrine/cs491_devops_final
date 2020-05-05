class Monster:
    def __init__(self):
        #self.name = "monster" + 1
        self.health = 1
        self.alive = True
        self.speed = 0
        self.maxSpeed = 4
        self.acceleration = 1

    def damage(self):
        self.health -= 1

    def checkAlive(self):
        if self.health == 0:
            self.alive = False
        return self.alive

