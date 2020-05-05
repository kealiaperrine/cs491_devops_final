import math

class Physics:

    def update_speed(self, speed, maxSpeed, accel):
        if speed < maxSpeed:
            speed += accel
        return speed

    def update_velocity(self, vel, speed, direction):
        vel[direction] = speed
        return vel

    def update_position(self, vel, pos, time):
        pos = [x * time for x in vel]
        return pos