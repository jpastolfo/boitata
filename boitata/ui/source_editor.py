from PyQt5.QtWidgets import (
    QWidget,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton
)


class SourceEditor(QWidget):

    def __init__(self, source, apply_callback):

        super().__init__()

        self.source = source
        self.apply_callback = apply_callback

        self.setWindowTitle("Source Editor")

        layout = QFormLayout()

        # Number of rays
        self.rays_box = QSpinBox()
        self.rays_box.setRange(1, 100000)
        self.rays_box.setValue(source.n_rays)

        # Divergence
        self.div_box = QDoubleSpinBox()
        self.div_box.setDecimals(5)
        self.div_box.setRange(0, 1)
        self.div_box.setValue(source.divergence)

        # Apply button
        apply_button = QPushButton("Apply")
        apply_button.clicked.connect(self.apply_changes)

        layout.addRow("Number of rays", self.rays_box)
        layout.addRow("Divergence", self.div_box)
        layout.addRow(apply_button)

        self.setLayout(layout)

    def apply_changes(self):

        self.source.n_rays = self.rays_box.value()
        self.source.divergence = self.div_box.value()

        self.apply_callback()