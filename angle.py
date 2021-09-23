from math import cos, sin, radians

class Angle:
    def __init__(self, angle):
        if angle < 0 or angle > 360:
            raise ValueError
        self.angle = angle
    
    def __str__(self):
        return str(self.angle) + " degrés"

    def ajoute(self, angle):
        return Angle(self.angle + angle.angle)

    def cos(self):
        return cos(radians(self.angle))

    def sin(self):
        return sin(radians(self.angle))
