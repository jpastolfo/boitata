class Beamline:
    def __init__(self):
        self.sources = []
        self.optics = []
        self.rays = []

    def generate_rays(self):
        self.rays.clear()
        
        for src in self.sources:
            self.rays.extend(src.generate_rays())
