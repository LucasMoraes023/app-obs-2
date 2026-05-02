from PySide6.QtWidgets import *
from core.recorder import Recorder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rec = Recorder()

        self.setWindowTitle("OBS GAMER EDITION")
        self.setFixedSize(700, 400)

        self.setStyleSheet("""
        QMainWindow {
            background-color: #0b0b0b;
            color: #00ff66;
        }
        QPushButton {
            background-color: black;
            border: 2px solid #00ff66;
            padding: 12px;
            font-size: 14px;
            color: #00ff66;
        }
        QPushButton:hover {
            background-color: #00ff66;
            color: black;
        }
        """)

        layout = QVBoxLayout()

        title = QLabel("🎮 OBS GAMER EDITION")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        self.btn_start = QPushButton("START RECORD")
        self.btn_stop = QPushButton("STOP RECORD")

        self.btn_start.clicked.connect(self.rec.start)
        self.btn_stop.clicked.connect(self.rec.stop)

        layout.addWidget(title)
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_stop)

        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)