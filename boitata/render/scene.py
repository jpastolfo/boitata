import pyvista as pv

class SceneRenderer:
    def __init__(self,plotter):
        self.plotter = plotter
        
        self.actor_map = {}
        self.ray_actors = None

    def clear(self):
        for a in self.ray_actors:
            self.plotter.remove_actor(a)
        
        self.ray_actors = []

    def clear_rays(self):

        for actor in self.ray_actors:
            self.plotter.remove_actor(actor)

        self.ray_actors.clear()

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
        for ray in rays:
            line = pv.Line(ray.path[0],ray.path[-1])

            actor = self.plotter.add_mesh(
                line,
                color="red",
                line_width=2
            )
            #self.mesh_map[id(line)] = ray
        
            self.ray_actors.append(actor)