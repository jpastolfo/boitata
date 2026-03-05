import numpy as np
import pyvista as pv

class SceneRenderer:
    def __init__(self,plotter):
        self.plotter = plotter
        
        self.actor_map = {}
        self.rays_actor = None

    def clear_rays(self):
        if self.rays_actor:
            self.plotter.remove_actor(self.rays_actor)
            self.rays_actor = None

    def add_source(self,source):
        sphere = pv.Sphere(
            radius=0.1,
            center=source.position
        )

        actor = self.plotter.add_mesh(
            sphere,
            color="red"
        )

        self.actor_map[actor] = source

    def draw_rays(self,rays):
        points = []
        lines = []

        idx = 0

        for ray in rays:
            p0 = ray.path[0]
            p1 = ray.path[1]
            points.append(p0)
            points.append(p1)
            lines.append([2,idx,idx+1])

            idx += 2
        
        points = np.array(points)
        lines = np.array(lines)

        poly = pv.PolyData()
        poly.points = points
        poly.lines = lines

        if self.rays_actor is None:

            self.rays_actor = self.plotter.add_mesh(
                poly,
                color="red",
                line_width=2
            )
        else:
            self.rays_actor.mapper.SetInputData(poly)
            self.plotter.render()