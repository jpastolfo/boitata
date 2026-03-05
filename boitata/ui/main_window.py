from PyQt5.QtWidgets import QMainWindow
from pyvistaqt import QtInteractor

from boitata.render.scene import SceneRenderer
from boitata.core.beamline import Beamline
from boitata.core.source import PointSource

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BOITATA - Beamline Optical Interactive Tracing And Trajectory Analyzer")

        self.plotter = QtInteractor(self)
        self.setCentralWidget(self.plotter)

        self.renderer = SceneRenderer(self.plotter)
        self.beamline = Beamline()
        
        self.init_scene()

    def init_scene(self):
        source = PointSource()
        self.beamline.sources.append(source)
        self.beamline.generate_rays()
        for ray in self.beamline.rays:
            ray.propagate(10)
            self.renderer.draw_rays(self.beamline.rays)