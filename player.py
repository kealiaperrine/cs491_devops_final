class Player:

    def __init__(self):
        self.name = "PlayerOne"
        self.position = [0,0,0]
        self.velocity = [0,0,0]
        self.acceleration = 5

    def increase_x_velocity(self):
        self.velocity[0] += self.acceleration

    def increase_y_velocity(self):
        self.velocity[1] += self.acceleration

    def increase_z_velocity(self):
        self.velocity[2] += self.acceleration


