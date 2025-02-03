from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtGui import QPalette, QColor

class MotionGUITest(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # X-axis controls
        x_layout = QHBoxLayout()
        x_label = QLabel('X-axis:')
        self.x_input = QLineEdit()
        x_left_button = QPushButton('Left')
        x_right_button = QPushButton('Right')
        x_layout.addWidget(x_label)
        x_layout.addWidget(self.x_input)
        x_layout.addWidget(x_left_button)
        x_layout.addWidget(x_right_button)
        layout.addLayout(x_layout)

        # Y-axis controls
        y_layout = QHBoxLayout()
        y_label = QLabel('Y-axis:')
        self.y_input = QLineEdit()
        y_back_button = QPushButton('Back')
        y_forth_button = QPushButton('Forth')
        y_layout.addWidget(y_label)
        y_layout.addWidget(self.y_input)
        y_layout.addWidget(y_back_button)
        y_layout.addWidget(y_forth_button)
        layout.addLayout(y_layout)

        # Z-axis controls
        z_layout = QHBoxLayout()
        z_label = QLabel('Z-axis:')
        self.z_input = QLineEdit()
        z_up_button = QPushButton('Up')
        z_down_button = QPushButton('Down')
        z_layout.addWidget(z_label)
        z_layout.addWidget(self.z_input)
        z_layout.addWidget(z_up_button)
        z_layout.addWidget(z_down_button)
        layout.addLayout(z_layout)

        self.setLayout(layout)
        self.setWindowTitle('Motion Control GUI')

if __name__ == '__main__':
    app = QApplication([])
    app.setPalette( QPalette( QColor( "#444444" ) ) )
    window = MotionGUITest()
    window.show()
    app.exec()
    def move_x_left(self):
        distance = self.x_input.text()
        print(f"Moving X left by {distance}")

    def move_x_right(self):
        distance = self.x_input.text()
        print(f"Moving X right by {distance}")

    def move_y_back(self):
        distance = self.y_input.text()
        print(f"Moving Y back by {distance}")

    def move_y_forth(self):
        distance = self.y_input.text()
        print(f"Moving Y forth by {distance}")

    def move_z_up(self):
        distance = self.z_input.text()
        print(f"Moving Z up by {distance}")

    def move_z_down(self):
        distance = self.z_input.text()
        print(f"Moving Z down by {distance}")

    def initUI(self):
        layout = QVBoxLayout()

        # X-axis controls
        x_layout = QHBoxLayout()
        x_label = QLabel('X-axis:')
        self.x_input = QLineEdit()
        x_left_button = QPushButton('Left')
        x_right_button = QPushButton('Right')
        x_left_button.clicked.connect(self.move_x_left)
        x_right_button.clicked.connect(self.move_x_right)
        x_layout.addWidget(x_label)
        x_layout.addWidget(self.x_input)
        x_layout.addWidget(x_left_button)
        x_layout.addWidget(x_right_button)
        layout.addLayout(x_layout)

        # Y-axis controls
        y_layout = QHBoxLayout()
        y_label = QLabel('Y-axis:')
        self.y_input = QLineEdit()
        y_back_button = QPushButton('Back')
        y_forth_button = QPushButton('Forth')
        y_back_button.clicked.connect(self.move_y_back)
        y_forth_button.clicked.connect(self.move_y_forth)
        y_layout.addWidget(y_label)
        y_layout.addWidget(self.y_input)
        y_layout.addWidget(y_back_button)
        y_layout.addWidget(y_forth_button)
        layout.addLayout(y_layout)

        # Z-axis controls
        z_layout = QHBoxLayout()
        z_label = QLabel('Z-axis:')
        self.z_input = QLineEdit()
        z_up_button = QPushButton('Up')
        z_down_button = QPushButton('Down')
        z_up_button.clicked.connect(self.move_z_up)
        z_down_button.clicked.connect(self.move_z_down)
        z_layout.addWidget(z_label)
        z_layout.addWidget(self.z_input)
        z_layout.addWidget(z_up_button)
        z_layout.addWidget(z_down_button)
        layout.addLayout(z_layout)

        self.setLayout(layout)
        self.setWindowTitle('Motion Control GUI')

if __name__ == '__main__':
    app = QApplication([])
    window = MotionGUITest()
    window.show()
    app.exec()