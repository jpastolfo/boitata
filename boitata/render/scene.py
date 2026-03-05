import pyvista as pv

class SceneRenderer:
    def __init__(self,plotter):
        self.plotter = plotter
        
        self.ray_actors = []
        self.optic_actors = []

    def clear(self):
        for a in self.ray_actors:
            self.plotter.remove_actor(a)
        
        self.ray_actors = []

    def draw_rays(self,rays):
        for ray in rays:
            line = pv.Line(ray.path[0],ray.path[-1])

            actor = self.plotter.add_mesh(
                line,
                color="red",
                line_width=2
            )
        
        self.ray_actors.append(actor)