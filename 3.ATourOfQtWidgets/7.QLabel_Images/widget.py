from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Image Demo")


        image_label = QLabel()
        image_label.setPixmap(QPixmap("./images/minions.png") )

        button = QPushButton()
        button.setIcon( QPixmap( "images/ButtonTest.png" ) )
        button.clicked.connect( self.do_something )

        layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addWidget( button )

        self.setLayout(layout)

    def do_something( self ):
        print( f"doing something" )