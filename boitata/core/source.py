import numpy as np
from .ray import Ray

class PointSource:
    def __init__(self,position=(0,0,0),n_rays=10,divergence=0.01):
        self.position = np.array(position)
        self.n_rays = n_rays
        self.divergence = divergence

    def generate_rays(self):
        rays = []
        for _ in range(self.n_rays):
            dx = np.random.normal(scale = self.divergence)
            dy = np.random.normal(scale = self.divergence)

            direction = np.array([dx,dy,1.0])

            rays.apend(
                Ray(self.position,direction)
            )

        return rays