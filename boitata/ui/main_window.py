from PyQt5.QtWidgets import QMainWindow
from pyvistaqt import QtInteractor

from boitata.render.scene import SceneRenderer
from boitata.core.beamline import Beamline
from boitata.core.source import PointSource
from boitata.ui.source_editor import SourceEditor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BOITATA - Beamline Optical Interactive Tracing And Trajectory Analyzer")

        self.plotter = QtInteractor(self)
        self.setCentralWidget(self.plotter)

        self.renderer = SceneRenderer(self.plotter)
        self.beamline = Beamline()
        
        self.plotter.add_axes()
        self.plotter.view_zy()
        self.init_scene()
        self.enable_picking()

    def init_scene(self):
        self.source = PointSource(n_rays=100)
        self.beamline.sources.append(self.source)
        self.renderer.add_source(self.source)
        self.beamline.generate_rays()
        for ray in self.beamline.rays:
            ray.propagate(100)
        self.renderer.draw_rays(self.beamline.rays)
    
    def enable_picking(self):
        self.plotter.enable_mesh_picking(
            callback = self.on_object_clicked,
            left_clicking=True,
            use_actor=True,
            show=False
        )

    def on_object_clicked(self, actor):
        obj = self.renderer.actor_map.get(actor)
        if obj is None:
            print("No object mapped")
            return
        print("Clicked object: ", obj)

        if hasattr(obj,"generate_rays"):
            print("Source!")
            self.open_source_editor(obj)

    def open_source_editor(self,source):
        self.editor = SourceEditor(
            source,
            apply_callback=self.update_source
        )
        self.editor.show()

    def update_source(self):
        self.renderer.clear_rays()
        rays = self.source.generate_rays()

        for ray in rays:
            ray.propagate(100)
        
        self.renderer.draw_rays(rays)
        self.plotter.render()
