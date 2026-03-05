import numpy as np

class Ray:
    def __init__(self,origin,direction):
        self.origin = np.array(origin)
        self.direction = self._normalize(direction)

        self.path = [self.origin.copy()]

    def propagate(self,distance):
        new_point = self.origin + distance * self.direction
        self.path.append(new_point)
        self.origin = new_point

    def _normalize(self,v):
        return v / np.linalg.norm(v)
    